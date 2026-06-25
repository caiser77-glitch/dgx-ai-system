#!/usr/bin/env python3
"""Maintenance utilities for Atom baseline DB."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

from atom_ignore_rules import should_exclude_path

DEFAULT_DB = "/home/caiser77/dgx_workspace/data/atom_watcher/atom_baseline.sqlite"
BATCH_SIZE = 5000


def connect(db: str) -> sqlite3.Connection:
    conn = sqlite3.connect(str(Path(db).expanduser().resolve()))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout=30000")
    return conn


def mark_ignored(conn: sqlite3.Connection, dry_run: bool) -> int:
    total = 0
    updates: list[tuple[str]] = []
    for row in conn.execute("SELECT path_hash, abs_path FROM files WHERE status='present'"):
        if should_exclude_path(row["abs_path"]):
            updates.append((row["path_hash"],))
        if len(updates) >= BATCH_SIZE:
            total += len(updates)
            if not dry_run:
                conn.executemany("UPDATE files SET status='ignored' WHERE path_hash=?", updates)
                conn.commit()
            updates.clear()
    if updates:
        total += len(updates)
        if not dry_run:
            conn.executemany("UPDATE files SET status='ignored' WHERE path_hash=?", updates)
            conn.commit()
    return total


def status_counts(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT status, COUNT(*) AS count FROM files GROUP BY status ORDER BY status"
    ).fetchall()


def main() -> int:
    parser = argparse.ArgumentParser(description="Maintain Atom baseline DB")
    parser.add_argument("--db", default=DEFAULT_DB)
    parser.add_argument("--mark-ignored", action="store_true", help="Mark ignored paths as status=ignored")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()

    conn = connect(args.db)
    try:
        if args.mark_ignored:
            count = mark_ignored(conn, args.dry_run)
            action = "would_mark" if args.dry_run else "marked"
            print(f"{action}_ignored={count:,}")
        if args.status or not args.mark_ignored:
            for row in status_counts(conn):
                print(f"status={row['status']} count={row['count']:,}")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
