#!/usr/bin/env python3
# 006 — 실패한 HWP 재추출(backfill). ai_classification 보존, outputs.text 만 실본문으로 갱신.
# Created: 2026-07-22 by Antigravity(Claude Opus 4.8)
# Updated: 2026-07-23 by Antigravity(Claude Opus 4.8) — churn 버그 수정:
#   쓰기문턱(20B)≠실패판정문턱(1500B) 불일치로 <1500B 소진문서를 매 배치 영구 재선택하던 문제.
#   hwp5txt 소진(짧은본문/하드실패) 문서에 extract_exhausted="hwp5txt" 마커 → 재선택 제외.
import json, glob, os, subprocess, sys, time
MD = "/home/caiser77/dgx_workspace/data/processed/metadata"
TEXTDIR = "/home/caiser77/dgx_workspace/data/processed/text"
BIN = "/home/caiser77/hwp_extract_venv/bin/hwp5txt"
MIN = 1500
FAIL_MARK = ("unsupported_file_type", "추출이 지원되지 않", "content_extraction: unsupported")
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 50
dry = "--dry" in sys.argv

def failed(tp):
    if not tp or not os.path.exists(tp):
        return True
    if os.path.getsize(tp) >= MIN:
        try:
            if not any(k in open(tp, encoding="utf-8", errors="ignore").read(1200) for k in FAIL_MARK):
                return False
        except Exception:
            return True
    return True

def save_meta(p, m):
    json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

done = fail = scanned = skipped = 0
for p in glob.iglob(MD + "/*.metadata.json"):
    scanned += 1
    try:
        m = json.load(open(p, encoding="utf-8"))
    except Exception:
        continue
    sp = m.get("source_path", "")
    if not sp.lower().endswith(".hwp") or not os.path.exists(sp):
        continue
    tp = (m.get("outputs") or {}).get("text")
    if not failed(tp):
        continue                      # 이미 정상
    if m.get("extract_exhausted") == "hwp5txt":
        skipped += 1                  # hwp5txt 소진 — 재시도 무의미(후속 HWPX/OCR 대상)
        continue
    if dry:
        done += 1
        if done >= limit: break
        continue
    try:
        r = subprocess.run([BIN, sp], capture_output=True, text=True, timeout=300)
        text = (r.stdout or "").strip()
    except Exception:
        r = None
        text = ""
    if r is not None and r.returncode == 0 and len(text) >= 20:
        if not tp:
            tp = os.path.join(TEXTDIR, os.path.basename(p).replace(".metadata.json", ".txt"))
            m.setdefault("outputs", {})["text"] = tp
        open(tp, "w", encoding="utf-8").write(text + "\n")
        done += 1
        # 짧은 본문(<1500B)이면 hwp5txt 한계 도달 — 재선택 방지
        if len((text + "\n").encode("utf-8")) < MIN:
            m["extract_exhausted"] = "hwp5txt"
        save_meta(p, m)
    else:
        # hwp5txt가 아예 못 뚫음(HWPX/구형3.x/이미지스캔) — 재선택 방지 + 후속 OCR/HWPX 라우팅 대상
        fail += 1
        m["extract_exhausted"] = "hwp5txt"
        save_meta(p, m)
    if done >= limit:
        break
print(json.dumps({"scanned": scanned, "reextracted": done, "failed": fail, "skipped_exhausted": skipped, "dry": dry}, ensure_ascii=False))
