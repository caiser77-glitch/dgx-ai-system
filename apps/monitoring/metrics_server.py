#!/usr/bin/env python3
# Created: 2026-07-05 by Antigravity AI
# Purpose: Micro responsive live web dashboard server for Aurum Live Monitoring (No Blinking, Low Memory)

import os
import sys
import json
import sqlite3
import time
import glob
import re
import shutil
import shlex
import subprocess
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

# 경로 바인딩
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
METADATA_DIR = PROCESSED_DIR / "metadata"
EVENT_QUEUE_DB = PROJECT_ROOT / "data" / "atom_watcher" / "atom_baseline.sqlite"
TOTAL_FILES = 94513
# 005 아톰-모하비-아우룸 협업 파이프라인 스테이징 루트 (아톰)
PIPELINE_ROOT = Path("/home/caiser77/AI_BASE")

def get_gpu_status():
    try:
        res = subprocess.check_output(
            ["/usr/bin/nvidia-smi", "--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu", "--format=csv,noheader,nounits"],
            encoding="utf-8"
        )
        parts = res.strip().split("\n")[0].split(", ")
        gpu_util = parts[0]
        mem_used = parts[1]
        mem_total = parts[2]
        temp = parts[3]

        vram_str = "N/A"
        try:
            vram_str = f"{float(mem_used)/1024:.1f} GB / {float(mem_total)/1024:.1f} GB"
        except Exception:
            vram_str = f"{mem_used} / {mem_total}"

        return {
            "util": f"{gpu_util}%" if gpu_util != "[N/A]" else "N/A",
            "vram": vram_str,
            "temp": f"{temp}°C" if temp != "[N/A]" else "N/A"
        }
    except Exception:
        return {"util": "Offline", "vram": "Offline", "temp": "Offline"}

def get_cpu_temp():
    try:
        temps = []
        for path in glob.glob("/sys/class/thermal/thermal_zone*/temp"):
            with open(path, "r") as f:
                val = int(f.read().strip())
                temps.append(val / 1000.0)
        if temps:
            return f"{max(temps):.1f}°C"
        return "N/A"
    except Exception:
        return "N/A"

def get_cpu_ram_status():
    try:
        import psutil
        cpu = f"{psutil.cpu_percent()}%"
        ram = f"{psutil.virtual_memory().percent}%"
        return cpu, ram
    except Exception:
        return "N/A", "N/A"

def get_mac_status():
    metrics_path = PROCESSED_DIR / "metrics_mac.json"
    if metrics_path.exists():
        try:
            mtime = os.path.getmtime(metrics_path)
            if (time.time() - mtime) < 60:
                with open(metrics_path, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
    return {
        "cpu": "Offline",
        "ram": "Offline",
        "gpu": "Offline",
        "temp": "Offline",
        "ollama_status": "Offline",
        "workers": 0,
        "status": "Sleeping"
    }

# AI 요약 결과가 '미생성/실패' 인지 판정하기 위한 마커
# (예: "요약을 생성하지 못했습니다.", "Hermes binary not found locally.")
SUMMARY_FAIL_MARKERS = ("생성하지 못", "not found", "hermes binary")

# 틱당 상세 read 상한 (요약본이 늘어나도 서버가 멈추지 않도록 하는 성능 가드)
READ_CAP = 60000


def _is_ignored_history_path(*paths):
    """운영 이력에서 Git 저장소/시스템 산출물처럼 업무 파일이 아닌 항목을 숨긴다."""
    ignored_parts = {
        "#recycle", "@eadir", "@eaDir", "_AURUM_AI_PROCESSED",
        ".git", ".hg", ".svn", ".@__thumb", ".snapshot", "@recycle",
    }
    for raw in paths:
        if not raw:
            continue
        parts = Path(str(raw)).parts
        for part in parts:
            if part in ignored_parts or part.endswith(".git"):
                return True
    return False


def _summary_state(meta):
    """메타데이터 1건의 실제 파이프라인 상태를 판정한다.

    - 'extract_failed' : 텍스트 추출 자체가 실패 (status == failed)
    - 'pending'        : 추출/분류는 됐으나 AI 요약이 아직 생성되지 않음
    - 'failed'         : AI 요약을 시도했으나 실패 placeholder 만 존재
    - 'done'           : 유효한 AI 요약이 정상 생성됨
    """
    if meta.get("status") == "failed":
        return "extract_failed"
    summary_block = meta.get("ai_summary")
    classification_block = meta.get("ai_classification")
    if not summary_block and not classification_block:
        return "pending"

    block = summary_block if isinstance(summary_block, dict) and summary_block else classification_block
    summ = block.get("summary") if isinstance(block, dict) else None
    txt = " ".join(summ) if isinstance(summ, list) else str(summ or "")
    low = txt.lower()
    if not txt.strip() or any(m in txt or m in low for m in SUMMARY_FAIL_MARKERS):
        return "failed"
    return "done"


def _proc_alive(pat):
    """프로세스 존재로 서비스 생존 판정(systemctl --user 세션 의존 회피)."""
    try:
        r = subprocess.run(["pgrep", "-f", pat], capture_output=True, text=True, timeout=3)
        return "active" if r.returncode == 0 else "stopped"
    except Exception:
        return "unknown"


def get_pipeline_status():
    """005 아톰-모하비-아우룸 협업 파이프라인의 실시간 작업 현황."""
    p = PIPELINE_ROOT

    def cnt(stage):
        try:
            return sum(1 for f in os.listdir(p / stage) if f.endswith(".summary.md"))
        except Exception:
            return 0

    corpus, overnight = 0, ""
    try:
        st = json.load(open(p / "overnight_status.json", encoding="utf-8"))
        corpus, overnight = st.get("corpus_docs", 0), st.get("updated", "")
    except Exception:
        pass
    try:
        nas = len({f.rsplit(".", 1)[0] for f in os.listdir(p / "NAS_Distribution") if "." in f})
    except Exception:
        nas = 0
    mac = {}
    try:
        f = p / "pipeline_mac_status.json"
        if time.time() - os.path.getmtime(f) < 900:
            mac = json.load(open(f, encoding="utf-8"))
    except Exception:
        pass
    return {
        "raw": cnt("01_raw_analyzed"),
        "drafting_atom": _drafting_count(),
        "review_pending": _review_pending_count(),
        "published": cnt("04_published"),
        "nas_deliverables": nas,
        "corpus_docs": corpus,
        "overnight_updated": overnight,
        "svc_engine": _proc_alive("pipeline_engine.py"),
        "svc_tracker": _proc_alive("track_pipeline_status.py"),
        "svc_deployer": _proc_alive("aurum_deployer.py"),
        "admin_pending": _review_pending_count(),
        "mac_admin_pending": mac.get("admin_pending", -1),
        "mac_drafting": mac.get("drafting", -1),
        "mac_launchd": mac.get("launchd", "unknown"),
        "mac_updated": mac.get("updated", ""),
        "mac_jobs": mac.get("jobs", []),
        "mac_active_jobs": mac.get("active_jobs", []),
        "mac_idle_reason": mac.get("idle_reason", ""),
        "mac_last_action": mac.get("last_action", ""),
        "mac_available_slots": mac.get("available_slots", -1),
    }


def _event_queue_counts():
    counts = {"pending": 0, "processing": 0, "failed": 0}
    try:
        conn = sqlite3.connect(str(EVENT_QUEUE_DB))
        try:
            for status, count in conn.execute("SELECT status, COUNT(*) FROM event_queue GROUP BY status"):
                counts[str(status)] = int(count)
        finally:
            conn.close()
    except Exception:
        pass
    return counts


def _latest_stage_job(stage):
    stage_dir = _stage_dir(stage)
    if not stage_dir or not stage_dir.exists():
        return None
    paths = []
    for pattern in ("*.draft.md", "*.summary.md"):
        paths.extend(stage_dir.glob(pattern))
    if not paths:
        return None
    path = max(paths, key=lambda item: item.stat().st_mtime)
    try:
        return _pipeline_item(stage, path)
    except Exception:
        return {
            "job_id": _job_id_from_path(path),
            "title": path.name,
            "status": "",
            "updated": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(path.stat().st_mtime)),
        }


def _activity_state(active, waiting):
    if active:
        return "active"
    if waiting:
        return "waiting"
    return "idle"


