#!/usr/bin/env python3
"""
간단한 Watchdog 기반 파이프라인 예제.
감시 폴더에 파일이 생성되면 데이터 추출 스크립트를 호출합니다.
"""
import argparse
from datetime import datetime, timezone, timedelta
import json
import logging
from pathlib import Path
import shlex
import subprocess
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver

try:
    from slack_notify import send_slack_message, slack_enabled
except Exception:
    def send_slack_message(*args, **kwargs):
        return False

    def slack_enabled() -> bool:
        return False


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_EXTRACTOR = BASE_DIR / "scripts" / "extract_data.py"
DEFAULT_INDEXER = BASE_DIR / "scripts" / "index_documents.py"
DEFAULT_LOG = BASE_DIR / "logs" / "watchdog_pipeline.log"
DEFAULT_STATE = BASE_DIR / "data" / "processed" / "state.json"
DEFAULT_PROCESSED_DIR = BASE_DIR / "data" / "processed"
DEFAULT_INDEX_DIR = BASE_DIR / "data" / "indexes" / "faiss"


def now_iso() -> str:
    kst = timezone(timedelta(hours=9))
    return datetime.now(kst).isoformat(timespec="seconds")


def setup_logger(log_path: Path) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("watchdog_pipeline")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] %(message)s"
    )
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


def update_state(state_path: Path, device_name: str, event: dict) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        state = {"watchers": {}, "recent_events": []}

    event = {"timestamp": now_iso(), "device_name": device_name, **event}
    watchers = state.setdefault("watchers", {})
    watcher = watchers.setdefault(device_name, {})
    watcher.update(
        {
            "last_event": event.get("type"),
            "last_event_at": event["timestamp"],
            "last_file": event.get("file_path", watcher.get("last_file")),
            "last_status": event.get("status", watcher.get("last_status")),
        }
    )
    state.setdefault("recent_events", []).insert(0, event)
    state["recent_events"] = state["recent_events"][:50]
    state["updated_at"] = event["timestamp"]
    tmp_path = state_path.with_suffix(state_path.suffix + ".tmp")
    tmp_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp_path.replace(state_path)


def wait_for_stable_file(path: Path, checks: int, interval: float) -> bool:
    last_size = -1
    stable_count = 0
    for _ in range(max(checks, 1)):
        if not path.exists():
            return False
        current_size = path.stat().st_size
        if current_size == last_size:
            stable_count += 1
            if stable_count >= 2:
                return True
        else:
            stable_count = 0
            last_size = current_size
        time.sleep(interval)
    return path.exists()


def parse_command(command: str, default_script: Path) -> list[str]:
    if not command:
        return [str(default_script)]

    expanded = Path(command).expanduser()
    if expanded.exists():
        return [str(expanded)]

    return shlex.split(command)


def build_command(command: str, file_path: Path, device_name: str, detected_at: str) -> list[str]:
    parts = parse_command(command, DEFAULT_EXTRACTOR)

    executable = Path(parts[0])
    if not executable.is_absolute():
        candidate = BASE_DIR / executable
        if candidate.exists():
            parts[0] = str(candidate)

    if parts[0].endswith(".py"):
        parts = [sys.executable, *parts]

    return [
        *parts,
        "--input",
        str(file_path),
        "--device-name",
        device_name,
        "--detected-at",
        detected_at,
    ]


def resolve_script_command(command: str, default_script: Path) -> list[str]:
    parts = parse_command(command, default_script)

    executable = Path(parts[0])
    if not executable.is_absolute():
        candidate = BASE_DIR / executable
        if candidate.exists():
            parts[0] = str(candidate)

    if parts[0].endswith(".py"):
        parts = [sys.executable, *parts]
    return parts


def build_index_command(
    command: str,
    processed_dir: Path,
    index_dir: Path,
    state_file: Path,
) -> list[str]:
    return [
        *resolve_script_command(command, DEFAULT_INDEXER),
        "--processed-dir",
        str(processed_dir),
        "--index-dir",
        str(index_dir),
        "--state-file",
        str(state_file),
    ]


