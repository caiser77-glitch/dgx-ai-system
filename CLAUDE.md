# Claude Code 작업공간 지침 - AI_BASE

`AI_BASE` 작업공간에 오신 것을 환영합니다. 이 파일은 이 프로젝트와 상호작용하는 개발자와 AI 에이전트를 위한 규칙과 표준 워크플로를 담고 있습니다.

## 🔌 연결된 MCP 서비스 및 인프라
이 작업공간은 법률 데이터베이스, 지도, 금융 시장, 검색 엔진을 위한 외부 API 139개를 노출하는 **Kakao PlayMCP Gateway** (`mcp-gateway`)와 통합되어 있습니다.

> [!IMPORTANT]
> **PlayMCP 통합 세부 사항:**
> * 설정 및 인증 정보는 `~/.mcporter/mcporter.json` 및 `~/.mcporter/credentials.json`에 있습니다.
> * `mcporter` 같은 Node 기반 클라이언트를 통해 도구를 호출할 때 **Brotli 압축 해제 실패** (`TypeError: terminated`)가 발생하면 Python (`httpx` 또는 `requests`)으로 게이트웨이 API를 직접 호출하세요.
> * `406` 또는 `400` 오류를 방지하려면 항상 `"Accept": "application/json, text/event-stream"`를 지정하고 초기화 중 반환된 `Mcp-Session-Id` 헤더를 전달하세요.
> * 상세 에이전트 통합 매뉴얼: [`rules/kakao-mcp-guide.md`](file:///Users/nams/AI_BASE/rules/kakao-mcp-guide.md).

## 🛠️ 빌드, 테스트 및 실행 명령
- **FastAPI 백엔드 시작 (포트 8005):** `./venv/bin/python Fauna_Dashboard/server/main.py`
- **Vite+React 프런트엔드 시작 (포트 5173):** `npm run dev --prefix Fauna_Dashboard -- --port 5173 --host 0.0.0.0`
- **Telegram Bot Bridge 실행:** `python3 telegram_bridge/telegram_bot_bridge.py`
- **Hermes Agent Dialog Shell 실행:** `./run_hermes.sh`

## 📋 코딩 지침 및 규칙
1. **주석 유지:** 기존의 모든 주석과 docstring을 보존하세요.
2. **플레이스홀더 금지:** 이미지 또는 데이터 블록에 플레이스홀더를 절대 사용하지 마세요. `generate_image` 또는 실제로 가져온 파일을 사용하세요.
3. **오래된 테스트 파일 금지:** 디버깅을 위해 만든 임시 Python 스크립트나 임시 `.log` 파일은 세션 완료 전에 즉시 삭제해야 합니다. `scratch/` 폴더에 불필요한 파일을 남기지 마세요.
4. **환각 금지:** 법률/금융 질의 도구(DART 또는 법제처 API 등)가 비어 있음/찾을 수 없음 결과를 반환하면 "데이터를 찾을 수 없음"으로 보고하고 질의어를 조정하세요. 법률 문구나 코드를 지어내지 마세요.
5. **결과물 언어:** 결과물 작성은 한국어로 한다.
