#!/usr/bin/env bash
# 005/monitoring — 야간 효율화 배치 래퍼 (아톰). 21시~06시에만 실행.
# Created: 2026-07-21 by Antigravity(Claude Opus 4.8)
# Updated: 2026-07-22 by Antigravity(Claude Opus 4.8) — HWP 재추출 backfill 편입(같은 시간창·lock).
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

# ── 볼트 동기화: 맥 문헌 연구원이 갱신한 종노트를 아톰으로 pull(2차 KB를 아톰 드래프터에 반영). ──
VAULT_LOG=/home/caiser77/AI_BASE/vault_sync.log
if rsync -az -e ssh aurum-mac:/Users/nams/AI_BASE/ObsidianVault/ /home/caiser77/AI_BASE/ObsidianVault/ >>"$VAULT_LOG" 2>&1; then
  echo "$(date '+%F %T') [vault-sync] pull 완료" >> "$VAULT_LOG"
fi

"$VENV" "$PY" "$BATCH" >> "$LOG" 2>&1

# ── HWP 재추출 backfill: 실패 HWP 본문을 hwp5txt로 복구(코퍼스 96% 회복). ──
# 같은 시간창·lock 안에서 순차 실행. 회복 완료분은 자동 skip(idempotent).
REEXTRACT=/home/caiser77/AI_BASE/reextract_hwp.py
RELOG=/home/caiser77/AI_BASE/reextract_hwp.log
REBATCH="${REEXTRACT_BATCH:-80}"
if [ -f "$REEXTRACT" ]; then
  echo "$(date '+%F %T') [reextract] batch=$REBATCH 시작" >> "$RELOG"
  "$VENV" "$REEXTRACT" "$REBATCH" >> "$RELOG" 2>&1
fi

# ── HWPX 재추출 backfill: PK포맷(HWPX) 본문을 XML파서로 복구(hwp5txt 미지원 포맷). ──
HWPX_RE=/home/caiser77/AI_BASE/reextract_hwpx.py
HWPX_LOG=/home/caiser77/AI_BASE/reextract_hwpx.log
if [ -f "$HWPX_RE" ]; then
  echo "$(date +%F %T) [reextract-hwpx] batch=${HWPX_BATCH:-100} 시작" >> "$HWPX_LOG"
  python3 "$HWPX_RE" "${HWPX_BATCH:-100}" >> "$HWPX_LOG" 2>&1
fi

# ── 이미지잠금 HWP OCR 회복: BinData 스캔이미지에 잠긴 본문을 tesseract(kor+eng, CPU)로 추출. ──
# 가장 무거운 단계(마지막). GPU 무경합. 회복분은 ocr_extracted 마커로 재시도 방지.
OCR_RE=/home/caiser77/AI_BASE/reextract_hwp_ocr.py
OCR_LOG=/home/caiser77/AI_BASE/reextract_hwp_ocr.log
if [ -f "$OCR_RE" ]; then
  echo "$(date +%F %T) [reextract-ocr] batch=${OCR_BATCH:-15} 시작" >> "$OCR_LOG"
  "$VENV" "$OCR_RE" "${OCR_BATCH:-15}" >> "$OCR_LOG" 2>&1
fi
