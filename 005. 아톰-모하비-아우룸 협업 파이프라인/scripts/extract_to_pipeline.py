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

import urllib.request

def _clean_passage(s):
    """PDF 추출 잡음 정리: 불릿 'w '/'ㅇ ', 과도 공백 축소."""
    s = re.sub(r'(^|\s)[wㅇ]\s+', ' ', s)     # 불릿 마커 제거
    s = re.sub(r' {2,}', ' ', s)
    return s.strip()

def _sentences(text):
    """추출 blob을 문장 단위로 대략 분할."""
    t = re.sub(r'\s+', ' ', text)
    parts = re.split(r'(?<=[.。])\s+|(?<=다)\s+|(?<=함)\s+|(?<=음)\s+|(?<=됨)\s+', t)
    return [_clean_passage(s) for s in parts if len(s.strip()) >= 15]

def extract_overview(text):
    """원문에서 조사 개요(기간·차수·지역·기관) 자동 추출."""
    ov = {}
    m = re.search(r'(20\d{2}\s*년\s*[0-9]\s*분기|[0-9]\s*차\s*년도?|[0-9]\s*분기)', text)
    if m: ov["기간_차수"] = re.sub(r'\s+', '', m.group(1))
    m = re.search(r'(사업|공사|지구|단지|정비사업)[^\n]{0,20}', text)
    m2 = re.search(r'조사\s*지역[^\n]{0,40}', text)
    if m2: ov["조사지역"] = re.sub(r'\s+', ' ', m2.group(0))[:60]
    m3 = re.search(r'((?:주식회사|㈜)?\s*아우룸생태연구소)', text)
    ov["조사기관"] = "㈜아우룸생태연구소" if m3 else ""
    return ov

def species_passages(text, sp, n=3):
    """특정 종이 등장하는 문장 중 서식/저감 맥락 문장 상위 n개."""
    KW = re.compile(r'서식|이주|저감|웅덩이|산란|서식지|둥지|번식|출현|개체|이동|보호|펜스|울타리|모니터링|확인|포획')
    out, seen = [], set()
    for s in _sentences(text):
        if sp in s and KW.search(s):
            k = s[:40]
            if k not in seen:
                seen.add(k); out.append(s[:220])
            if len(out) >= n:
                break
    return out

def mitigation_passages(text, n=4):
    KW = re.compile(r'저감\s*대책|저감\s*방안|이주|포획|보호\s*휀스|보호\s*펜스|대체\s*서식|모니터링|저감을|훼손')
    out, seen = [], set()
    for s in _sentences(text):
        if KW.search(s):
            k = s[:40]
            if k not in seen:
                seen.add(k); out.append(s[:220])
            if len(out) >= n:
                break
    return out

def disturbance_species(text):
    m = re.search(r'생태계\s*교란[^\n]{0,120}', text)
    return re.sub(r'\s+', ' ', m.group(0))[:150] if m else ""

def vllm_overview(text):
    """아톰 vLLM(Qwen)으로 3~4문장 개관 요약. 실패 시 빈 문자열."""
    try:
        chunk = text[:1600]   # vLLM max-model-len 4096 대비 안전 청크
        payload = json.dumps({
            "model": "Qwen/Qwen2.5-72B-Instruct-AWQ",
            "messages": [
                {"role": "system", "content": "생태조사 보고서 요약가. 아래 발췌를 3~4문장 한국어 존댓말로 요약. 사업/조사 성격·확인 종·핵심 조치만. 없는 사실 지어내지 말 것."},
                {"role": "user", "content": chunk}],
            "max_tokens": 220, "temperature": 0.2
        }, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request("http://localhost:8088/v1/chat/completions",
                                     data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=40) as r:
            d = json.loads(r.read().decode("utf-8"))
        return nfc(d["choices"][0]["message"]["content"].strip())
    except Exception:
        return ""

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

    # 구조화 상세 요약 구성 (전체 텍스트 대상 추출 + vLLM 개관)
    ov = extract_overview(text)
    dist = disturbance_species(text)
    mits = mitigation_passages(text)
    ai_overview = vllm_overview(text) if len(text) > 200 else ""
    preview = text[:PREVIEW_CHARS]

    sp_sections = []
    for sp in detected[:12]:
        ps = species_passages(text, sp)
        block = f"### {sp}\n" + ("\n".join(f"> {p}" for p in ps) if ps
                                  else "> (본문 내 서식/저감 맥락 문구 미확인 — 종 출현만 기록)")
        sp_sections.append(block)

    L = ["---", "status: raw_analyzed", "assigned_agent: Mohave",
         f'source_file: "{src}"', f'original_nas_path: "{path}"',
         f'year_vendor: "{year_vendor}"', f'project_name: "{project}"',
         f'survey_period: "{ov.get("기간_차수","")}"',
         "document_type: 생태조사보고서",
         f'detected_protected_species: {json.dumps(detected, ensure_ascii=False)}',
         f'last_updated: "{now_iso()}"', "---", "",
         f"# {src} 상세 1차 요약", "",
         "## 📋 조사 개요",
         f"- 사업명: {project or '미상'}",
         f"- 조사 기간/차수: {ov.get('기간_차수','미확인')}",
         f"- 조사 지역: {ov.get('조사지역','본문 참조')}",
         f"- 조사 기관: {ov.get('조사기관') or '㈜아우룸생태연구소'}",
         f"- 추출 글자수: {len(text):,}", ""]
    if ai_overview:
        L += ["## 🤖 AI 개관 (Qwen2.5-72B)", ai_overview, ""]
    L += [f"## 🐸 확인된 법정보호종 ({len(detected)}종)",
          (", ".join(detected) if detected else "자동탐지 없음(본문 확인 필요)"), ""]
    if sp_sections:
        L += sp_sections + [""]
    if dist:
        L += ["## 🌿 생태계교란종", f"- {dist}", ""]
    if mits:
        L += ["## 🛠️ 주요 조치·저감 내용"] + [f"- {m}" for m in mits] + [""]
    L += [f"## 원문 발췌 (상위 {len(preview):,}자)", "```text", preview, "```"]
    summary = "\n".join(L) + "\n"
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
