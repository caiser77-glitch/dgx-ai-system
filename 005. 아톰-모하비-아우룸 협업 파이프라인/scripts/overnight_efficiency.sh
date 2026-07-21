#!/usr/bin/env bash
# 005/monitoring — 야간 효율화 배치 래퍼 (아톰). 21시~06시에만 실행.
# Created: 2026-07-21 by Antigravity(Claude Opus 4.8)
# cron 이 상시 호출해도 시간창 밖이면 즉시 종료(안전). 중복실행 lock.
set -uo pipefail

H=$(date +%H)
# 21,22,23,00,01,02,03,04,05 시에만 실행 (06시 이후 정지)
if [ "$((10#$H))" -lt 21 ] && [ "$((10#$H))" -ge 6 ]; then
  exit 0
fi

LOCK=/tmp/overnight_efficiency.lock
mkdir "$LOCK" 2>/dev/null || exit 0
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

VENV=/home/caiser77/hwp_extract_venv/bin/python
PY=/home/caiser77/AI_BASE/overnight_efficiency.py
LOG=/home/caiser77/AI_BASE/overnight_efficiency.log
BATCH="${OVERNIGHT_BATCH:-30}"

"$VENV" "$PY" "$BATCH" >> "$LOG" 2>&1
