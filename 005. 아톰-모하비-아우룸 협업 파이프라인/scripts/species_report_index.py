# 코퍼스에서 각 종이 확인된 사내 보고서 목록을 산출(깨끗한 provenance).
import os, re, json, glob, sys
CORPUS = "/home/caiser77/AI_BASE/clean_corpus"
species = sys.argv[1:]
idx = {s: [] for s in species}
for jf in glob.glob(CORPUS + "/*.json"):
    try: meta = json.load(open(jf, encoding="utf-8"))
    except Exception: continue
    path = meta.get("path", ""); name = os.path.basename(path)
    det = set(meta.get("protected_species", []))
    tf = jf[:-5] + ".txt"
    txt = ""
    if os.path.exists(tf):
        try: txt = open(tf, encoding="utf-8", errors="ignore").read()
        except Exception: pass
    for s in species:
        if s in det or (s in txt):
            if name and name not in [r["report"] for r in idx[s]]:
                # 사업/연도 추정(경로에서)
                seg = ""
                m = re.search(r'/mnt/nas\d+/([^/]+)/([^/]+)/', path)
                if m: seg = f"{m.group(1)} · {m.group(2)}"
                idx[s].append({"report": name, "project": seg})
print(json.dumps(idx, ensure_ascii=False))
