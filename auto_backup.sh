#!/bin/bash

cd /home/caiser77/dgx_workspace

# 가상환경 활성화 (혹시 필요할 경우)
source /home/caiser77/ai_env/bin/activate

# 변경사항 확인
if [[ -n $(git status --porcelain) ]]; then
    git add .
    git commit -m "auto backup $(date '+%Y-%m-%d %H:%M:%S')"
    git push
else
    echo "No changes to backup"
fi
