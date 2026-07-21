import os, re, json, glob, sys
CORPUS = "/home/caiser77/AI_BASE/clean_corpus"
KW = re.compile(r'서식|이주|저감|웅덩이|산란|서식지|둥지|번식|출현|개체|이동|보호|펜스|울타리|모니터링|확인|번식지|월동')
JUNK = re.compile(r'file://|\.xlsx|\.hwp|열기\]|겉표지|제출기관|목차|http')
species = sys.argv[1:]
result = {s: [] for s in species}
seen = {s: set() for s in species}
meta = {}
for jf in glob.glob(CORPUS + "/*.json"):
    try: meta[jf[:-5]] = json.load(open(jf, encoding="utf-8")).get("path", "")
    except Exception: pass
for tf in glob.glob(CORPUS + "/*.txt"):
    try: txt = open(tf, encoding="utf-8", errors="ignore").read()
    except Exception: continue
    src = os.path.basename(meta.get(tf[:-4], "")) or os.path.basename(tf)
    for s in species:
        if s not in txt or len(result[s]) >= 6: continue
        for m in re.finditer(re.escape(s), txt):
            i = m.start()
            w = re.sub(r'\s+', ' ', txt[max(0, i-100):i+200]).strip()
            if not (30 <= len(w) <= 260) or not KW.search(w) or JUNK.search(w): continue
            k = w[:45]
            if k in seen[s]: continue
            seen[s].add(k); result[s].append({"text": w, "src": src})
            if len(result[s]) >= 6: break
print(json.dumps(result, ensure_ascii=False))
