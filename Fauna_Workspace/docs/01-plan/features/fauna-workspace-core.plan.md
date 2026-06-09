# fauna-workspace-core 계획서 (Planning Document)

> **요약**: 생태 조사 원시 야장 데이터 파싱, 계통 분류 보정, 위경도 공간 좌표 매핑 및 XML 한글 HWPX/Markdown 최종 보고서를 자동 제작하는 데이터 파이프라인 엔진 구축 계획.
>
> **프로젝트**: Fauna_Workspace
> **버전**: 1.0
> **작성자**: Antigravity AI
> **날짜**: 2026-05-31
> **상태**: Approved

---

## 1. 개요 (Overview)

### 1.1 목적 (Purpose)
본 프로젝트는 현지 생태 조사 야장 텍스트 파일(`1_입력_야장기록.txt`)로부터 다차수별 생물종 데이터(분류군, 발견 유형, 개체수)를 유실률 0%로 정밀 추출하고, 학술용 분류계통 데이터베이스 및 WGS84 위경도 좌표 사전과 매핑하여 구조화된 JSON 데이터(`parsed_data.json`)를 생성한 후, 최종 마크다운 및 HWPX 보고서로 자동 가공해내는 'Fauna Ecology Hybrid-Engine' 데이터 파이프라인의 구축 및 안정성을 확보하는 것을 목적으로 합니다.

### 1.2 배경 (Background)
생태 조사 분야의 원시 데이터는 수기 야장, 불완전한 학명 기입, 서로 다른 GIS 좌표계 등 비정형적이고 파편화된 특징이 강합니다. 이를 일관된 데이터베이스로 동기화하고 정량적 통계 보고서를 생성하기 위해, 신속하고 결정론적인 파싱 오케스트레이터 및 로컬 언어 모델(Swarm) 연동 지능형 엔진을 갖춘 데이터 가공 허브가 반드시 필요합니다.

### 1.3 관련 문서 (Related Documents)
- 요구사항 및 구조 분석: [Report_Structure_Analysis.md](../../Report_Structure_Analysis.md)
- 보고서 DNA 가이드: [report_dna_analysis.md](../../../report_dna_analysis.md)
- 실행 파일: [▶️_분석시작.sh](../../▶️_분석시작.sh)

---

## 2. 범위 (Scope)

### 2.1 범위 내 항목 (In Scope)
- [x] **원천 야장 파싱**: `1_입력_야장기록.txt` 로드 및 정규표현식 기반 무오류 파싱 엔진 (`swarm_orchestrator.py`) 구현.
- [x] **계통 및 보호종 대조**: `species_search_index.json` 데이터베이스 및 마스터 매핑 딕셔너리를 활용하여 목/과 분류군 치환, 법적보호종 유무 판정.
- [x] **위경도 매핑 및 공간 데이터 정제**: 멸종위기종 발견 지점에 대한 도분초(DMS) 좌표의 위경도(WGS84) 자동 십진수 보정 및 `ingested_spatial_data.geojson` 생성.
- [x] **하이브리드 의견 생성**: 로컬 AI 서버(LM Studio 포트 8007) 또는 API 호출을 통해 생태 심의위원 격식체의 종합의견을 동적으로 수렴하고, 오프라인 시 견고한 하드코딩 의견 백업 대응.
- [x] **최종 보고서 자동 제작**: `HwpxBuilder` 연동 한글 보고서 패키지 생성 및 마크다운 최종 보고서(`2_결과_최종보고서.md`) 빌드.

### 2.2 범위 외 항목 (Out of Scope)
- 외부 상용 클라우드 데이터베이스 호스팅 (본 로컬 파이프라인은 무중단 로컬 JSON 파일 트랜잭션 보장에 집중)

---

## 3. 요구사항 (Requirements)

### 3.1 기능적 요구사항 (Functional Requirements)

| ID | 요구사항 명칭 | 중요도 | 상태 |
|----|-------------|----------|--------|
| FR-01 | 원천 수필 야장 데이터 파싱 및 정제 (정규표현식 기반 유실율 0% 보장) | High | Completed |
| FR-02 | 분류계통 정보(목, 과 명칭)의 국명 자동 치환 및 법적보호종 등급 매핑 | High | Completed |
| FR-03 | DMS/도표 생태 조사 공간 좌표의 위경도 표준 변환 및 GeoJSON 공간 레이어 정제 | High | Completed |
| FR-04 | LM Studio(포트 8007) 연동 또는 마스터 DNA 분석 가이드를 동적 연동한 종합의견 생성 | Medium | Completed |
| FR-05 | 무결성 HWPX 빌더 패키징 및 마크다운 기반 최종 보고서 문서 빌드 자동화 | High | Completed |

