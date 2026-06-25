#!/usr/bin/env python3
"""Classify Atom NAS file events against the baseline DB and optionally enqueue them.

This is the bridge between atom-watcher events and the existing-file baseline.
It answers the small operational question: is this path already known, new, or
changed since the baseline was built?
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from atom_ignore_rules import should_exclude_path

DEFAULT_DB = "/home/caiser77/dgx_workspace/data/atom_watcher/atom_baseline.sqlite"
DEFAULT_ROOTS = {
    "2023old": "/mnt/nas2023old",
    "2024": "/mnt/nas2024",
    "2025": "/mnt/nas2025",
    "2026": "/mnt/nas2026",
}


@dataclass(frozen=True)
class Decision:
    path: str
    root_label: str | None
    root_path: str | None
    rel_path: str | None
    decision: str
    event_type: str
    reason: str
    path_hash: str
    baseline_signature: str | None
    current_signature: str | None
    size_bytes: int | None
    mtime_ns: int | None
    queue_id: int | None = None


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def hash_path(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8", errors="surrogateescape")).hexdigest()


def make_signature(size: int, mtime_ns: int) -> str:
    return f"size={size};mtime_ns={mtime_ns}"


def connect_db(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA busy_timeout=30000")
    return conn


def init_queue_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS event_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_key TEXT NOT NULL UNIQUE,
            path_hash TEXT NOT NULL,
            root_label TEXT,
            root_path TEXT,
            rel_path TEXT,
            abs_path TEXT NOT NULL,
            event_type TEXT NOT NULL,
            decision TEXT NOT NULL,
            reason TEXT NOT NULL,
            baseline_signature TEXT,
            current_signature TEXT,
            size_bytes INTEGER,
            mtime_ns INTEGER,
            queued_at TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            attempt_count INTEGER NOT NULL DEFAULT 0,
            last_error TEXT,
            processed_at TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_event_queue_status ON event_queue(status, queued_at);
        CREATE INDEX IF NOT EXISTS idx_event_queue_path_hash ON event_queue(path_hash);
        CREATE INDEX IF NOT EXISTS idx_event_queue_root ON event_queue(root_label);
        """
    )
    conn.commit()


def load_roots(conn: sqlite3.Connection) -> list[tuple[str, Path]]:
    rows = conn.execute(
        "SELECT label, root_path FROM scan_roots WHERE enabled=1 ORDER BY length(root_path) DESC"
    ).fetchall()
    if rows:
        return [(row["label"], Path(row["root_path"]).resolve()) for row in rows]
    return [(label, Path(path).resolve()) for label, path in DEFAULT_ROOTS.items()]


def find_root(path: Path, roots: Iterable[tuple[str, Path]]) -> tuple[str | None, Path | None, str | None]:
    resolved = path.resolve(strict=False)
    for label, root in roots:
        try:
            rel = resolved.relative_to(root)
            return label, root, rel.as_posix()
        except ValueError:
            continue
    return None, None, None


def classify_path(conn: sqlite3.Connection, raw_path: str, event_type: str) -> Decision:
    path = Path(raw_path).expanduser().resolve(strict=False)
    abs_path = str(path)
    path_hash = hash_path(abs_path)
    roots = load_roots(conn)
    root_label, root_path, rel_path = find_root(path, roots)

    row = conn.execute("SELECT * FROM files WHERE path_hash=?", (path_hash,)).fetchone()

    if should_exclude_path(path):
        return Decision(
            path=abs_path,
            root_label=root_label,
            root_path=str(root_path) if root_path else None,
            rel_path=rel_path,
            decision="ignored",
            event_type=event_type,
            reason="path matches Atom NAS ignore rules",
            path_hash=path_hash,
            baseline_signature=row["signature"] if row else None,
            current_signature=None,
            size_bytes=None,
            mtime_ns=None,
        )

    try:
        stat = path.stat()
        if not path.is_file():
            current_signature = None
            size_bytes = None
            mtime_ns = None
        else:
            size_bytes = stat.st_size
            mtime_ns = stat.st_mtime_ns
            current_signature = make_signature(size_bytes, mtime_ns)
    except FileNotFoundError:
        current_signature = None
        size_bytes = None
        mtime_ns = None
        if row is None:
            return Decision(
                path=abs_path,
                root_label=root_label,
                root_path=str(root_path) if root_path else None,
                rel_path=rel_path,
                decision="missing_unknown",
                event_type=event_type,
                reason="path does not exist and is not in baseline",
                path_hash=path_hash,
                baseline_signature=None,
                current_signature=None,
                size_bytes=None,
                mtime_ns=None,
            )
        return Decision(
            path=abs_path,
            root_label=row["root_label"],
            root_path=row["root_path"],
            rel_path=row["rel_path"],
            decision="deleted",
            event_type=event_type,
            reason="path existed in baseline but is now missing",
            path_hash=path_hash,
            baseline_signature=row["signature"],
            current_signature=None,
            size_bytes=None,
            mtime_ns=None,
        )

    if root_label is None:
        return Decision(
            path=abs_path,
            root_label=None,
            root_path=None,
            rel_path=None,
            decision="outside_roots",
            event_type=event_type,
            reason="path is outside official NAS watcher roots",
            path_hash=path_hash,
            baseline_signature=row["signature"] if row else None,
            current_signature=current_signature,
            size_bytes=size_bytes,
            mtime_ns=mtime_ns,
        )

    if current_signature is None:
        return Decision(
            path=abs_path,
            root_label=root_label,
            root_path=str(root_path) if root_path else None,
            rel_path=rel_path,
            decision="not_file",
            event_type=event_type,
            reason="path exists but is not a regular file",
            path_hash=path_hash,
            baseline_signature=row["signature"] if row else None,
            current_signature=None,
            size_bytes=None,
            mtime_ns=None,
        )

    if row is None:
        return Decision(
            path=abs_path,
            root_label=root_label,
            root_path=str(root_path) if root_path else None,
            rel_path=rel_path,
            decision="new",
            event_type=event_type,
            reason="path is not present in baseline",
            path_hash=path_hash,
            baseline_signature=None,
            current_signature=current_signature,
            size_bytes=size_bytes,
            mtime_ns=mtime_ns,
        )

    if row["signature"] == current_signature and row["status"] == "present":
        return Decision(
            path=abs_path,
            root_label=row["root_label"],
            root_path=row["root_path"],
            rel_path=row["rel_path"],
            decision="existing",
            event_type=event_type,
            reason="path and signature match baseline",
            path_hash=path_hash,
            baseline_signature=row["signature"],
            current_signature=current_signature,
            size_bytes=size_bytes,
            mtime_ns=mtime_ns,
        )

    return Decision(
        path=abs_path,
        root_label=row["root_label"],
        root_path=row["root_path"],
        rel_path=row["rel_path"],
        decision="changed",
        event_type=event_type,
        reason="path exists in baseline but size or mtime changed",
        path_hash=path_hash,
        baseline_signature=row["signature"],
        current_signature=current_signature,
        size_bytes=size_bytes,
        mtime_ns=mtime_ns,
    )


