# fauna-dashboard-core 계획서 (Planning Document)

> **요약**: 야장 기록 텍스트 스캔, 종 다양성 지수 분석, GIS 데이터 연동 및 WGS84 좌표계 정밀 보정, 그리고 HWPX/CSV 최종 보고서 자동 추출을 포함하는 통합 생태계 데이터 대시보드 구축 계획.
>
> **프로젝트**: Fauna_Dashboard
> **버전**: 1.0
> **작성자**: Antigravity AI
> **날짜**: 2026-05-31
> **상태**: Approved

---

## 1. 개요 (Overview)

### 1.1 목적 (Purpose)
본 프로젝트는 광명하안2 공공주택지구 등 개발 사업지구 일대의 환경영향평가 과정에서 발견되는 다양한 야생생물(맹꽁이, 금개구리, 수달 등)의 현지 조사 야장 기록을 디지털화하고, 종 다양성 분석 통계를 자동 계산하며, 공간 GIS 도면 데이터와 실시간으로 융합 시각화하여, 최종적으로 고품질의 HWPX 한글 보고서 및 CSV 데이터로 자동 변환 및 추출할 수 있는 프리미엄 생태 데이터 대시보드 솔루션을 구축하는 것을 목적으로 합니다.

### 1.2 배경 (Background)
법정보호종 및 다양한 야생생물의 분포는 개발 사업의 승인 및 보전 대책 수립에 핵심적인 정보입니다. 기존의 생태계 조사는 수작업 기록(야장), 개별 GPS 좌표 정제, 수동 다양성 계산, 아래아한글(HWP) 형식 보고서의 수작업 편집 등으로 인해 병목 현상과 오류 발생 가능성이 높았습니다. 본 대시보드는 로컬 MLX 8007 엔진 및 Gemini API, GIS 정밀 투영 보정 파이프라인을 융합하여 이를 고도화된 자동화 파이프라인으로 해결하고자 합니다.

### 1.3 관련 문서 (Related Documents)
- 요구사항 정의: [생태계 데이터 대시보드 구축.md](../../docs/생태계 데이터 대시보드 구축.md)
- 설계 참조: [DESIGN.md](../../DESIGN.md)
- 환경영향평가 참조: [eia_report_reference.md](../../docs/eia_report_reference.md)

---

## 2. 범위 (Scope)

### 2.1 범위 내 항목 (In Scope)
- [x] **백엔드(FastAPI)**: 포트 `8005` 가동, `database.json`과의 유기적 동기화, Shannon 다양성 지수 및 Pielou 균등도 지수 계산 엔진 탑재.
- [x] **프론트엔드(React + Vite)**: Berkeley Mono 기반 Stark Dark Monospace 테마 적용, 실시간 데이터 그리드 관리.
- [x] **공간 데이터 파이프라인**: DXF(CAD), SHP zip, KML 도면의 GeoJSON 표준화 및 5186/5179/5181/3857 투영 좌표계의 WGS84 위경도 정밀 좌표 자동 변환 및 생태 공간 좌표(refined geojson) 실시간 병합 시각화.
- [x] **보고서 추출 파이프라인**: 엑셀 호환 UTF-8-BOM CSV 분류군 정렬 추출 및 HWPX 한글 보고서 빌더 연동.
- [x] **AI 스캔 및 해독**: Gemini API를 이용한 수필 야장 이미지 텍스트 해독 및 개체 정보 정밀 추출.

### 2.2 범위 외 항목 (Out of Scope)
- 모바일 전용 앱 배포 (본 대시보드는 모바일 친화형 반응형 웹으로만 제공)
- 실시간 야생동물 CCTV 영상 스트리밍 분석 (차후 단계 고려)

---

## 3. 요구사항 (Requirements)

### 3.1 기능적 요구사항 (Functional Requirements)

| ID | 요구사항 명칭 | 중요도 | 상태 |
|----|-------------|----------|--------|
| FR-01 | 야장 이미지 및 텍스트 데이터 로드/AI 해독 (Gemini 연동) | High | Completed |
| FR-02 | 분류군별 데이터 정렬 (포유류, 조류, 어류, 양서파충류, 저서무척추 순) 및 DB 동기화 | High | Completed |
| FR-03 | GIS 레이어(DXF, SHP, KML) 업로드, WGS84 좌표 변환 및 생태 공간 좌표 융합 맵 시각화 | High | Completed |
| FR-04 | 분류군별 종 다양성 지수(Shannon Index H', Pielou Evenness J') 자동 산출 | High | Completed |
| FR-05 | 엑셀 포맷 호환 CSV 다운로드 및 HwpxBuilder 연동 HWPX 한글 보고서 패키지 다운로드 | High | Completed |

### 3.2 비기능적 요구사항 (Non-Functional Requirements)