### 3.2 비기능적 요구사항 (Non-Functional Requirements)

| 분류 | 기준 | 측정 방법 |
|----------|----------|-------------------|
| 무결성 (Integrity) | 야장 원천 데이터 파싱 시 정량 수치 유실 0% 및 데이터 누락 방지 | parsed_data.json과 야장 수동 검증 대조 |
| 성능 (Performance) | 오프라인 백업 의견 매핑 시 전체 파싱 및 가공 파이프라인 완료 시간 0.2초 이내 | 쉘 스크립트 실행 시간 `time` 측정 |
| 보안 (Security) | API Key 및 로컬 네트워크 세부 주소 노출 방지 (`.env` 관리) | 소스코드 검사 및 커밋 히스토리 확인 |

---

## 4. 성공 기준 (Success Criteria)

### 4.1 완료 정의 (Definition of DoD)
- [x] `▶️_분석시작.sh` 원터치 쉘 스크립트 실행 시 오케스트레이터 파이프라인이 즉각 오차 없이 기동함.
- [x] 파싱 결과인 `parsed_data.json`이 누락 종 없이 데이터 스키마 규칙을 준수함.
- [x] WGS84 위경도가 매핑된 공간 파일(`생태현장_정밀공간좌표_정제완료.geojson`)이 성공적으로 생성됨.
- [x] 최종 HWPX 보고서 및 `2_결과_최종보고서.md`가 report_dna 스타일에 맞게 올바르게 조립됨.

### 4.2 품질 기준 (Quality Criteria)
- [x] 파이썬 파이프라인 구동 시 런타임 에러 또는 인코딩 버그가 전혀 발생하지 않음.
- [x] LM Studio 오프라인 구동 시에도 지능형 백업 의견을 조율하여 최종 보고서 완성 보장.

---

## 5. 리스크 및 완화 방안 (Risks and Mitigation)

| 리스크 | 영향도 | 발생 가능성 | 완화 방안 |
|------|--------|------------|------------|
| 로컬 LM Studio 미구동에 따른 파이프라인 병목 | High | High | 포트 감지 및 모델 응답 제한 시간을 2초 미만으로 타이트하게 감증하고, 호출 실패 시 우아한 격식체의 백업 종합의견(하드코딩 마스터 텍스트)을 즉각 반환하여 에러 전파 차단. |
| 비정형 야장 텍스트 라인의 구조 붕해 | Medium | Medium | 유연한 정규표현식 매칭(`re.search` 및 `re.findall`) 패턴을 중첩 탑재하여 차수(Phase) 정보 및 다분류군 라인이 붕괴되어도 유실 없이 안정적 추출. |

---

## 6. 아키텍처 고려 사항 (Architecture Considerations)

### 6.1 프로젝트 레벨 선택

| 레벨 | 특징 | 선택 여부 |
|-------|-----------------|:--------:|
| **Starter** | 단일 스크립트 및 정적 텍스트 관리 | - |
| **Dynamic** | 하이브리드 자동화 파이프라인, AI 모델 연동 및 GeoJSON 지리 공간 매핑 | **Selected** |
| **Enterprise** | MSA 구조, 원격 데이터 레이크 연동 | - |

### 6.2 주요 아키텍처 결정

| 결정 사항 | 대안 목록 | 최종 선택 | 채택 근거 |
|----------|---------|----------|-----------|
| **오케스트레이션** | Airflow / Bash Shell / Python Subprocess | **Python Swarm Orchestrator** | 런타임 가벼움과 로컬 디렉토리 접근성, 정밀 정규표현식 파싱 처리의 정교성을 극대화하기 위해 Python native 오케스트레이터로 구축. |
| **자연어 처리 엔진** | OpenAI API / Local LM Studio / Hardcoding | **LM Studio + API Fallback** | 인터넷 환경 오프라인 상태에서도 100% 작동 가능한 로컬 호환성을 지원하면서 고품질 AI 보전 의견 조율을 지능적으로 달성. |

---

## 7. 향후 일정 (Next Steps)

1. [x] 기획서 최종 승인
2. [x] 파이프라인 기술 설계서 작성 (`fauna-workspace-core.design.md`)
3. [x] 설계-코드 검증 갭 분석서 작성 (`fauna-workspace-core.analysis.md`)
4. [x] 최종 완료 보고서 작성 및 등록 (`fauna-workspace-core.report.md`)
5. [x] 워크스페이스 에이전트 지침서(`AGENTS.md`)의 최종 릴리즈 및 갱신

---

## 버전 이력 (Version History)

| 버전 | 날짜 | 변경 사항 | 작성자 |
|---------|------|---------|--------|
| 1.0 | 2026-05-31 | 최초 기획서 작성 및 승인 | Antigravity AI |
