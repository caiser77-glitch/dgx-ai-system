#!/usr/bin/env python3
# 005/monitoring — 야간 NAS 재추출 효율화 배치 (아톰).
# Created: 2026-07-21 by Antigravity(Claude Opus 4.8)
# 저효율(빈값) 002 추출을 보완: NAS 생태문서(HWP/PDF)를 hangul_mcp 로 실추출해
# 클린 코퍼스(text+메타+보호종)를 구축한다. 21~06시에만 cron 으로 배치 실행.
import sys, os, json, sqlite3, hashlib, time

sys.path.insert(0, "/home/caiser77/dgx_workspace/005. 아톰-모하비-아우룸 협업 파이프라인/scripts")
from extract_to_pipeline import extract_text, load_protected, nfc  # 추출 로직 재사용

CORPUS = "/home/caiser77/AI_BASE/clean_corpus"
LEDGER = os.path.join(CORPUS, ".done_ledger")
STATUS = "/home/caiser77/AI_BASE/overnight_status.json"   # apps/monitoring 가 읽을 상태
DB = "/home/caiser77/dgx_workspace/data/atom_watcher/atom_baseline.sqlite"

def main():
    batch = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    os.makedirs(CORPUS, exist_ok=True)
    open(LEDGER, "a").close()
    done = set(x for x in open(LEDGER, encoding="utf-8").read().splitlines() if x)
    protected = load_protected()

    con = sqlite3.connect(DB)
    rows = con.execute(
        "SELECT abs_path FROM files WHERE status='present' "
        "AND (root_label LIKE '%2025%' OR root_label LIKE '%2024%' OR root_label LIKE '%2026%') "
        "AND lower(extension) IN ('.hwp','.hwpx','.pdf') "
        "AND (name LIKE '%보고서%' OR name LIKE '%종평%' OR name LIKE '%동식물%' OR name LIKE '%모니터링%') "
        "AND name NOT LIKE '%부록%' AND name NOT LIKE '%조사표%' AND name NOT LIKE '%계획서%' "
        "AND name NOT LIKE '%증빙%' AND name NOT LIKE '%사진%' AND name NOT LIKE '%목차%' "
        "AND name NOT LIKE '%성적%' AND abs_path NOT LIKE '%문헌%' "
        "AND size_bytes BETWEEN 524288 AND 104857600 ORDER BY mtime_ns DESC"
    ).fetchall()
    con.close()

    processed = ok = 0
    for (path,) in rows:
        if processed >= batch:
            break
        path = nfc(path)
        if path in done:
            continue
        try:
            text = extract_text(path)
        except Exception:
            text = ""
        h = "doc_" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:12]
        if len(text.strip()) >= 100:
            detected = sorted({s for s in protected if s and s in text})[:30]
            with open(os.path.join(CORPUS, f"{h}.txt"), "w", encoding="utf-8") as f:
                f.write(text)
            with open(os.path.join(CORPUS, f"{h}.json"), "w", encoding="utf-8") as f:
                json.dump({"path": path, "chars": len(text), "protected_species": detected,
                           "extracted_at": time.strftime("%F %T")}, f, ensure_ascii=False)
            ok += 1
        with open(LEDGER, "a", encoding="utf-8") as f:
            f.write(path + "\n")
        done.add(path); processed += 1

    corpus_docs = len([x for x in os.listdir(CORPUS) if x.endswith(".txt")])
    status = {"updated": time.strftime("%F %T"), "processed_this_run": processed,
              "extracted_ok_this_run": ok, "total_seen": len(done),
              "corpus_docs": corpus_docs, "candidates_total": len(rows)}
    with open(STATUS, "w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)
    print(f"{time.strftime('%F %T')} 야간재추출: 처리 {processed}, 성공 {ok}, "
          f"누적 {len(done)}, 코퍼스 {corpus_docs}/{len(rows)}")

if __name__ == "__main__":
    main()
