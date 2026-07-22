#!/usr/bin/env python3
# 005 파이프라인 — 자동 투입기(auto-feeder). 아톰/맥이 유휴로 멈추지 않도록
# 처리완료 코퍼스에서 미투입 성공문서를 골라 01_raw_analyzed 로 상시 투입한다.
# Created: 2026-07-22 by Antigravity(Claude Opus 4.8)
# 정책(핸드오프 #4): 시간대별 목표재고 유지 + 미승인 상한 역압 + 재투입 방지 + 정결후보만.
#   - 주간(06~21시) 목표 AUTOFEED_TARGET_DAY, 야간(21~06시) AUTOFEED_TARGET_NIGHT 까지 채움
#   - admin_pending >= AUTOFEED_MAX_ADMIN_PENDING 이면 hold(검토 적체 방지)
#   - 한 번 투입한 job_id 는 ledger 로 영구 제외 → published 후 파일이 빠져도 재투입 안 함
#   - git/objects/quarantine/시스템 경로·UNKNOWN·요약없음·비문서 제외
# 사용: pipeline_autofeeder.py [--execute] [--verbose]   (--execute 없으면 dry-run: 판단만 출력)
import os
import re
import sys
import json
import glob
import time
import subprocess

ATOM_ROOT = os.environ.get("ATOM_PIPELINE_ROOT", "/home/caiser77/AI_BASE")
PROCESSED_DIR = os.environ.get("AUTOFEED_PROCESSED_DIR", "/home/caiser77/dgx_workspace/data/processed")
EXPORT_SCRIPT = os.environ.get(
    "AUTOFEED_EXPORT_SCRIPT",
    "/home/caiser77/dgx_workspace/005. 아톰-모하비-아우룸 협업 파이프라인/scripts/export_processed_to_pipeline.py")
LEDGER = os.environ.get("AUTOFEED_LEDGER", os.path.join(ATOM_ROOT, "autofeed_ledger.txt"))
STATUS_FILE = os.environ.get("AUTOFEED_STATUS_FILE", os.path.join(ATOM_ROOT, "autofeed_status.json"))
MAC_STATUS_FILE = os.environ.get("PIPELINE_MAC_STATUS_FILE", os.path.join(ATOM_ROOT, "pipeline_mac_status.json"))
DASHBOARD_API = os.environ.get("AUTOFEED_DASHBOARD_API", "http://127.0.0.1:8502/api/metrics")

# 1차 목표(레퍼런스 구축)는 작업량 제한 없이 최대 처리 — 주/야 구분 없이 동일 고재고 버퍼로
# 파이프라인을 상시 포화시킨다. 실제 처리속도는 모하비 초안 동시성이 상한이므로 재고를 크게
# 잡아도 01_raw 가 과도히 불어나지 않는 선에서 맥/아톰이 절대 굶지 않게 한다.
TARGET_DAY = int(os.environ.get("AUTOFEED_TARGET_DAY", "12"))
TARGET_NIGHT = int(os.environ.get("AUTOFEED_TARGET_NIGHT", "12"))
# 승인대기 상한: 지금 코퍼스는 대부분 참고용이라 승인 대상이 적음 → 사실상 역압 완화(안전선만 유지).
MAX_ADMIN_PENDING = int(os.environ.get("AUTOFEED_MAX_ADMIN_PENDING", "30"))
MAX_PER_RUN = int(os.environ.get("AUTOFEED_MAX_PER_RUN", "8"))
NIGHT_START = int(os.environ.get("AUTOFEED_NIGHT_START", "21"))
NIGHT_END = int(os.environ.get("AUTOFEED_NIGHT_END", "6"))

# 재고(in-flight) = 아직 처리 중인 단계만. 완료(published/NAS)는 재투입 제외용으로만 집계.
STAGES_INFLIGHT = ("01_raw_analyzed", "02_drafting", "03_review_pending")
STAGES_DONE = ("04_published", "NAS_Distribution")
BAD_PATH = ("/git/", ".git/", "/objects/", "_quarantine", "_AURUM_AI_PROCESSED",
            "recycle", "RECYCLE", ".Trash", "AppleDouble")
DOCEXT = (".hwp", ".hwpx", ".pdf", ".docx", ".doc")


def job_id_from_file(fname):
    for suf in (".summary.md", ".result.json", ".draft.md", ".metadata.json"):
        if fname.endswith(suf):
            return fname[: -len(suf)]
    return fname.split(".")[0]


def _ids_in(stages):
    ids = set()
    for st in stages:
        d = os.path.join(ATOM_ROOT, st)
        if os.path.isdir(d):
            for f in os.listdir(d):
                ids.add(job_id_from_file(f))
    return ids


def inflight_ids():
    """진행 중(raw+drafting+review) 잡 — 목표재고 판정용.
    완료(published/NAS)와 중복되는 stale 파일은 제외(대시보드 카운트와 동일 정의)."""
    return _ids_in(STAGES_INFLIGHT) - _ids_in(STAGES_DONE)


