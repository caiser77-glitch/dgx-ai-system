#!/usr/bin/env bash
# 두 개의 슬라이서 백그라운드 프로세스를 병렬 실행하고 대기하는 래퍼 스크립트 (전수조사용)

# 파이썬 출력 버퍼링 비활성화 (실시간 대시보드 반영용)
export PYTHONUNBUFFERED=1

PROJECT_DIR="/home/caiser77/dgx_workspace"
SCRIPT_PATH="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/scripts/longterm_batch_slicer.py"
PYTHON_BIN="${PROJECT_DIR}/venv/bin/python3"
DAILY_REPORT="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/logs/daily_report.log"

# 중복 실행 방지를 위해 기존 슬라이서 정리
pkill -f longterm_batch_slicer.py || true
sleep 2

# 1. nas2026 대상 슬라이서 구동
$PYTHON_BIN "$SCRIPT_PATH" \
  --input-dir /mnt/nas2026 \
  --processed-dir "$PROJECT_DIR/data/processed" \
  --index-dir "$PROJECT_DIR/data/indexes/faiss" \
  --limit 500000 \
  --workers 2 \
  --ocr-endpoint http://localhost:7870 \
  --vllm-endpoint http://localhost:8088/v1/chat/completions \
  --vllm-model Qwen/Qwen2.5-72B-Instruct-AWQ \
  --report-file "$DAILY_REPORT" \
  > "$PROJECT_DIR/003. NAS 장기 배치 파이프라인/logs/slicer_nas2026.log" 2>&1 &

# 2. mnt 전체 대상 슬라이서 구동
$PYTHON_BIN "$SCRIPT_PATH" \
  --input-dir /mnt \
  --processed-dir "$PROJECT_DIR/data/processed" \
  --index-dir "$PROJECT_DIR/data/indexes/faiss" \
  --limit 500000 \
  --workers 2 \
  --ocr-endpoint http://localhost:7870 \
  --vllm-endpoint http://localhost:8088/v1/chat/completions \
  --vllm-model Qwen/Qwen2.5-72B-Instruct-AWQ \
  --report-file "$DAILY_REPORT" \
  > "$PROJECT_DIR/003. NAS 장기 배치 파이프라인/logs/slicer_mnt.log" 2>&1 &

# 자식 프로세스들이 모두 종료될 때까지 대기
wait
