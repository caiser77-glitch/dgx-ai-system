#!/bin/bash
echo "🌿 [생태분석 워크스페이스] Fauna Ecology Swarm을 가동합니다..."
echo "데이터를 분석 중입니다. 잠시만 기다려 주세요 (약 1~3분 소요)..."

# Python 스크립트 실행
/Users/nams/AI_BASE/venv/bin/python3 /Users/nams/AI_BASE/Fauna_Workspace/System_Engine/swarm_orchestrator.py

echo ""
echo "✅ 분석이 모두 완료되었습니다!"
echo "같은 폴더 내의 '2_결과_최종보고서.md' 파일을 열어 결과물을 확인해 주세요."
