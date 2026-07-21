#!/usr/bin/env python3
# 005 파이프라인 — NAS 문서(HWP/HWPX) 텍스트 추출 → 입력(01_raw_analyzed) 투입기.
# Created: 2026-07-21 by Antigravity(Claude Opus 4.8)
# 목적: 002 처리기가 HWP 를 못 읽어(unsupported) 요약이 비던 문제를 해결.
#       hangul_mcp.HWPParser 로 표 내용까지 추출해 실 survey 텍스트를 요약에 담는다.
# 실행: /home/caiser77/hwp_extract_venv/bin/python extract_to_pipeline.py <파일...> [--limit N]
import sys, os, json, re, hashlib, argparse, unicodedata
from datetime import datetime, timezone, timedelta

from hangul_mcp.hwp_parser import HWPParser
try:
    from hangul_mcp.hwpx_parser import HWPXParser
except Exception:
    HWPXParser = None

KST = timezone(timedelta(hours=9))
PIPELINE_ROOT = os.environ.get("PIPELINE_ROOT", "/home/caiser77/AI_BASE")
RAW = os.path.join(PIPELINE_ROOT, "01_raw_analyzed")
PREVIEW_CHARS = 6000   # 요약에 담을 원문 상한
MAX_PDF_PAGES = 80     # PDF 추출 페이지 상한(대용량 런타임 폭주 방지)

def nfc(s):
    # NFC 정규화 + 무효 서로게이트/인코딩불가 문자 제거(HWP/PDF 추출 잔재로 인한 write 크래시 방지)
    s = unicodedata.normalize("NFC", s or "")
    return s.encode("utf-8", "ignore").decode("utf-8")

def now_iso(): return datetime.now(KST).isoformat(timespec="seconds")

def load_protected():
    """법정보호종 국명 집합 로드(있으면). 없으면 빈 집합."""
    for p in ("/home/caiser77/AI_BASE/protected_species.json",
              "/home/caiser77/dgx_workspace/data/protected_species.json"):
        if os.path.exists(p):
            try:
                data = json.load(open(p, encoding="utf-8"))
                names = set()
                if isinstance(data, dict):
                    for k, v in data.items():
                        names.add(k)
                        if isinstance(v, dict):
                            names.add(v.get("국명") or v.get("name") or "")
                elif isinstance(data, list):
                    for it in data:
                        if isinstance(it, str): names.add(it)
                        elif isinstance(it, dict):
                            names.add(it.get("국명") or it.get("name") or "")
                return {nfc(x) for x in names if x and len(x) >= 2}
            except Exception:
                pass
    return set()

PROTECTED = load_protected()

def extract_pdf(path):
    """PDF 본문 + 표 추출(pdfplumber). 페이지 상한으로 런타임 제한."""
    import pdfplumber
    parts = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages):
            if i >= MAX_PDF_PAGES:
                parts.append(f"[... {len(pdf.pages)}쪽 중 {MAX_PDF_PAGES}쪽까지만 추출]")
                break
            # 굵은글씨/그림자 효과로 같은 위치에 글리프가 겹쳐 그려진 경우 중복 제거
            try:
                page = page.dedupe_chars(tolerance=1)
            except Exception:
                pass
            parts.append(page.extract_text() or "")
            for tbl in (page.extract_tables() or []):
                for row in tbl:
                    parts.append("\t".join((c or "") for c in row))
    text = "\n".join(p for p in parts if p)
    # 잔여 반복(숫자·공백 제외, 같은 글자 6회 이상 연속)을 1회로 축약(표지 중복 잔재 정리).
    # 숫자를 제외해 측정치 손상 방지.
    text = re.sub(r'([^\d\s])\1{5,}', r'\1', text)
    return nfc(text)

def extract_text(path):
    low = path.lower()
    if low.endswith(".pdf"):
        return extract_pdf(path)
    parser = None
    try:
        if low.endswith(".hwpx") and HWPXParser:
            parser = HWPXParser(path)
        else:
            parser = HWPParser(path)
        t = parser.extract_text()
    finally:
        try: parser.close()
        except Exception: pass
    return nfc(t or "")

def infer_meta(path):
    parts = [p for p in nfc(path).split("/") if p]
    year_vendor, project = "", ""
    for i, seg in enumerate(parts):
        if re.match(r"^20\d\d\s", seg):   # 예: "2025 세일"
            year_vendor = seg
            if i + 1 < len(parts): project = parts[i + 1]
            break
    return year_vendor, project

def make_job(path):
    path = nfc(os.path.abspath(path))
    if not os.path.exists(path):
        return None, f"파일 없음: {path}"
    text = extract_text(path)
    if len(text.strip()) < 30:
        return None, f"추출 텍스트 부족({len(text)}자): {os.path.basename(path)}"

    job_id = "doc_" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:12]  # ASCII 안전
    year_vendor, project = infer_meta(path)
    src = os.path.basename(path)
    detected = sorted({s for s in PROTECTED if s and s in text})[:30]
    preview = text[:PREVIEW_CHARS]

    summary = (
        "---\n"
        "status: raw_analyzed\n"
        "assigned_agent: Mohave\n"
        f'source_file: "{src}"\n'
        f'original_nas_path: "{path}"\n'
        f'year_vendor: "{year_vendor}"\n'
        f'project_name: "{project}"\n'
        "document_type: 생태조사보고서\n"
        f'detected_protected_species: {json.dumps(detected, ensure_ascii=False)}\n'
        f'last_updated: "{now_iso()}"\n'
        "---\n\n"
        f"# {src} 1차 추출 요약\n\n"
        f"## 추출 정보\n- 추출 글자수: {len(text):,}\n"
        f"- 탐지된 법정보호종: {', '.join(detected) if detected else '자동탐지 없음(본문 확인 필요)'}\n\n"
        f"## 원문(추출 텍스트, 상위 {PREVIEW_CHARS:,}자)\n```text\n{preview}\n```\n"
    )
    result = {
        "metadata": {"job_id": job_id, "source_file": src, "original_nas_path": path,
                     "timestamp": now_iso(), "extractor": "hangul_mcp.HWPParser"},
        "payload": {
            "metrics": {"char_count": len(text),
                        "detected_protected_species_count": len(detected),
                        "year_vendor": year_vendor, "project_name": project},
            "detected_protected_species": detected,
            "spatial_observations": []
        }
    }
    os.makedirs(RAW, exist_ok=True)
    with open(os.path.join(RAW, f"{job_id}.summary.md"), "w", encoding="utf-8") as f:
        f.write(summary)
    with open(os.path.join(RAW, f"{job_id}.result.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    return job_id, f"{src} → {job_id} ({len(text):,}자, 보호종 {len(detected)})"

def main():
    ap = argparse.ArgumentParser(description="NAS HWP/HWPX → 005 파이프라인 입력")
    ap.add_argument("files", nargs="+", help="HWP/HWPX 파일 경로(들)")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    files = args.files[:args.limit] if args.limit else args.files
    ok, fail = [], []
    for f in files:
        try:
            job, msg = make_job(f)
            (ok if job else fail).append(msg)
            print(("[OK] " if job else "[SKIP] ") + msg)
        except Exception as e:
            fail.append(f"{f}: {e}")
            print(f"[ERR] {f}: {e}")
    print(json.dumps({"ok": len(ok), "fail": len(fail)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
