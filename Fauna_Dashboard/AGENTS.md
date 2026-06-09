# 📊 서브 프로젝트 지침 - Fauna_Dashboard

이 파일은 `Fauna_Dashboard` 서비스 개발 및 검증 시 AI 에이전트와 개발자가 준수해야 할 아키텍처 규칙, 빌드/실행 명령, 데이터 처리 규격 및 PDCA 마일스톤을 명시한 개발 지침서입니다. 본 서브 프로젝트 내 작업을 수행할 때는 이 가이드를 최우선으로 준수하십시오.

---

## 🛠️ 빌드, 테스트 및 실행 명령

### 1. 서비스 가동 명령
* **FastAPI 백엔드 시작 (포트 8005):**
  ```bash
  ./venv/bin/python Fauna_Dashboard/server/main.py
  ```
* **Vite+React 프론트엔드 시작 (포트 5173):**
  ```bash
  npm run dev --prefix Fauna_Dashboard -- --port 5173 --host 0.0.0.0
  ```

### 2. 프로덕션 빌드 및 린트 검증
* **Vite 정적 리소스 빌드:**
  ```bash
  npm run build --prefix Fauna_Dashboard
  ```
* **린트(ESLint) 구동:**
  ```bash
  npm run lint --prefix Fauna_Dashboard
  ```

---

## 📐 대시보드 고유 아키텍처 및 데이터 처리 규칙

### 1. 데이터 베이스 및 동기화 원칙 (Single Source of Truth)
* 모든 생태 조사 원시 데이터는 `Fauna_Dashboard/server/database.json` 파일에 저장 및 관리됩니다.
* 백엔드 기동 또는 `/load-data` 호출 시, `database.json` 파일이 없거나 비어 있다면 상위 디렉토리 `Fauna_Workspace/parsed_data.json`으로부터 데이터셋을 읽어와 영구 동기화합니다.
* 프론트엔드 테이블 상의 인라인 데이터 편집 내용은 `/save-data` 엔드포인트를 거쳐 즉각 백엔드의 `database.json`에 반영되어야 합니다.

### 2. 공간 GIS 데이터 정밀 변환 및 융합 파이프라인
* **투영좌표계 감지 및 WGS84 위경도 변환**: 사용자가 CAD(.dxf), SHP(.zip), KML(.kml) 도면 파일을 업로드할 때, 한국 생태/환경평가 도면의 4대 표준 투영 좌표계(EPSG:5186, EPSG:5179, EPSG:5181, EPSG:3857) 범위를 백엔드(`server/main.py` 내 `convert_to_wgs84`)에서 수치 판별하여 WGS84 위경도 표준 좌표로 자동 보정 매핑해야 합니다.
* **실시간 공간 융합**: 도면 경계 피처와 `Fauna_Workspace/생태현장_정밀공간좌표_정제완료.geojson`에 기재된 실시간 생태 공간 좌표 피처들을 동적으로 머지하여 Leaflet 지도상에 중첩 렌더링합니다.

### 3. 다운로드 및 보고서 빌딩 규격
* **BOM 주입 CSV**: 엑셀(Excel)에서 한글이 깨지지 않도록, CSV 인코딩 추출 시 바이트스트림의 접두어에 반드시 UTF-8-BOM 헤더인 `\xef\xbb\xbf`를 주입하여 출력하십시오.
* **분류군 표준 정렬**: CSV 및 HWPX 보고서 내 생물종 표기 순서는 반드시 국가 생태 조사 표준 순서인 **[포유류 -> 조류 -> 어류 -> 양서파충류 -> 저서무척추]** 순으로 엄격하게 정렬하십시오.
* **HWPX 보고서 패키지**: `HwpxBuilder` 연동 시 한글 표준 XML 스키마 규격이 완전히 유지되도록 보장하고, 다운로드 스트림 생성 시 손상되지 않아야 합니다.

### 4. AI 야장 OCR 및 Swarm 연동
* Gemini API(`gemini-2.5-flash`)를 활용한 수필 야장 이미지 텍스트 해독 및 로컬 MLX 8007 Swarm 오케스트레이터 프로세스 연동 시, 로컬 API 통신 거부 등의 예외 상황을 고려하여 안전한 에러 토스트 피드백과 로그를 지원해야 합니다.

---

## 📊 PDCA 마일스톤 문서화 체계

본 하위 프로젝트는 검증 중심의 PDCA(Plan-Do-Check-Act) 라이프사이클에 맞추어 설계 및 개발을 관리합니다. 작업 변경 시 아래의 한글 마일스톤 문서를 순서대로 업데이트하십시오.

```
Fauna_Dashboard/docs/
├── 01-plan/
│   └── features/
│       └── fauna-dashboard-core.plan.md        # 생태 대시보드 구축 요구사항 및 성공 기준
├── 02-design/
│   └── features/
│       └── fauna-dashboard-core.design.md      # 아키텍처, API 스펙, 데이터 모델, UI 컴포넌트 설계
├── 03-analysis/
│   └── fauna-dashboard-core.analysis.md        # 설계 대비 구현 갭 분석서 (Match Rate 100% 검증)
└── 04-report/
    └── features/
        └── fauna-dashboard-core.report.md      # 통합 기능 검증 및 Lessons Learned 보고서
```

---

## 📋 서브 프로젝트 전용 제약조건 (우선 준수)

1. **임시 산출물 청소 규칙 (우선 순위 1)**: 
   * 디버깅용으로 생성한 임시 파이썬 스크립트, 테스트용 `.txt`, 그리고 `.log` 확장자 로그 파일들은 작업 세션 종료 또는 최종 커밋 이전에 반드시 `Fauna_Dashboard/scratch/` 및 루트 경로에서 영구 소거하여 깨끗한 작업 공간을 유지해야 합니다.
2. **Brotli 압축 해제 실패 시 우회**:
   * 로컬 연동 및 API Gateway 호출 중 Brotli 압축 관련 오류(`TypeError: terminated`)가 감지되면, Node 환경의 압축 해제를 비활성화하거나 Python 런타임을 우선 실행하여 이를 강제 우회하십시오.
3. **데이터 환각(Hallucination) 금지 및 예외 캡슐화**:
   * AI 해독 및 스캔 엔진이 이미지나 입력 텍스트로부터 유효한 종 데이터를 식별하지 못할 시, 임의의 더미 값을 추정하여 출력하지 말고 반드시 정확하게 `데이터를 찾을 수 없음` 안내를 제공하십시오.
