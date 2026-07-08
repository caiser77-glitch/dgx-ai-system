#!/usr/bin/env python3
"""아톰-모하비-아우룸 협업 파이프라인 상태 트래커.

역할:
- stage 디렉터리 생성 및 점검
- 02_drafting 안의 draft가 review_pending/reviewed가 되면 03_review_pending으로 파일 세트 이동
- frontmatter status/assigned_agent 갱신
"""

import argparse
import logging
import os
import re
import shutil
import time
import unicodedata
from pathlib import Path

STAGES = {
    "error": "00_error_failed",
    "raw": "01_raw_analyzed",
    "drafting": "02_drafting",
    "review": "03_review_pending",
    "published": "04_published",
}
HANDOFF_STATUSES = {"review_pending", "reviewed"}
JOB_SUFFIXES = ("summary.md", "result.json", "draft.md")


def nfc(value):
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    return value


def setup_logging(verbose=False):
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def ensure_stages(root: Path):
    root = Path(nfc(str(root))).expanduser().resolve()
    for dirname in STAGES.values():
        (root / dirname).mkdir(parents=True, exist_ok=True)
    return root


def read_text(path: Path):
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str):
    path.write_text(text, encoding="utf-8")


def parse_frontmatter(path: Path):
    try:
        content = read_text(path)
    except FileNotFoundError:
        return {}, ""

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    meta = {}
    if not match:
        return meta, content

    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, content


def update_frontmatter(path: Path, updates: dict):
    meta, content = parse_frontmatter(path)
    if re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL):
        body = re.sub(r"^---\s*\n(.*?)\n---\s*\n", "", content, count=1, flags=re.DOTALL)
    else:
        body = content
    meta.update(updates)
    fm = "---\n" + "\n".join(f"{key}: {value}" for key, value in meta.items()) + "\n---\n"
    write_text(path, fm + "\n" + body.lstrip("\n"))


def job_id_from_draft(draft_path: Path):
    name = nfc(draft_path.name)
    if not name.endswith(".draft.md"):
        raise ValueError(f"draft 파일명이 아닙니다: {draft_path}")
    return name[: -len(".draft.md")]


def collect_job_files(stage_dir: Path, job_id: str):
    files = []
    for suffix in JOB_SUFFIXES:
        path = stage_dir / f"{job_id}.{suffix}"
        if path.exists():
            files.append(path)
    return files


def move_files(files, target_dir: Path, dry_run=False):
    target_dir.mkdir(parents=True, exist_ok=True)
    moved = []
    for src in files:
        dst = target_dir / src.name
        if dst.exists():
            raise FileExistsError(f"대상 파일이 이미 있습니다: {dst}")
        logging.info("MOVE %s -> %s", src, dst)
        if not dry_run:
            shutil.move(str(src), str(dst))
        moved.append(dst)
    return moved


def scan_once(root: Path, dry_run=False):
    root = ensure_stages(root)
    drafting = root / STAGES["drafting"]
    review = root / STAGES["review"]
    moved_jobs = []

    for draft_path in sorted(drafting.glob("*.draft.md")):
        draft_path = Path(nfc(str(draft_path)))
        meta, _ = parse_frontmatter(draft_path)
        status = meta.get("status", "drafting")
        if status not in HANDOFF_STATUSES:
            logging.debug("skip %s status=%s", draft_path.name, status)
            continue

        job_id = job_id_from_draft(draft_path)
        if not dry_run:
            update_frontmatter(draft_path, {"status": status, "assigned_agent": "Aurum"})
        files = collect_job_files(drafting, job_id)
        if draft_path not in files:
            files.append(draft_path)
        move_files(files, review, dry_run=dry_run)
        moved_jobs.append(job_id)

    logging.info("scan complete: moved_jobs=%d", len(moved_jobs))
    return moved_jobs


def promote_draft(root: Path, draft_file: Path, dry_run=False):
    root = ensure_stages(root)
    draft_file = Path(nfc(str(draft_file))).expanduser().resolve()
    if not draft_file.exists():
        raise FileNotFoundError(draft_file)
    if not dry_run:
        update_frontmatter(draft_file, {"status": "review_pending", "assigned_agent": "Aurum"})
    job_id = job_id_from_draft(draft_file)
    files = collect_job_files(draft_file.parent, job_id)
    if draft_file not in files:
        files.append(draft_file)
    return move_files(files, root / STAGES["review"], dry_run=dry_run)


def watch(root: Path, interval: int, dry_run=False):
    logging.info("상태 트래커 시작: root=%s interval=%s", root, interval)
    while True:
        scan_once(root, dry_run=dry_run)
        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description="아톰-모하비-아우룸 상태 트래커")
    parser.add_argument("--root", default=os.environ.get("PIPELINE_ROOT", "~/AI_BASE"), help="파이프라인 stage 루트")
    parser.add_argument("--dry-run", action="store_true", help="파일 이동 없이 수행 내용만 출력")
    parser.add_argument("--verbose", action="store_true")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="stage 디렉터리 생성")
    sub.add_parser("scan", help="한 번 스캔하고 handoff 수행")

    promote = sub.add_parser("promote-draft", help="draft를 review_pending으로 갱신하고 review stage로 이동")
    promote.add_argument("draft_file")

    watch_parser = sub.add_parser("watch", help="주기적으로 scan 수행")
    watch_parser.add_argument("--interval", type=int, default=int(os.environ.get("PIPELINE_TRACK_INTERVAL", "5")))

    args = parser.parse_args()
    setup_logging(args.verbose)
    root = Path(args.root)

    if args.command == "init":
        resolved = ensure_stages(root)
        logging.info("stage 디렉터리 준비 완료: %s", resolved)
    elif args.command == "scan":
        scan_once(root, dry_run=args.dry_run)
    elif args.command == "promote-draft":
        promote_draft(root, Path(args.draft_file), dry_run=args.dry_run)
    elif args.command == "watch":
        watch(root, interval=args.interval, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
