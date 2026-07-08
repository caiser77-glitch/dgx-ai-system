#!/usr/bin/env python3
"""002/003 processed 산출물을 005 협업 파이프라인 입력으로 변환한다.

입력:
- processed/metadata/*.metadata.json
- processed/text/*.txt

출력:
- <pipeline-root>/01_raw_analyzed/<job_id>.summary.md
- <pipeline-root>/01_raw_analyzed/<job_id>.result.json
"""

import argparse
import json
import logging
import re
import unicodedata
from datetime import datetime, timezone, timedelta
from pathlib import Path


def now_iso():
    return datetime.now(timezone(timedelta(hours=9))).isoformat(timespec="seconds")


def nfc(value):
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    return value


def safe_job_id(value: str):
    value = nfc(value or "job")
    value = re.sub(r"[^A-Za-z0-9가-힣_.-]+", "_", value).strip("._")
    return value or "job"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path | None, max_chars=4000):
    if not path or not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    return text[:max_chars]


def yaml_scalar(value):
    text = str(value or "")
    text = text.replace('"', "'").replace("\n", " ").strip()
    return f'"{text}"'


def normalize_tags(tags):
    out = []
    for tag in tags or []:
        tag = str(tag).strip()
        if not tag:
            continue
        if not tag.startswith("#"):
            tag = f"#{tag}"
        if tag not in out:
            out.append(tag)
    return out


def metadata_job_id(metadata_path: Path, meta: dict):
    source_path = meta.get("source_path") or meta.get("original_path") or ""
    source_name = meta.get("source_name") or Path(source_path).name
    stem = metadata_path.name
    if stem.endswith(".metadata.json"):
        stem = stem[: -len(".metadata.json")]
    return safe_job_id(stem or source_name)


def extract_classification(meta: dict):
    ai = meta.get("ai_classification")
    if not isinstance(ai, dict):
        ai = {}
    ai_summary = meta.get("ai_summary")
    if not isinstance(ai_summary, dict):
        ai_summary = {}

    summary = ai.get("summary") or ""
    if not summary:
        lines = ai_summary.get("summary") or []
        if isinstance(lines, list):
            summary = "\n".join(str(line) for line in lines if line)
        elif isinstance(lines, str):
            summary = lines

    class_name = ai.get("class_name") or ai.get("taxon_group") or ai_summary.get("category") or "미정"
    return {
        "year_vendor": ai.get("year_vendor") or "미정",
        "project_name": ai.get("project_name") or "미정",
        "class_name": class_name,
        "document_type": ai.get("document_type") or "미정",
        "summary": summary or "AI 요약이 비어 있습니다.",
        "tags": normalize_tags(ai.get("tags") or ai_summary.get("keywords") or []),
        "is_ambiguous": bool(ai.get("is_ambiguous", False)),
        "question": ai.get("question") or "",
    }


def build_summary_markdown(job_id: str, meta: dict, classification: dict, preview: str):
    source_path = meta.get("source_path") or ""
    source_name = meta.get("source_name") or Path(source_path).name or job_id
    tags = classification["tags"] or ["#자동색인", "#NAS_데이터"]
    frontmatter = [
        "---",
        "status: raw_analyzed",
        "assigned_agent: Mohave",
        f"source_file: {yaml_scalar(source_name)}",
        f"original_nas_path: {yaml_scalar(source_path)}",
        f"year_vendor: {yaml_scalar(classification['year_vendor'])}",
        f"project_name: {yaml_scalar(classification['project_name'])}",
        f"class_name: {yaml_scalar(classification['class_name'])}",
        f"document_type: {yaml_scalar(classification['document_type'])}",
        f"tags: {json.dumps(tags, ensure_ascii=False)}",
        f"last_updated: {yaml_scalar(now_iso())}",
        "---",
    ]
    return "\n".join(frontmatter) + f"\n\n# {source_name} 1차 분석 요약\n\n## AI 요약\n{classification['summary']}\n\n## 원문 미리보기\n\n```text\n{preview}\n```\n"