def all_stage_ids():
    """전 단계(완료 포함) 잡 — 재투입 제외용."""
    return _ids_in(STAGES_INFLIGHT + STAGES_DONE)


def load_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8") as f:
            return set(l.strip() for l in f if l.strip())
    return set()


def append_ledger(job_ids):
    with open(LEDGER, "a", encoding="utf-8") as f:
        for j in job_ids:
            f.write(j + "\n")


def read_mac_admin_pending():
    """balancer 가 2분마다 갱신하는 mac 상태에서 맥 미승인 수를 읽는다(없으면 0)."""
    try:
        m = json.load(open(MAC_STATUS_FILE, encoding="utf-8"))
        v = int(m.get("admin_pending", 0))
        return v if v > 0 else 0
    except Exception:
        return 0


def read_total_admin_pending():
    """사람 승인이 필요한 총 대기(총 승인대기)를 반환. (total, atom_review) 튜플.
    조화의 핵심: 대시보드가 계산한 정본값(pipeline.total_admin_pending)을 그대로 읽어
    역압 기준과 화면 숫자가 항상 일치하게 한다. API 불가 시에만 로컬 추정으로 폴백."""
    try:
        import urllib.request
        with urllib.request.urlopen(DASHBOARD_API, timeout=3) as r:
            p = json.load(r).get("pipeline", {})
            t = p.get("total_admin_pending")
            a = p.get("admin_pending", 0)
            if isinstance(t, int) and t >= 0:
                return t, (a if isinstance(a, int) and a >= 0 else 0)
    except Exception:
        pass
    # 폴백: published/NAS 중복 제외한 아톰 review + 맥 admin (대시보드 미가동 시)
    atom_review = len(_ids_in(("03_review_pending",)) - _ids_in(STAGES_DONE))
    return atom_review + read_mac_admin_pending(), atom_review


def is_night(h):
    if NIGHT_START <= NIGHT_END:
        return NIGHT_START <= h < NIGHT_END
    return h >= NIGHT_START or h < NIGHT_END   # 자정 넘김(21~06)


# ── 보호종·동식물상 우선 선별(1차 목표: 생태 보고서 레퍼런스) ──
# taxon_group 은 대부분 비어 있으므로 class_name·tags·summary·파일명 텍스트로 판정.
PROTECTED_KW = re.compile(r"법정보호종|멸종위기|천연기념물|보호종|멸종위기야생생물|적색목록|국가적색|지정관리")
FAUNA_KW = re.compile(
    r"동식물상|동물상|식물상|생물상|생태|서식|저감|환경영향|자연환경|훼손|생물다양성|"
    r"조류|포유류|포유동물|양서|파충|어류|어류상|곤충|저서|육수|식생|식물군|플랑크톤|부착조류|"
    r"멸종위기|보호종|천연기념물")
NONFAUNA_KW = re.compile(
    r"설계도|제안서|VE|터널|굴착|지보|순서도|측량|토양|지형지질|지질|상세도|개황도|조경|"
    r"영수증|회계|계약|견적|시방서|내역서|구조계산|공정표|도로건설|포장|교량|옹벽")
SCAN_BUDGET = int(os.environ.get("AUTOFEED_SCAN_BUDGET", "3000"))
# 추출 본문 최소 크기(바이트). 이하이거나 실패마커 포함이면 빈 문서로 보고 투입 제외.
MIN_TEXT_BYTES = int(os.environ.get("AUTOFEED_MIN_TEXT_BYTES", "1500"))
EXTRACT_FAIL_MARKERS = ("unsupported_file_type", "추출이 지원되지 않", "내용 분석은 불가능",
                        "content_extraction: unsupported")


def fauna_score(aic, name):
    """3=법정보호종 신호, 2=동식물상/생태조사, 1=일반, 0=비-fauna(설계·회계 등 후순위)."""
    blob = " ".join([
        str(aic.get("class_name") or ""),
        " ".join(aic.get("tags") or []),
        str(aic.get("summary") or ""),
        str(aic.get("document_type") or ""),
        name,
    ])
    if PROTECTED_KW.search(blob):
        return 3
    if FAUNA_KW.search(blob):
        return 2
    if NONFAUNA_KW.search(blob):
        return 0
    return 1


