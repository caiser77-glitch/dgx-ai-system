#!/usr/bin/env python3
# Created: 2026-07-05 by Antigravity AI
# Purpose: Micro responsive live web dashboard server for Aurum Live Monitoring (No Blinking, Low Memory)

import os
import sys
import json
import time
import glob
import subprocess
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

# 경로 바인딩
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
METADATA_DIR = PROCESSED_DIR / "metadata"
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
    if not summary_block:
        return "pending"
    summ = summary_block.get("summary")
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
        "drafting_atom": cnt("02_drafting"),
        "review_pending": cnt("03_review_pending"),
        "published": cnt("04_published"),
        "nas_deliverables": nas,
        "corpus_docs": corpus,
        "overnight_updated": overnight,
        "svc_engine": _proc_alive("pipeline_engine.py"),
        "svc_tracker": _proc_alive("track_pipeline_status.py"),
        "svc_deployer": _proc_alive("aurum_deployer.py"),
        "admin_pending": mac.get("admin_pending", -1),
        "mac_drafting": mac.get("drafting", -1),
        "mac_launchd": mac.get("launchd", "unknown"),
        "mac_updated": mac.get("updated", ""),
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
        "pipeline": get_pipeline_status()
    }

# 전역 캐시 딕셔너리 및 동기화 락
import threading
cached_data = {
    "catalogued": 0, "summary_done": 0, "summary_failed": 0, "summary_pending": 0, "extract_failed": 0,
    "summary_progress": 0.0, "catalog_progress": 0.0, "total_target": TOTAL_FILES,
    "atom": {"cpu": "N/A", "ram": "N/A", "temp": "N/A", "gpu_util": "N/A", "gpu_vram": "N/A", "gpu_temp": "N/A"},
    "mac": {"cpu": "Offline", "ram": "Offline", "gpu": "Offline", "temp": "Offline", "status": "Offline", "ollama": "Offline", "workers": 0},
    "recent_files_mac": [], "recent_files_atom": [],
    "pipeline": {"raw": 0, "drafting_atom": 0, "review_pending": 0, "published": 0, "nas_deliverables": 0,
                 "corpus_docs": 0, "overnight_updated": "", "svc_engine": "unknown", "svc_tracker": "unknown",
                 "svc_deployer": "unknown", "admin_pending": -1, "mac_drafting": -1, "mac_launchd": "unknown", "mac_updated": ""}
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

class LiveMonitorHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # 로그 출력 억제하여 디스크 I/O 절약

    def do_GET(self):
        if self.path == "/api/metrics":
            try:
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(cached_data, ensure_ascii=False).encode("utf-8"))
            except (ConnectionError, BrokenPipeError):
                pass # 브라우저 중도 이탈로 인한 BrokenPipeError 예방 (서버 멈춤 완전 차단)
            except Exception as e:
                print(f"[API Response Error] {e}", file=sys.stderr)
        elif self.path == "/" or self.path == "/index.html":
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
            .content-layout {
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
                <div class="hw-metric">
                    <div class="hw-metric-label">배포 완료</div>
                    <div class="hw-metric-value" id="pipe-published" style="color: var(--accent-green);">-</div>
                </div>
                <div class="hw-metric">
                    <div class="hw-metric-label">승인대기</div>
                    <div class="hw-metric-value" id="pipe-admin" style="color: var(--accent-amber);">-</div>
                </div>
                <div class="hw-metric">
                    <div class="hw-metric-label">처리중</div>
                    <div class="hw-metric-value" id="pipe-inflight">-</div>
                </div>
                <div class="hw-metric">
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
