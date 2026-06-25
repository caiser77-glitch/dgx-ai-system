#!/usr/bin/env python3
"""Build and maintain the Atom NAS baseline SQLite database.

The baseline records files that already exist in the official NAS watcher roots.
It intentionally avoids full-content hashing by default because these roots are
SMB/CIFS mounts and the first pass should be fast enough to establish a working
"known existing file" boundary.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sqlite3
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from atom_ignore_rules import should_exclude_path

DEFAULT_ROOTS = {
    "2023old": "/mnt/nas2023old",
    "2024": "/mnt/nas2024",
    "2025": "/mnt/nas2025",
    "2026": "/mnt/nas2026",
}
DEFAULT_DB = "/home/caiser77/dgx_workspace/data/atom_watcher/atom_baseline.sqlite"
DEFAULT_BATCH_SIZE = 1000


@dataclass(frozen=True)
class ScanRoot:
    label: str
    path: Path


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def hash_path(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8", errors="surrogateescape")).hexdigest()


def connect_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA temp_store=MEMORY")
    conn.execute("PRAGMA busy_timeout=30000")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS scan_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            status TEXT NOT NULL,
            root_count INTEGER NOT NULL DEFAULT 0,
            file_count INTEGER NOT NULL DEFAULT 0,
            dir_count INTEGER NOT NULL DEFAULT 0,
            error_count INTEGER NOT NULL DEFAULT 0,
            note TEXT
        );

        CREATE TABLE IF NOT EXISTS scan_roots (
            label TEXT PRIMARY KEY,
            root_path TEXT NOT NULL,
            enabled INTEGER NOT NULL DEFAULT 1,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS files (
            path_hash TEXT PRIMARY KEY,
            root_label TEXT NOT NULL,
            root_path TEXT NOT NULL,
            rel_path TEXT NOT NULL,
            abs_path TEXT NOT NULL,
            name TEXT NOT NULL,
            extension TEXT NOT NULL,
            size_bytes INTEGER NOT NULL,
            mtime_ns INTEGER NOT NULL,
            ctime_ns INTEGER NOT NULL,
            mode INTEGER NOT NULL,
            first_seen_at TEXT NOT NULL,
            last_seen_at TEXT NOT NULL,
            last_run_id INTEGER NOT NULL,
            status TEXT NOT NULL DEFAULT 'present',
            signature TEXT NOT NULL,
            FOREIGN KEY(last_run_id) REFERENCES scan_runs(id)
        );

        CREATE TABLE IF NOT EXISTS scan_errors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER NOT NULL,
            root_label TEXT NOT NULL,
            path TEXT NOT NULL,
            error_type TEXT NOT NULL,
            error_message TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(run_id) REFERENCES scan_runs(id)
        );

        CREATE INDEX IF NOT EXISTS idx_files_root_rel ON files(root_label, rel_path);
        CREATE INDEX IF NOT EXISTS idx_files_abs_path ON files(abs_path);
        CREATE INDEX IF NOT EXISTS idx_files_signature ON files(signature);
        CREATE INDEX IF NOT EXISTS idx_files_last_run ON files(last_run_id);
        CREATE INDEX IF NOT EXISTS idx_files_status ON files(status);
        """
    )
    conn.commit()


def parse_roots(values: list[str] | None) -> list[ScanRoot]:
    if not values:
        return [ScanRoot(label, Path(path)) for label, path in DEFAULT_ROOTS.items()]

    roots: list[ScanRoot] = []
    for raw in values:
        if "=" in raw:
            label, path = raw.split("=", 1)
            label = label.strip()
            path = path.strip()
        else:
            path_obj = Path(raw)
            label = path_obj.name or str(len(roots) + 1)
            path = raw
        if not label or not path:
            raise ValueError(f"invalid root spec: {raw!r}")
        roots.append(ScanRoot(label, Path(path)))
    return roots


