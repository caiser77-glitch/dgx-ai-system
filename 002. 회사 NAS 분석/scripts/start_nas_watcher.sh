#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_PYTHON="$BASE_DIR/../venv/bin/python"

LOG_FILE="$BASE_DIR/logs/watchdog_pipeline.log"
PID_FILE="$BASE_DIR/logs/watchdog_pipeline.pid"
NAS_AI_ROOT="/mnt/dgxbackup/_AURUM_AI_PROCESSED"
WATCH_DIR="/mnt/dgxbackup/_AURUM_AI_INBOX"
PROCESSED_DIR="$NAS_AI_ROOT/processed"
STATE_FILE="$PROCESSED_DIR/state.json"
INDEX_DIR="/home/caiser77/dgx_workspace/cache/faiss_current"

mkdir -p "$BASE_DIR/logs"
mkdir -p "$PROCESSED_DIR"
mkdir -p "$INDEX_DIR"
mkdir -p "$NAS_AI_ROOT/logs"
mkdir -p "$WATCH_DIR"

echo "Starting Watchdog pipeline for Company NAS (26Project 2026)..."
echo "Watch target: $WATCH_DIR"
echo "Processed output: $PROCESSED_DIR"
echo "FAISS cache: $INDEX_DIR"
echo "Log: $LOG_FILE"
echo "PID file: $PID_FILE"

if [ -f "$PID_FILE" ]; then
  EXISTING_PID="$(cat "$PID_FILE" 2>/dev/null || true)"
  if [ -n "$EXISTING_PID" ] && ps -p "$EXISTING_PID" -o cmd= 2>/dev/null | grep -q "watchdog_pipeline.py"; then
    echo "NAS Watcher already running: $EXISTING_PID"
    exit 0
  fi
fi

setsid -f "$VENV_PYTHON" "$SCRIPT_DIR/watchdog_pipeline.py" \
  --watch "$WATCH_DIR" \
  --device-name "NAS_2026" \
  --log-file "$LOG_FILE" \
  --state-file "$STATE_FILE" \
  --processed-dir "$PROCESSED_DIR" \
  --index-dir "$INDEX_DIR" \
  --observer native \
  --auto-index \
  > "$BASE_DIR/logs/watcher_stdout.log" 2>&1

# Give the detached process a moment to appear, then persist its PID for health checks.
sleep 1
pgrep -f "watchdog_pipeline.py.*--device-name NAS_2026" | tail -n 1 > "$PID_FILE" || true

echo "NAS Watcher daemon started successfully."
