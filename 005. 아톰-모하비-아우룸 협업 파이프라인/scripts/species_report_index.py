# 코퍼스에서 각 종이 확인된 사내 보고서 목록을 산출(깨끗한 provenance).
# Updated: 2026-07-22 by Antigravity(Claude Opus 4.8) — 보호종 부분일치 오탐 제거(위치기반 standalone).
import os, re, json, glob, sys, unicodedata
CORPUS = "/home/caiser77/AI_BASE/clean_corpus"
species = sys.argv[1:]
idx = {s: [] for s in species}

# 흡수 집합: 전체 법정보호종명(짧은 종명이 더 긴 종명에 흡수됐는지 판정용)
def _load_protected():
    for p in ("/home/caiser77/AI_BASE/protected_species.json",
              "/home/caiser77/dgx_workspace/data/protected_species.json"):
        if os.path.exists(p):
            try:
                d = json.load(open(p, encoding="utf-8"))
                keys = d.keys() if isinstance(d, dict) else \
                    [(it.get("name") or it.get("국명") or it) if isinstance(it, dict) else it for it in d]
                return {unicodedata.normalize("NFC", str(k)) for k in keys if k and len(str(k)) >= 2}
            except Exception:
                pass
    return set()

PROT = _load_protected() | set(species)


def standalone_in(s, text):
    """s가 text에 등장하되, 더 긴 보호종명에 흡수되지 않는 단독 등장이 하나라도 있으면 True.
    예: '재두루미'만 있으면 '두루미'는 False, '두루미'가 단독 등장하면 True."""
    if not text or s not in text:
        return False
    longer = [t for t in PROT if t != s and s in t]
    idx0 = 0
    while True:
        i = text.find(s, idx0)
        if i < 0:
            return False
        absorbed = False
        for t in longer:
            j = text.find(t)
            while j >= 0:
                if j <= i and i + len(s) <= j + len(t):
                    absorbed = True
                    break
                j = text.find(t, j + 1)
            if absorbed:
                break
        if not absorbed:
            return True
        idx0 = i + 1


for jf in glob.glob(CORPUS + "/*.json"):
    try:
        meta = json.load(open(jf, encoding="utf-8"))
    except Exception:
        continue
    path = meta.get("path", "")
    name = os.path.basename(path)
    det = set(meta.get("protected_species", []))
    tf = jf[:-5] + ".txt"
    txt = ""
    if os.path.exists(tf):
        try:
            txt = open(tf, encoding="utf-8", errors="ignore").read()
        except Exception:
            pass
    for s in species:
        # 본문(txt) 있으면 위치기반 검증, 없으면 메타데이터 det 폴백
        matched = standalone_in(s, txt) if txt else (s in det)
        if matched and name and name not in [r["report"] for r in idx[s]]:
            seg = ""
            m = re.search(r'/mnt/nas\d+/([^/]+)/([^/]+)/', path)
            if m:
                seg = f"{m.group(1)} · {m.group(2)}"
            idx[s].append({"report": name, "project": seg})
print(json.dumps(idx, ensure_ascii=False))
