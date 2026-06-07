# hermes-nas-classifier Design Document

> **Summary**: 아톰 서버의 Hermes 에이전트를 활용하여 NAS 다계층 하위 폴더의 문서를 지능적으로 자동 분류/요약하고, 사용자 메신저 피드백을 통해 분류 성능을 자가 학습하는 RAG 시스템 상세 설계서
>
> **Project**: 004. 에르메스 NAS 분류기
> **Version**: 0.1
> **Author**: Antigravity
> **Date**: 2026-06-05
> **Status**: Draft
> **Planning Doc**: [hermes-nas-classifier.plan.md](../01-plan/features/hermes-nas-classifier.plan.md)

---

## 1. Overview (개요)

### 1.1 Design Goals (설계 목표)
* 아톰 서버에서 영구 구동되는 Watchdog과 Hermes 에이전트 간의 프로세스 파이프라인 수립
* 단순 Regex 글자 매칭이 아닌, 로컬 LLM(vLLM/Ollama)의 인지 추론 능력을 결합한 맥락 기반 지능형 태깅 구현
* 모호한 문서 판정 시 사용자 메신저(Telegram/Slack) 피드백 루프를 결합하고, 수집된 피드백을 에이전트의 SQLite 장기 기억에 축적하여 분류 규칙을 자가 학습(고도화)

### 1.2 Design Principles (설계 원칙)
* **네트워크 독립성**: 모든 LLM 추론 및 RAG 연산은 아톰 서버 내부의 Blackwell GPU 가속 환경에서 단독 처리한다.
* **원본 보존 법칙**: 임베딩 파이프라인의 입출력 및 RAG 부산물은 아톰 서버 로컬 하드웨어(NVMe) 영역에 격리하여 보존하고, NAS 원본 데이터 계층은 훼손하지 않는다.
* **Human-in-the-loop**: 자가 학습의 핵심 기준이 되는 피드백 루프는 비동기 대화 방식으로 사용자에게 과도한 모니터링 부담을 주지 않는다.

---

## 2. Architecture (아키텍처)

### 2.1 Component Diagram (구성도)

```text
 [ NAS 드라이브 (/mnt/dgxbackup) ]
        │
        ▼ (1) 실시간 폴더 감시 (recursive=True)
 [ Watchdog Pipeline (아톰 백엔드) ]
        │
        ▼ (2) 1차 텍스트 추출 & 요약 의뢰 (subprocess)
 [ Hermes 에이전트 (Ollama/vLLM) ] ──(4) 모호성 발생 시 ──▶ [ Telegram / Slack ]
        │                                                          │
        ▼ (3) RAG 벡터 색인 및 요약본 md 생성                       ▼ (5) 사용자 피드백 승인
 [ FAISS Vector DB / obsidian_notes/ ] ◀──(6) 학습 반영 ─── [ Session Memory DB (FTS5) ]
```

### 2.2 Data Flow (데이터 흐름)
1. **감지**: NAS 하위 임의의 경로(예: `2026 LH/일부사업/양서파충류/조사표.pdf`)에 파일 업로드 감지
2. **추출**: watchdog이 `extract_data.py`를 실행하여 텍스트 및 기본 메타데이터 추출
3. **분류/추론**: watchdog이 Hermes 에이전트 쉘(`hermes chat --skills aurum_nas_classifier`)을 실행하여 텍스트 본문과 폴더 경로 맥락을 기반으로 최종 분류 태그 판정
4. **연동**: 추출된 최종 요약본 마크다운 파일을 `data/processed/obsidian_notes/`에 저장
5. **동기화**: 맥북의 `pull_obsidian_notes.sh` 호출 시 로컬 옵시디언 볼트로 요약본 수집

---

## 3. Data Model (데이터 모델)

### 3.1 Hermes 장기 기억 스키마 (SQLite Session Memory)
에르메스가 사용자 피드백을 축적하고 지시 사항을 학습하는 로컬 SQLite Session DB 테이블 구조입니다. (hermes-agent 기본 SQLite FTS5 규격에 매핑)

```sql
-- 에르메스 메모리 테이블 정의 (자가 학습 데이터)
CREATE TABLE IF NOT EXISTS aurum_nas_rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_name TEXT NOT NULL,         -- 원본 파일명
    original_path TEXT NOT NULL,       -- 업로드되었던 NAS 경로
    inferred_class TEXT,               -- AI가 1차 판단했던 분류군
    user_approved_class TEXT,          -- 사용자가 승인/교정한 분류군
    user_instruction TEXT,             -- 사용자가 지시한 예외 학습 규칙
    feedback_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 검색 성능 향상을 위한 FTS5 가상 테이블 연동
CREATE VIRTUAL TABLE IF NOT EXISTS aurum_nas_rules_fts USING fts5(
    user_instruction,
    original_path,
    content='aurum_nas_rules'
);
```