def iter_tree(root: Path) -> Iterable[tuple[Path, os.stat_result | None, Exception | None, bool]]:
    stack = [root]
    while stack:
        current = stack.pop()
        try:
            with os.scandir(current) as entries:
                for entry in entries:
                    path = Path(entry.path)
                    try:
                        is_dir = entry.is_dir(follow_symlinks=False)
                        if should_exclude_path(path, is_dir=is_dir):
                            continue
                        stat = entry.stat(follow_symlinks=False)
                    except OSError as exc:
                        yield path, None, exc, False
                        continue
                    yield path, stat, None, is_dir
                    if is_dir:
                        stack.append(path)
        except OSError as exc:
            yield current, None, exc, True


def make_signature(size: int, mtime_ns: int) -> str:
    return f"size={size};mtime_ns={mtime_ns}"


def upsert_batch(conn: sqlite3.Connection, rows: list[tuple]) -> None:
    conn.executemany(
        """
        INSERT INTO files (
            path_hash, root_label, root_path, rel_path, abs_path, name, extension,
            size_bytes, mtime_ns, ctime_ns, mode, first_seen_at, last_seen_at,
            last_run_id, status, signature
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'present', ?)
        ON CONFLICT(path_hash) DO UPDATE SET
            root_label=excluded.root_label,
            root_path=excluded.root_path,
            rel_path=excluded.rel_path,
            abs_path=excluded.abs_path,
            name=excluded.name,
            extension=excluded.extension,
            size_bytes=excluded.size_bytes,
            mtime_ns=excluded.mtime_ns,
            ctime_ns=excluded.ctime_ns,
            mode=excluded.mode,
            last_seen_at=excluded.last_seen_at,
            last_run_id=excluded.last_run_id,
            status='present',
            signature=excluded.signature
        """,
        rows,
    )


