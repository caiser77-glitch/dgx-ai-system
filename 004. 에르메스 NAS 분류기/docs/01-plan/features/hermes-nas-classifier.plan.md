# hermes-nas-classifier Planning Document

> **Summary**: 아톰 서버의 에르메스(Hermes) 로컬 AI 에이전트를 활용하여, NAS에 업로드되는 대용량 다차원 계층 구조의 데이터(현장조사표, 사진, 엑셀 등)를 자동 분석, 요약 및 최적의 태그로 분류하여 맥북 옵시디언으로 연동하는 지능형 RAG 분류 시스템 계획서
>
> **Project**: 004. 에르메스 NAS 분류기
> **Version**: 0.1
> **Author**: Antigravity
> **Date**: 2026-06-05
> **Status**: Draft

---

## 1. Overview (개요)

### 1.1 Purpose (목적)
본 프로젝트는 기존의 정적이고 단순한 정규식(Regex) 기반 경로 매핑 한계를 극복하고, **로컬 AI 에이전트(Hermes)**의 인지 및 추론 능력을 결합하여 복잡하게 분류된 NAS 폴더 구조(`년도별 ➡️ 업체별 ➡️ 사업별 ➡️ 분류군별 ➡️ 파일`)에 맞추어 지능적인 자동 RAG 색인 및 옵시디언 요약 노팅 파이프라인을 구축하는 것을 목적으로 합니다.
또한 모호하거나 에러가 발생한 분류에 대해 사용자와의 메신저 대화(Slack/Telegram)를 통해 피드백을 수집하고 이를 스스로 기억(Memory)에 누적시켜 자가 학습하도록 구현합니다.

### 1.2 Background (배경)
* **대용량 파일 분류 관리 오버헤드**: 맥북의 하드 드라이브 용량 부족 및 옵시디언의 파일 감시자(File Watcher) OOM 크래시를 예방하기 위해 데이터와 노트를 분리(NAS 마운트 활용)했습니다.
* **지능형 태깅 필요성**: 텍스트 분석에 기반하여 폴더 구조와 문서 내용의 모순을 감지하고, RAG용 최상급 태깅(예: `#양서파충류`, `#2026LH` 등)을 동적으로 자동 부여해야 할 필요성이 커졌습니다.
* **자가 학습 필요성**: 실무에서 보고서 형식이 다양하게 변하더라도 에이전트가 사용자의 가이드를 학습하여 장기적으로 휴먼 에러를 줄이고 자동화 신뢰도를 높여야 합니다.

### 1.3 Related Documents (관련 문서)
- 사용설명서: [로컬_AI_서버_및_대용량_파일_관리_사용설명서.md](../../../아우룸%20AI_서버%20구축/docs/로컬_AI_서버_및_대용량_파일_관리_사용설명서.md)
- 아우룸 AI 서버 계획서: [gigabyte-local-ai-server.plan.md](../../../아우룸%20AI_서버%20구축/docs/01-plan/features/gigabyte-local-ai-server.plan.md)

---

## 2. Scope (범위)

### 2.1 In Scope (포함 범위)
- [ ] 아톰 서버 `watchdog_pipeline.py`에 재귀적 감시(`recursive=True`) 모드 통합
- [ ] 에르메스 에이전트에 NAS 분류 및 요약 전문 **커스텀 스킬 (`aurum_nas_classifier`)** 설계 및 이식
- [ ] 파일 업로드 경로 계층 파싱 및 메타데이터 필드/옵시디언 태그 자동 추출 연동
- [ ] 텍스트(조사표/엑셀)와 사진 이미지의 선택적 임베딩 RAG 분류 처리
- [ ] 처리 성공 후 맥북 옵시디언 볼트로 요약 마크다운(.md) 노트를 동기화(rsync/scp)하는 클라이언트 자동화 스크립트 고도화
- [ ] 애매한 분류건 발생 시 메신저 API(Slack/Telegram)를 통해 사용자 피드백을 구하고 기억(Memory DB)에 학습시키는 인터페이스 구현

### 2.2 Out of Scope (제외 범위)
- NAS의 하드웨어 RAID 설정 및 SMB 네트워크 공유 자체의 보안/방화벽 설정 자동화
- RAG 외부 클라우드 상용 API(OpenAI 등) 의존적 서비스 설계 (100% 로컬 아톰 인프라로 구동)
- 다중 노드 오케스트레이션 및 완전 자동화된 LLM 미세조정(Fine-Tuning) 파이프라인

---

## 3. Requirements (요구사항)

### 3.1 Functional Requirements (기능 요구사항)

| ID | Requirement (요구사항) | Priority | Status |
|----|-------------|----------|--------|
| FR-01 | 아톰 서버가 NAS 하위 임의의 깊은 폴더 업로드를 실시간으로 전수 감지해야 함 | High | Pending |
| FR-02 | 에르메스가 파일 본문과 업로드 경로명 정보를 결합해 년도, 업체, 사업명, 분류군을 동적으로 추론해야 함 | High | Pending |
| FR-03 | 인덱싱 성공 시 1KB 미만의 경량 마크다운 요약본 노트가 생성되어 맥북으로 즉시 복사되어야 함 | High | Pending |
| FR-04 | 텍스트 파일은 FAISS에 임베딩하고, 사진 대장은 메타데이터 노트만 생성하여 선택적으로 분류 처리함 | Medium | Pending |
| FR-05 | 분류 모호성 발생 시 텔레그램/슬랙으로 질문을 전송하고, 사용자가 준 답을 세션 기억에 영구 학습해야 함 | Medium | Pending |

