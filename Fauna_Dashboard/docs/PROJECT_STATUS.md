# 🧬 Fauna Dashboard Project Status
**Last Updated: 2026-05-12**

## 1. 프로젝트 개요
사용자의 생태계 조사 데이터를 국가생물종목록(4.3만 종)과 연동하여 전문적인 통계 지수($H', J'$ 등)를 분석하고 시각화하는 통합 대시보드 시스템.

## 2. 통합 디렉토리 구조 (Unified Structure)
모든 파일은 `/Users/nams/AI_BASE/fauna-dashboard/` 하위에 위치함.
- `streamlit_app.py`: 메인 대시보드 및 분석 엔진 (파스텔톤/라이트모드/폰트축소 적용)
- `/data`: 
    - `2025년 국가생물종목록_v1.0.xlsx`: 원본 마스터 데이터
    - `species_search_index.json`: AI 및 시스템용 고속 검색 인덱스
- `/scripts`: 
    - `preprocess.py`: 엑셀 데이터 통합 가공 및 인덱싱 스크립트
- `/docs`: 
    - `생태계 데이터 대시보드 구축.md`: 시스템 설계 원칙 및 분석 로직 문서

## 3. 핵심 기능 구현 현황
- [x] **마스터 데이터 통합**: 엑셀의 모든 분류군 시트(포유류~고세균)를 하나로 인덱싱 완료.
- [x] **누락 방지 기록**: 종명 입력 시 마스터 DB 자동 매핑 및 분류 체계 자동 완성.
- [x] **전문 생태 분석**: Shannon($H'$), Pielou($J'$) 등 5대 지수 실시간 계산 엔진 탑재.
- [x] **비교 분석**: 문헌조사 vs 현지조사 데이터 간의 교집합/차집합 분석 기능.
- [x] **벌크 업로드**: 엑셀/CSV 파일을 통한 대량 데이터 일괄 등록 기능.

## 4. 실행 및 관리
- **대시보드 실행**: `streamlit run /Users/nams/AI_BASE/fauna-dashboard/streamlit_app.py`
- **데이터 가공**: `python3 /Users/nams/AI_BASE/fauna-dashboard/scripts/preprocess.py`

## 5. 향후 과제
- Open WebUI 연동을 통한 AI 기반 조사 야장(이미지) 분석 기능 복구.
- 현장 사진 업로드 및 종 판별 AI 연동 강화.
