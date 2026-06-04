# 코덱스 워크스페이스 지침 - AI_BASE (Global)

`AI_BASE` 워크스페이스에 오신 것을 환영합니다. 이 파일은 프로젝트 전체에 걸쳐 상호작용하는 개발자 및 AI 에이전트를 위한 핵심 규칙과 공통 인프라를 담고 있습니다.

## 🔌 공통 연결 인프라 (Kakao PlayMCP)
이 워크스페이스는 법률 데이터베이스, 지도, 금융 시장 및 검색 엔진을 위한 139개의 외부 API를 제공하는 **Kakao PlayMCP Gateway** (`mcp-gateway`)와 통합되어 있습니다.

> [!IMPORTANT]
> **PlayMCP 연동 세부 사항:**
> * 설정 및 인증 정보(Credentials)는 `~/.mcporter/mcporter.json` 및 `~/.mcporter/credentials.json`에 위치합니다.
> * 지정된 경로에 credentials 파일이 존재하지 않거나 읽기 권한이 없으면 작업을 중단하고 정확한 오류 메시지 `Credentials missing or unreadable at <path>`를 출력하십시오. 파일 생성이나 권한 변경 자동 시도는 하지 마십시오.
> * `mcporter`와 같은 Node 기반 클라이언트를 통해 도구를 호출할 때 **Brotli 압축 해제 실패** (`TypeError: terminated`)가 발생하면, 먼저 Python 실행 환경을 사용하려고 시도하십시오. Python 실행 환경이 없거나 사용 불가인 경우에는 (1) Node에서 압축 해제 옵션을 비활성화하고, (2) 게이트웨이 요청에서 압축을 비활성화할 수 있는 쿼리나 헤더를 적용하십시오. 모두 실패하면 `BROTLi_ERROR` 코드와 함께 운영자에게 알리십시오.
> * `406` 또는 `400` 오류를 방지하려면 항상 `"Accept": "application/json, text/event-stream"`을 지정하고, 초기화 중에 반환된 `Mcp-Session-Id` 헤더를 전달하십시오. 위 헤더를 설정했음에도 `406`/`400`이 발생하면 요청/응답 헤더와 바디를 캡처하여 로그에 저장하고, 에러 코드 `MCP_GATEWAY_ERROR`를 반환하십시오. 3회 자동 재시도 후에도 실패하면 운영자에게 알리십시오.
> * 상세 에이전트 연동 가이드: [`rules/kakao-mcp-guide.md`](file:///Users/nams/AI_BASE/rules/kakao-mcp-guide.md).

## 🛠️ 서브 프로젝트별 지침 (Index)
작업 중인 특정 하위 프로젝트에 진입하면, 해당 폴더의 `AGENTS.md` 가이드라인을 최우선으로 준수하십시오.
- 🏢 [002. 회사 NAS 분석 지침](file:///Volumes/caiser77/dgx_workspace/002.%20%E1%84%92%E1%85%AC%E1%84%89%E1%85%A1%20NAS%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8/AGENTS.md): 시놀로지 NAS 마운트 및 실시간 Watchdog 감시 기반 RAG 구축 파이프라인
- 🤖 [003. NAS 장기 배치 파이프라인 지침](file:///Volumes/caiser77/dgx_workspace/003.%20NAS%20%EC%9E%A5%EA%B8%B0%20%EB%B0%B0%EC%B9%98%20%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8/AGENTS.md): 10개년 대용량 문서 일자별 증분 슬라이싱 및 자정 크론탭 스케줄러 자동 배치 연동
- 📊 [Fauna_Dashboard 지침](file:///Users/nams/AI_BASE/Fauna_Dashboard/AGENTS.md): FastAPI 백엔드 및 Vite+React 프론트엔드 빌드/실행/규칙
- 🤖 [telegram_bridge 지침](file:///Users/nams/AI_BASE/telegram_bridge/AGENTS.md): 텔레그램 봇 브릿지 실행 및 전용 설정
- 🧠 [hermes-agent 지침](file:///Users/nams/AI_BASE/hermes-agent/AGENTS.md): Hermes 에이전트 대화 쉘 실행 및 규칙
- 🌾 [자원관 결과 변환 자동화 지침](file:///Users/nams/AI_BASE/자원관 결과 변환 자동화/AGENTS.md): 야생멧돼지 수색 조사 결과 데이터 표준화 및 구글 설문지 자동 제출 파이프라인.
- 🏢 [ERP_인천 지침](file:///Users/nams/AI_BASE/ERP_인천/ERP/AGENT.MD): 아우룸생태연구소 인천사무실 통합 ERP 시스템 (연차 잔액 관리, 출장 일정 신청 및 날짜 바인딩 경비 정산, 볼타(Bolta) 전자세금계산서 발급 연동 및 새만금 해양환경조사용역 PDF 견적서 매핑)

## 📋 전역 공통 규칙
1. **데이터 및 출력 규칙 (우선 순위 1) - 환각(Hallucination) 금지:**
   * 법률/금융 쿼리 도구(예: DART 또는 법제처 API)가 결과를 반환하지 않으면 정확히 `데이터를 찾을 수 없음`이라는 메시지를 출력하고, 사용자에게 제안할 검색어 3개(각 3~5단어)를 목록으로 제시하십시오. 자동 재시도하지 마십시오; 재시도 권장은 사용자 승인 후 수행합니다.
2. **보존 규칙 (우선 순위 2) - 주석 유지:**
   * 기존의 모든 주석과 독스트링(docstring)은 의미와 정보(의도)를 변경하지 않는 범위 내에서만 포맷/맞춤법 수정을 허용합니다. 의미를 변경하는 내용 수정은 금지합니다.
3. **콘텐츠 출처 규칙 (우선 순위 3) - 자리표시자(Placeholder) 금지:**
   * 실제 콘텐츠를 제공할 수 없을 때에도 `PLACEHOLDER`와 같은 더미 텍스트, 1x1 투명 이미지, 또는 임의 더미는 사용 금지입니다. 테스트용 파일이 필요한 경우 반드시 `generate_image`로 생성하거나 원본 파일을 첨부하십시오.
   * `generate_image` 호출이 실패하면 정확한 에러 코드 `IMAGE_GENERATION_FAILED` 및 실패 원인(HTTP 상태, 에러 메시지)을 로그에 남기고 사용자에게 `이미지 생성 실패`와 함께 재시도 여부를 묻는 메시지를 반환하십시오.
4. **정리 규칙 (우선 순위 4) - 잔여 테스트 파일 금지:**
   * 디버깅을 위해 생성된 모든 임시 파이썬 스크립트나 `.log` 파일은 작업 세션 종료 시점(예: 터미널 세션 종료, 해당 작업에 대한 PR 머지/닫힘, 또는 배포/커밋 전에 먼저 발생한 시점)까지 반드시 삭제하십시오. `scratch/` 폴더에 불필요한 파일을 남겨두지 마십시오.
5. **결과물 언어 규칙 (우선 순위 5):**
   * 결과물 작성은 한국어로 한다.