### 3.2 Non-Functional Requirements (비기능 요구사항)

| Category | Criteria (기준) | Measurement Method (측정 방법) |
|----------|----------|-------------------|
| Performance | 질문 시 로컬 AI RAG 답변 응답 시간 5초 이내 | 아톰 서버 vLLM/Ollama 로그 시간 측정 |
| Reliability | 네트워크 드라이브(NAS) 일시 단절 시 프로세스 멈춤 없이 5회 이상 재시도 | watchdog_pipeline.log 예외 트레이스 모니터링 |
| Storage Efficiency | 맥북 로컬 디스크 추가 용량 점유 문서당 1KB 미만 | 동기화된 obsidian_notes 폴더 내 md 파일 크기 측정 |

---

## 4. Success Criteria (성공 기준)

### 4.1 Definition of Done (완료 정의)
- [ ] 아톰 서버 Watchdog의 하위 폴더 재귀 감시(`recursive=True`) 및 동작 검증 완료
- [ ] 경로 파싱 기반 자동 태깅 스크립트 작성 및 오동작률 5% 미만 검증
- [ ] 에르메스 에이전트에 커스텀 스킬 등록 및 로컬 API(Ollama/vLLM) 호출 연동 완료
- [ ] 맥북 옵시디언 볼트로의 요약 노트 원격 전송 파이프라인 완료 및 테스트 통과
- [ ] Slack/Telegram 인터페이스 연동 및 기억 축적 확인

### 4.2 Quality Criteria (품질 기준)
- [ ] 예외 처리 및 재시도 로직이 100% 작동하여 파이프라인 중단 없음
- [ ] 동기화 스크립트 실행 후 꼬임 현상이나 중복 파일 발생 제로
- [ ] 로컬 git 저장소 트리가 오류 없이 깨끗한 상태 유지

---

## 5. Risks and Mitigation (리스크 및 완화 대책)

| Risk | Impact | Likelihood | Mitigation (완화 대책) |
|------|--------|------------|------------|
| NAS 마운트 불안정으로 감시 누수 발생 | High | Medium | watchdog에 `--observer polling` 모드를 상시 강제하고 재접속 루프 삽입 |
| 모호한 문서에 대해 AI가 잘못된 태그를 강제 분류함 | Medium | High | 1차 분류 결과 신뢰도가 낮을 경우 마음대로 분류하지 않고 사용자에게 메신저로 최종 판단을 묻도록 임계값 설정 |
| 로컬 LLM 연산 부하로 아톰 서버 다운 | Medium | Low | vLLM의 최대 동시 배치 제한 및 GPU 메모리 예비 공간 확보(OOM 방지 설정) |

---

## 6. Architecture Considerations (아키텍처 고려사항)

### 6.1 Project Level Selection (프로젝트 레벨 선정)

| Level | Characteristics | Selected |
|-------|-----------------|:--------:|
| **Starter** | 단순 구조, 단독 스크립트 위주 | - |
| **Dynamic** | 파이프라인, 로컬 에이전트, 외부 메신저 API, 벡터 DB 연동 | **Selected** |
| **Enterprise** | 대규모 클러스터 분산, 영구 지속 DB | - |

### 6.2 Key Architectural Decisions (핵심 아키텍처 결정)

| Decision | Options | Selected | Rationale |
|----------|---------|----------|-----------|
| AI 에이전트 엔진 | LangChain / Custom Python / **Hermes-Agent** | **Hermes-Agent** | SQLite 세션 DB와 FTS5 검색 기반의 강력한 기억(Memory) 관리 및 툴 오케스트레이션 기본 제공 |
| 데이터 마운트 | SMB 직접 연결 / **SSHFS 우회 터널** | **SSHFS 우회 터널** | 로컬 환경에 구애받지 않고 아톰 백엔드를 경유하여 외부에서도 안정적으로 NAS 데이터 연결 및 링크 작동 보장 |
| 알림/학습 인터페이스 | Slack / Telegram / Web UI | **Telegram & Slack** | 상시 켜져 있는 hermes-agent gateway 플랫폼을 활용하여 간편하게 인터페이스 구축 가능 |

---

## 7. Next Steps (향후 절차)

1. [ ] 상세 설계서 작성 (`hermes-nas-classifier.design.md`)
2. [ ] 에르메스 커스텀 스킬 코드베이스 설계 및 아톰 서버 런타임 검증
3. [ ] 구현 및 Check 분석 검증 단계 수립

---

## Version History (버전 이력)

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1 | 2026-06-05 | 최초 계획 수립 및 3각 아키텍처 연동 구상 등록 | Antigravity |
