#!/usr/bin/env python3
"""Process pending Atom baseline event_queue rows.

The worker is intentionally not enabled as a service yet. Run it manually first,
then promote it to a timer/service once queue behavior is verified.
"""

from __future__ import annotations

import argparse
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB = "/home/caiser77/dgx_workspace/data/atom_watcher/atom_baseline.sqlite"
DEFAULT_EXTRACT_SCRIPT = "/home/caiser77/dgx_workspace/002. 회사 NAS 분석/scripts/extract_data.py"
DEFAULT_PYTHON = "/home/caiser77/dgx_workspace/venv/bin/python"
DEFAULT_OUTPUT_DIR = "/home/caiser77/dgx_workspace/data/processed"
DEFAULT_OCR_ENDPOINT = "http://localhost:7870"
DEFAULT_DEVICE_NAME = "atom-baseline-queue"


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def connect(db: str) -> sqlite3.Connection:
    conn = sqlite3.connect(str(Path(db).expanduser().resolve()))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout=30000")
    return conn


def fetch_pending(conn: sqlite3.Connection, limit: int) -> list[sqlite3.Row]:
    return conn.execute(
        """
        SELECT *
        FROM event_queue
        WHERE status='pending'
        ORDER BY queued_at, id
        LIMIT ?
        """,
        (limit,),
    ).fetchall()


def mark_status(conn: sqlite3.Connection, row_id: int, status: str, error: str | None = None) -> None:
    conn.execute(
        """
        UPDATE event_queue
        SET status=?, last_error=?, processed_at=?
        WHERE id=?
        """,
        (status, error, now_iso(), row_id),
    )
    conn.commit()


def increment_attempt(conn: sqlite3.Connection, row_id: int) -> None:
    conn.execute(
        "UPDATE event_queue SET attempt_count=attempt_count+1 WHERE id=?",
        (row_id,),
    )
    conn.commit()


def build_extract_command(args: argparse.Namespace, abs_path: str) -> list[str]:
    return [
        args.python,
        args.extract_script,
        "--input",
        abs_path,
        "--device-name",
        args.device_name,
        "--output-dir",
        args.output_dir,
        "--ocr-endpoint",
        args.ocr_endpoint,
    ]


def process_row(conn: sqlite3.Connection, row: sqlite3.Row, args: argparse.Namespace) -> int:
    row_id = int(row["id"])
    decision = row["decision"]
    abs_path = row["abs_path"]

    if args.dry_run:
        print(f"dry_run id={row_id} decision={decision} path={abs_path}")
        return 0

    increment_attempt(conn, row_id)

    if decision == "deleted":
        mark_status(conn, row_id, "skipped_deleted", None)
        print(f"skipped_deleted id={row_id} path={abs_path}")
        return 0

    if decision not in {"new", "changed"}:
        mark_status(conn, row_id, "skipped", f"unsupported decision: {decision}")
        print(f"skipped id={row_id} decision={decision} path={abs_path}")
        return 0

    if not Path(abs_path).exists():
        mark_status(conn, row_id, "failed", "path no longer exists")
        print(f"failed id={row_id} missing path={abs_path}")
        return 1

    mark_status(conn, row_id, "processing", None)
    cmd = build_extract_command(args, abs_path)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=args.timeout_seconds)
    if result.returncode == 0:
        mark_status(conn, row_id, "done", None)
        stdout = result.stdout.strip().splitlines()[-1:] if result.stdout else []
        suffix = f" stdout_tail={stdout[0]}" if stdout else ""
        print(f"done id={row_id} path={abs_path}{suffix}")
        return 0

    error = (result.stderr or result.stdout or "unknown error").strip()[-2000:]
    mark_status(conn, row_id, "failed", error)
    print(f"failed id={row_id} returncode={result.returncode} path={abs_path} error={error}")
    return 1


def queue_summary(conn: sqlite3.Connection) -> None:
    rows = conn.execute(
        """
        SELECT status, decision, COUNT(*) AS count
        FROM event_queue
        GROUP BY status, decision
        ORDER BY status, decision
        """
    ).fetchall()
    if not rows:
        print("queue=empty")
        return
    for row in rows:
        print(f"queue status={row['status']} decision={row['decision']} count={row['count']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Process Atom baseline event queue")
    parser.add_argument("--db", default=DEFAULT_DB)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--python", default=DEFAULT_PYTHON)
    parser.add_argument("--extract-script", default=DEFAULT_EXTRACT_SCRIPT)
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--ocr-endpoint", default=DEFAULT_OCR_ENDPOINT)
    parser.add_argument("--device-name", default=DEFAULT_DEVICE_NAME)
    parser.add_argument("--timeout-seconds", type=int, default=600)
    args = parser.parse_args(argv)

    conn = connect(args.db)
    try:
        if args.summary:
            queue_summary(conn)
            return 0
        rows = fetch_pending(conn, args.limit)
        if not rows:
            print("queue=empty")
            return 0
        failures = 0
        for row in rows:
            failures += process_row(conn, row, args)
        return 1 if failures else 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
