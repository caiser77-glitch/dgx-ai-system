#!/usr/bin/env python3
# 007 — 이미지잠금 HWP OCR 회복: BinData 이미지에 잠긴 보고서 본문을 tesseract(kor+eng)로 추출.
# Created: 2026-07-23 by Antigravity(Claude Opus 4.8)
# 대상: OLE(hwp5.x) .hwp, outputs.text<1500B, BinData>=MIN_BIN, ocr_extracted 미표기.
# ai_classification 보존, outputs.text 만 갱신. idempotent(ocr_extracted 마커). CPU tesseract → GPU 무경합.
import json, glob, os, sys, zlib, subprocess, tempfile
import olefile
MD = "/home/caiser77/dgx_workspace/data/processed/metadata"
TEXTDIR = "/home/caiser77/dgx_workspace/data/processed/text"
MIN = 1500                 # 회복 성공 기준(byte)
MIN_BIN = 100_000          # 이미지잠금 판정: BinData 총합
MIN_IMG = 8_000            # 개별 이미지 하한(로고·도장 스킵)
MAX_IMG = 60               # 문서당 OCR 이미지 상한
ENOUGH = 8000              # 누적 OCR 글자 이 정도면 조기중단
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 20
dry = "--dry" in sys.argv

def sniff(d):
    if d[:8] == b"\x89PNG\r\n\x1a\n": return "png"
    if d[:2] == b"\xff\xd8": return "jpg"
    if d[:2] == b"BM": return "bmp"
    if d[:3] == b"GIF": return "gif"
    if d[:4] == b"II*\x00" or d[:4] == b"MM\x00*": return "tif"
    return None

def to_image(raw):
    f = sniff(raw)
    if f: return raw, f
    for wbits in (-15, 15, 47):
        try:
            d = zlib.decompress(raw, wbits); f2 = sniff(d)
            if f2: return d, f2
        except Exception: pass
    return None, None

def bindata(sp):
    out = []
    try:
        ole = olefile.OleFileIO(sp)
    except Exception:
        return out
    try:
        streams = [e for e in ole.listdir() if e and e[0] == "BinData"]
        tot = sum(ole.get_size("/".join(e)) for e in streams)
        if tot < MIN_BIN:
            return out
        for e in streams:
            if ole.get_size("/".join(e)) < MIN_IMG: continue
            out.append(ole.openstream("/".join(e)).read())
            if len(out) >= MAX_IMG: break
    finally:
        ole.close()
    return out

def ocr_doc(sp):
    imgs = bindata(sp)
    if not imgs: return None, 0
    parts = []; nimg = 0
    with tempfile.TemporaryDirectory() as td:
        for i, raw in enumerate(imgs):
            img, fmt = to_image(raw)
            if not img: continue
            fn = os.path.join(td, f"i{i}.{fmt}")
            open(fn, "wb").write(img)
            try:
                r = subprocess.run(["tesseract", fn, "-", "-l", "kor+eng"],
                                   capture_output=True, text=True, timeout=180)
                t = (r.stdout or "").strip()
            except Exception:
                t = ""
            if t:
                parts.append(t); nimg += 1
            if sum(len(x) for x in parts) >= ENOUGH: break
    return "\n\n".join(parts), nimg

def cur_size(tp):
    return os.path.getsize(tp) if (tp and os.path.exists(tp)) else 0

done = fail = scanned = skip = 0
for p in glob.iglob(MD + "/*.metadata.json"):
    scanned += 1
    try: m = json.load(open(p, encoding="utf-8"))
    except Exception: continue
    sp = m.get("source_path", "")
    if not sp.lower().endswith(".hwp") or not os.path.exists(sp): continue
    tp = (m.get("outputs") or {}).get("text")
    if cur_size(tp) >= MIN: continue
    if m.get("ocr_extracted"): skip += 1; continue
    try:
        with open(sp, "rb") as f:
            if f.read(4) != b"\xd0\xcf\x11\xe0": continue   # OLE만
    except Exception: continue
    if dry:
        done += 1
        if done >= limit: break
        continue
    text, nimg = ocr_doc(sp)
    if text is None:
        continue                       # BinData<MIN_BIN → 이미지잠금 아님(진짜 짧은 문서), 마커 안 남김
    text = text.strip()
    if len(text.encode("utf-8")) >= MIN:
        if not tp:
            tp = os.path.join(TEXTDIR, os.path.basename(p).replace(".metadata.json", ".txt"))
            m.setdefault("outputs", {})["text"] = tp
        header = "[OCR 자동추출 — 원본 이미지스캔 HWP, 오탈자 가능]\n"
        open(tp, "w", encoding="utf-8").write(header + text + "\n")
        m["ocr_extracted"] = True
        m["ocr_images"] = nimg
        m.pop("extract_exhausted", None)
        done += 1
    else:
        fail += 1
        m["ocr_extracted"] = True       # 시도완료(회복 실패) — 재시도 방지
        m["ocr_images"] = nimg
    json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if done >= limit: break
print(json.dumps({"scanned": scanned, "recovered": done, "failed": fail, "skipped": skip, "dry": dry}, ensure_ascii=False))
