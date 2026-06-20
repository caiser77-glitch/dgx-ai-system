#!/usr/bin/env python3
from __future__ import annotations

import json
import logging
import os
import signal
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path


ROOTS = [
    Path("/mnt/nas2026/_AURUM_AI_INBOX"),
]
STATE_PATH = Path("/home/caiser77/dgx_workspace/atom_watcher_user/state/seen.json")
LOG_PATH = Path("/home/caiser77/dgx_workspace/atom_watcher_user/logs/polling_watcher.log")
ENV_PATH = Path("/home/caiser77/.hermes/.env")
POLL_SECONDS = 10
MAX_NOTIFY_PER_SCAN = 20

IGNORE_NAMES = {
    ".DS_Store",
    "Thumbs.db",
}
IGNORE_SEGMENTS = {
    "#recycle",
    ".tmp",
    "_AURUM_AI_PROCESSED",
}


stop_requested = False


@dataclass(frozen=True)
class FileRecord:
    path: str
    size: int
    mtime_ns: int


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.exists():
        return env
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def setup_logging() -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-7s %(message)s",
        handlers=[
            logging.FileHandler(LOG_PATH, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def should_ignore(path: Path) -> bool:
    if path.name in IGNORE_NAMES:
        return True
    if path.name.startswith("~$"):
        return True
    return any(part in IGNORE_SEGMENTS for part in path.parts)


def scan_roots() -> dict[str, FileRecord]:
    records: dict[str, FileRecord] = {}
    for root in ROOTS:
        if not root.exists():
            logging.warning("root missing: %s", root)
            continue
        try:
            iterator = root.rglob("*")
            for path in iterator:
                if should_ignore(path):
                    continue
                try:
                    if not path.is_file():
                        continue
                    stat = path.stat()
                except OSError as exc:
                    logging.warning("skip unreadable path: %s (%s)", path, exc)
                    continue
                records[str(path)] = FileRecord(
                    path=str(path),
                    size=stat.st_size,
                    mtime_ns=stat.st_mtime_ns,
                )
        except OSError as exc:
            logging.warning("scan failed for root %s: %s", root, exc)
    return records


def load_seen() -> dict[str, dict[str, int]]:
    if not STATE_PATH.exists():
        return {}
    try:
        data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        logging.exception("failed to load state, starting fresh")
        return {}
    if not isinstance(data, dict):
        return {}
    return data


def save_seen(records: dict[str, FileRecord]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = {
        path: {"size": record.size, "mtime_ns": record.mtime_ns}
        for path, record in records.items()
    }
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(STATE_PATH)


def telegram_send(token: str, chat_id: str, text: str) -> bool:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode(
        {
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": "true",
        }
    ).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            if response.status != 200:
                logging.warning("telegram status: %s", response.status)
                return False
            return True
    except Exception as exc:
        logging.warning("telegram send failed: %s", exc)
        return False


def format_notice(record: FileRecord) -> str:
    path = Path(record.path)
    root_name = next((str(root) for root in ROOTS if record.path.startswith(str(root))), "")
    rel = record.path.removeprefix(root_name).lstrip("/") if root_name else record.path
    return (
        "[Atom NAS Watcher]\n"
        "신규/변경 파일 감지\n"
        f"루트: {root_name or '?'}\n"
        f"상대경로: {rel}\n"
        f"파일명: {path.name}\n"
        f"크기: {record.size} bytes"
    )


def handle_signal(signum, _frame) -> None:
    global stop_requested
    logging.info("signal %s received, stopping...", signum)
    stop_requested = True


def main() -> int:
    setup_logging()
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    env = load_env(ENV_PATH)
    token = env.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = env.get("TELEGRAM_HOME_CHANNEL") or env.get("ALLOWED_USER_ID", "")
    if not token or not chat_id:
        logging.error("missing TELEGRAM_BOT_TOKEN or TELEGRAM_HOME_CHANNEL in %s", ENV_PATH)
        return 2

    logging.info("polling watcher starting")
    for root in ROOTS:
        logging.info("watch root: %s exists=%s", root, root.exists())

    seen = load_seen()
    if not seen:
        records = scan_roots()
        save_seen(records)
        seen = load_seen()
        logging.info("baseline initialized with %d files", len(seen))

    while not stop_requested:
        records = scan_roots()
        changed: list[FileRecord] = []
        for path, record in records.items():
            old = seen.get(path)
            if old is None:
                changed.append(record)
            elif old.get("size") != record.size or old.get("mtime_ns") != record.mtime_ns:
                changed.append(record)

        if changed:
            logging.info("detected %d new/changed files", len(changed))
            for record in changed[:MAX_NOTIFY_PER_SCAN]:
                logging.info("notify path=%s", record.path)
                telegram_send(token, chat_id, format_notice(record))
            if len(changed) > MAX_NOTIFY_PER_SCAN:
                telegram_send(
                    token,
                    chat_id,
                    f"[Atom NAS Watcher]\n추가 변경 {len(changed) - MAX_NOTIFY_PER_SCAN}건은 로그에 기록했습니다.",
                )
            save_seen(records)
            seen = load_seen()

        for _ in range(POLL_SECONDS):
            if stop_requested:
                break
            time.sleep(1)

    logging.info("polling watcher stopped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
