#!/usr/bin/env python3
# 006 — 실패한 HWP 재추출(backfill). ai_classification 보존, outputs.text 만 실본문으로 갱신.
# Created: 2026-07-22 by Antigravity(Claude Opus 4.8)
import json, glob, os, subprocess, sys, time
MD = "/home/caiser77/dgx_workspace/data/processed/metadata"
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

done = fail = scanned = 0
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
    if dry:
        done += 1
        if done >= limit: break
        continue
    try:
        r = subprocess.run([BIN, sp], capture_output=True, text=True, timeout=300)
        text = (r.stdout or "").strip()
        if r.returncode == 0 and len(text) >= 20:
            if not tp:
                tp = os.path.join("/home/caiser77/dgx_workspace/data/processed/text",
                                  os.path.basename(p).replace(".metadata.json", ".txt"))
                m.setdefault("outputs", {})["text"] = tp
                json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            open(tp, "w", encoding="utf-8").write(text + "\n")
            done += 1
        else:
            fail += 1
    except Exception:
        fail += 1
    if done >= limit:
        break
print(json.dumps({"scanned": scanned, "reextracted": done, "failed": fail, "dry": dry}, ensure_ascii=False))
