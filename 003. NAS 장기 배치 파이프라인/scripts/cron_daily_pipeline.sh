#!/usr/bin/env bash

# 003. NAS 장기 배치 파이프라인 - 매일 자동 구동 쉘 스크립트
# Cron 스케줄러가 매일 자정에 이 스크립트를 기동합니다.

# 1. 환경 변수 로드 및 경로 설정
export LANG=ko_KR.UTF-8
export LC_ALL=ko_KR.UTF-8

PROJECT_DIR="/home/caiser77/dgx_workspace"
SCRIPT_PATH="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/scripts/longterm_batch_slicer.py"
VENV_ACTIVATE="${PROJECT_DIR}/venv/bin/activate"

CRON_LOG="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/logs/cron_run.log"
DAILY_REPORT="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/logs/daily_report.log"

mkdir -p "$(dirname "${CRON_LOG}")"

echo "=== [$(date)] 배치 기동 프로세스 시작 ===" >> "${CRON_LOG}"

# 2. 가상환경(venv) 활성화
if [ -f "${VENV_ACTIVATE}" ]; then
    source "${VENV_ACTIVATE}"
    echo "가상환경 활성화 완료: ${VENV_ACTIVATE}" >> "${CRON_LOG}"
else
    echo "[경고] 가상환경 활성화 스크립트가 없습니다. 기본 python3으로 실행을 시도합니다." >> "${CRON_LOG}"
fi

# 3. 슬라이싱 일괄 배치 실행 (하루 한도 300개 파일 설정)
python3 "${SCRIPT_PATH}" \
  --input-dir "/mnt/dgxbackup" \
  --processed-dir "${PROJECT_DIR}/data/processed" \
  --index-dir "${PROJECT_DIR}/data/indexes/faiss" \
  --limit 300 \
  --ocr-endpoint "http://localhost:7870" \
  --vllm-endpoint "http://localhost:8088/v1/chat/completions" \
  --vllm-model "Qwen/Qwen2.5-72B-Instruct-AWQ" \
  --report-file "${DAILY_REPORT}" \
  >> "${CRON_LOG}" 2>&1

EXIT_CODE=$?

echo "=== [$(date)] 배치 프로세스 종료 (Exit Code: ${EXIT_CODE}) ===" >> "${CRON_LOG}"
echo "--------------------------------------------------------" >> "${CRON_LOG}"

exit ${EXIT_CODE}
