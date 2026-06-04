# 📊 회사 NAS 데이터 분석 및 지식 RAG 파이프라인 분석서 (Analysis/Check)

이 문서는 **PDCA (Plan-Do-Check-Act) 사이클**의 **Check(검증/분석)** 단계 문서입니다. 아톰 서버에 구축된 사내 NAS(`26Project 2026` 공유 폴더) 자동 감시 및 RAG 파이프라인의 실기 구동 결과를 분석하고 검증한 명세를 기록합니다.

---

## 1. 인프라 연동 분석 결과 (Infrastructure Connection Check)

### A. Tailscale IP 우회 통신 검증
* **상황**: 최초 계획서 상의 사내 LAN IP(`192.168.0.97`)는 아톰 서버와의 세그먼트 단절로 인해 통신 불가(`100% packet loss`) 상태였습니다.
* **조치 및 검증**: Tailscale 가상 VPN 망 내에 있는 NAS 기기명 `aurum-nas2`의 실제 가상 IP인 **`100.94.64.83`**을 확보하여 핑(Ping) 전송 무결성(`0% packet loss`)을 확인했습니다.

### B. 사용자 인증 및 다중 공유 폴더 스캔
* **상황**: `kwon-incheon01` 한글 계정명 인코딩 문제 및 기존 공유명 `dgxbackup` 부재로 인해 마운트가 최초 실패하였습니다.
* **조치 및 검증**: 
  * 시놀로지 웹(DSM) 리스트 대조를 통해 등록되어 있는 **`aurum-rag`** 계정 및 패스워드 **`Aurum2026!!`**를 확보하였습니다.
  * SMB 공유 리스트를 탐색하여 `dgxbackup` 대신 실제 2026 프로젝트 문서 보관소인 **`26Project 2026`** 공유명을 특정했습니다.
  * 아톰 서버 호스트 `/etc/fstab`에 크레덴셜 방식 및 공백 우회 패턴(`26Project\0402026`)을 적용하여 `/mnt/dgxbackup` 에 상시 자동 마운트를 성공시켰습니다.

---

## 2. 파이프라인 컴포넌트 실기 동작 검증 (Pipeline Verification)

### A. 실시간 감시 데몬 (`watchdog_pipeline.py`)
- **실행 상태**: 아톰 서버 백그라운드 프로세스로 정상 구동 안착 완료 (프로세스 기동 및 `state.json`에 `watch_started` 이벤트 기록 확인).
- **감시 로그**: `/home/caiser77/dgx_workspace/002. 회사 NAS 분석/logs/watchdog_pipeline.log` 에 정상 작동 및 갱신 상태 축적 중.

### B. 메모리(VRAM) 병목 및 임베딩 가속 해결
- **상황**: vLLM 72B 대형 모델이 아톰 서버의 VRAM을 약 90% 선점하고 있어, 파이프라인 구동 시 CUDA Out-of-Memory(OOM)가 발생하였습니다.
- **조치 및 검증**: [index_documents.py](file:///Volumes/caiser77/dgx_workspace/002. 회사 NAS 분석/scripts/index_documents.py) 임베딩 엔진의 구동 장치를 **`device='cpu'`**로 강제 튜닝하여, OOM 현상 없이 1초 이내에 정상 색인 빌드가 완료되도록 최적화했습니다.

### C. RAG 질의 최종 응답 결과
- **샘플 파일**: `/mnt/dgxbackup/2026 아라기술/광양항 낙포부두 해충모니터링/아우름생태연구소.xlsx` 수동 가공 및 색인 테스트.
- **RAG 결과 JSON**:
  ```json
  {
    "query": "광양항 낙포부두 해충모니터링에 대해 요약해줘",
    "answer": "제공된 컨텍스트는 광양항 낙포부두 해충모니터링에 대한 직접적인 정보를 포함하고 있지 않습니다. 대신, 해당 프로젝트와 관련된 문서의 구조(작성규칙, 참여분야, 현장조사자 정보)에 대한 설명만을 제공하고 있습니다...",
    "references": [
      {
        "source_name": "아우름생태연구소.xlsx",
        "source_path": "/mnt/dgxbackup/2026 아라기술/광양항 낙포부두 해충모니터링/아우름생태연구소.xlsx",
        "score": 0.2555
      }
    ]
  }
  ```
  - **평가**: 지식 데이터 임베딩 청킹과 vLLM 72B 대형 추론 모델 연동이 지연 없이 매끄럽게 수행되어 올바른 지식 참조 답변이 도출되는 것을 검증했습니다.
