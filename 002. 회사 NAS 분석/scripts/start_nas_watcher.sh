#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_PYTHON="$BASE_DIR/../venv/bin/python"

LOG_FILE="$BASE_DIR/logs/watchdog_pipeline.log"
STATE_FILE="$BASE_DIR/data/processed/state.json"
PROCESSED_DIR="$BASE_DIR/data/processed"
INDEX_DIR="$BASE_DIR/data/indexes/faiss"

mkdir -p "$BASE_DIR/logs"
mkdir -p "$BASE_DIR/data/processed"
mkdir -p "$BASE_DIR/data/indexes/faiss"

echo "Starting Watchdog pipeline for Company NAS (26Project 2026)..."
echo "Watch target: /mnt/dgxbackup"
echo "Log: $LOG_FILE"

nohup "$VENV_PYTHON" "$SCRIPT_DIR/watchdog_pipeline.py" \
  --watch /mnt/dgxbackup \
  --device-name "NAS_2026" \
  --log-file "$LOG_FILE" \
  --state-file "$STATE_FILE" \
  --processed-dir "$PROCESSED_DIR" \
  --index-dir "$INDEX_DIR" \
  --auto-index \
  > "$BASE_DIR/logs/watcher_stdout.log" 2>&1 &

echo "NAS Watcher daemon started successfully."
