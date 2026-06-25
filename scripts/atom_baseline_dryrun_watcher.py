#!/usr/bin/env python3
"""Dry-run Atom watcher bridge backed by the baseline DB.

This sidecar watches the official NAS roots and classifies file events against
atom_baseline.sqlite. It is intentionally separate from the root-owned official
atom-watcher service so decisions can be validated before a privileged patch.
"""

from __future__ import annotations

import argparse
import logging
import queue
import signal
import sys
import time
from pathlib import Path
from typing import Iterable

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers.polling import PollingObserver

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from atom_event_classifier import classify_path, connect_db, enqueue_decision, init_queue_schema

DEFAULT_DB = "/home/caiser77/dgx_workspace/data/atom_watcher/atom_baseline.sqlite"
DEFAULT_LOG = "/home/caiser77/dgx_workspace/logs/atom_baseline_dryrun_watcher.log"
DEFAULT_ROOTS = [
    "/mnt/nas2023old",
    "/mnt/nas2024",
    "/mnt/nas2025",
    "/mnt/nas2026",
]
DEFAULT_DEBOUNCE_SECONDS = 3.0
DEFAULT_FLUSH_SECONDS = 1.0

stop_requested = False


class QueueingHandler(FileSystemEventHandler):
    def __init__(self, events: queue.Queue[tuple[str, str]]) -> None:
        self.events = events

    def on_any_event(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        self.events.put((event.event_type, event.src_path))
        dest_path = getattr(event, "dest_path", None)
        if dest_path:
            self.events.put(("moved_to", dest_path))


def setup_logging(log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-7s %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def handle_signal(signum, _frame) -> None:
    global stop_requested
    logging.info("signal %s received, stopping", signum)
    stop_requested = True


def parse_roots(values: list[str] | None) -> list[Path]:
    raw_roots = values or DEFAULT_ROOTS
    return [Path(value).expanduser().resolve(strict=False) for value in raw_roots]


def drain_events(events: queue.Queue[tuple[str, str]], pending: dict[str, tuple[str, float]]) -> None:
    while True:
        try:
            event_type, path = events.get_nowait()
        except queue.Empty:
            return
        pending[path] = (event_type, time.monotonic())


def process_ready(
    pending: dict[str, tuple[str, float]],
    db_path: Path,
    debounce_seconds: float,
    enqueue: bool,
) -> None:
    now = time.monotonic()
    ready = [path for path, (_event_type, seen_at) in pending.items() if now - seen_at >= debounce_seconds]
    if not ready:
        return

    conn = connect_db(db_path)
    try:
        init_queue_schema(conn)
        for path in ready:
            event_type, _seen_at = pending.pop(path)
            try:
                decision = classify_path(conn, path, event_type)
                if enqueue:
                    decision = enqueue_decision(conn, decision)
                queue_part = f" queue_id={decision.queue_id}" if decision.queue_id is not None else ""
                logging.info(
                    "decision=%s event=%s root=%s path=%s reason=%s%s",
                    decision.decision,
                    decision.event_type,
                    decision.root_label,
                    decision.path,
                    decision.reason,
                    queue_part,
                )
            except Exception:
                logging.exception("failed to classify event path=%s event=%s", path, event_type)
    finally:
        conn.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Dry-run baseline-backed Atom NAS watcher")
    parser.add_argument("--db", default=DEFAULT_DB)
    parser.add_argument("--log-file", default=DEFAULT_LOG)
    parser.add_argument("--root", action="append", help="Root path to watch. Defaults to official four NAS roots.")
    parser.add_argument("--enqueue", action="store_true", help="Enqueue new/changed/deleted events instead of log-only dry-run")
    parser.add_argument("--debounce-seconds", type=float, default=DEFAULT_DEBOUNCE_SECONDS)
    parser.add_argument("--flush-seconds", type=float, default=DEFAULT_FLUSH_SECONDS)
    args = parser.parse_args(argv)

    setup_logging(Path(args.log_file).expanduser().resolve())
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    db_path = Path(args.db).expanduser().resolve()
    roots = parse_roots(args.root)
    events: queue.Queue[tuple[str, str]] = queue.Queue()
    handler = QueueingHandler(events)
    observer = PollingObserver(timeout=1.0)

    logging.info("baseline dry-run watcher starting db=%s enqueue=%s", db_path, args.enqueue)
    for root in roots:
        if not root.exists():
            logging.warning("watch root missing: %s", root)
            continue
        observer.schedule(handler, str(root), recursive=True)
        logging.info("watch root: %s", root)

    observer.start()
    pending: dict[str, tuple[str, float]] = {}
    try:
        while not stop_requested:
            drain_events(events, pending)
            process_ready(pending, db_path, args.debounce_seconds, args.enqueue)
            time.sleep(args.flush_seconds)
    finally:
        observer.stop()
        observer.join(timeout=10)
        logging.info("baseline dry-run watcher stopped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
