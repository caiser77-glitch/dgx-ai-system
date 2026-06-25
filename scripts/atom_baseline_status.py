#!/usr/bin/env python3
"""Print Atom NAS baseline scan and queue status."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

DEFAULT_DB = "/home/caiser77/dgx_workspace/data/atom_watcher/atom_baseline.sqlite"


def connect(db: str) -> sqlite3.Connection:
    conn = sqlite3.connect(str(Path(db).expanduser().resolve()))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout=30000")
    return conn


def fetch_one(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> dict | None:
    row = conn.execute(sql, params).fetchone()
    return dict(row) if row else None


def fetch_all(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> list[dict]:
    return [dict(row) for row in conn.execute(sql, params).fetchall()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Show Atom baseline DB status")
    parser.add_argument("--db", default=DEFAULT_DB)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    conn = connect(args.db)
    try:
        latest_run = fetch_one(
            conn,
            """
            SELECT id, started_at, finished_at, status, root_count, file_count, dir_count, error_count
            FROM scan_runs
            ORDER BY id DESC
            LIMIT 1
            """,
        )
        roots = fetch_all(
            conn,
            """
            SELECT root_label, COUNT(*) AS file_count, COALESCE(SUM(size_bytes), 0) AS size_bytes
            FROM files
            WHERE status='present'
            GROUP BY root_label
            ORDER BY root_label
            """,
        )
        queue = fetch_all(
            conn,
            """
            SELECT status, decision, COUNT(*) AS count
            FROM event_queue
            GROUP BY status, decision
            ORDER BY status, decision
            """,
        ) if fetch_one(conn, "SELECT name FROM sqlite_master WHERE type='table' AND name='event_queue'") else []
        total_files = fetch_one(conn, "SELECT COUNT(*) AS count FROM files WHERE status='present'") or {"count": 0}
        errors = fetch_one(conn, "SELECT COUNT(*) AS count FROM scan_errors") or {"count": 0}
        payload = {
            "latest_run": latest_run,
            "total_present_files": total_files["count"],
            "scan_error_count": errors["count"],
            "roots": roots,
            "queue": queue,
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            run = latest_run or {}
            print(
                "run="
                f"{run.get('id')} status={run.get('status')} started={run.get('started_at')} "
                f"finished={run.get('finished_at')} files_in_run={run.get('file_count')} "
                f"errors_in_run={run.get('error_count')}"
            )
            print(f"baseline_present_files={payload['total_present_files']:,} scan_errors={payload['scan_error_count']:,}")
            for root in roots:
                gib = root["size_bytes"] / (1024 ** 3)
                print(f"root={root['root_label']} files={root['file_count']:,} size_gib={gib:,.2f}")
            if queue:
                for item in queue:
                    print(f"queue status={item['status']} decision={item['decision']} count={item['count']:,}")
            else:
                print("queue=empty")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
