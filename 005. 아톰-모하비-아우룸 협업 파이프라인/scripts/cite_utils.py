#!/usr/bin/env python3
# 005 파이프라인 — 인용 추출·정규화·볼트 실재 검증 공용 헬퍼.
# Created: 2026-07-22 by Antigravity(Claude Opus 4.8)
# 목적: 생성 사후검증(draft_with_mohave.sh)과 자동승인 게이트(classify_approval.py)가
#       '노트 인용이 볼트에 실재하는가'를 동일 로직으로 판정하도록 단일 정본화한다.
#       (두 곳이 따로 판정하면 생성기가 통과시킨 인용을 게이트가 반려하는 드리프트 발생)
# CLI: cite_utils.py sanitize <vault>   # stdin 본문의 미실재 인용을 '(근거자료 미확인)'으로 치환, stdout 출력
import os
import re
import glob
import unicodedata

# 노트성 인용으로 볼 키워드 — (소괄호)에만 적용(학명·버전 등 비-노트 괄호 제외용).
# 대괄호 [제목]·위키링크 [[제목]]는 이 보고서에서 관례상 '노트 인용'이므로 키워드 불요.
NOTE_KW = re.compile(r'논문분석|보고서|연구|분포|서식|가이드|지침|목록|데이터|참고|분석|매뉴얼')

# 인용 후보 추출 패턴(생성 사후검증·승인게이트 양쪽에서 동일하게 사용).
# 모델은 실제로 근거를 단일 대괄호 [제목] 로 표기하므로 반드시 포함해야 한다.
_PAREN = re.compile(r'\(([^()]{1,200})\)')
_WIKI = re.compile(r'\[\[([^\[\]]+)\]\]')
_BRACKET = re.compile(r'(?<!\[)\[([^\[\]]{1,200})\](?!\])')   # 단일 대괄호(위키링크 [[ ]] 는 제외)

# 노트 인용이 아닌 구조참조/체크박스/각주/플레이스홀더 제외
_NONCITE = re.compile(r'^(표|그림|사진|도표|붙임|별첨|각주|참고문헌|사업|구간)\s*[\d\-]|^\^|근거자료\s*미확인')


def _note_ref(s, kw_required):
    """인용 후보 문자열이 '노트 인용'이면 정규화된 원문 반환, 아니면 None."""
    s = s.strip().strip('"')
    # [참고 노트] 목록이 '### 노트명' 형식이라 모델이 '###'째로 인용해온다.
    # 그대로 두면 실재하는 노트가 미실재로 판정돼 근거가 통째로 지워진다(실측 33건).
    s = re.sub(r'^#{1,6}\s*', '', s).strip()
    if len(s) < 5:
        return None
    if _NONCITE.search(s):
        return None
    if re.fullmatch(r'[\s\dxX✓·\-–—.,]+', s):   # 숫자/기호만
        return None
    if kw_required and not NOTE_KW.search(s):
        return None
    return s


def nfc(s):
    """NFC 정규화 + 잘못된 서로게이트 제거."""
    s = unicodedata.normalize("NFC", s or "")
    return s.encode("utf-8", "ignore").decode("utf-8")


def norm(x):
    """비교용 정규화: NFC + 모든 공백 제거."""
    return re.sub(r'\s+', '', nfc(x))


# 노트 안에 '실재하는 근거 제목' — 문헌 연구원이 적재한 참고문헌 줄과 〔근거: 제목〕 표기.
#   참고문헌 줄 형식: '- [KCI] 제목 — url' / '- [웹] 제목 — url' / '- [해외] 제목 — url'
_REF_LINE = re.compile(r'^-\s*\[(?:KCI|웹|해외)\]\s*(.+?)\s*—\s*\S+\s*$', re.M)
_GROUND_TITLE = re.compile(r'〔근거:\s*(.+?)〕')


def build_vault_index(vault):
    """볼트 실재 인덱스(set): 노트 파일명·title/H1 + 노트에 적재된 참고문헌·〔근거〕 논문 제목.

    논문 제목을 포함시키는 이유: 드래프터가 근거로 논문 제목을 인용하면 노트 제목과 일치하지 않아
    전부 '(근거자료 미확인)'으로 치환됐다(실제 근거가 삭제되는 오탐). 논문 제목은 볼트 노트 안에
    실재하는 문자열이므로 인정해도 환각 차단 기능은 유지된다 — 지어낸 제목은 여전히 걸러진다.
    """
    idx = set()
    for p in glob.glob(vault + "/**/*.md", recursive=True):
        if "/." in p:  # .git/.obsidian/.smart-env 등 숨김경로 제외
            continue
        idx.add(norm(os.path.basename(p)[:-3]))
        try:
            c = nfc(open(p, encoding="utf-8", errors="ignore").read())
        except Exception:
            continue
        m = re.search(r'^title:\s*(.+)$', c, re.M) or re.search(r'^#\s+(.+)$', c, re.M)
        if m:
            idx.add(norm(m.group(1).strip().strip('"')))
        for t in _REF_LINE.findall(c):
            if len(t) >= 8:                       # 짧은 제목은 부분일치 오탐 위험 → 제외
                idx.add(norm(t))
        for t in _GROUND_TITLE.findall(c):
            for one in re.split(r';', t):
                one = one.strip()
                if len(one) >= 8 and "근거 불명" not in one:
                    idx.add(norm(one))
    return idx


