#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PROJECT_DIR="/home/caiser77/dgx_workspace"
PYTHON_BIN="/home/caiser77/hermes-agent/.venv/bin/python"
BOT_SCRIPT="$SCRIPT_DIR/telegram_feedback_bot.py"
LOG_DIR="$BASE_DIR/logs"
PID_FILE="$LOG_DIR/telegram_feedback_bot.pid"
LOG_FILE="$LOG_DIR/telegram_feedback_bot.log"
ENV_FILE="/home/caiser77/.hermes/.env"

mkdir -p "$LOG_DIR"

if [ -f "$ENV_FILE" ]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

export AURUM_RAG_INDEX_DIR="${AURUM_RAG_INDEX_DIR:-/home/caiser77/dgx_workspace/cache/faiss_current}"

if [ -z "${ALLOWED_USER_ID:-}" ] && [ -n "${TELEGRAM_ALLOWED_USERS:-}" ]; then
  ALLOWED_USER_ID="${TELEGRAM_ALLOWED_USERS%%,*}"
  ALLOWED_USER_ID="${ALLOWED_USER_ID//[[:space:]]/}"
  export ALLOWED_USER_ID
fi

if [ -z "${TELEGRAM_BOT_TOKEN:-}" ] || [ -z "${ALLOWED_USER_ID:-}" ]; then
  echo "TELEGRAM_BOT_TOKEN and ALLOWED_USER_ID or TELEGRAM_ALLOWED_USERS must be set before starting the Telegram feedback bot." >&2
  exit 1
fi

if [ -f "$PID_FILE" ]; then
  EXISTING_PID="$(cat "$PID_FILE" 2>/dev/null || true)"
  if [ -n "$EXISTING_PID" ] && ps -p "$EXISTING_PID" -o cmd= 2>/dev/null | grep -q "telegram_feedback_bot.py"; then
    echo "Telegram feedback bot already running: $EXISTING_PID"
    exit 0
  fi
fi

setsid -f "$PYTHON_BIN" "$BOT_SCRIPT" > "$LOG_FILE" 2>&1
sleep 1
pgrep -f "telegram_feedback_bot.py" | tail -n 1 > "$PID_FILE" || true

echo "Telegram feedback bot start requested. PID file: $PID_FILE"