def build_ai_activity(pipeline, atom_gpu_util):
    q = _event_queue_counts()
    raw = int(pipeline.get("raw") or 0)
    drafting = int(pipeline.get("drafting_atom") or 0)
    admin = int(pipeline.get("admin_pending") or 0)
    mac_admin = int(pipeline.get("mac_admin_pending") or 0)
    mac_drafting = int(pipeline.get("mac_drafting") or 0)
    gpu_num = 0.0
    try:
        gpu_num = float(str(atom_gpu_util).replace("%", ""))
    except Exception:
        pass

    atom_latest = _latest_stage_job("raw") or _latest_stage_job("drafting") or _latest_stage_job("review")
    atom_title = atom_latest.get("title") if atom_latest else "신규 NAS 이벤트 감시"
    atom_active = raw > 0 or q.get("pending", 0) > 0 or q.get("processing", 0) > 0 or gpu_num >= 5
    atom_waiting = admin > 0 or drafting > 0
    if raw > 0:
        atom_task = "1차 요약 입력을 협업 파이프라인으로 넘기는 중"
        atom_next = "엔진이 02_drafting으로 전이 후 맥에 배정"
    elif q.get("pending", 0) or q.get("processing", 0):
        atom_task = "NAS 신규/변경 이벤트 추출 처리 중"
        atom_next = "처리 완료 후 요약 산출물 생성"
    elif admin > 0:
        atom_task = "검토 완료본 승인 대기"
        atom_next = "승인 또는 거절 필요"
    elif drafting > 0:
        atom_task = "맥 작업 결과 동기화/후처리 대기"
        atom_next = "맥 상태 회수 또는 중복 아카이브"
    else:
        atom_task = "신규 파일 감시 및 vLLM 대기"
        atom_next = "신규 입력 발생 시 즉시 처리"

    mac_jobs = pipeline.get("mac_jobs") or []
    mac_job = next((j for j in mac_jobs if j.get("status") == "drafting"), None) or next((j for j in mac_jobs if j.get("status") in {"admin_pending", "review_pending", "reviewed"}), None)
    mac_title = (mac_job or {}).get("job_id") or "맥 큐 대기"
    mac_active = mac_drafting > 0
    mac_waiting = mac_admin > 0
    if mac_drafting > 0:
        mac_task = "모하비 초안 작성 또는 아우룸 검토 중"
        mac_next = "완료 시 승인대기로 전환"
    elif mac_admin > 0:
        mac_task = "초안/검토 완료, 운영자 승인 대기"
        mac_next = "대시보드 승인/거절 또는 아톰 회수"
    else:
        mac_task = "작업 슬롯 대기"
        mac_next = pipeline.get("mac_idle_reason") or "아톰 후보 발생 시 자동 배정"

    return {
        "atom": {
            "state": _activity_state(atom_active, atom_waiting),
            "headline": atom_task,
            "job": atom_title,
            "queue": f"이벤트 {q.get('pending', 0)} · raw {raw} · 처리중 {drafting} · 승인대기 {admin}",
            "next": atom_next,
        },
        "mac": {
            "state": _activity_state(mac_active, mac_waiting),
            "headline": mac_task,
            "job": mac_title,
            "queue": f"초안작성 {mac_drafting} · 승인대기 {mac_admin} · 여유슬롯 {pipeline.get('mac_available_slots', '-')}",
            "next": mac_next,
        }
    }


