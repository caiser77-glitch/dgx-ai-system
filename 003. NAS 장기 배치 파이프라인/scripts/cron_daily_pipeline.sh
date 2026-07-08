#!/usr/bin/env bash
# Created: 2026-06-30 by Antigravity AI
# Purpose: Remote batch script for daily ingestion pipeline (Refactored to 12 workers for full-speed execution)

# 1. 환경 변수 로드 및 경로 설정
export LANG=ko_KR.UTF-8
export LC_ALL=ko_KR.UTF-8

PROJECT_DIR="/home/caiser77/dgx_workspace"
SCRIPT_PATH="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/scripts/longterm_batch_slicer.py"
VENV_ACTIVATE="${PROJECT_DIR}/venv/bin/activate"

# 002 지침서 공식 로컬 RAG 경로 지정 (NAS 원본 보존 규칙)
PROCESSED_DIR="${PROJECT_DIR}/data/processed"
INDEX_DIR="${PROJECT_DIR}/data/indexes/faiss"

# 운영 프로파일: 기본값은 기존 high_quality 계약을 보존한다.
ATOM_PROFILE="${AURUM_ATOM_PROFILE:-high_quality}"
VLLM_ENDPOINT="http://localhost:8088/v1/chat/completions"
VLLM_MODEL="Qwen/Qwen2.5-72B-Instruct-AWQ"
EMBEDDING_MODEL="${AURUM_EMBEDDING_MODEL:-sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2}"
EMBEDDING_DEVICE="${AURUM_EMBEDDING_DEVICE:-cpu}"
EMBEDDING_BATCH_SIZE="${AURUM_EMBEDDING_BATCH_SIZE:-32}"
SKIP_CURRENT_INDEX="${AURUM_SKIP_CURRENT_INDEX:-1}"

CRON_LOG="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/logs/cron_run.log"
DAILY_REPORT="${PROJECT_DIR}/003. NAS 장기 배치 파이프라인/logs/daily_report.log"

mkdir -p "$(dirname "${CRON_LOG}")"
mkdir -p "${PROCESSED_DIR}" "${INDEX_DIR}"

echo "=== [$(date)] 배치 기동 프로세스 시작 ===" >> "${CRON_LOG}"
echo "운영 프로파일: ${ATOM_PROFILE}, LLM: ${VLLM_MODEL}, Embedding: ${EMBEDDING_MODEL}/${EMBEDDING_DEVICE}" >> "${CRON_LOG}"

# 2. 가상환경(venv) 활성화
if [ -f "${VENV_ACTIVATE}" ]; then
    source "${VENV_ACTIVATE}"
    echo "가상환경 활성화 완료: ${VENV_ACTIVATE}" >> "${CRON_LOG}"
else
    echo "[경고] 가상환경 활성화 스크립트가 없습니다. 기본 python3으로 실행을 시도합니다." >> "${CRON_LOG}"
fi

# 3. 공식 NAS 마운트 디렉토리 /mnt 가공 (Workers: 12로 초고속 풀가동)
NAS_PATHS=("/mnt")

for path in "${NAS_PATHS[@]}"; do
    if [ -d "${path}" ]; then
        echo "[$(date)] ${path} 디렉토리 배치 가공 개시 (제한 없음 - 전수조사 모드, Workers: 12)" >> "${CRON_LOG}"
        INDEX_ARGS=()
        if [ "${SKIP_CURRENT_INDEX}" = "1" ]; then
          INDEX_ARGS+=(--skip-current-index)
        fi

        python3 "${SCRIPT_PATH}" \
          --input-dir "${path}" \
          --processed-dir "${PROCESSED_DIR}" \
          --index-dir "${INDEX_DIR}" \
          --limit 500000 \
          --workers 20 \
          --ocr-endpoint "http://localhost:7870" \
          --vllm-endpoint "${VLLM_ENDPOINT}" \
          --vllm-model "${VLLM_MODEL}" \
          --embedding-model "${EMBEDDING_MODEL}" \
          --embedding-device "${EMBEDDING_DEVICE}" \
          --embedding-batch-size "${EMBEDDING_BATCH_SIZE}" \
          "${INDEX_ARGS[@]}" \
          --report-file "${DAILY_REPORT}" \
          >> "${CRON_LOG}" 2>&1
    else
        echo "[경고] 감시 경로 누락 건너뜀: ${path}" >> "${CRON_LOG}"
    fi
done

EXIT_CODE=$?

echo "=== [$(date)] 배치 프로세스 종료 (Exit Code: ${EXIT_CODE}) ===" >> "${CRON_LOG}"
echo "--------------------------------------------------------" >> "${CRON_LOG}"

exit ${EXIT_CODE}