def build_result_json(job_id: str, meta: dict, classification: dict, text_path: Path | None, preview: str):
    source_path = meta.get("source_path") or ""
    outputs = meta.get("outputs") if isinstance(meta.get("outputs"), dict) else {}
    metrics = {
        "source_size_bytes": Path(source_path).stat().st_size if source_path and Path(source_path).exists() else 0,
        "text_chars": len(preview),
        "table_count": len(outputs.get("tables") or []),
        "is_ambiguous": classification["is_ambiguous"],
    }
    return {
        "metadata": {
            "job_id": job_id,
            "timestamp": meta.get("processed_at") or now_iso(),
            "source_path": source_path,
            "source_name": meta.get("source_name") or Path(source_path).name,
            "source_type": meta.get("source_type") or "unknown",
            "device_name": meta.get("device_name") or "unknown",
            "metadata_path": outputs.get("metadata") or "",
            "text_path": str(text_path) if text_path else "",
            "ai_classification": classification,
        },
        "payload": {
            "metrics": metrics,
            "spatial_observations": [],
            "summary": classification["summary"],
            "preview": preview,
            "outputs": outputs,
        },
    }


def export_one(metadata_path: Path, processed_dir: Path, pipeline_root: Path, overwrite=False):
    metadata_path = Path(nfc(str(metadata_path))).expanduser().resolve()
    processed_dir = Path(nfc(str(processed_dir))).expanduser().resolve()
    pipeline_root = Path(nfc(str(pipeline_root))).expanduser().resolve()
    raw_dir = pipeline_root / "01_raw_analyzed"
    raw_dir.mkdir(parents=True, exist_ok=True)

    meta = read_json(metadata_path)
    if meta.get("status") != "success":
        logging.info("skip non-success metadata: %s", metadata_path)
        return None

    job_id = metadata_job_id(metadata_path, meta)
    outputs = meta.get("outputs") if isinstance(meta.get("outputs"), dict) else {}
    text_path = Path(outputs.get("text", "")) if outputs.get("text") else None
    if text_path and not text_path.is_absolute():
        text_path = processed_dir / text_path
    preview = read_text(text_path)
    classification = extract_classification(meta)

    summary_path = raw_dir / f"{job_id}.summary.md"
    result_path = raw_dir / f"{job_id}.result.json"
    if not overwrite and (summary_path.exists() or result_path.exists()):
        logging.info("skip existing job: %s", job_id)
        return job_id

    summary_path.write_text(build_summary_markdown(job_id, meta, classification, preview), encoding="utf-8")
    result_path.write_text(
        json.dumps(build_result_json(job_id, meta, classification, text_path, preview), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    logging.info("exported %s -> %s", metadata_path.name, raw_dir)
    return job_id


def iter_metadata(processed_dir: Path, metadata_files: list[str], limit: int):
    if metadata_files:
        for item in metadata_files:
            yield Path(item)
        return
    meta_dir = processed_dir / "metadata"
    count = 0
    for path in sorted(meta_dir.glob("*.metadata.json")):
        if limit and count >= limit:
            break
        count += 1
        yield path


def main():
    parser = argparse.ArgumentParser(description="processed 산출물을 005 협업 파이프라인 입력으로 export")
    parser.add_argument("--processed-dir", required=True, help="002/003 processed 루트")
    parser.add_argument("--pipeline-root", required=True, help="005 stage 루트, 예: ~/AI_BASE")
    parser.add_argument("--metadata-file", action="append", default=[], help="특정 metadata json만 export. 반복 가능")
    parser.add_argument("--limit", type=int, default=0, help="metadata-file 미지정 시 최대 처리 개수")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    processed_dir = Path(args.processed_dir).expanduser().resolve()
    pipeline_root = Path(args.pipeline_root).expanduser().resolve()
    exported = []
    for metadata_path in iter_metadata(processed_dir, args.metadata_file, args.limit):
        job_id = export_one(metadata_path, processed_dir, pipeline_root, overwrite=args.overwrite)
        if job_id:
            exported.append(job_id)
    print(json.dumps({"exported_count": len(exported), "jobs": exported}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