def find_candidates(need, exclude):
    """정결·성공·미투입 문서를 보호종>동식물상>일반 순으로 선별.
    점수>=2(fauna) 후보가 need 개 모이면 조기 종료(빠름). 부족하면 SCAN_BUDGET까지
    훑어 하위 tier(일반→비-fauna)로 폴백해 파이프라인이 굶지 않게 채운다."""
    md = os.path.join(PROCESSED_DIR, "metadata")
    tiers = {3: [], 2: [], 1: [], 0: []}
    scanned = 0
    for p in glob.iglob(md + "/*.metadata.json"):
        scanned += 1
        stem = os.path.basename(p)[: -len(".metadata.json")]
        if stem in exclude:
            continue
        try:
            m = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        if m.get("status") != "success":
            continue
        sp = m.get("source_path") or ""
        name = m.get("source_name") or os.path.basename(sp)
        if any(b in sp for b in BAD_PATH):
            continue
        if os.path.splitext(name)[1].lower() not in DOCEXT:
            continue
        aic = m.get("ai_classification") or {}
        cls = (aic.get("class_name") or "").upper()
        summ = aic.get("summary") or ""
        if cls == "UNKNOWN" or not str(summ).strip():
            continue
        # ★ 본문 추출 실재 검증: 추출된 text 파일이 충분히 커야 함(HWP unsupported 등 빈 문서 제외).
        #   코퍼스 96%가 추출실패 보일러플레이트(~110~665B)라, 이걸 투입하면 mohave가 빈 보고서를 씀.
        tpath = (m.get("outputs") or {}).get("text")
        if not tpath or not os.path.exists(tpath) or os.path.getsize(tpath) < MIN_TEXT_BYTES:
            continue
        try:
            head = open(tpath, encoding="utf-8", errors="ignore").read(1200)
        except Exception:
            continue
        if any(k in head for k in EXTRACT_FAIL_MARKERS):   # 추출 실패 마커
            continue
        sc = fauna_score(aic, name)
        tiers[sc].append((p, name, sc))
        # 보호종+동식물상(>=2)만으로 need 채워지면 즉시 종료(우선 목표 달성)
        if len(tiers[3]) + len(tiers[2]) >= need:
            break
        if scanned >= SCAN_BUDGET:
            break
    ranked = tiers[3] + tiers[2] + tiers[1] + tiers[0]
    return ranked[:need], scanned


def write_status(payload):
    payload["updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(STATUS_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False)
    except Exception:
        pass


def main():
    execute = "--execute" in sys.argv
    verbose = "--verbose" in sys.argv

    inflight_set = inflight_ids()
    ledger = load_ledger()
    inflight = len(inflight_set)
    admin_pending, atom_review = read_total_admin_pending()   # 총 승인대기(아톰+맥), 아톰 내역
    h = time.localtime().tm_hour
    target = TARGET_NIGHT if is_night(h) else TARGET_DAY

    base = {
        "inflight": inflight, "target": target, "admin_pending": admin_pending,
        "admin_atom": atom_review, "admin_mac": admin_pending - atom_review,
        "night": is_night(h), "mode": "execute" if execute else "dry-run",
    }

    # 역압 1: 사람 승인이 필요한 총 대기가 상한 이상이면 투입 중단(검토 적체 방지)
    if admin_pending >= MAX_ADMIN_PENDING:
        base.update(decision="hold", reason="총 승인대기(아톰%d+맥%d)=%d ≥ 상한 %d — 검토 대기"
                    % (atom_review, admin_pending - atom_review, admin_pending, MAX_ADMIN_PENDING), fed=[])
        write_status(base); print(json.dumps(base, ensure_ascii=False)); return

    # 역압 2: 목표재고 충족
    need = min(target - inflight, MAX_PER_RUN)
    if need <= 0:
        base.update(decision="hold", reason="재고 %d ≥ 목표 %d — 투입 불필요" % (inflight, target), fed=[])
        write_status(base); print(json.dumps(base, ensure_ascii=False)); return

    exclude = all_stage_ids() | ledger
    cands, scanned = find_candidates(need, exclude)
    if not cands:
        base.update(decision="hold", reason="미투입 정결후보 없음(scanned=%d)" % scanned, fed=[])
        write_status(base); print(json.dumps(base, ensure_ascii=False)); return

    fed_ids = [os.path.basename(p)[: -len(".metadata.json")] for p, _, _ in cands]
    scores = [s for _, _, s in cands]
    tiers = {"보호종": scores.count(3), "동식물상": scores.count(2), "일반": scores.count(1), "기타": scores.count(0)}
    if not execute:
        base.update(decision="would-feed", reason="투입 후보 %d건(dry-run)" % len(cands),
                    fed=fed_ids, names=[n for _, n, _ in cands], tiers=tiers, scanned=scanned)
        write_status(base); print(json.dumps(base, ensure_ascii=False)); return

    cmd = ["python3", EXPORT_SCRIPT, "--processed-dir", PROCESSED_DIR, "--pipeline-root", ATOM_ROOT]
    for p, _, _ in cands:
        cmd += ["--metadata-file", p]
    r = subprocess.run(cmd, capture_output=True, text=True)
    ok = (r.returncode == 0)
    if ok:
        append_ledger(fed_ids)   # 성공분만 원장에 기록 → 재투입 영구 차단
    base.update(decision="feed" if ok else "error",
                reason=("투입 %d건 완료(보호종%d·동식물상%d)" % (len(fed_ids), tiers["보호종"], tiers["동식물상"])) if ok else ("export 실패 rc=%d: %s" % (r.returncode, r.stderr[-200:])),
                fed=fed_ids, names=[n for _, n, _ in cands], tiers=tiers, scanned=scanned)
    write_status(base)
    print(json.dumps(base, ensure_ascii=False))
    if verbose:
        sys.stderr.write(r.stdout + "\n" + r.stderr + "\n")


if __name__ == "__main__":
    main()
