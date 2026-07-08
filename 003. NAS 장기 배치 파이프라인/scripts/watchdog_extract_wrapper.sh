#!/usr/bin/env bash
# watchdog_pipeline.py의 --command 인자에서 공백 포함 경로를 shlex.split이
# 깨뜨리는 문제를 피하기 위한 얇은 래퍼. extract_data.py에 고정 인자를 전달한다.
exec /home/caiser77/dgx_workspace/venv/bin/python3 "/home/caiser77/dgx_workspace/002. 회사 NAS 분석/scripts/extract_data.py" \
  --output-dir /home/caiser77/dgx_workspace/data/processed \
  --ocr-endpoint http://localhost:7870 \
  "$@"