def extract_citations(body):
    """본문에서 노트성 인용 후보(원문 문자열)를 추출.
    소괄호는 NOTE_KW 필터 적용, 대괄호/위키링크는 관례상 인용이므로 필터 없이."""
    out = []
    for s in _PAREN.findall(body):
        r = _note_ref(s, True)
        if r:
            out.append(r)
    for pat in (_WIKI, _BRACKET):
        for s in pat.findall(body):
            r = _note_ref(s, False)
            if r:
                out.append(r)
    return out


def is_known(cite, vault_norm):
    """인용이 볼트에 실재하는가: 정확일치 | 인용⊆제목(인용≥8) | 제목⊆인용(제목≥12, 짧은제목 오탐방지)."""
    cn = norm(cite)
    return (cn in vault_norm) or any(
        (cn in t and len(cn) >= 8) or (t in cn and len(t) >= 12) for t in vault_norm)


def find_suspects(body, vault_norm):
    """실재하지 않는(환각 의심) 노트성 인용 목록."""
    return [c for c in extract_citations(body) if not is_known(c, vault_norm)]


# 모델이 [참고 노트] 발췌의 소제목을 그대로 인용으로 적는 경우 — '문헌 근거 생태적 특성' 등.
# 실체는 그 종노트에서 온 내용이므로 지울 것이 아니라 출처 노트명으로 되돌려야 한다.
_LIT_HEAD = re.compile(r'^(?:문헌근거|참고문헌근거)')
# 종 항목 머리글: '### 1. 맹꽁이(Kaloula borealis, …)' / '1. 검독수리(…)' / '**삵(…)**'
# ★한 글자 종명(삵·매·꽃)도 반드시 잡아야 한다. 두 글자 이상만 잡던 판(…{1,14})에서는 '삵(' 머리글이
#  통째로 무시돼 직전 종(맹꽁이)의 노트가 삵 서술의 근거로 붙었다(실측 2026-07-24). 오귀속은
#  근거 누락보다 위험하다 — 보고서가 다른 종의 문헌을 이 종의 근거로 제시하게 되기 때문이다.
_SPECIES_HEAD = re.compile(r'^\s{0,3}(?:[#>\-*\s]{0,8})(?:\d+[.)]\s*)?\*{0,2}([가-힣][가-힣\s]{0,14}?)\*{0,2}\s*[(（]')
# 학명·등급이 없는 맨이름 머리글('먹황새' 한 줄). 대상 법정보호종 메타에 없는 종은 모델이 학명을
# 못 붙여 이렇게 쓴다. 이걸 못 잡으면 직전 종이 이어져 오귀속된다(실측: 먹황새 서술에 (황새) 귀속).
# 공백 없는 한 덩어리만 허용 — '습지와 하천' 같은 서술 조각을 머리글로 오인하지 않기 위함.
_BARE_HEAD = re.compile(r'^\s{0,3}(?:[#>\-*\s]{0,8})(?:\d+[.)]\s*)?\*{0,2}([가-힣]{1,15})\*{0,2}\s*$')