---

## 4. API Specification & Interface (인터페이스 명세)

### 4.1 Hermes Custom Skill (`aurum_nas_classifier`) 정의
* **역할 (System Prompt)**:
  ```text
  당신은 아우룸생태연구소의 NAS 전문 문서 분류 및 인덱싱 에이전트입니다.
  입력된 문서의 본문 내용과 파일이 위치한 폴더 경로를 분석하여 아래의 JSON 구조로만 반환하십시오.
  모호한 정보나 모순점이 있으면 'is_ambiguous': true 로 표시하고 사용자에게 보낼 질문(question)을 작성하십시오.
  ```
* **Input JSON (에이전트 인풋)**:
  ```json
  {
    "file_path": "/mnt/dgxbackup/2026 LH/경인사업/양서파충류/field_report.pdf",
    "extracted_text": "본 보고서는 경인 지역의 맹꽁이 보호 조치에 관한..."
  }
  ```
* **Output JSON (에이전트 아웃풋)**:
  ```json
  {
    "year_vendor": "2026 LH",
    "project_name": "경인사업",
    "class_name": "양서파충류",
    "tags": ["#2026LH", "#경인사업", "#양서파충류", "#맹꽁이"],
    "summary": "경인 지역 맹꽁이 보호 조치 최종 현장 보고서.",
    "is_ambiguous": false,
    "question": ""
  }
  ```

### 4.2 Telegram 피드백 루프 웹훅 규격
에르메스가 분류의 모호함을 판정했을 때 텔레그램 봇으로 사용자에게 인라인 승인 버튼을 보내는 API 페이로드 규격입니다.

```json
{
  "chat_id": "@aurum_ai_admin",
  "text": "⚠️ [분류 모호성 감지] 현장조사표.pdf의 분류를 확인해 주세요.\n* AI 판정: #양서파충류\n* 파일 경로: .../양서파충류/현장조사표.pdf\n* 본문 분석: 조류 흔적 발견",
  "reply_markup": {
    "inline_keyboard": [
      [
        {"text": "✅ 양서파충류로 승인", "callback_data": "approve_class:양서파충류:id_123"},
        {"text": "🦅 조류로 교정", "callback_data": "approve_class:조류:id_123"}
      ],
      [
        {"text": "✍️ 예외 지시어 작성", "callback_data": "user_instruction:id_123"}
      ]
    ]
  }
}
```

---

## 5. Test Plan (검증 및 테스트 계획)

| 검증 단계 | 검증 대상 | 검증 방법 | 성공 조건 |
|------|--------|------|------|
| **단위 검증** | 폴더 경로 파싱 및 태그 추출 로직 | 테스트 파일(PDF) NAS 업로드 | 생성된 metadata.json에 태그가 4개 이상 포함되는지 확인 |
| **연동 검증** | 에르메스 스킬 API 호출 및 추론 | `hermes chat --skills` 실행 테스트 | 반환된 JSON에 올바른 `class_name`이 채워지는지 확인 |
| **통합 검증** | 텔레그램 메시지 송수신 및 SQLite 기억 저장 | 임의 모호성 트리거 발생 | 텔레그램 인라인 승인 시 `aurum_nas_rules` 테이블에 데이터가 인서트되는지 확인 |

---

## 6. Implementation Guide (구현 가이드)

### 6.1 단계별 구현 순서
1. [ ] 아톰 서버에 SQLite RAG 규칙 및 메모리 피드백용 SQLite 테이블 생성 스크립트 작성
2. [ ] 에르메스(`hermes-agent/skills/`) 하위에 `aurum_nas_classifier` 스킬 명세서 및 프롬프트 탑재
3. [ ] `watchdog_pipeline.py`의 파일 감지 콜백 단에서 에르메스 스킬을 호출하고 결과를 처리하는 연동 코드 추가
4. [ ] 텔레그램 API 브리지 연동 및 콜백 처리 로직 완성
5. [ ] 맥북 `pull_obsidian_notes.sh` 및 사용설명서 최종 수정 후 프로덕션 실행 검증

---

## Version History (버전 이력)

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1 | 2026-06-05 | 아톰 서버 전용 에르메스 NAS 분류기 아키텍처 상세 설계서 수립 | Antigravity |
