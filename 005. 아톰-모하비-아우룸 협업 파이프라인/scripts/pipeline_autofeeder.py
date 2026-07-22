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

TARGET_DAY = int(os.environ.get("AUTOFEED_TARGET_DAY", "3"))
TARGET_NIGHT = int(os.environ.get("AUTOFEED_TARGET_NIGHT", "8"))
MAX_ADMIN_PENDING = int(os.environ.get("AUTOFEED_MAX_ADMIN_PENDING", "5"))
MAX_PER_RUN = int(os.environ.get("AUTOFEED_MAX_PER_RUN", "4"))
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
    """진행 중(raw+drafting+review) 잡 — 목표재고 판정용."""
    return _ids_in(STAGES_INFLIGHT)


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


def read_admin_pending():
    """balancer 가 2분마다 갱신하는 mac 상태에서 미승인 수를 읽는다(없으면 0)."""
    try:
        m = json.load(open(MAC_STATUS_FILE, encoding="utf-8"))
        return int(m.get("admin_pending", 0))
    except Exception:
        return 0


def is_night(h):
    if NIGHT_START <= NIGHT_END:
        return NIGHT_START <= h < NIGHT_END
    return h >= NIGHT_START or h < NIGHT_END   # 자정 넘김(21~06)


def find_candidates(need, exclude):
    """정결·성공·미투입 문서 metadata 경로를 need 개 찾는다(충분히 모이면 조기 종료)."""
    md = os.path.join(PROCESSED_DIR, "metadata")
    out = []
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
        out.append((p, name))
        if len(out) >= need:
            break
    return out, scanned


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
    admin_pending = read_admin_pending()
    h = time.localtime().tm_hour
    target = TARGET_NIGHT if is_night(h) else TARGET_DAY

    base = {
        "inflight": inflight, "target": target, "admin_pending": admin_pending,
        "night": is_night(h), "mode": "execute" if execute else "dry-run",
    }

    # 역압 1: 미승인 적체
    if admin_pending >= MAX_ADMIN_PENDING:
        base.update(decision="hold", reason="미승인(admin_pending) %d ≥ 상한 %d — 검토 대기" % (admin_pending, MAX_ADMIN_PENDING), fed=[])
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

    fed_ids = [os.path.basename(p)[: -len(".metadata.json")] for p, _ in cands]
    if not execute:
        base.update(decision="would-feed", reason="투입 후보 %d건(dry-run)" % len(cands),
                    fed=fed_ids, names=[n for _, n in cands], scanned=scanned)
        write_status(base); print(json.dumps(base, ensure_ascii=False)); return

    cmd = ["python3", EXPORT_SCRIPT, "--processed-dir", PROCESSED_DIR, "--pipeline-root", ATOM_ROOT]
    for p, _ in cands:
        cmd += ["--metadata-file", p]
    r = subprocess.run(cmd, capture_output=True, text=True)
    ok = (r.returncode == 0)
    if ok:
        append_ledger(fed_ids)   # 성공분만 원장에 기록 → 재투입 영구 차단
    base.update(decision="feed" if ok else "error",
                reason=("투입 %d건 완료" % len(fed_ids)) if ok else ("export 실패 rc=%d: %s" % (r.returncode, r.stderr[-200:])),
                fed=fed_ids, names=[n for _, n in cands], scanned=scanned)
    write_status(base)
    print(json.dumps(base, ensure_ascii=False))
    if verbose:
        sys.stderr.write(r.stdout + "\n" + r.stderr + "\n")


if __name__ == "__main__":
    main()