def remap_section_citations(body, vault_norm, placeholder="근거자료 미확인"):
    """발췌 소제목을 인용으로 적은 것을 그 발췌의 출처 종노트명으로 되돌린다. (body, 정정건수) 반환.

    이걸 하지 않으면 sanitize 가 '(근거자료 미확인)'으로 지워버려, 실제로는 볼트 문헌을 그대로
    반영한 서술이 '근거 없음'으로 오표기된다. 그 결과 아우룸이 '빈 보고서/근거부족'으로 판정하고
    재드래프를 반복해도 결과가 같아 승인대기가 영구 적체됐다(2026-07-24 실측: 문헌 보유 100%인
    6건 78종이 전부 이 경로로 미확인 처리됨). 종 머리글을 못 찾은 구간은 손대지 않는다(안전측)."""
    fixed, cur, out = 0, None, []
    for line in body.splitlines(True):
        m = _SPECIES_HEAD.match(line) or _BARE_HEAD.match(line)
        if m:
            cand = m.group(1).strip()
            # 새 종 구간에 들어서면 귀속 대상을 반드시 교체한다. 볼트에 노트가 없는 종이면 None —
            # 그대로 두면 직전 종의 노트가 다음 종 서술의 근거로 잘못 붙는다(오귀속이 환각보다 나쁘다).
            cur = cand if norm(cand) in vault_norm else None
        def _repl(mm):
            nonlocal fixed
            inner = re.sub(r'^#{1,6}\s*', '', mm.group(1).strip())
            if not _LIT_HEAD.match(norm(inner)):
                return mm.group(0)
            if cur:
                fixed += 1
                return "(" + cur + ")"
            # 귀속할 종노트를 못 찾은 소제목 인용은 남겨두면 본문에 그대로 노출된다 → 정직하게 미확인.
            return "(" + placeholder + ")"
        line = _PAREN.sub(_repl, line)
        line = _BRACKET.sub(_repl, line)
        out.append(line)
    return "".join(out), fixed


def sanitize(body, vault_norm, placeholder="근거자료 미확인"):
    """실재하지 않는 노트성 인용을 placeholder로 치환. (clean_body, removed_list) 반환.
    대괄호 안에 소괄호(학명 등)가 있을 수 있으므로 대괄호를 먼저 처리한다."""
    removed = []
    # 괄호·대괄호 안에 딸려온 마크다운 제목 표기를 먼저 털어낸다 → 본문에도 '[### 종명]'이 남지 않는다.
    body = re.sub(r'([\[\(])\s*#{1,6}\s*', r'\1', body)

    def _mk(kw_required):
        def _repl(m):
            r = _note_ref(m.group(1), kw_required)
            if r and not is_known(r, vault_norm):
                removed.append(r)
                return "(" + placeholder + ")"
            return m.group(0)
        return _repl

    body = _WIKI.sub(_mk(False), body)
    body = _BRACKET.sub(_mk(False), body)
    body = _PAREN.sub(_mk(True), body)
    return body, removed


# 모델이 placeholder를 흔들어 쓰는 변형(근거자야/근거 자료/근거자로 미확인 …)을 정본으로 통일.
# 승인 게이트(classify_approval·pipeline_admin_review)가 '근거자료 미확인' 문자열을 그대로 세기 때문에,
# 변형이 남으면 빈 항목이 실질 서술로 계산돼 부실 보고서가 자동승인을 통과할 수 있다.
# 정규화는 놓치던 것을 잡는 방향으로만 작용하므로 판정은 더 보수적으로만 움직인다.
# '자' 뒤 1글자까지만 허용하고(료/야/재 등 오타), 뒤에 한글이 이어지면 제외 →
# '근거자료가 미확인된 항목' 같은 정상 서술문은 건드리지 않는다.
# 토큰 사이 구분자는 공백뿐 아니라 _ · - 도 허용(실제로 '근거_자료 미확인'이 초안에 있었음).
_PH_SEP = r'[\s_·\-]*'
_PH_VARIANT = re.compile(r'근거' + _PH_SEP + r'자[가-힣]?' + _PH_SEP + r'미' + _PH_SEP + r'확인(?![가-힣])')


def normalize_placeholder(body, placeholder="근거자료 미확인"):
    """placeholder 표기 변형을 정본 문자열로 통일. (clean_body, 정정건수) 반환."""
    fixed = [0]

    def _repl(m):
        if m.group(0) != placeholder:
            fixed[0] += 1
        return placeholder

    return _PH_VARIANT.sub(_repl, body), fixed[0]


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3 and sys.argv[1] == "sanitize":
        vault = sys.argv[2]
        body = sys.stdin.read()
        idx = build_vault_index(vault)
        body, remapped = remap_section_citations(body, idx)   # 소제목 인용 → 출처 종노트로 복원(지우기 전에)
        if remapped:
            sys.stderr.write("cite_remap 소제목→종노트 %d건\n" % remapped)
        clean, removed = sanitize(body, idx)
        clean, ph_fixed = normalize_placeholder(clean)
        if ph_fixed:
            sys.stderr.write("placeholder 표기 정규화 %d건\n" % ph_fixed)
        sys.stdout.write(clean)
        if removed:
            sys.stderr.write("cite_sanitize 정정 %d건: %s\n" % (len(removed), " | ".join(removed[:5])))
    else:
        sys.stderr.write("usage: cite_utils.py sanitize <vault>  (본문은 stdin)\n")
        sys.exit(2)