def enqueue_decision(conn: sqlite3.Connection, decision: Decision) -> Decision:
    if decision.decision not in {"new", "changed", "deleted"}:
        return decision
    event_key = hash_path(
        "|".join(
            [
                decision.path_hash,
                decision.decision,
                decision.current_signature or "",
                decision.event_type,
            ]
        )
    )
    conn.execute(
        """
        INSERT OR IGNORE INTO event_queue (
            event_key, path_hash, root_label, root_path, rel_path, abs_path,
            event_type, decision, reason, baseline_signature, current_signature,
            size_bytes, mtime_ns, queued_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            event_key,
            decision.path_hash,
            decision.root_label,
            decision.root_path,
            decision.rel_path,
            decision.path,
            decision.event_type,
            decision.decision,
            decision.reason,
            decision.baseline_signature,
            decision.current_signature,
            decision.size_bytes,
            decision.mtime_ns,
            utc_now_iso(),
        ),
    )
    conn.commit()
    row = conn.execute("SELECT id FROM event_queue WHERE event_key=?", (event_key,)).fetchone()
    return Decision(**{**asdict(decision), "queue_id": int(row["id"]) if row else None})


def queue_summary(conn: sqlite3.Connection) -> list[dict]:
    rows = conn.execute(
        """
        SELECT status, decision, COUNT(*) AS count
        FROM event_queue
        GROUP BY status, decision
        ORDER BY status, decision
        """
    ).fetchall()
    return [dict(row) for row in rows]


def print_decisions(decisions: list[Decision], json_output: bool) -> None:
    if json_output:
        print(json.dumps([asdict(decision) for decision in decisions], ensure_ascii=False, indent=2))
        return
    for decision in decisions:
        queue = f" queue_id={decision.queue_id}" if decision.queue_id is not None else ""
        print(
            f"{decision.decision} event={decision.event_type} root={decision.root_label} "
            f"path={decision.path}{queue} reason={decision.reason}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify Atom watcher file events against baseline DB")
    parser.add_argument("paths", nargs="*", help="File paths to classify")
    parser.add_argument("--db", default=DEFAULT_DB)
    parser.add_argument("--event-type", default="manual", help="created, modified, deleted, moved, manual, etc.")
    parser.add_argument("--enqueue", action="store_true", help="Enqueue new/changed/deleted decisions")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    parser.add_argument("--queue-summary", action="store_true", help="Print event queue summary")
    args = parser.parse_args()

    conn = connect_db(Path(args.db).expanduser().resolve())
    try:
        init_queue_schema(conn)
        if args.queue_summary:
            print(json.dumps(queue_summary(conn), ensure_ascii=False, indent=2))
            return 0
        if not args.paths:
            parser.error("paths are required unless --queue-summary is used")
        decisions: list[Decision] = []
        for raw_path in args.paths:
            decision = classify_path(conn, raw_path, args.event_type)
            if args.enqueue:
                decision = enqueue_decision(conn, decision)
            decisions.append(decision)
        print_decisions(decisions, args.json)
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