def record_error(
    conn: sqlite3.Connection,
    run_id: int,
    root_label: str,
    path: Path,
    exc: Exception,
) -> None:
    conn.execute(
        """
        INSERT INTO scan_errors (run_id, root_label, path, error_type, error_message, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (run_id, root_label, str(path), type(exc).__name__, str(exc), utc_now_iso()),
    )


def scan_roots(
    conn: sqlite3.Connection,
    roots: list[ScanRoot],
    batch_size: int,
    limit: int | None,
    mark_missing: bool,
    progress_every: int,
) -> tuple[int, int, int]:
    started_at = utc_now_iso()
    cur = conn.execute(
        "INSERT INTO scan_runs (started_at, status, root_count, note) VALUES (?, 'running', ?, ?)",
        (started_at, len(roots), "atom NAS baseline scan"),
    )
    run_id = int(cur.lastrowid)
    conn.commit()

    file_count = 0
    dir_count = 0
    error_count = 0
    rows: list[tuple] = []
    last_progress = time.monotonic()

    try:
        for root in roots:
            root_path = root.path.resolve()
            now = utc_now_iso()
            conn.execute(
                """
                INSERT INTO scan_roots (label, root_path, enabled, updated_at)
                VALUES (?, ?, 1, ?)
                ON CONFLICT(label) DO UPDATE SET
                    root_path=excluded.root_path,
                    enabled=1,
                    updated_at=excluded.updated_at
                """,
                (root.label, str(root_path), now),
            )
            conn.commit()

            if not root_path.exists():
                error_count += 1
                record_error(conn, run_id, root.label, root_path, FileNotFoundError(str(root_path)))
                conn.commit()
                continue

            for path, stat, exc, is_dir in iter_tree(root_path):
                if exc is not None:
                    error_count += 1
                    record_error(conn, run_id, root.label, path, exc)
                    if error_count % batch_size == 0:
                        conn.commit()
                    continue

                if is_dir:
                    dir_count += 1
                    continue

                assert stat is not None
                try:
                    rel_path = path.relative_to(root_path).as_posix()
                except ValueError:
                    rel_path = str(path)
                abs_path = str(path)
                extension = path.suffix.lower()
                seen_at = utc_now_iso()
                signature = make_signature(stat.st_size, stat.st_mtime_ns)
                rows.append(
                    (
                        hash_path(abs_path),
                        root.label,
                        str(root_path),
                        rel_path,
                        abs_path,
                        path.name,
                        extension,
                        stat.st_size,
                        stat.st_mtime_ns,
                        stat.st_ctime_ns,
                        stat.st_mode,
                        seen_at,
                        seen_at,
                        run_id,
                        signature,
                    )
                )
                file_count += 1

                if len(rows) >= batch_size:
                    upsert_batch(conn, rows)
                    conn.commit()
                    rows.clear()

                if progress_every and file_count % progress_every == 0:
                    elapsed = max(time.monotonic() - last_progress, 0.001)
                    print(
                        f"progress files={file_count:,} dirs={dir_count:,} errors={error_count:,} "
                        f"last_root={root.label} rate={progress_every / elapsed:.1f}/s",
                        flush=True,
                    )
                    last_progress = time.monotonic()

                if limit is not None and file_count >= limit:
                    break
            if limit is not None and file_count >= limit:
                break

        if rows:
            upsert_batch(conn, rows)
            conn.commit()

        if mark_missing and limit is None:
            conn.execute(
                "UPDATE files SET status='missing' WHERE last_run_id != ? AND status='present'",
                (run_id,),
            )
            conn.commit()

        conn.execute(
            """
            UPDATE scan_runs
            SET finished_at=?, status='completed', file_count=?, dir_count=?, error_count=?
            WHERE id=?
            """,
            (utc_now_iso(), file_count, dir_count, error_count, run_id),
        )
        conn.commit()
        return run_id, file_count, error_count
    except KeyboardInterrupt:
        if rows:
            upsert_batch(conn, rows)
        conn.execute(
            """
            UPDATE scan_runs
            SET finished_at=?, status='interrupted', file_count=?, dir_count=?, error_count=?
            WHERE id=?
            """,
            (utc_now_iso(), file_count, dir_count, error_count, run_id),
        )
        conn.commit()
        raise
    except Exception:
        if rows:
            upsert_batch(conn, rows)
        conn.execute(
            """
            UPDATE scan_runs
            SET finished_at=?, status='failed', file_count=?, dir_count=?, error_count=?
            WHERE id=?
            """,
            (utc_now_iso(), file_count, dir_count, error_count, run_id),
        )
        conn.commit()
        raise


def print_summary(conn: sqlite3.Connection) -> None:
    total = conn.execute("SELECT COUNT(*) FROM files WHERE status='present'").fetchone()[0]
    print(f"baseline_present_files={total:,}")
    for row in conn.execute(
        """
        SELECT root_label, COUNT(*), COALESCE(SUM(size_bytes), 0)
        FROM files
        WHERE status='present'
        GROUP BY root_label
        ORDER BY root_label
        """
    ):
        label, count, bytes_total = row
        gib = bytes_total / (1024 ** 3)
        print(f"root={label} files={count:,} size_gib={gib:,.2f}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build Atom NAS existing-file baseline DB")
    parser.add_argument("--db", default=DEFAULT_DB, help="SQLite DB path")
    parser.add_argument(
        "--root",
        action="append",
        help="Root spec. Use label=/path. Defaults to official four NAS roots.",
    )
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--limit", type=int, default=None, help="Scan at most N files for smoke tests")
    parser.add_argument("--mark-missing", action="store_true", help="Mark previously present files missing after a full scan")
    parser.add_argument("--progress-every", type=int, default=5000)
    parser.add_argument("--summary-only", action="store_true", help="Print DB summary without scanning")
    args = parser.parse_args(argv)

    if args.batch_size < 1:
        parser.error("--batch-size must be positive")

    db_path = Path(args.db).expanduser().resolve()
    conn = connect_db(db_path)
    try:
        init_schema(conn)
        if args.summary_only:
            print_summary(conn)
            return 0

        roots = parse_roots(args.root)
        print(f"db={db_path}")
        print("roots=" + ", ".join(f"{root.label}:{root.path}" for root in roots))
        run_id, file_count, error_count = scan_roots(
            conn,
            roots=roots,
            batch_size=args.batch_size,
            limit=args.limit,
            mark_missing=args.mark_missing,
            progress_every=args.progress_every,
        )
        print(f"scan_run_id={run_id} scanned_files={file_count:,} errors={error_count:,}")
        print_summary(conn)
        return 0 if error_count == 0 else 2
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
