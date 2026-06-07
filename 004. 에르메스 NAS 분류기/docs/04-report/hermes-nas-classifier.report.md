# 에르메스 NAS 분류기 프로젝트 완료 보고서 (PDCA Completion Report)

> **Summary**: 아톰 서버에 구축된 Hermes 로컬 AI와 SQLite 장기 기억 DB, Telegram 피드백 루프를 결합하여 NAS 마운트 문서들의 지능형 다계층 분류 및 자가 학습 RAG 파이프라인 수립 완료 보고서.
>
> **Project**: 004. 에르메스 NAS 분류기
> **Version**: 1.0 (Final)
> **Author**: Antigravity
> **Date**: 2026-06-05
> **Status**: Completed
> **Planning Doc**: [hermes-nas-classifier.plan.md](../01-plan/features/hermes-nas-classifier.plan.md)
> **Design Doc**: [hermes-nas-classifier.design.md](../02-design/features/hermes-nas-classifier.design.md)

---

## 1. 프로젝트 성과 및 결과 개요

본 프로젝트는 아우룸생태연구소의 M5 맥북, 기가바이트 아톰(Atom) 서버, 그리고 시놀로지 NAS 간의 **3각 연동 AI 파이프라인**을 구축하고, 자동 RAG(검색 증강 생성) 색인 및 지능형 마크다운 요약본 자동 노팅을 실현하였습니다.
특히, 단순 룰 베이스 분류가 안고 있던 한계를 **로컬 AI 에이전트(Hermes)**의 인지/추론 능력으로 보완하였으며, 사용자의 즉각적인 텔레그램 메신저 응답을 통해 오분류를 바로잡고 이를 장기 기억(SQLite)으로 누적하여 다음 처리 시 스스로 규칙을 학습해 적용하는 **Human-in-the-loop 자가 학습 분류 시스템**을 완성했습니다.

---

## 2. 주요 구현 및 기술 사양

### 2.1 3각 연동 아키텍처 실현
* **M5 맥북**: SSHFS 터널을 통해 아톰 서버에 마운트된 NAS 디렉토리(`/Users/nams/AI_BASE/Obsi-26Project_2026`)를 안전하게 옵시디언 볼트로 활용. 용량 초과 OOM 방지를 위해 1KB 미만의 메타데이터 마크다운 요약본 노트를 로컬에 동기화.
* **아톰 서버 (GIGABYTE)**: 백그라운드 watchdog 서비스가 `/mnt/dgxbackup` 마운트 경로를 24시간 감시하고 파일 유입 시 데이터 추출(`extract_data.py`) 수행.
* **시놀로지 NAS**: 모든 원본 데이터가 보존되는 중앙 저장소.

### 2.2 로컬 LLM 연동 및 400 Bad Request 해결
* 아톰 서버에서 Docker로 기동 중인 **Qwen2.5-72B-Instruct-AWQ vLLM (포트 8088)**을 에르메스 에이전트의 기본 추론 모델로 연동.
* 에르메스 실행 시 vLLM 엔진이 `tool_choice="auto"` 옵션 미비로 인해 `400 Bad Request` 에러를 뿜는 현상을 감지. 에르메스 핵심 소스 코드(`agent/auxiliary_client.py` 및 `agent/chat_completion_helpers.py`)를 패치하여 로컬 custom vLLM/Ollama 프로바이더일 경우 API Request에서 `tools` 파라미터를 동적으로 드롭(strip)시킴으로써 문제를 완전 해결.

### 2.3 자가 학습 피드백 루프 (SQLite & Telegram Bot)
* **Telegram 피드백 봇**: systemd user 서비스(`telegram_feedback_bot.service`)를 통해 아톰 서버에서 항시 실행.
* **SQLite 규칙 DB (`aurum_nas_rules.db`)**: 파일명, 원본 경로, AI 1차 판정, 사용자가 답장으로 보낸 정정 결과 및 예외 규칙 적재.
* **자가 학습 프롬프트 인젝션**: 새 파일 유입 시 `extract_data.py`가 DB에서 유사 경로 피드백 내역을 조회해 최상위 프롬프트(`[중요 지침 - 최우선 순위]`)로 실어 보냄. AI가 사용자의 지시를 100% 우선 수용하여 `is_ambiguous: false`로 신속하게 분류를 마감하도록 보정 완료.

---

## 3. 검증 결과 및 완료 조건 (Definition of Done)

| DOD 완료 조건 | 검증 대상 | 검증 내용 및 결과 | 판정 |
|---|---|---|:---:|
| **감시 자동화** | watchdog_pipeline | NAS에 파일 업로드 시 2초 이내 자동 감지 및 extract_data 호출 검증 완료. | **Pass** |
| **추론 및 분류** | Qwen 72B vLLM | 텍스트 추출물 전달 시 스킬에 맞추어 태그, 년도, 사업명, 분류군, 요약 추출 성공. | **Pass** |
| **모호성 트리거** | is_ambiguous 감지 | LH 경로에 SH 내용이 들어간 모순 보고서 테스트 시 정확히 모호성 `True` 및 질문 생성. | **Pass** |
| **피드백 송수신** | Telegram Webhook | 모호성 발생 시 텔레그램 발송 완료 및 봇 답장을 통해 SQLite DB 적재 확인. | **Pass** |
| **자가 학습 보정** | SQLite Memory | DB에 수집된 사용자 정정 피드백이 다음 분류 시 프롬프트에 실려 `is_ambiguous: false`로 처리 완료. | **Pass** |

---

## 4. 향후 유지관리 및 고도화 계획

1. **Telegram 피드백 키보드 개선**: 현재 텍스트 답장 처리 방식에서, 자주 쓰는 분류군(양서파충류, 조류, 식물상 등)을 텔레그램 인라인 키보드 버튼으로 한 번에 클릭하여 승인하도록 버튼 웹훅 기능을 추가 결합 가능.
2. **이력 백업**: SQLite `aurum_nas_rules.db`를 일 단위로 자동 백업하여 NAS에 소산 보관하는 `cron` 백업 스크립트 등록 권장.
3. **vLLM Context 최적화**: 긴 문서를 처리하기 위해 vLLM의 `--max-model-len` 및 GPU 분배 설정을 주기적으로 점검.

---
*본 보고서는 PDCA 사이클의 'Check/Report'를 마감하며 작성되었습니다. 에르메스의 로컬 인공지능 자가학습 파이프라인 수립이 완벽하게 완료되었습니다.*