def collect_metrics():
    catalogued = 0        # 텍스트 추출·분류가 끝나 카탈로그된 파일 수 (= metadata 파일 수)
    summary_done = 0      # AI 요약 정상 완료
    summary_failed = 0    # AI 요약 시도했으나 실패
    summary_pending = 0   # AI 요약 대기 (아직 미시도)
    extract_failed = 0    # 텍스트 추출 자체 실패
    recent_files_mac = []
    recent_files_atom = []

    if METADATA_DIR.exists():
        file_entries = []
        try:
            for entry in os.scandir(METADATA_DIR):
                if entry.is_file() and entry.name.endswith(".metadata.json"):
                    try:
                        stat = entry.stat()
                        file_entries.append((entry.path, entry.name, stat.st_size, stat.st_mtime))
                    except Exception:
                        pass
        except Exception:
            pass

        catalogued = len(file_entries)
        # ai_summary 블록이 붙으면 파일이 1KB를 넘는다 → <1KB 는 read 없이 '요약 대기'로 확정(초고속).
        # 1KB 이상인 소수 파일만 실제로 열어 요약 정상/실패를 정확히 구분한다.
        big_entries = [e for e in file_entries if e[2] >= 1024]
        summary_pending = catalogued - len(big_entries)

        if len(big_entries) <= READ_CAP:
            for path, _, _, _ in big_entries:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        state = _summary_state(json.load(f))
                except Exception:
                    state = "failed"
                if state == "done":
                    summary_done += 1
                elif state == "extract_failed":
                    extract_failed += 1
                else:
                    summary_failed += 1
        else:
            # 상세 read 상한 초과 시 요약본이 있으면 완료로 근사하여 성능을 보호한다.
            summary_done = len(big_entries)

        # 최근 이력: mtime 최신순 상위 150개만 열어 맥북/아톰 각각 10개 확보
        STATE_KR = {"done": "요약완료", "failed": "요약실패", "pending": "요약대기", "extract_failed": "추출실패"}
        file_entries.sort(key=lambda x: x[3], reverse=True)
        for path, name, _, mtime in file_entries[:150]:
            if len(recent_files_mac) >= 10 and len(recent_files_atom) >= 10:
                break
            try:
                with open(path, "r", encoding="utf-8") as file:
                    meta = json.load(file)
                state = _summary_state(meta)
                source_path = meta.get("source_path", "")
                outputs = meta.get("outputs", {})
                meta_path_str = outputs.get("metadata", "")
                if _is_ignored_history_path(source_path, meta_path_str):
                    continue
                category = (meta.get("ai_summary") or {}).get("category") \
                    or (meta.get("ai_classification") or {}).get("taxon_group") \
                    or meta.get("category", "미정")

                item = {
                    "filename": meta.get("filename", meta.get("source_name", name.replace(".metadata.json", ""))),
                    "category": category,
                    "status": STATE_KR.get(state, "요약대기"),
                    "time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                }

                # 경로 명세를 기반으로 로컬 맥북 가공 여부 필터링
                if "/Users/nams" in source_path or "/Users/nams" in meta_path_str:
                    if len(recent_files_mac) < 10:
                        recent_files_mac.append(item)
                else:
                    if len(recent_files_atom) < 10:
                        recent_files_atom.append(item)
            except Exception:
                pass

    # 진행률: 실제 남은 작업인 'AI 요약' 완료율을 기준으로 하며 100%를 넘지 않도록 clamp.
    # (기존엔 metadata 수 / 고정분모(94513) 라서 서버에서 210% 같은 값이 나왔다.)
    summary_progress = round(min(summary_done / catalogued * 100, 100.0), 2) if catalogued else 0.0
    catalog_progress = round(min(catalogued / TOTAL_FILES * 100, 100.0), 2) if TOTAL_FILES else 0.0

    cpu_val, ram_val = get_cpu_ram_status()
    gpu_info = get_gpu_status()
    mac_data = get_mac_status()
    pipeline_data = get_pipeline_status()
    ai_activity = build_ai_activity(pipeline_data, gpu_info["util"])

    return {
        "catalogued": catalogued,
        "summary_done": summary_done,
        "summary_failed": summary_failed,
        "summary_pending": summary_pending,
        "extract_failed": extract_failed,
        "summary_progress": summary_progress,
        "catalog_progress": catalog_progress,
        "total_target": TOTAL_FILES,
        "atom": {
            "cpu": cpu_val,
            "ram": ram_val,
            "temp": get_cpu_temp(),
            "gpu_util": gpu_info["util"],
            "gpu_vram": gpu_info["vram"],
            "gpu_temp": gpu_info["temp"]
        },
        "mac": {
            "cpu": mac_data.get("cpu", "Offline"),
            "ram": mac_data.get("ram", "Offline"),
            "gpu": mac_data.get("gpu", "Offline"),
            "temp": mac_data.get("temp", "Offline"),
            "status": mac_data.get("status", "Offline"),
            "ollama": mac_data.get("ollama_status", "Offline"),
            "workers": mac_data.get("workers", 0)
        },
        "recent_files_mac": recent_files_mac,
        "recent_files_atom": recent_files_atom,
        "pipeline": pipeline_data,
        "ai_activity": ai_activity
    }

# 전역 캐시 딕셔너리 및 동기화 락
import threading
cached_data = {
    "catalogued": 0, "summary_done": 0, "summary_failed": 0, "summary_pending": 0, "extract_failed": 0,
    "summary_progress": 0.0, "catalog_progress": 0.0, "total_target": TOTAL_FILES,
    "atom": {"cpu": "N/A", "ram": "N/A", "temp": "N/A", "gpu_util": "N/A", "gpu_vram": "N/A", "gpu_temp": "N/A"},
    "mac": {"cpu": "Offline", "ram": "Offline", "gpu": "Offline", "temp": "Offline", "status": "Offline", "ollama": "Offline", "workers": 0},
    "recent_files_mac": [], "recent_files_atom": [],
    "ai_activity": {"atom": {"state": "idle", "headline": "대기", "job": "-", "queue": "-", "next": "-"}, "mac": {"state": "idle", "headline": "대기", "job": "-", "queue": "-", "next": "-"}},
    "pipeline": {"raw": 0, "drafting_atom": 0, "review_pending": 0, "published": 0, "nas_deliverables": 0,
                 "corpus_docs": 0, "overnight_updated": "", "svc_engine": "unknown", "svc_tracker": "unknown",
                 "svc_deployer": "unknown", "admin_pending": 0, "mac_admin_pending": -1, "mac_drafting": -1, "mac_launchd": "unknown", "mac_updated": "",
                 "mac_jobs": [], "mac_active_jobs": [], "mac_idle_reason": "", "mac_last_action": "", "mac_available_slots": -1}
}

def cache_updater_loop():
    global cached_data
    print("[Cache Daemon Started] Background metrics collector running...", flush=True)
    while True:
        try:
            # 5초마다 넌블로킹 백그라운드 스캔 및 리소스 수집
            latest = collect_metrics()
            cached_data = latest
        except Exception as e:
            print(f"[Cache Daemon Error] {e}", file=sys.stderr, flush=True)
        time.sleep(5)

JOB_SUFFIXES = ("summary.md", "result.json", "draft.md")
JOB_ID_RE = re.compile(r"^[A-Za-z0-9_.-]+$")
MAC_PIPELINE_SSH = os.environ.get("AURUM_MAC_SSH", "aurum-mac")
MAC_PIPELINE_ROOT = os.environ.get("MOHAVE_PIPELINE_ROOT", "/Users/nams/AI_BASE/AurumPipeline_mohave")
SYNCABLE_MAC_STATUSES = {"admin_pending", "review_pending", "reviewed"}
BALANCER_SCRIPT = PROJECT_ROOT / "005. 아톰-모하비-아우룸 협업 파이프라인" / "scripts" / "pipeline_balancer.py"


def _stage_dir(stage):
    mapping = {
        "raw": PIPELINE_ROOT / "01_raw_analyzed",
        "drafting": PIPELINE_ROOT / "02_drafting",
        "review": PIPELINE_ROOT / "03_review_pending",
        "published": PIPELINE_ROOT / "04_published",
        "error": PIPELINE_ROOT / "00_error_failed",
        "corpus": PIPELINE_ROOT / "clean_corpus",
    }
    return mapping.get(stage)


def _published_job_ids():
    published = _stage_dir("published")
    if not published or not published.exists():
        return set()
    ids = set()
    for path in published.glob("*.draft.md"):
        ids.add(_job_id_from_path(path))
    for path in published.glob("*.summary.md"):
        ids.add(_job_id_from_path(path))
    return ids


def _review_job_ids():
    review = _stage_dir("review")
    if not review or not review.exists():
        return set()
    ids = set()
    for path in list(review.glob("*.draft.md")) + list(review.glob("*.summary.md")):
        ids.add(_job_id_from_path(path))
    return ids


def _advanced_job_ids():
    return _published_job_ids() | _review_job_ids()


def _drafting_count():
    drafting = _stage_dir("drafting")
    advanced = _advanced_job_ids()
    if not drafting or not drafting.exists():
        return 0
    ids = set()
    for path in drafting.glob("*.summary.md"):
        job_id = _job_id_from_path(path)
        if job_id not in advanced:
            ids.add(job_id)
    return len(ids)


def _review_pending_count():
    review = _stage_dir("review")
    published = _published_job_ids()
    if not review or not review.exists():
        return 0
    count = 0
    seen = set()
    for draft in review.glob("*.draft.md"):
        job_id = _job_id_from_path(draft)
        if job_id in seen or job_id in published:
            continue
        meta = _parse_frontmatter_text(_read_text_safe(draft, limit=1200))
        if meta.get("status", "") in {"admin_pending", "review_pending"}:
            seen.add(job_id)
            count += 1
    return count


def _read_text_safe(path, limit=1800):
    try:
        txt = Path(path).read_text(encoding="utf-8", errors="replace")
        return txt[:limit]
    except Exception:
        return ""


def _parse_frontmatter_text(content):
    meta = {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content or "", re.DOTALL)
    if not match:
        return meta
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def _write_frontmatter(path, updates):
    path = Path(path)
    content = path.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    meta = _parse_frontmatter_text(content)
    body = re.sub(r"^---\s*\n(.*?)\n---\s*\n", "", content, count=1, flags=re.DOTALL) if match else content
    meta.update(updates)
    fm = "---\n" + "\n".join(f"{k}: {v}" for k, v in meta.items()) + "\n---\n"
    path.write_text(fm + "\n" + body.lstrip("\n"), encoding="utf-8")


def _job_id_from_path(path):
    name = Path(path).name
    for suffix in (".draft.md", ".summary.md", ".result.json"):
        if name.endswith(suffix):
            return name[:-len(suffix)]
    return Path(path).stem


def _job_files(stage_dir, job_id):
    paths = []
    for suffix in JOB_SUFFIXES:
        path = Path(stage_dir) / f"{job_id}.{suffix}"
        if path.exists():
            paths.append(path)
    return paths


def _infer_job_title(content, fallback):
    for line in (content or "").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- Project Name:"):
            value = stripped.split(":", 1)[1].strip()
            if value:
                return value
    for line in (content or "").splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            if title:
                return title
    return fallback


def _mac_pending_jobs():
    script = r"""
import glob
import json
import os
import re
import sys

root = sys.argv[1]
jobs = []
for path in glob.glob(os.path.join(root, "02_drafting", "*.draft.md")):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            content = f.read(4096)
    except Exception:
        continue
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    meta = {}
    if match:
        for line in match.group(1).splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"').strip("'")
    if meta.get("status") in {"admin_pending", "review_pending", "reviewed"}:
        name = os.path.basename(path)
        jobs.append(name[:-len(".draft.md")])
print(json.dumps(jobs, ensure_ascii=False))
"""
    remote_cmd = "python3 -c " + shlex.quote(script) + " " + shlex.quote(MAC_PIPELINE_ROOT)
    result = subprocess.run(
        ["ssh", MAC_PIPELINE_SSH, remote_cmd],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "맥 승인대기 조회 실패").strip())
    jobs = json.loads(result.stdout or "[]")
    return [job for job in jobs if JOB_ID_RE.match(job or "")]


def sync_mac_pending_to_atom():
    published = _published_job_ids()
    jobs = [job for job in _mac_pending_jobs() if job not in published]
    review_dir = _stage_dir("review")
    review_dir.mkdir(parents=True, exist_ok=True)
    copied = []
    for job_id in jobs:
        for suffix in JOB_SUFFIXES:
            remote = f"{MAC_PIPELINE_SSH}:{MAC_PIPELINE_ROOT}/02_drafting/{job_id}.{suffix}"
            result = subprocess.run(
                ["rsync", "-az", "--update", "--partial", remote, str(review_dir) + "/"],
                capture_output=True,
                text=True,
                timeout=30,
            )
            if result.returncode == 0:
                copied.append(f"{job_id}.{suffix}")
            elif "No such file" not in (result.stderr or "") and "link_stat" not in (result.stderr or ""):
                raise RuntimeError((result.stderr or result.stdout or f"{job_id}.{suffix} 동기화 실패").strip())
    return {
        "ok": True,
        "action": "sync_mac_pending",
        "jobs": jobs,
        "copied": copied,
        "message": f"맥 승인대기 {len(jobs)}건을 아톰 승인대기함으로 회수했습니다.",
    }


def _pipeline_item(stage_name, draft_or_summary):
    path = Path(draft_or_summary)
    job_id = _job_id_from_path(path)
    draft = path.parent / f"{job_id}.draft.md"
    summary = path.parent / f"{job_id}.summary.md"
    result = path.parent / f"{job_id}.result.json"
    main = draft if draft.exists() else (summary if summary.exists() else path)
    content = _read_text_safe(main, limit=2200)
    meta = _parse_frontmatter_text(content)
    stat = main.stat()
    title = meta.get("project_name") or meta.get("source_file") or _infer_job_title(content, main.name)
    return {
        "job_id": job_id,
        "stage": stage_name,
        "title": title,
        "status": meta.get("status", ""),
        "assigned_agent": meta.get("assigned_agent", ""),
        "updated": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)),
        "files": {
            "draft": draft.name if draft.exists() else "",
            "summary": summary.name if summary.exists() else "",
            "result": result.name if result.exists() else "",
        },
        "preview": content[:1800],
        "actionable": stage_name == "review" and draft.exists(),
    }