class NewFileHandler(FileSystemEventHandler):
    def __init__(
        self,
        command,
        device_name,
        logger,
        stable_checks,
        stable_interval,
        state_file,
        auto_index,
        index_command,
        processed_dir,
        index_dir,
        index_mode,
        index_debounce_seconds,
        index_every_n_files,
    ):
        self.command = command
        self.device_name = device_name
        self.logger = logger
        self.stable_checks = stable_checks
        self.stable_interval = stable_interval
        self.state_file = state_file
        self.auto_index = auto_index
        self.index_command = index_command
        self.processed_dir = processed_dir
        self.index_dir = index_dir
        self.index_mode = index_mode
        self.index_debounce_seconds = index_debounce_seconds
        self.index_every_n_files = max(index_every_n_files, 1)
        self.pending_index_files = []
        self.last_index_completed_at = time.time()

    def is_ignored_path(self, file_path: Path) -> bool:
        ignored_roots = [self.processed_dir, self.index_dir]
        try:
            resolved_file = file_path.resolve()
        except OSError:
            resolved_file = file_path

        for root in ignored_roots:
            try:
                resolved_root = root.resolve()
            except OSError:
                resolved_root = root
            try:
                resolved_file.relative_to(resolved_root)
                return True
            except ValueError:
                continue
        return False

    def run_auto_index(self, file_path: Path) -> None:
        index_started_at = time.time()
        run_command = build_index_command(
            self.index_command,
            self.processed_dir,
            self.index_dir,
            self.state_file,
        )
        self.logger.info("auto_index_started file=%s command=%s", file_path, run_command)
        update_state(
            self.state_file,
            self.device_name,
            {
                "type": "auto_index_started",
                "status": "running",
                "file_path": str(file_path),
                "command": run_command,
                "processed_dir": str(self.processed_dir),
                "index_dir": str(self.index_dir),
            },
        )

        try:
            result = subprocess.run(
                run_command,
                check=True,
                capture_output=True,
                text=True,
            )
            elapsed = time.time() - index_started_at
            self.logger.info(
                "auto_index_completed file=%s device=%s elapsed=%.2fs stdout=%s",
                file_path,
                self.device_name,
                elapsed,
                result.stdout.strip(),
            )
            update_state(
                self.state_file,
                self.device_name,
                {
                    "type": "auto_index_completed",
                    "status": "success",
                    "file_path": str(file_path),
                    "elapsed_seconds": round(elapsed, 2),
                    "stdout": result.stdout.strip(),
                    "processed_dir": str(self.processed_dir),
                    "index_dir": str(self.index_dir),
                },
            )
            if slack_enabled():
                send_slack_message(f"자동 색인 완료: {file_path}")
        except subprocess.CalledProcessError as e:
            error_text = (e.stderr or str(e)).strip()
            self.logger.error(
                "auto_index_failed file=%s device=%s returncode=%s stderr=%s",
                file_path,
                self.device_name,
                e.returncode,
                error_text,
            )
            update_state(
                self.state_file,
                self.device_name,
                {
                    "type": "auto_index_failed",
                    "status": "failed",
                    "file_path": str(file_path),
                    "return_code": e.returncode,
                    "error": error_text,
                    "processed_dir": str(self.processed_dir),
                    "index_dir": str(self.index_dir),
                },
            )
            if slack_enabled():
                send_slack_message(f"자동 색인 실패: {file_path}\n{error_text}")

    def maybe_run_auto_index(self, file_path: Path) -> None:
        if not self.auto_index:
            return

        if self.index_mode == "immediate":
            self.run_auto_index(file_path)
            self.last_index_completed_at = time.time()
            return

        self.pending_index_files.append(str(file_path))
        pending_count = len(self.pending_index_files)
        elapsed_since_index = time.time() - self.last_index_completed_at
        should_index = False
        reason = ""

        if self.index_mode == "batch":
            should_index = pending_count >= self.index_every_n_files
            reason = f"batch_count={pending_count}/{self.index_every_n_files}"
        elif self.index_mode == "debounced":
            should_index = (
                pending_count >= self.index_every_n_files
                or elapsed_since_index >= self.index_debounce_seconds
            )
            reason = (
                f"pending_count={pending_count}, "
                f"elapsed_since_index={elapsed_since_index:.2f}s, "
                f"debounce={self.index_debounce_seconds}s"
            )

        if not should_index:
            self.logger.info(
                "auto_index_deferred file=%s mode=%s pending=%s",
                file_path,
                self.index_mode,
                pending_count,
            )
            update_state(
                self.state_file,
                self.device_name,
                {
                    "type": "auto_index_deferred",
                    "status": "deferred",
                    "file_path": str(file_path),
                    "index_mode": self.index_mode,
                    "pending_count": pending_count,
                    "index_dir": str(self.index_dir),
                },
            )
            return

        self.logger.info(
            "auto_index_flush_started file=%s mode=%s reason=%s",
            file_path,
            self.index_mode,
            reason,
        )
        self.run_auto_index(file_path)
        self.last_index_completed_at = time.time()
        self.pending_index_files.clear()

    def on_created(self, event):
        if event.is_directory:
            return
        file_path = Path(event.src_path)
        if self.is_ignored_path(file_path):
            self.logger.info("ignored_generated_file file=%s", file_path)
            return
        started_at = time.time()
        detected_at = now_iso()
        self.logger.info(
            "detected file=%s device=%s command=%s",
            file_path,
            self.device_name,
            self.command,
        )
        update_state(
            self.state_file,
            self.device_name,
            {
                "type": "detected",
                "status": "running",
                "file_path": str(file_path),
                "command": self.command,
                "detected_at": detected_at,
            },
        )
        if slack_enabled():
            send_slack_message(
                f"새 파일 감지: {event.src_path}\nWatchdog가 데이터 추출을 시작합니다."
            )

        if not wait_for_stable_file(file_path, self.stable_checks, self.stable_interval):
            self.logger.error("file_not_ready file=%s", file_path)
            update_state(
                self.state_file,
                self.device_name,
                {
                    "type": "extraction_failed",
                    "status": "failed",
                    "file_path": str(file_path),
                    "error": "file_not_ready",
                    "detected_at": detected_at,
                },
            )
            return

        run_command = build_command(self.command, file_path, self.device_name, detected_at)
        self.logger.info("extraction_started file=%s command=%s", file_path, run_command)
        update_state(
            self.state_file,
            self.device_name,
            {
                "type": "extraction_started",
                "status": "running",
                "file_path": str(file_path),
                "command": run_command,
                "detected_at": detected_at,
            },
        )
        try:
            result = subprocess.run(
                run_command,
                check=True,
                capture_output=True,
                text=True,
            )
            elapsed = time.time() - started_at
            self.logger.info(
                "extraction_completed file=%s device=%s elapsed=%.2fs stdout=%s",
                file_path,
                self.device_name,
                elapsed,
                result.stdout.strip(),
            )
            update_state(
                self.state_file,
                self.device_name,
                {
                    "type": "extraction_completed",
                    "status": "success",
                    "file_path": str(file_path),
                    "elapsed_seconds": round(elapsed, 2),
                    "stdout": result.stdout.strip(),
                    "detected_at": detected_at,
                },
            )
            if slack_enabled():
                send_slack_message(
                    f"데이터 추출 완료: {event.src_path}"
                )
            self.maybe_run_auto_index(file_path)
        except subprocess.CalledProcessError as e:
            error_text = (e.stderr or str(e)).strip()
            self.logger.error(
                "extraction_failed file=%s device=%s returncode=%s stderr=%s",
                file_path,
                self.device_name,
                e.returncode,
                error_text,
            )
            update_state(
                self.state_file,
                self.device_name,
                {
                    "type": "extraction_failed",
                    "status": "failed",
                    "file_path": str(file_path),
                    "return_code": e.returncode,
                    "error": error_text,
                    "detected_at": detected_at,
                },
            )
            if slack_enabled():
                send_slack_message(
                    f"데이터 추출 실패: {event.src_path}\n{error_text}"
                )


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--watch', required=True, help='감시할 폴더 경로')
    p.add_argument('--command', default=str(DEFAULT_EXTRACTOR), help='호출할 스크립트 경로')
    p.add_argument('--device-name', default='unknown', help='메타데이터에 기록할 장비명')
    p.add_argument('--log-file', default=str(DEFAULT_LOG), help='watcher 로그 파일 경로')
    p.add_argument('--state-file', default=str(DEFAULT_STATE), help='Dashboard가 읽을 파이프라인 상태 JSON 경로')
    p.add_argument('--auto-index', action='store_true', help='추출 성공 후 FAISS 색인을 자동 갱신')
    p.add_argument('--index-command', default=str(DEFAULT_INDEXER), help='자동 색인에 사용할 스크립트 경로')
    p.add_argument('--processed-dir', default=str(DEFAULT_PROCESSED_DIR), help='자동 색인 입력 추출 결과 루트')
    p.add_argument('--index-dir', default=str(DEFAULT_INDEX_DIR), help='자동 색인 FAISS 저장 경로')
    p.add_argument(
        '--index-mode',
        choices=('immediate', 'debounced', 'batch'),
        default='immediate',
        help='자동 색인 실행 방식. immediate는 기존 동작, debounced/batch는 대량 유입 시 전체 재색인 빈도를 낮춤',
    )
    p.add_argument(
        '--index-debounce-seconds',
        type=float,
        default=1800.0,
        help='index-mode=debounced일 때 마지막 색인 이후 이 시간이 지나면 누적분을 색인',
    )
    p.add_argument(
        '--index-every-n-files',
        type=int,
        default=50,
        help='debounced/batch 모드에서 이 개수만큼 누적되면 색인',
    )
    p.add_argument(
        '--observer',
        choices=('native', 'polling'),
        default='native',
        help='감시 방식. NAS/임시/네트워크 경로에서 문제가 있으면 polling 사용',
    )
    p.add_argument('--stable-checks', type=int, default=10, help='파일 안정 대기 최대 확인 횟수')
    p.add_argument('--stable-interval', type=float, default=0.5, help='파일 안정 확인 간격(초)')
    args = p.parse_args()

    logger = setup_logger(Path(args.log_file))
    watch_path = Path(args.watch)
    if not watch_path.exists():
        raise SystemExit(f"감시 경로 없음: {watch_path}")

    handler = NewFileHandler(
        args.command,
        args.device_name,
        logger,
        args.stable_checks,
        args.stable_interval,
        Path(args.state_file),
        args.auto_index,
        args.index_command,
        Path(args.processed_dir),
        Path(args.index_dir),
        args.index_mode,
        args.index_debounce_seconds,
        args.index_every_n_files,
    )
    observer = PollingObserver() if args.observer == 'polling' else Observer()
    observer.schedule(handler, str(watch_path), recursive=True)
    observer.start()
    logger.info("watch_started path=%s device=%s", watch_path, args.device_name)
    update_state(
        Path(args.state_file),
        args.device_name,
        {
            "type": "watch_started",
            "status": "running",
            "watch_path": str(watch_path),
        },
    )
    if slack_enabled():
        send_slack_message(f"Watchdog 감시 시작: {args.watch}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logger.info("watch_stopped path=%s device=%s", watch_path, args.device_name)
        update_state(
            Path(args.state_file),
            args.device_name,
            {
                "type": "watch_stopped",
                "status": "stopped",
                "watch_path": str(watch_path),
            },
        )
    observer.join()

if __name__ == '__main__':
    main()
