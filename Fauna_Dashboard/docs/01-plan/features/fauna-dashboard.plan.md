# fauna-dashboard - Plan Document

> Version: 1.0.0 | Date: 2026-06-02 | Status: Approved
> Level: Dynamic

---

## 1. Overview

### 1.1 Purpose
`fauna-dashboard`는 생태 현장 조사 데이터를 수집, 정제, 시각화, 분석, 보고서화하는 통합 대시보드 기능을 관리하기 위한 PDCA 계획 단위이다. FastAPI 백엔드와 Vite+React 프론트엔드를 중심으로 야장 OCR, 생물종 데이터 편집, GIS 도면 업로드, WGS84 좌표 보정, 생태 통계 산출, CSV/HWPX 보고서 다운로드까지 하나의 검증 가능한 워크플로우로 묶는 것을 목표로 한다.

### 1.2 Background
생태 조사 업무는 수기 야장, 좌표 정제, 분류군별 표준 정렬, 공간 도면 검토, 보고서 작성이 분리되어 진행되기 쉽다. 이로 인해 데이터 누락, 좌표계 불일치, 엑셀 한글 깨짐, 보고서 패키지 손상 같은 운영 리스크가 발생한다. 본 계획은 `Fauna_Dashboard`의 핵심 기능을 PDCA 문서 체계에 맞춰 재정리하고, 설계 및 구현 검증으로 이어질 수 있는 기준을 제공한다.

## 2. Goals

### 2.1 Primary Goals
- [x] `server/database.json`을 단일 진실 공급원으로 유지하고 `/load-data`, `/save-data`를 통해 프론트엔드 편집 결과를 백엔드에 반영한다.
- [x] CAD DXF, SHP zip, KML 업로드 데이터를 GeoJSON으로 표준화하고 EPSG:5186, EPSG:5179, EPSG:5181, EPSG:3857 좌표계를 WGS84 위경도로 보정한다.
- [x] `Fauna_Workspace/생태현장_정밀공간좌표_정제완료.geojson`의 생태 좌표와 업로드 도면 레이어를 Leaflet 지도에서 융합 시각화한다.
- [x] Gemini API 기반 야장 이미지 OCR 및 로컬 MLX 8007 Swarm 연동에서 실패 시 임의 데이터 없이 사용자에게 안전한 오류 피드백을 제공한다.
- [x] 국가 생태 조사 표준 분류군 순서에 따라 CSV/HWPX 보고서를 생성하고, CSV에는 UTF-8-BOM을 주입해 엑셀 한글 호환성을 보장한다.

### 2.2 Non-Goals
- 네이티브 모바일 앱 또는 별도 데스크톱 앱을 제공하지 않는다.
- 실시간 CCTV 영상 분석, 장기 모니터링 센서 수집, 자동 종 동정 모델 학습은 이번 PDCA 범위에 포함하지 않는다.
- DART, 법제처, 외부 금융 API 등 생태 대시보드와 무관한 PlayMCP 데이터 연동은 포함하지 않는다.

## 3. Scope

### 3.1 In Scope
- FastAPI 백엔드 API, 데이터 파일 동기화, 통계 계산, OCR/Swarm 예외 처리
- React 대시보드 화면, 데이터 그리드, 지도 뷰어, 차트, 수동 입력 모달, 보고서 뷰어
- GIS 파일 업로드, 좌표계 감지, WGS84 변환, GeoJSON 병합 렌더링
- CSV 다운로드, HWPX 보고서 빌더, 분류군 표준 정렬
- `npm run build`, `npm run lint`, 백엔드/프론트엔드 로컬 구동 검증
- PDCA 후속 산출물: 설계서, 구현 검증 분석서, 완료 보고서

### 3.2 Out of Scope
- 프로덕션 클라우드 배포 자동화 및 운영 모니터링 대시보드
- 다중 사용자 인증, RBAC, 감사 로그, 조직별 권한 분리
- 신규 데이터베이스 서버 도입 또는 `database.json` 구조의 전면 교체
- 상용 GIS 서버, 외부 지도 과금 API, 실시간 스트리밍 데이터 파이프라인

## 4. Functional Requirements

| ID | Requirement | Priority | Acceptance Signal |
|----|-------------|----------|-------------------|
| FR-01 | 초기 데이터 로드 및 편집 저장 | High | `database.json`이 비어 있거나 없을 때 상위 데이터셋에서 동기화되고, 인라인 편집 후 `/save-data`로 저장된다. |
| FR-02 | 생태 데이터 표준 정렬 | High | CSV/HWPX 출력에서 포유류, 조류, 어류, 양서파충류, 저서무척추 순서가 유지된다. |
| FR-03 | GIS 업로드 및 좌표 변환 | High | DXF/SHP/KML 입력이 GeoJSON으로 변환되고 WGS84 좌표로 지도에 표시된다. |
| FR-04 | 생태 통계 산출 | High | Shannon 다양성 지수와 Pielou 균등도 지수가 분류군 데이터 기준으로 산출된다. |
| FR-05 | AI 야장 OCR | Medium | Gemini API 또는 Swarm 처리 실패 시 임의 종 데이터를 만들지 않고 오류 피드백을 표시한다. |
| FR-06 | 보고서 다운로드 | High | UTF-8-BOM CSV와 손상 없는 HWPX 패키지를 다운로드할 수 있다. |

