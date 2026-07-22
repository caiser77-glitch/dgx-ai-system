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


def build_vault_index(vault):
    """볼트 내 모든 노트의 파일명(.md 제거)과 title/H1을 정규화한 실재 인덱스(set)."""
    idx = set()
    for p in glob.glob(vault + "/**/*.md", recursive=True):
        if "/." in p:  # .git/.obsidian/.smart-env 등 숨김경로 제외
            continue
        idx.add(norm(os.path.basename(p)[:-3]))
        try:
            c = nfc(open(p, encoding="utf-8", errors="ignore").read(600))
        except Exception:
            continue
        m = re.search(r'^title:\s*(.+)$', c, re.M) or re.search(r'^#\s+(.+)$', c, re.M)
        if m:
            idx.add(norm(m.group(1).strip().strip('"')))
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


def sanitize(body, vault_norm, placeholder="근거자료 미확인"):
    """실재하지 않는 노트성 인용을 placeholder로 치환. (clean_body, removed_list) 반환.
    대괄호 안에 소괄호(학명 등)가 있을 수 있으므로 대괄호를 먼저 처리한다."""
    removed = []

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


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3 and sys.argv[1] == "sanitize":
        vault = sys.argv[2]
        body = sys.stdin.read()
        idx = build_vault_index(vault)
        clean, removed = sanitize(body, idx)
        sys.stdout.write(clean)
        if removed:
            sys.stderr.write("cite_sanitize 정정 %d건: %s\n" % (len(removed), " | ".join(removed[:5])))
    else:
        sys.stderr.write("usage: cite_utils.py sanitize <vault>  (본문은 stdin)\n")
        sys.exit(2)
