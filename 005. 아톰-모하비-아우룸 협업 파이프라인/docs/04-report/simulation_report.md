# 📊 아톰-모하비-아우룸 3단 협업 파이프라인 시뮬레이션 결과 및 최종 배포 가이드

본 보고서는 아톰 서버와 모하비 맥북 간의 **1차 핸드오프(Hand-off) 시뮬레이션 성공** 결과와 이에 따른 3단계 아우룸(Aurum) 최종 배포망 연계 설계 의견을 정리한 결과서입니다.

---

## 🏁 1. 시뮬레이션 수행 결과 요약 및 기술 검증

### A. 수행 결과 및 데이터 흐름
* **감시 및 감지:** 감시 디렉토리(`01_raw_analyzed`) 내의 `TEST-REPORT-001.summary.md`의 완료 상태(`status: completed`)를 정확히 감지했습니다.
* **초안 생성 (Dump):** JSON의 기상/생태 관측 원본 데이터를 마크다운 포맷의 기술 초안(`TEST-REPORT-001.draft.md`)으로 자동 가공했습니다.
* **물리 격리 이동:** 생성된 초안 파일과 원본 요약/JSON 데이터를 물리적 디렉토리인 `02_drafting` 폴더로 손실 없이 이동(shutil.move) 처리함으로써 데이터 충돌을 원천 차단했습니다.

### B. 기술적 성과
1. **NFCGuard의 한글/특수문자 경로 완전성 보장:** macOS(NFD)의 자모분리 특성과 폴더명 내 특수 문자(`■`)가 혼합된 복잡한 경로에서도 경로 이탈이나 파싱 오류 없이 정상 작동했습니다.
2. **동기화 지연 극복 (Retry):** summary 파일 탐색 후 json 파일이 완전히 쓰일 때까지의 레이스 컨디션을 방지하는 예외 처리가 검증되었습니다.

---

## 🦅 2. 3단계 아우룸(Aurum) 배포망 연계 가이드 (Next Step)

1차 요약 데이터가 `02_drafting` 스테이지로 안전하게 연착륙함에 따라, 최종 단계인 **아우룸(Aurum) 배포 에이전트**로 바통을 넘기기 위한 연계 아키텍처를 제시합니다.

```mermaid
flowchart TD
    subgraph 2단계: 모하비 (macOS)
        A[02_drafting 폴더] -->|RAG 보완 및 편집| B(문서 수정 완료)
        B -->|status 변경: review_pending| C[03_review_pending 폴더로 이동]
    end

    subgraph 3단계: 아우룸 (Windows / Server)
        C -->|Rsync / SSHFS 동기화 감지| D{아우룸 배포 감시 데몬}
        D -->|검수 확인 통지| E[텔레그램 메신저 전송]
        E -->|검수 승인| F[HWP / PDF 최종 변환]
        F -->|NAS 배포 및 아카이빙| G[04_published 폴더 이동]
    end
```

### 💡 개선 실행 방향 1. 모하비 ➡️ 아우룸 전환 (Review Pending) 핸들러 구현
모하비 맥북의 RAG 검색 및 연구원 수동 보완 작업이 끝나면, 파일을 `03_review_pending` 스테이지로 이동시키고 `assigned_agent`를 `Aurum`으로 변경하는 쉘/파이썬 트리거를 준비합니다.
* **동작 시나리오:**
  1. 연구원이 Obsidian 상에서 초안 작성을 끝내고 Frontmatter를 `status: review_pending` 및 `assigned_agent: Aurum`으로 수정합니다.
  2. 모하비 측 백그라운드 스케줄러가 이를 감지하여 해당 파일 세트를 `03_review_pending` 폴더로 이동시킵니다.
  3. Rsync/Git 동기화를 통해 아우룸(배포 서버) 측 `03_review_pending` 폴더로 파일이 전송됩니다.

### 💡 개선 실행 방향 2. 아우룸(Aurum) 텔레그램 통지 및 자동 배포 연동
아우룸 에이전트 측에 폴더 감시 프로그램(`watchdog` 기반)을 구축하여 `03_review_pending`에 문서가 감지되는 즉시 메신저 통지 및 포맷 변환을 진행합니다.
* **텔레그램 알림 주입 예시:**
  > **🔔 [에르메스 배포 알림] 검수 대기 보고서 감지**
  > * **작업 ID:** `TEST-REPORT-001`
  > * **프로젝트:** `경인사업 (양서파충류)`
  > * **요청 상태:** 최종 정밀 검수 대기 (`status: review_pending`)
  > * [검수 및 PDF 배포 승인하려면 아래 버튼 클릭 혹은 커맨드 전송]
* **HWP/PDF 자동 배포 엔진 연계:**
  * 아우룸 봇이 검수 완료 신호(`status: reviewed` 혹은 수동 텔레그램 명령어 `/deploy`)를 수신하는 즉시, 사내 Windows API(한글 OLE Automation/Pandoc-Weasyprint 등)를 트리거하여 정식 규격 한글문서(.hwp) 및 PDF를 생성하고 사내 NAS 배포 폴더로 자동 복사합니다.
  * 최종 완료 시 파일들은 `04_published` 단계로 영구 아카이빙됩니다.

### 💡 개선 실행 방향 3. 상시 가동 데몬(Daemon)화 작업
* 파이프라인 엔진을 상시 가동 시스템 서비스로 등록하여 무중단 기동을 확보합니다.
* **Linux (systemd) 예시:** `/etc/systemd/system/pipeline-engine.service` 파일 등록 및 활성화.
* **macOS (launchd) 예시:** `~/Library/LaunchAgents/com.hermes.pipeline.plist` 파일 등록 및 활성화.

---

## 🛠️ 즉시 실행 계획
현재 구축된 [pipeline_engine.py](file:///home/caiser77/dgx_workspace/005.%20%EC%95%84%ED%86%B0-%EB%AA%A8%ED%95%98%EB%B9%84-%EC%95%84%EC%9A%B0%EB%A3%B8%20%ED%98%91%EC%97%85%20%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8/scripts/pipeline_engine.py)에 이어서, **아우룸 에이전트와의 동기화 및 텔레그램 브릿지 알림을 트리거하기 위한 뼈대 연동 함수** 작성을 바로 시작할 수 있습니다. 

아우룸 텔레그램 연동 및 launchd/systemd 백그라운드 서비스 등록 중 어떤 작업을 우선하여 구체화할까요? 의견을 부탁드립니다.
