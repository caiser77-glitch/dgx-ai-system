#!/usr/bin/env python3
# 007 — 아톰 병렬 드래프터. draft_with_mohave.sh(맥)의 아톰판: 동기화된 볼트로 RAG,
# vLLM 72B로 생성, cite_utils로 인용 실재검증. 노트선택·프롬프트·규칙은 모하비와 동일 이식.
# Created: 2026-07-22 by Antigravity(Claude Opus 4.8)
# 사용: draft_with_vllm.py --summary <summary.md> --out <draft.md> [--job <id>]
#       (Phase1 뼈대: 단일 잡 처리. Phase2에서 라우터가 아톰 로컬 큐로 호출)
import os, re, sys, json, glob, argparse, unicodedata, urllib.request

VAULT = os.environ.get("ATOM_VAULT", "/home/caiser77/AI_BASE/ObsidianVault")
CITE = os.environ.get("CITE_UTILS", "/home/caiser77/AI_BASE/cite_utils.py")
LLM_URL = os.environ.get("VLLM_URL", "http://127.0.0.1:8088/v1/chat/completions")
LLM_MODEL = os.environ.get("VLLM_MODEL", "Qwen/Qwen2.5-72B-Instruct-AWQ")
PER_SPECIES = 3

sys.path.insert(0, os.path.dirname(CITE))
try:
    import cite_utils
except Exception:
    cite_utils = None


def nfc(s):
    return unicodedata.normalize("NFC", s or "")


def build_notelist(summ_text):
    """요약의 종·키워드로 볼트 실존 노트를 선별(모하비와 동일 PER_SPECIES 로직).
    인용 정답=파일명. 종마다 상위 N개 슬롯 보장(얇은 종 굶주림 방지)."""
    txt = nfc(summ_text)
    terms = set()
    m = re.search(r'detected_protected_species:\s*(\[.*\])', txt)
    if m:
        try:
            terms |= set(json.loads(m.group(1)))
        except Exception:
            pass
    for m in re.finditer(r'^(?:species|project_name|class_name):\s*(.+)$', txt, re.M):
        terms.add(m.group(1).strip().strip('"'))
    terms = {nfc(t) for t in terms if t and len(t) >= 2}

    LIT_MARK = "## 문헌 근거 저감·보전 방안"
    def excerpt(content, span=260):
        # 2차 문헌 연구원이 붙인 방안 카탈로그 전체를 우선 제공(2차 KB 실활용). 인용은 종노트만 → 〔근거:논문〕 제거.
        li = content.find(LIT_MARK)
        if li != -1:
            seg = content[li:]
            ri = seg.find("## 참고문헌")
            if ri != -1:
                seg = seg[:ri]
            seg = re.sub(r'〔근거:[^〕]*〕', '', seg)
            seg = re.sub(r'[ \t]+', ' ', seg[:1600]).strip()
            if len(seg) > 40:
                return seg
        for t in terms:
            i = content.find(t)
            if i != -1:
                s = max(0, i - 70)
                return re.sub(r'\s+', ' ', content[s:s + span]).strip()
        return re.sub(r'\s+', ' ', content[:span]).strip()

    notes = []
    for p in glob.glob(VAULT + "/**/*.md", recursive=True):
        if "/." in p:
            continue
        name = nfc(os.path.basename(p)[:-3])
        try:
            content = nfc(open(p, encoding="utf-8", errors="ignore").read(12000))
        except Exception:
            continue
        notes.append((name, content))

    picked = {}
    for t in sorted(terms):
        named = [(2, n, c) for n, c in notes if t in n]
        cand = named if named else [(0, n, c) for n, c in notes if t in c]
        cand.sort(key=lambda x: (-x[0], len(x[1])))
        seen_t, added = set(), 0
        for s, n, c in cand:
            if n in seen_t:
                continue
            seen_t.add(n)
            picked.setdefault(n, (s, n, c))
            added += 1
            if added >= PER_SPECIES:
                break
    rows = sorted(picked.values(), key=lambda x: -x[0])[:12]
    return "\n\n".join(f"### {n}\n발췌: {excerpt(c)}" for s, n, c in rows)


PROMPT_RULES = """너는 (주)아우룸생태연구소의 생태조사 보고서 작성 담당이다.
아래 [1차 요약]과 [참고 노트] 발췌를 근거로 정식 생태조사 보고서 초안 섹션을
한국어 존댓말로 작성하라.
규칙:
(1) **추가로 볼트를 검색·탐색하지 말 것.** 아래 [참고 노트]의 제목과 발췌 내용만을 근거로
    서식특성·영향예측·저감대책을 구체적으로 서술하라. 근거 인용은 반드시 [참고 노트]에 제시된
    제목(파일명)을 **한 글자도 바꾸지 말고 그대로** 괄호 안에 쓰라(요약·의역·재구성 금지).
    목록에 없는 제목은 어떤 경우에도 지어내지 말 것. 파일 경로는 쓰지 말 것.
    목록에 근거 노트가 없는 종·항목은 '(근거자료 미확인)'으로 표기하라.
(2) 목록의 노트로 뒷받침되는 내용은 충실히 서술하라. 어떤 노트로도 확인되지 않는 특정
    수치·사실만 지어내지 말 것(그런 항목에 한해 '근거자료 미확인'으로 표기).
(3) '서식특성 → 영향예측 → 저감대책' 구조로 서술할 것. 모든 한글은 조합형으로 작성.
(4) 최종 보고서 초안은 반드시 아래 두 마커 사이에만 출력하라. 마커 밖 텍스트는 폐기된다.
    시작 마커: <<<REPORT_START>>>
    끝 마커: <<<REPORT_END>>>"""


def generate(notelist, ctx):
    user = ("%s\n\n[참고 노트] (인용은 이 제목만 사용; 추가 검색 불필요)\n%s\n\n[1차 요약]\n%s"
            % (PROMPT_RULES, notelist or "- (관련 노트 자동검색 결과 없음)", ctx))
    payload = {"model": LLM_MODEL, "temperature": 0.3, "max_tokens": 1800,
               "messages": [{"role": "user", "content": user}]}
    req = urllib.request.Request(LLM_URL, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return json.load(r)["choices"][0]["message"]["content"]


def extract_report(out):
    m = re.search(r'<<<REPORT_START>>>(.*?)<<<REPORT_END>>>', out, re.S)
    body = m.group(1).strip() if m else out.strip()
    return nfc(body)


def sanitize(body):
    if cite_utils is None:
        return body
    try:
        idx = cite_utils.build_vault_index(VAULT)
        clean, _ = cite_utils.sanitize(body, idx)
        return clean
    except Exception:
        return body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--job", default="")
    a = ap.parse_args()
    ctx = open(a.summary, encoding="utf-8", errors="ignore").read()
    notelist = build_notelist(ctx)
    out = generate(notelist, ctx)
    if not out or len(out) < 100:
        sys.stderr.write("초안 비었거나 실패\n"); sys.exit(2)
    body = sanitize(extract_report(out))
    job = a.job or os.path.basename(a.out).replace(".draft.md", "")
    import time
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("---\nstatus: review_pending\nassigned_agent: Aurum\n")
        f.write('job_id: "%s"\ndrafted_by: atom-vllm(qwen2.5-72b)\n' % job)
        f.write('drafted_at: "%s"\n---\n\n%s\n' % (time.strftime("%FT%T%z"), body))
    sys.stderr.write("초안 완료(atom-vllm): %s | 노트 %d블록\n"
                     % (a.out, notelist.count("### ") if notelist else 0))


if __name__ == "__main__":
    main()