## 5. Non-Functional Requirements

| Category | Requirement | Verification |
|----------|-------------|--------------|
| Reliability | 빈 데이터, OCR 실패, 로컬 Swarm 연결 실패를 사용자 작업 중단 없이 처리한다. | API 응답 및 프론트엔드 토스트/상태 메시지 확인 |
| Compatibility | CSV는 Excel 한글 표시를 지원하고 HWPX는 한글 표준 XML 패키지 구조를 유지한다. | 다운로드 파일 수동 열람 및 패키지 무결성 확인 |
| Performance | 일반적인 현장 조사 데이터와 지도 레이어 렌더링에서 사용자가 체감하는 지연을 최소화한다. | 로컬 브라우저 렌더링 및 네트워크 응답 확인 |
| Maintainability | React 컴포넌트, hooks, FastAPI 엔드포인트, 유틸리티 모듈의 책임을 분리한다. | 코드 리뷰 및 설계서 대비 갭 분석 |
| Build Quality | 프론트엔드 린트와 빌드가 통과해야 한다. | `npm run lint`, `npm run build` |

## 6. Success Criteria

- [ ] `npm run lint --prefix Fauna_Dashboard`가 치명적 오류 없이 완료된다.
- [ ] `npm run build --prefix Fauna_Dashboard`가 성공해 Vite 정적 리소스를 생성한다.
- [ ] FastAPI 백엔드가 포트 `8005`에서 실행되고 주요 API가 프론트엔드와 정상 통신한다.
- [ ] Vite+React 프론트엔드가 포트 `5173`에서 실행되고 데이터 그리드, 지도, 차트, 보고서 다운로드 흐름이 동작한다.
- [ ] CSV 출력의 첫 바이트에 UTF-8-BOM이 포함되고, 분류군 표준 정렬이 유지된다.
- [ ] GIS 좌표 변환 로직이 국내 생태/환경평가 도면의 주요 좌표계 범위를 WGS84로 보정한다.
- [ ] AI/OCR 또는 Swarm 실패 상황에서 `데이터를 찾을 수 없음` 또는 구체적 오류 안내가 표시되고 더미 데이터가 생성되지 않는다.
- [ ] 후속 `$pdca design fauna-dashboard` 문서가 본 계획의 요구사항을 API, 데이터 모델, UI, 테스트 계획으로 구체화할 수 있다.

## 7. Schedule

| Phase | Target Date | Status |
|-------|-------------|--------|
| Plan | 2026-06-02 | Complete |
| Design | 2026-06-02 | Pending |
| Implementation | 2026-06-03 | Pending |
| Check | 2026-06-03 | Pending |
| Act | 2026-06-04 | Pending |
| Report | 2026-06-04 | Pending |

## 8. Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| 좌표계 자동 판별 실패 | High | Medium | EPSG별 대표 좌표 범위 판별 로직을 설계서에 명시하고 변환 결과를 지도 렌더링으로 검증한다. |
| OCR 또는 Swarm 응답 불안정 | Medium | Medium | 실패 응답을 캡슐화하고 임의 데이터 생성을 금지하며 사용자에게 명확한 오류 상태를 제공한다. |
| CSV/HWPX 보고서 호환성 문제 | High | Medium | BOM 주입, 분류군 정렬, HWPX 패키지 구조를 성공 기준과 테스트 항목에 포함한다. |
| `database.json`과 상위 원시 데이터 불일치 | High | Low | 백엔드 초기화 및 `/load-data` 동기화 규칙을 단일 진실 공급원 원칙으로 고정한다. |
| 기존 `fauna-dashboard-core` 문서와 범위 중복 | Low | High | 본 문서는 전체 feature명 기준의 신규 PDCA 흐름으로 사용하고, 기존 문서는 참조 문서로 연결한다. |

## 9. Architecture Considerations

- Project level: Dynamic
- Frontend: Vite, React, React Leaflet, Recharts, lucide-react
- Backend: FastAPI, local JSON persistence, GIS conversion utilities, report builders
- Data source of truth: `Fauna_Dashboard/server/database.json`
- External/local integrations: Gemini API, MLX 8007 Swarm orchestrator, `Fauna_Workspace` parsed and refined geospatial datasets
- Verification flow: local backend run, local frontend run, lint, build, API smoke checks, browser inspection

## 10. Convention Prerequisites

- 하위 프로젝트 지침 `Fauna_Dashboard/AGENTS.md`를 최우선으로 적용한다.
- 기존 주석과 독스트링의 의미를 변경하지 않는다.
- 테스트 또는 디버깅용 임시 파일과 `.log` 파일은 작업 종료 전 삭제한다.
- 실제 콘텐츠를 제공할 수 없는 경우 더미 값이나 placeholder를 만들지 않는다.
- 법률/금융 등 무관한 외부 데이터 조회 결과가 없을 때는 자동 추정하지 않는다.

## 11. References

- `Fauna_Dashboard/AGENTS.md`
- `Fauna_Dashboard/DESIGN.md`
- `Fauna_Dashboard/docs/01-plan/features/fauna-dashboard-core.plan.md`
- `Fauna_Dashboard/docs/02-design/features/fauna-dashboard-core.design.md`
- `Fauna_Dashboard/docs/03-analysis/fauna-dashboard-core.analysis.md`
- `Fauna_Dashboard/docs/04-report/features/fauna-dashboard-core.report.md`
