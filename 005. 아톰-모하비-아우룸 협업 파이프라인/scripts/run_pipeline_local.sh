#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PIPELINE_ROOT="${PIPELINE_ROOT:-$HOME/AI_BASE}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
LOG_DIR="${PIPELINE_LOG_DIR:-$PIPELINE_ROOT/logs}"
mkdir -p "$LOG_DIR"

"$PYTHON_BIN" "$SCRIPT_DIR/track_pipeline_status.py" --root "$PIPELINE_ROOT" init

pids=()
stop_all() {
  for pid in "${pids[@]:-}"; do
    if kill -0 "$pid" 2>/dev/null; then
      kill "$pid" 2>/dev/null || true
    fi
  done
}
trap stop_all EXIT INT TERM

"$PYTHON_BIN" "$SCRIPT_DIR/pipeline_engine.py" "$PIPELINE_ROOT/01_raw_analyzed" >> "$LOG_DIR/pipeline_engine.log" 2>&1 &
pids+=("$!")

"$PYTHON_BIN" "$SCRIPT_DIR/track_pipeline_status.py" --root "$PIPELINE_ROOT" watch --interval "${PIPELINE_TRACK_INTERVAL:-5}" >> "$LOG_DIR/track_pipeline_status.log" 2>&1 &
pids+=("$!")

"$PYTHON_BIN" "$SCRIPT_DIR/aurum_deployer.py" --root "$PIPELINE_ROOT" --interval "${AURUM_DEPLOY_INTERVAL:-2}" >> "$LOG_DIR/aurum_deployer.log" 2>&1 &
pids+=("$!")

echo "Pipeline started: root=$PIPELINE_ROOT logs=$LOG_DIR pids=${pids[*]}"
wait -n "${pids[@]}"
