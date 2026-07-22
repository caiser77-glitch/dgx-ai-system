#!/usr/bin/env python3
# 007 — HWPX backfill: PK포맷(HWPX) 문서 본문 회복. hwp5txt 소진분(<1500B) 대상.
# Created: 2026-07-23 by Antigravity(Claude Opus 4.8)
# ai_classification 보존, outputs.text 만 실본문으로 갱신. idempotent(hwpx_extracted 마커).
import json, glob, os, sys
sys.path.insert(0, "/home/caiser77/AI_BASE")
from extract_hwpx import extract_hwpx
MD = "/home/caiser77/dgx_workspace/data/processed/metadata"
TEXTDIR = "/home/caiser77/dgx_workspace/data/processed/text"
MIN = 1500
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
dry = "--dry" in sys.argv

def cur_size(tp):
    return os.path.getsize(tp) if (tp and os.path.exists(tp)) else 0

done = fail = scanned = skip = 0
for p in glob.iglob(MD + "/*.metadata.json"):
    scanned += 1
    try:
        m = json.load(open(p, encoding="utf-8"))
    except Exception:
        continue
    sp = m.get("source_path", "")
    if not sp.lower().endswith(".hwpx") or not os.path.exists(sp):
        continue
    tp = (m.get("outputs") or {}).get("text")
    if cur_size(tp) >= MIN:
        continue                      # 이미 정상
    if m.get("hwpx_extracted"):
        skip += 1
        continue                      # 시도완료 — 재시도 방지
    if dry:
        done += 1
        if done >= limit: break
        continue
    try:
        text = extract_hwpx(sp).strip()
    except Exception:
        text = ""
    if len(text.encode("utf-8")) >= 20:
        if not tp:
            tp = os.path.join(TEXTDIR, os.path.basename(p).replace(".metadata.json", ".txt"))
            m.setdefault("outputs", {})["text"] = tp
        open(tp, "w", encoding="utf-8").write(text + "\n")
        m["hwpx_extracted"] = True
        m.pop("extract_exhausted", None)      # hwp5txt 소진마커 해제(회복됨)
        done += 1
    else:
        fail += 1
        m["hwpx_extracted"] = True             # 빈 결과여도 시도완료 기록
    json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if done >= limit:
        break
print(json.dumps({"scanned": scanned, "reextracted": done, "failed": fail, "skipped": skip, "dry": dry}, ensure_ascii=False))