| 분류 | 기준 | 측정 방법 |
|----------|----------|-------------------|
| 디자인 (Aesthetics) | Berkeley Mono 타이포그래피 기반 Stark Dark Monospace 테마 (`#201d1d` 배경, `#fdfcfc` 폰트, Glassmorphism, 유려한 호버 애니메이션) | 브라우저 렌더링 확인 |
| 성능 (Performance) | 대용량 생태 GIS 피처 병합 시 렌더링 지연 시간 1초 미만 | 브라우저 Lighthouse / Performance 패널 측정 |
| 호환성 (Compatibility) | 엑셀에서 바로 열어도 한글이 깨지지 않는 UTF-8-BOM CSV 제공 및 국가 표준 HWPX 문서 규격 준수 | MS Excel 및 한컴오피스 한글 뷰어 호환성 검증 |

---

## 4. 성공 기준 (Success Criteria)

### 4.1 완료 정의 (Definition of Done)
- [x] 백엔드(FastAPI) 및 프론트엔드(Vite+React)의 모든 기능 요건 완벽 구현 및 동작.
- [x] Stark Dark Monospace UI/UX가 설계 명세서(DESIGN.md)와 100% 부합.
- [x] GIS 도면 파싱 및 WGS84 자동 좌표계 변환 성공.
- [x] 한글 HWPX 보고서 파일이 빌드 및 다운로드 시 손상 없이 정상 다운로드됨.

### 4.2 품질 기준 (Quality Criteria)
- [x] 콘솔 에러가 없으며, 린트(eslint) 체크 시 치명적 오류 없음.
- [x] 백엔드 포트 `8005` 및 프론트엔드 포트 `5173` 동시 구동 시 원활한 API 데이터 바인딩 확인.

---

## 5. 리스크 및 완화 방안 (Risks and Mitigation)

| 리스크 | 영향도 | 발생 가능성 | 완화 방안 |
|------|--------|------------|------------|
| 도면 파일 투영 좌표계 식별 실패 | High | Medium | 국내 생태/환경 영향 평가 도면에서 사용되는 전형적인 4대 좌표계(5186, 5179, 5181, 3857) 범위를 수치적으로 자동 판별하여 스마트 WGS84 위경도 변환을 백엔드에서 수행하도록 보정 로직 구현. |
| CSV 추출 시 엑셀 한글 깨짐 | Medium | High | CSV 파일 내보내기 시 UTF-8 바이트스트림의 맨 앞에 `\xef\xbb\xbf` (BOM) 헤더를 주입하여 엑셀에서 즉각적인 유니코드 한글 매핑을 보장함. |

---

## 6. 아키텍처 고려 사항 (Architecture Considerations)

### 6.1 프로젝트 레벨 선택

| 레벨 | 특징 | 선택 여부 |
|-------|-----------------|:--------:|
| **Starter** | 단일 정적 페이지 중심 구조 | - |
| **Dynamic** | FastAPI 백엔드 + React SPA 구조, AI API 연동 및 정밀 데이터 파이프라인 가동 | **Selected** |
| **Enterprise** | MSA 구조, 분산 오케스트레이션 | - |

### 6.2 주요 아키텍처 결정

| 결정 사항 | 대안 목록 | 최종 선택 | 채택 근거 |
|----------|---------|----------|-----------|
| **프레임워크** | React / Next.js / Streamlit | **React + Vite / FastAPI** | 대화형 GIS 지도 매핑 및 실시간 통계 계산에 반응성이 뛰어난 React SPA와 고성능 비동기 API 처리에 유리한 FastAPI 백엔드 조합 채택. |
| **지도 시각화** | Leaflet / OpenLayers / Google Maps | **Leaflet** | 경량화되고 모바일 반응성에 적합하며 GeoJSON 통합 및 GIS 레이어 중첩 커스터마이징이 간편한 오픈소스 Leaflet 라이브러리 사용. |
| **스타일링** | TailwindCSS / Vanilla CSS | **Vanilla CSS + Stark Theme** | DESIGN.md의 Stark Dark Monospace 감성을 고급스럽게 표출하기 위해 정교하게 맞춤 정의된 CSS 스타일링 적용. |

---

## 7. 향후 일정 (Next Steps)

1. [x] 기획서 최종 승인
2. [x] 기술 설계서 작성 및 검증 (`fauna-dashboard-core.design.md`)
3. [x] 코드-설계 일치도 분석(Gap Analysis, `fauna-dashboard-core.analysis.md`)
4. [x] 최종 완료 보고서 작성 (`fauna-dashboard-core.report.md`)
5. [x] 에이전트 지침서(`AGENTS.md`)의 최종 릴리즈 및 갱신

---

## 버전 이력 (Version History)

| 버전 | 날짜 | 변경 사항 | 작성자 |
|---------|------|---------|--------|
| 1.0 | 2026-05-31 | 최초 기획안 작성 및 승인 | Antigravity AI |
