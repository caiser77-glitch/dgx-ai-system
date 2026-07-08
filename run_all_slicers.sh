#!/usr/bin/env bash
# Created: 2026-07-05 by Antigravity AI
# Purpose: Optimized multi-slicer execution script targeting 20 workers and local Qwen-72B vLLM

export PYTHONUNBUFFERED=1

PROJECT_DIR="/home/caiser77/dgx_workspace"
SCRIPT_PATH="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/scripts/longterm_batch_slicer.py"
PYTHON_BIN="${PROJECT_DIR}/venv/bin/python3"
DAILY_REPORT="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/logs/daily_report.log"

# 중복 가동 프로세스 클린업
pkill -f longterm_batch_slicer.py || true
sleep 1

# 1. nas2026 대상은 맥북이 역방향(16 Workers)으로 고속 가공 중이므로 아톰에서는 생략 처리합니다.
# 2. mnt 전체 대상 슬라이서 구동 (Workers 20으로 한계 돌파 & 로컬 Qwen 72B 연동)
$PYTHON_BIN "$SCRIPT_PATH" \
  --input-dir /mnt \
  --processed-dir "$PROJECT_DIR/data/processed" \
  --index-dir "$PROJECT_DIR/data/indexes/faiss" \
  --limit 500000 \
  --workers 8 \
  --ocr-endpoint http://localhost:7870 \
  --vllm-endpoint http://localhost:8088/v1/chat/completions \
  --vllm-model Qwen/Qwen2.5-72B-Instruct-AWQ \
  --embedding-model sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 \
  --embedding-device cpu \
  --embedding-batch-size 32 \
  --skip-current-index \
  --report-file "$DAILY_REPORT" \
  >> "$PROJECT_DIR/003. NAS 장기 배치 파이프라인/logs/slicer_mnt.log" 2>&1 &

wait