def get_pipeline_items(kind, limit=80):
    items = []
    if kind == "published":
        dirs = [("published", _stage_dir("published"))]
    elif kind == "admin":
        dirs = [("review", _stage_dir("review"))]
    elif kind == "inflight":
        dirs = [("raw", _stage_dir("raw")), ("drafting", _stage_dir("drafting")), ("review", _stage_dir("review"))]
    elif kind == "corpus":
        corpus = _stage_dir("corpus")
        if corpus and corpus.exists():
            for path in sorted(corpus.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True)[:limit]:
                txt_path = path.with_suffix(".txt")
                stat = path.stat()
                items.append({
                    "job_id": path.stem,
                    "stage": "corpus",
                    "title": path.name,
                    "status": "clean_corpus",
                    "assigned_agent": "",
                    "updated": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)),
                    "files": {"json": path.name, "text": txt_path.name if txt_path.exists() else ""},
                    "preview": _read_text_safe(txt_path if txt_path.exists() else path, limit=1800),
                    "actionable": False,
                })
        return {"kind": kind, "items": items, "local_count": len(items), "mac_admin_pending": cached_data.get("pipeline", {}).get("mac_admin_pending", -1)}
    else:
        dirs = []

    seen = set()
    for stage_name, directory in dirs:
        if not directory or not directory.exists():
            continue
        candidates = list(directory.glob("*.draft.md")) + list(directory.glob("*.summary.md"))
        for path in sorted(candidates, key=lambda x: x.stat().st_mtime, reverse=True):
            job_id = _job_id_from_path(path)
            key = (stage_name, job_id)
            if key in seen:
                continue
            seen.add(key)
            item = _pipeline_item(stage_name, path)
            if kind == "admin":
                if item["job_id"] in _published_job_ids():
                    continue
                if item.get("status") not in {"admin_pending", "review_pending"}:
                    continue
            elif kind == "inflight":
                if stage_name in {"raw", "drafting"} and item["job_id"] in _advanced_job_ids():
                    continue
                if stage_name == "review" and item["job_id"] in _published_job_ids():
                    continue
            elif stage_name == "review" and item["job_id"] in _published_job_ids():
                continue
            items.append(item)
            if len(items) >= limit:
                break
    return {"kind": kind, "items": items, "local_count": len(items), "mac_admin_pending": cached_data.get("pipeline", {}).get("mac_admin_pending", -1)}


def run_pipeline_balancer():
    result = subprocess.run(
        [sys.executable, str(BALANCER_SCRIPT)],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "맥 작업 배정 점검 실패").strip())
    payload = json.loads(result.stdout or "{}")
    payload["message"] = (
        f"판단: {payload.get('decision', 'unknown')} · "
        f"아톰 여유 {payload.get('atom_pressure', {}).get('available_gib', '?')}GiB · "
        f"PSI {payload.get('atom_pressure', {}).get('psi_some_avg60', '?')} · "
        f"후보 {len(payload.get('candidate_jobs', []))}건 · "
        f"선택 {len(payload.get('selected_jobs', []))}건"
    )
    return payload


def apply_pipeline_action(job_id, action):
    if action == "sync_mac_pending":
        return sync_mac_pending_to_atom()
    if action == "balance_mac_work":
        return run_pipeline_balancer()
    if not JOB_ID_RE.match(job_id or ""):
        raise ValueError("잘못된 작업 ID입니다.")
    if action not in {"approve", "reject"}:
        raise ValueError("지원하지 않는 액션입니다.")
    review_dir = _stage_dir("review")
    error_dir = _stage_dir("error")
    draft = review_dir / f"{job_id}.draft.md"
    if not draft.exists():
        raise FileNotFoundError(f"승인대기 draft를 찾을 수 없습니다: {job_id}")
    if action == "approve":
        _write_frontmatter(draft, {"status": "reviewed", "assigned_agent": "Aurum"})
        return {"ok": True, "job_id": job_id, "action": action, "message": "승인했습니다. 배포기가 reviewed 문서를 배포합니다."}
    _write_frontmatter(draft, {"status": "rejected", "assigned_agent": "Aurum"})
    error_dir.mkdir(parents=True, exist_ok=True)
    moved = []
    for src in _job_files(review_dir, job_id):
        dst = error_dir / src.name
        if dst.exists():
            dst = error_dir / f"{int(time.time())}.{src.name}"
        shutil.move(str(src), str(dst))
        moved.append(dst.name)
    return {"ok": True, "job_id": job_id, "action": action, "message": "거절했습니다. 관련 파일을 오류 보관함으로 이동했습니다.", "moved": moved}

class LiveMonitorHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # 로그 출력 억제하여 디스크 I/O 절약

    def _send_json(self, payload, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(payload, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/metrics":
            try:
                self._send_json(cached_data)
            except (ConnectionError, BrokenPipeError):
                pass # 브라우저 중도 이탈로 인한 BrokenPipeError 예방 (서버 멈춤 완전 차단)
            except Exception as e:
                print(f"[API Response Error] {e}", file=sys.stderr)
        elif parsed.path == "/api/pipeline":
            try:
                qs = parse_qs(parsed.query)
                kind = qs.get("kind", ["admin"])[0]
                self._send_json(get_pipeline_items(kind))
            except Exception as e:
                self._send_json({"ok": False, "error": str(e)}, status=500)
        elif parsed.path == "/" or parsed.path == "/index.html":
            try:
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(HTML_TEMPLATE.encode("utf-8"))
            except (ConnectionError, BrokenPipeError):
                pass
            except Exception as e:
                print(f"[API HTML Error] {e}", file=sys.stderr)
        else:
            try:
                self.send_error(404)
            except Exception:
                pass

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != "/api/pipeline/action":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length).decode("utf-8") if length else "{}"
            payload = json.loads(body)
            result = apply_pipeline_action(payload.get("job_id", ""), payload.get("action", ""))
            self._send_json(result)
        except Exception as e:
            self._send_json({"ok": False, "error": str(e)}, status=400)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aurum Live Dashboard</title>
    <style>
        :root {
            --bg-color: #05070a;
            --surface: #1b222c;
            --surface-2: #242d39;
            --surface-3: #303b49;
            --border-color: #465365;
            --border-strong: #6b7a90;
            --accent-blue: #7bc7ff;
            --accent-green: #7ee39a;
            --accent-red: #ff8585;
            --accent-amber: #ffd166;
            --text-main: #f7fbff;
            --text-sub: #c0cad6;
            --text-muted: #8d9aaa;
            --shadow: 0 12px 28px rgba(0, 0, 0, 0.38);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            padding: 12px 14px;
            overflow-x: hidden;
            line-height: 1.45;
        }

        body::before {
            content: "";
            position: fixed;
            inset: 0;
            z-index: -2;
            background:
                linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.024) 1px, transparent 1px);
            background-size: 36px 36px;
            mask-image: linear-gradient(to bottom, rgba(0,0,0,0.9), rgba(0,0,0,0.2));
        }

        #particle-canvas {
            display: none;
        }

        .header,
        .metric-grid,
        .progress-section,
        .summary-layout,
        .content-layout {
            max-width: 1760px;
            margin-left: auto;
            margin-right: auto;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            gap: 14px;
            margin-bottom: 8px;
            border-bottom: 1px solid var(--border-color);
            padding: 6px 0 14px;
        }

        .header-title h1 {
            font-size: clamp(1.15rem, 1.6vw, 1.55rem);
            font-weight: 700;
            color: var(--text-main);
            letter-spacing: 0;
        }

        .header-title p {
            font-size: 0.72rem;
            color: var(--text-sub);
            margin-top: 4px;
        }

        .live-badge {
            flex: 0 0 auto;
            background: rgba(126, 227, 154, 0.16);
            color: var(--accent-green);
            padding: 7px 10px;
            border-radius: 6px;
            font-size: 0.72rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 6px;
            border: 1px solid rgba(126, 227, 154, 0.52);
        }

        .header-actions {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 7px;
        }

        .live-dot {
            width: 8px;
            height: 8px;
            background-color: var(--accent-green);
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }

        .sync-meta {
            color: var(--text-muted);
            font-size: 0.76rem;
            font-variant-numeric: tabular-nums;
            white-space: nowrap;
        }

        .sync-meta.is-error {
            color: var(--accent-red);
        }

        .service-row {
            margin-top: 8px;
            display: grid;
            grid-template-columns: 1fr;
            gap: 5px;
            color: var(--text-sub);
            font-size: 0.76rem;
            min-width: 0;
        }

        .service-row span {
            min-width: 0;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .ai-activity {
            max-width: 1760px;
            margin: 0 auto 10px;
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 10px;
        }

        .ai-card {
            background: var(--surface);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 10px 12px;
            box-shadow: var(--shadow);
            min-width: 0;
        }

        .ai-card.is-active {
            border-color: rgba(126, 227, 154, 0.58);
            background: linear-gradient(180deg, rgba(126, 227, 154, 0.12), var(--surface));
        }

        .ai-card.is-waiting {
            border-color: rgba(255, 209, 102, 0.58);
            background: linear-gradient(180deg, rgba(255, 209, 102, 0.12), var(--surface));
        }

        .ai-card-header {
            display: flex;
            justify-content: space-between;
            gap: 10px;
            align-items: center;
            margin-bottom: 8px;
            font-size: 0.8rem;
            font-weight: 700;
        }

        .ai-state {
            flex: 0 0 auto;
            border: 1px solid var(--border-color);
            border-radius: 999px;
            padding: 3px 8px;
            color: var(--text-sub);
            font-size: 0.68rem;
            font-weight: 700;
        }

        .ai-card.is-active .ai-state { color: var(--accent-green); border-color: rgba(126, 227, 154, 0.5); }
        .ai-card.is-waiting .ai-state { color: var(--accent-amber); border-color: rgba(255, 209, 102, 0.5); }

        .ai-task {
            color: var(--text-main);
            font-size: 0.9rem;
            font-weight: 700;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .ai-meta {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6px 12px;
            margin-top: 8px;
            color: var(--text-sub);
            font-size: 0.73rem;
        }

        .ai-meta div {
            min-width: 0;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        @keyframes pulse {
            0% { transform: scale(0.9); opacity: 0.5; }
            50% { transform: scale(1.2); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.5; }
        }

        .summary-layout {
            display: grid;
            grid-template-columns: minmax(0, 1.35fr) minmax(340px, 0.85fr);
            gap: 10px;
            max-width: 1760px;
            margin: 0 auto 10px;
            align-items: stretch;
        }

        .summary-main,
        .pipeline-panel {
            background: var(--surface);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 12px;
            box-shadow: var(--shadow);
        }

        .metric-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px;
            margin-bottom: 8px;
        }

        .metric-card {
            background: var(--surface);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 10px 12px;
            text-align: left;
            box-shadow: var(--shadow);
        }

        .metric-card:hover {
            border-color: var(--border-strong);
        }

        .metric-value {
            font-size: clamp(1.18rem, 1.7vw, 1.55rem);
            line-height: 1.05;
            font-weight: 700;
            color: var(--accent-blue);
            margin-bottom: 3px;
            font-variant-numeric: tabular-nums;
        }

        .metric-label {
            font-size: 0.72rem;
            color: var(--text-sub);
            letter-spacing: 0;
        }

        .progress-section {
            background: var(--surface);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 8px;
        }

        .progress-info {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            margin-bottom: 8px;
        }

        .progress-title {
            font-weight: 600;
            font-size: 0.95rem;
        }

        .progress-percentage {
            font-weight: 700;
            color: var(--accent-blue);
            font-size: 0.92rem;
            font-variant-numeric: tabular-nums;
        }

        .progress-bar-bg {
            background: #121821;
            height: 8px;
            border-radius: 999px;
            overflow: hidden;
            border: 1px solid var(--border-color);
        }

        .progress-bar-fill {
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-green));
            height: 100%;
            width: 0%;
            border-radius: 999px;
            transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .content-layout {
            display: grid;
            grid-template-columns: minmax(360px, 0.85fr) minmax(420px, 1.15fr) minmax(420px, 1.15fr);
            gap: 10px;
            align-items: stretch;
        }

        .panel-title {
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--text-main);
            border-left: 3px solid var(--accent-blue);
            padding-left: 9px;
        }

        .hw-section {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .hw-card {
            background: var(--surface);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 8px;
            box-shadow: var(--shadow);
        }

        .hw-card-header {
            font-weight: 700;
            font-size: 0.72rem;
            margin-bottom: 8px;
            color: var(--text-main);
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 9px;
            display: flex;
            justify-content: space-between;
            gap: 10px;
            align-items: center;
        }

        .hw-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 8px;
        }

        .hw-metric {
            background: var(--surface-2);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 8px;
            min-width: 0;
            transition: border-color 0.2s ease, background 0.2s ease;
        }

        .hw-metric.is-normal,
        .metric-card.is-normal {
            border-color: rgba(126, 227, 154, 0.54);
            background: linear-gradient(180deg, rgba(126, 227, 154, 0.14), var(--surface-2));
        }

        .hw-metric.is-warn,
        .metric-card.is-warn {
            border-color: rgba(255, 209, 102, 0.62);
            background: linear-gradient(180deg, rgba(255, 209, 102, 0.16), var(--surface-2));
        }

        .hw-metric.is-critical,
        .metric-card.is-critical {
            border-color: rgba(255, 133, 133, 0.68);
            background: linear-gradient(180deg, rgba(255, 133, 133, 0.18), var(--surface-2));
        }

        .hw-metric.is-offline,
        .metric-card.is-offline {
            border-color: rgba(192, 202, 214, 0.32);
            background: linear-gradient(180deg, rgba(192, 202, 214, 0.08), var(--surface-2));
            opacity: 0.82;
        }

        .hw-metric-value {
            font-size: 0.92rem;
            font-weight: 600;
            color: var(--text-main);
            margin-top: 4px;
            min-height: 1.45em;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            font-variant-numeric: tabular-nums;
        }

        .hw-metric-label {
            font-size: 0.72rem;
            color: var(--text-sub);
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .history-section {
            background: var(--surface);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 8px;
            display: flex;
            flex-direction: column;
            height: 100%;
            min-height: 370px;
            box-shadow: var(--shadow);
        }

        .table-container {
            flex-grow: 1;
            overflow-y: auto;
            overflow-x: auto;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: #121821;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.76rem;
        }

        th {
            color: var(--text-sub);
            font-weight: 600;
            padding: 7px 8px;
            border-bottom: 1px solid var(--border-color);
            background: var(--surface-3);
            position: sticky;
            top: 0;
            z-index: 1;
            white-space: nowrap;
        }

        td {
            padding: 7px 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.075);
            color: #dbe5ef;
            vertical-align: middle;
        }

        tr:hover td {
            background: rgba(123, 199, 255, 0.12);
            color: var(--text-main);
        }

        td:first-child {
            max-width: 260px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 64px;
            padding: 3px 7px;
            border-radius: 4px;
            font-size: 0.72rem;
            font-weight: 600;
            white-space: nowrap;
        }

        .badge-success {
            background: rgba(126, 227, 154, 0.16);
            color: var(--accent-green);
            border: 1px solid rgba(126, 227, 154, 0.40);
        }

        .badge-fail {
            background: rgba(255, 133, 133, 0.16);
            color: var(--accent-red);
            border: 1px solid rgba(255, 133, 133, 0.42);
        }

        .badge-pending {
            background: rgba(192, 202, 214, 0.14);
            color: var(--text-sub);
            border: 1px solid rgba(192, 202, 214, 0.34);
        }

        .pipeline-action {
            cursor: pointer;
        }

        .pipeline-action:hover {
            border-color: var(--accent-blue);
            background: linear-gradient(180deg, rgba(123, 199, 255, 0.14), var(--surface-2));
        }

        .modal-backdrop {
            position: fixed;
            inset: 0;
            z-index: 20;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 18px;
            background: rgba(0, 0, 0, 0.62);
        }

        .modal-backdrop.is-open {
            display: flex;
        }

        .modal-panel {
            width: min(1120px, 96vw);
            max-height: 86vh;
            display: grid;
            grid-template-rows: auto minmax(0, 1fr);
            background: var(--surface);
            border: 1px solid var(--border-strong);
            border-radius: 8px;
            box-shadow: 0 22px 60px rgba(0,0,0,0.55);
            overflow: hidden;
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            gap: 12px;
            align-items: center;
            padding: 12px 14px;
            border-bottom: 1px solid var(--border-color);
        }

        .modal-title {
            font-weight: 700;
            font-size: 0.98rem;
        }

        .modal-close {
            border: 1px solid var(--border-color);
            background: var(--surface-2);
            color: var(--text-main);
            border-radius: 6px;
            padding: 6px 10px;
            cursor: pointer;
        }

        .modal-body {
            overflow: auto;
            padding: 12px;
        }

        .pipeline-list {
            display: grid;
            gap: 8px;
        }

        .pipeline-item {
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            gap: 12px;
            padding: 10px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: var(--surface-2);
        }

        .pipeline-item-title {
            font-weight: 700;
            margin-bottom: 4px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .pipeline-item-meta {
            color: var(--text-sub);
            font-size: 0.75rem;
            margin-bottom: 7px;
        }

        .pipeline-preview {
            max-height: 120px;
            overflow: auto;
            white-space: pre-wrap;
            color: #dbe5ef;
            font-size: 0.74rem;
            line-height: 1.45;
            background: #121821;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 8px;
        }

        .pipeline-buttons {
            display: flex;
            flex-direction: column;
            gap: 7px;
            min-width: 74px;
        }

        .action-btn {
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 7px 9px;
            color: var(--text-main);
            background: var(--surface-3);
            cursor: pointer;
            font-weight: 700;
            font-size: 0.76rem;
        }

        .action-btn.approve {
            border-color: rgba(126, 227, 154, 0.58);
            color: var(--accent-green);
        }

        .action-btn.reject {
            border-color: rgba(255, 133, 133, 0.58);
            color: var(--accent-red);
        }

        .modal-note {
            color: var(--text-sub);
            font-size: 0.78rem;
            margin-bottom: 10px;
        }

        @media (max-width: 1280px) {
            .summary-layout,
            .content-layout {
                grid-template-columns: 1fr 1fr;
            }

            .hw-section {
                grid-column: 1 / -1;
            }

            .hw-card .hw-grid {
                grid-template-columns: repeat(6, minmax(0, 1fr));
            }
        }

        @media (max-width: 860px) {
            body {
                padding: 12px;
            }

            .header {
                align-items: flex-start;
                flex-direction: column;
            }

            .header-actions {
                align-items: flex-start;
            }

            .summary-layout,
            .content-layout,
            .ai-activity {
                grid-template-columns: 1fr;
            }

            .metric-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .hw-card .hw-grid,
            .hw-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .progress-info {
                align-items: flex-start;
                flex-direction: column;
                gap: 6px;
            }

            .ai-meta {
                grid-template-columns: 1fr;
            }

            .history-section {
                min-height: 360px;
            }
        }

        @media (max-width: 520px) {
            .metric-grid,
            .hw-card .hw-grid,
            .hw-grid {
                grid-template-columns: 1fr;
            }

            td:first-child {
                max-width: 180px;
            }
        }
    </style>
</head>
<body>
    <!-- 하이테크 실시간 별무리 파티클 배경 -->
    <canvas id="particle-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none; opacity: 0.35;"></canvas>

    <div class="header">
        <div class="header-title">
            <h1>⚕ 아우룸 AI 실시간 관제 시스템 (Aurum Live Monitor)</h1>
            <p>1차 전수조사 진행률 및 시스템 자원 실시간 모니터링 (No Blinking, Low Memory)</p>
        </div>
        <div class="header-actions">
            <div class="live-badge">
                <div class="live-dot"></div>
                <span>LIVE (5s Refresh)</span>
            </div>
            <div class="sync-meta" id="last-sync">동기화 대기</div>
        </div>
    </div>

    <div class="summary-layout">
        <div class="summary-main">
            <!-- 진행 지표 카드 그리드 -->
            <div class="metric-grid">
                <div class="metric-card">
                    <div class="metric-value" id="val-processed">0</div>
                    <div class="metric-label">카탈로그 완료</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value" style="color: var(--accent-green);" id="val-success">0</div>
                    <div class="metric-label">AI 요약 완료</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value" style="color: var(--accent-red);" id="val-failed">0</div>
                    <div class="metric-label">요약 실패</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value" style="color: #dbe5ef;" id="val-remaining">0</div>
                    <div class="metric-label">요약 대기</div>
                </div>
            </div>

            <!-- 진행 바 세션 -->
            <div class="progress-info">
                <div class="progress-title">AI 요약 진행률 <span style="color: var(--text-sub); font-weight: 400; font-size: 0.78rem;" id="catalog-info"></span></div>
                <div class="progress-percentage" id="progress-text">0%</div>
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" id="progress-bar"></div>
            </div>
        </div>

        <!-- 005 아톰·아우룸맥 협업 파이프라인 현황 -->
        <div class="pipeline-panel">
            <div class="progress-info">
                <div class="progress-title">🔄 협업 파이프라인
                    <span style="color: var(--text-sub); font-weight: 400; font-size: 0.76rem;" id="pipe-updated"></span>
                </div>
            </div>
            <div class="hw-grid">
                <div class="hw-metric pipeline-action" data-pipeline-kind="published">
                    <div class="hw-metric-label">배포 완료</div>
                    <div class="hw-metric-value" id="pipe-published" style="color: var(--accent-green);">-</div>
                </div>
                <div class="hw-metric pipeline-action" data-pipeline-kind="admin">
                    <div class="hw-metric-label">승인대기</div>
                    <div class="hw-metric-value" id="pipe-admin" style="color: var(--accent-amber);">-</div>
                </div>
                <div class="hw-metric pipeline-action" data-pipeline-kind="inflight">
                    <div class="hw-metric-label">처리중</div>
                    <div class="hw-metric-value" id="pipe-inflight">-</div>
                </div>
                <div class="hw-metric pipeline-action" data-pipeline-kind="corpus">
                    <div class="hw-metric-label">코퍼스</div>
                    <div class="hw-metric-value" id="pipe-corpus" style="color: var(--accent-blue);">-</div>
                </div>
            </div>
            <div class="service-row">
                <span>아톰: <span id="pipe-svc-atom">-</span></span>
                <span>아우룸맥: <span id="pipe-svc-mac">-</span></span>
            </div>
        </div>
    </div>

    <div class="ai-activity">
        <div class="ai-card" id="atom-ai-card">
            <div class="ai-card-header">
                <span>ATOM AI 작업 현황</span>
                <span class="ai-state" id="atom-ai-state">대기</span>
            </div>
            <div class="ai-task" id="atom-ai-task">신규 파일 감시 중</div>
            <div class="ai-meta">
                <div id="atom-ai-job">작업: -</div>
                <div id="atom-ai-queue">큐: -</div>
                <div id="atom-ai-next">다음: -</div>
                <div id="atom-ai-role">역할: 1차 요약·분류·배정</div>
            </div>
        </div>
        <div class="ai-card" id="mac-ai-card">
            <div class="ai-card-header">
                <span>AURUM MAC AI 작업 현황</span>
                <span class="ai-state" id="mac-ai-state">대기</span>
            </div>
            <div class="ai-task" id="mac-ai-task">작업 슬롯 대기</div>
            <div class="ai-meta">
                <div id="mac-ai-job">작업: -</div>
                <div id="mac-ai-queue">큐: -</div>
                <div id="mac-ai-next">다음: -</div>
                <div id="mac-ai-role">역할: 초안·RAG·검토</div>
            </div>
        </div>
    </div>

    <!-- 하드웨어 자원 및 이력 분할 레이아웃 -->
    <div class="content-layout">
        <!-- 좌측: 하드웨어 리소스 -->
        <div class="hw-section">
            <h2 class="panel-title">⚙️ 실시간 하드웨어 리소스</h2>

            <!-- ATOM SERVER -->
            <div class="hw-card">
                <div class="hw-card-header">
                    <span>🤖 ATOM SERVER (아톰 서버 - 8 Workers)</span>
                    <span style="color: var(--accent-blue)">Online</span>
                </div>
                <div class="hw-grid">
                    <div class="hw-metric">
                        <div class="hw-metric-label">CPU 사용량</div>
                        <div class="hw-metric-value" id="atom-cpu">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">RAM 사용량</div>
                        <div class="hw-metric-value" id="atom-ram">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">CPU 최고온도</div>
                        <div class="hw-metric-value" id="atom-temp">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">GPU 로드율</div>
                        <div class="hw-metric-value" id="atom-gpu-util">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">GPU 온도</div>
                        <div class="hw-metric-value" id="atom-gpu-temp">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">VRAM 점유율</div>
                        <div class="hw-metric-value" id="atom-gpu-vram">-</div>
                    </div>
                </div>
            </div>

            <!-- AURUM MACBOOK -->
            <div class="hw-card">
                <div class="hw-card-header">
                    <span>💻 AURUM MACBOOK (아우룸 맥북)</span>
                    <span style="color: var(--accent-green)" id="mac-title-status">Online</span>
                </div>
                <div class="hw-grid">
                    <div class="hw-metric">
                        <div class="hw-metric-label">맥북 CPU 사용량</div>
                        <div class="hw-metric-value" id="mac-cpu">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">맥북 RAM 사용량</div>
                        <div class="hw-metric-value" id="mac-ram">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">맥북 내부온도</div>
                        <div class="hw-metric-value" id="mac-temp">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">맥북 GPU 사용량</div>
                        <div class="hw-metric-value" id="mac-gpu">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">가공 상태</div>
                        <div class="hw-metric-value" style="font-size: 0.9rem;" id="mac-status">-</div>
                    </div>
                    <div class="hw-metric">
                        <div class="hw-metric-label">Ollama 상태</div>
                        <div class="hw-metric-value" style="font-size: 0.8rem; overflow: hidden; text-overflow: ellipsis;" id="mac-ollama">-</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 가운데: 아우룸 맥북 가공 파일 이력 -->
        <div class="history-section">
            <h2 class="panel-title">💻 AURUM MACBOOK 가공 이력</h2>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>파일명</th>
                            <th>분류군</th>
                            <th>상태</th>
                            <th>시각</th>
                        </tr>
                    </thead>
                    <tbody id="mac-history-table-body">
                        <!-- Javascript 가 실시간 삽입 -->
                    </tbody>
                </table>
            </div>
        </div>

        <!-- 우측: 아톰 서버 가공 파일 이력 -->
        <div class="history-section">
            <h2 class="panel-title">🤖 ATOM SERVER 가공 이력</h2>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>파일명</th>
                            <th>분류군</th>
                            <th>상태</th>
                            <th>시각</th>
                        </tr>
                    </thead>
                    <tbody id="atom-history-table-body">
                        <!-- Javascript 가 실시간 삽입 -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>


    <div class="modal-backdrop" id="pipeline-modal" aria-hidden="true">
        <div class="modal-panel" role="dialog" aria-modal="true" aria-labelledby="pipeline-modal-title">
            <div class="modal-header">
                <div class="modal-title" id="pipeline-modal-title">파이프라인 상세</div>
                <button class="modal-close" id="pipeline-modal-close" type="button">닫기</button>
            </div>
            <div class="modal-body" id="pipeline-modal-body">불러오는 중...</div>
        </div>
    </div>

    <script>
        const numberFromText = (value) => {
            if (value === null || value === undefined) return NaN;
            const matched = String(value).match(/[0-9]+(?:[.][0-9]+)?/);
            return matched ? Number(matched[0]) : NaN;
        };

        const clearState = (el) => {
            if (!el) return;
            el.classList.remove('is-normal', 'is-warn', 'is-critical', 'is-offline');
        };

        const applyState = (el, state) => {
            if (!el) return;
            clearState(el);
            if (state) el.classList.add(state);
        };

        const stateForMetric = (value, kind) => {
            const text = String(value || '');
            const low = text.toLowerCase();
            if (low.includes('offline') || low.includes('n/a') || low.includes('unknown')) return 'is-offline';
            const num = numberFromText(text);
            if (!Number.isFinite(num)) return '';
            if (kind === 'temp') return num >= 82 ? 'is-critical' : (num >= 70 ? 'is-warn' : 'is-normal');
            if (kind === 'load') return num >= 92 ? 'is-critical' : (num >= 80 ? 'is-warn' : 'is-normal');
            if (kind === 'count-risk') return num > 0 ? 'is-warn' : 'is-normal';
            return '';
        };

        const updateMetric = (id, value, kind) => {
            const el = document.getElementById(id);
            if (!el) return;
            el.textContent = value;
            applyState(el.closest('.hw-metric, .metric-card'), stateForMetric(value, kind));
        };

        const updateSyncMeta = (text, isError) => {
            const el = document.getElementById('last-sync');
            if (!el) return;
            el.textContent = text;
            el.classList.toggle('is-error', Boolean(isError));
        };

        const stageLabels = {
            published: '배포 완료',
            admin: '승인대기',
            inflight: '처리중',
            corpus: '클린 코퍼스',
            review: '승인대기',
            drafting: '초안 작성',
            raw: '원문 분석'
        };

        const escapeHtml = (value) => String(value ?? '')
            .replaceAll('&', '&amp;')
            .replaceAll('<', '&lt;')
            .replaceAll('>', '&gt;')
            .replaceAll('"', '&quot;')
            .replaceAll("'", '&#39;');

        const modal = document.getElementById('pipeline-modal');
        const modalTitle = document.getElementById('pipeline-modal-title');
        const modalBody = document.getElementById('pipeline-modal-body');
        const closePipelineModal = () => {
            modal.classList.remove('is-open');
            modal.setAttribute('aria-hidden', 'true');
        };

        const openPipelineModal = async (kind) => {
            modal.classList.add('is-open');
            modal.setAttribute('aria-hidden', 'false');
            modalTitle.textContent = `${stageLabels[kind] || kind} 상세`;
            modalBody.innerHTML = '<div class="modal-note">목록을 불러오는 중입니다...</div>';
            try {
                const response = await fetch(`/api/pipeline?kind=${encodeURIComponent(kind)}`);
                const data = await response.json();
                if (!response.ok || data.ok === false) throw new Error(data.error || '목록 조회 실패');
                const localCount = data.local_count || 0;
                const macPending = Number(data.mac_admin_pending);
                const syncNote = kind === 'admin' && macPending > localCount
                    ? `<div class="modal-note">맥 승인대기 ${macPending.toLocaleString()}건 중 아톰에 동기화된 항목은 ${localCount.toLocaleString()}건입니다. <button class="action-btn" data-action="sync_mac_pending" type="button">맥 승인대기 회수</button></div>`
                    : '';
                const balanceNote = kind === 'inflight'
                    ? '<div class="modal-note">아톰 RAM 사용률 대신 MemAvailable·PSI·swap·맥 큐를 기준으로 점검합니다. <button class="action-btn" data-action="balance_mac_work" type="button">맥 배정 점검</button></div>'
                    : '';
                const rows = (data.items || []).map(renderPipelineItem).join('');
                modalBody.innerHTML = syncNote + balanceNote + (rows || '<div class="modal-note">표시할 로컬 항목이 없습니다.</div>');
            } catch (error) {
                modalBody.innerHTML = `<div class="modal-note">${escapeHtml(error.message)}</div>`;
            }
        };

        const renderPipelineItem = (item) => {
            const actions = item.actionable ? `
                <div class="pipeline-buttons">
                    <button class="action-btn approve" data-action="approve" data-job-id="${escapeHtml(item.job_id)}" type="button">승인</button>
                    <button class="action-btn reject" data-action="reject" data-job-id="${escapeHtml(item.job_id)}" type="button">거절</button>
                </div>` : '<div></div>';
            return `
                <div class="pipeline-item">
                    <div>
                        <div class="pipeline-item-title">${escapeHtml(item.title || item.job_id)}</div>
                        <div class="pipeline-item-meta">${escapeHtml(stageLabels[item.stage] || item.stage)} · ${escapeHtml(item.status || '상태 없음')} · ${escapeHtml(item.updated || '')} · ${escapeHtml(item.job_id)}</div>
                        <div class="pipeline-preview">${escapeHtml(item.preview || '미리보기 없음')}</div>
                    </div>
                    ${actions}
                </div>`;
        };

        const runMacPendingSync = async () => {
            if (!confirm('맥 승인대기 항목을 아톰 승인대기함으로 회수하시겠습니까?')) return;
            modalBody.innerHTML = '<div class="modal-note">맥 승인대기 항목을 회수하는 중입니다...</div>';
            const response = await fetch('/api/pipeline/action', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'sync_mac_pending' })
            });
            const data = await response.json();
            if (!response.ok || data.ok === false) {
                alert(data.error || '맥 승인대기 회수 실패');
                await openPipelineModal('admin');
                return;
            }
            alert(data.message || '맥 승인대기 회수 완료');
            await openPipelineModal('admin');
            await fetchMetrics();
        };

        const runMacWorkBalance = async () => {
            const response = await fetch('/api/pipeline/action', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'balance_mac_work' })
            });
            const data = await response.json();
            if (!response.ok || data.ok === false) {
                alert(data.error || '맥 배정 점검 실패');
                return;
            }
            const selected = (data.selected_jobs || []).join(', ') || '없음';
            alert(`${data.message || '맥 배정 점검 완료'}\n선택 후보: ${selected}\n실제 복사는 수행하지 않았습니다.`);
        };

        const runPipelineAction = async (jobId, action) => {
            const label = action === 'approve' ? '승인' : '거절';
            if (!confirm(`${jobId} 항목을 ${label}하시겠습니까?`)) return;
            const response = await fetch('/api/pipeline/action', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ job_id: jobId, action })
            });
            const data = await response.json();
            if (!response.ok || data.ok === false) {
                alert(data.error || `${label} 실패`);
                return;
            }
            alert(data.message || `${label} 완료`);
            await openPipelineModal('admin');
            await fetchMetrics();
        };

        document.querySelectorAll('[data-pipeline-kind]').forEach((el) => {
            el.addEventListener('click', () => openPipelineModal(el.dataset.pipelineKind));
        });
        document.getElementById('pipeline-modal-close').addEventListener('click', closePipelineModal);
        modal.addEventListener('click', (event) => {
            if (event.target === modal) closePipelineModal();
        });
        modalBody.addEventListener('click', (event) => {
            const syncButton = event.target.closest('[data-action="sync_mac_pending"]');
            if (syncButton) {
                runMacPendingSync();
                return;
            }
            const balanceButton = event.target.closest('[data-action="balance_mac_work"]');
            if (balanceButton) {
                runMacWorkBalance();
                return;
            }
            const button = event.target.closest('[data-action][data-job-id]');
            if (!button) return;
            runPipelineAction(button.dataset.jobId, button.dataset.action);
        });

        const activityLabels = { active: '작업중', waiting: '대기중', idle: '감시중' };
        const updateActivity = (prefix, activity) => {
            const card = document.getElementById(`${prefix}-ai-card`);
            if (!card || !activity) return;
            card.classList.remove('is-active', 'is-waiting');
            if (activity.state === 'active') card.classList.add('is-active');
            if (activity.state === 'waiting') card.classList.add('is-waiting');
            document.getElementById(`${prefix}-ai-state`).textContent = activityLabels[activity.state] || activity.state || '대기';
            document.getElementById(`${prefix}-ai-task`).textContent = activity.headline || '-';
            document.getElementById(`${prefix}-ai-job`).textContent = `작업: ${activity.job || '-'}`;
            document.getElementById(`${prefix}-ai-queue`).textContent = `큐: ${activity.queue || '-'}`;
            document.getElementById(`${prefix}-ai-next`).textContent = `다음: ${activity.next || '-'}`;
        };

        async function fetchMetrics() {
            try {
                const response = await fetch('/api/metrics');
                if (!response.ok) throw new Error('API Response Error');
                const data = await response.json();

                // 1. 최상단 지표 갱신
                updateMetric('val-processed', data.catalogued.toLocaleString(), '');
                updateMetric('val-success', data.summary_done.toLocaleString(), '');
                updateMetric('val-failed', data.summary_failed.toLocaleString(), 'count-risk');
                updateMetric('val-remaining', data.summary_pending.toLocaleString(), '');

                // 2. 진행률 바 갱신 (실제 잔여 작업 = AI 요약 기준, 100% clamp)
                document.getElementById('progress-text').innerText = data.summary_progress + '%';
                document.getElementById('progress-bar').style.width = data.summary_progress + '%';
                document.getElementById('catalog-info').innerText =
                    `· 카탈로그 ${data.catalogued.toLocaleString()}건 (${data.catalog_progress}%)`
                    + (data.extract_failed ? ` · 추출실패 ${data.extract_failed.toLocaleString()}` : '');

                // 3. 아톰 리소스 갱신
                updateMetric('atom-cpu', data.atom.cpu, 'load');
                updateMetric('atom-ram', data.atom.ram, 'load');
                updateMetric('atom-temp', data.atom.temp, 'temp');
                updateMetric('atom-gpu-util', data.atom.gpu_util, 'load');
                updateMetric('atom-gpu-temp', data.atom.gpu_temp, 'temp');
                updateMetric('atom-gpu-vram', data.atom.gpu_vram, '');

                // 4. 맥북 리소스 갱신
                updateMetric('mac-cpu', data.mac.cpu, 'load');
                updateMetric('mac-ram', data.mac.ram, 'load');
                updateMetric('mac-temp', data.mac.temp, 'temp');
                updateMetric('mac-gpu', data.mac.gpu, 'load');
                updateMetric('mac-status', data.mac.status, '');
                updateMetric('mac-ollama', data.mac.ollama, '');

                const macTitle = `💻 AURUM MACBOOK (아우룸 맥북 - ${data.mac.workers} Workers)`;
                document.getElementById('mac-title-status').previousElementSibling.innerText = macTitle;
                document.getElementById('mac-title-status').innerText = data.mac.cpu === 'Offline' ? 'Offline' : 'Online';
                document.getElementById('mac-title-status').style.color = data.mac.cpu === 'Offline' ? 'var(--accent-red)' : 'var(--accent-green)';

                // 4.5 005 협업 파이프라인 현황
                if (data.pipeline) {
                    const pp = data.pipeline;
                    updateMetric('pipe-published', (pp.published || 0).toLocaleString(), '');
                    updateMetric('pipe-admin', (pp.admin_pending >= 0 ? pp.admin_pending : '—'), 'count-risk');
                    updateMetric('pipe-inflight', ((pp.raw||0)+(pp.drafting_atom||0)+(pp.review_pending||0)), '');
                    updateMetric('pipe-corpus', (pp.corpus_docs || 0).toLocaleString(), '');
                    document.getElementById('pipe-updated').innerText = pp.overnight_updated ? ('· 코퍼스 갱신 ' + pp.overnight_updated) : '';
                    const dot = (s) => s === 'active' ? '🟢' : (s === 'stopped' ? '🔴' : '⚪');
                    document.getElementById('pipe-svc-atom').innerText =
                        `엔진${dot(pp.svc_engine)} 추적기${dot(pp.svc_tracker)} 배포기${dot(pp.svc_deployer)}`;
                    document.getElementById('pipe-svc-mac').innerText =
                        `launchd ${pp.mac_launchd === 'active' ? '🟢' : (pp.mac_launchd === 'inactive' ? '🔴' : '⚪')}`
                        + (pp.mac_drafting > 0 ? ` · 초안작성중 ${pp.mac_drafting}` : '')
                        + (pp.mac_updated ? ` (${pp.mac_updated})` : '');
                }

                if (data.ai_activity) {
                    updateActivity('atom', data.ai_activity.atom);
                    updateActivity('mac', data.ai_activity.mac);
                }

                // 5. 가공 이력 테이블 갱신 (부드럽게 각각 덮어쓰기)
                const buildTableRows = (files) => {
                    let html = '';
                    if (files && files.length > 0) {
                        files.forEach(file => {
                            const badgeClass = file.status === '요약완료' ? 'badge-success'
                                : (file.status === '요약대기' ? 'badge-pending' : 'badge-fail');
                            html += `
                                <tr>
                                    <td>${file.filename}</td>
                                    <td>${file.category}</td>
                                    <td><span class="badge ${badgeClass}">${file.status}</span></td>
                                    <td>${file.time}</td>
                                </tr>
                            `;
                        });
                    } else {
                        html = '<tr><td colspan="4" style="text-align: center; color: var(--text-sub);">실시간 대기 중...</td></tr>';
                    }
                    return html;
                };

                document.getElementById('mac-history-table-body').innerHTML = buildTableRows(data.recent_files_mac);
                document.getElementById('atom-history-table-body').innerHTML = buildTableRows(data.recent_files_atom);
                updateSyncMeta('마지막 동기화 ' + new Date().toLocaleTimeString('ko-KR', { hour12: false }), false);

            } catch (error) {
                updateSyncMeta('동기화 실패', true);
                console.error("Failed to sync metrics:", error);
            }
        }

        // 초기 로드 후 5초마다 깜빡임 없이 데이터만 리액티브 갱신
        fetchMetrics();
        setInterval(fetchMetrics, 5000);

        // 운영 관제형 화면에서는 장식 애니메이션을 비활성화한다.
        const canvas = document.getElementById('particle-canvas');
        if (canvas) canvas.width = canvas.height = 0;
    </script>
</body>
</html>
"""

def run(server_class=HTTPServer, handler_class=LiveMonitorHandler, port=8502):
    # 백그라운드 캐시 수집 데몬 활성화
    t = threading.Thread(target=cache_updater_loop, daemon=True)
    t.start()

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[Live Server Started] Serving Live Dashboard on port {port}...", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("[Live Server Stopped]")

if __name__ == '__main__':
    run()
