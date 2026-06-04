# 🏁 회사 NAS 데이터 분석 및 지식 RAG 파이프라인 보고서 (Report/Act)

이 문서는 **PDCA (Plan-Do-Check-Act) 사이클**의 **Act(개선/보고)** 단계 문서입니다. 아우룸생태연구소의 사내 고성능 AI 서버(아톰)와 회사 NAS 간 RAG 지식 파이프라인의 완성도 및 최종 보완 결과와 향후 운영 지침을 보고합니다.

---

## 1. PDCA 완료 요약 및 결과물 현황 (Status Summary)

* **Plan (계획)**: 사내 NAS의 비구조화 데이터를 보안 하에 실시간 RAG 지식으로 서비스하기 위한 요구사항 정의 및 가상화망 매핑 수립. (완료)
* **Design (설계)**: Watchdog 실시간 감지 데몬 설계, CPU/GPU 가속 분리 설계 및 CIFS 크레덴셜 영구 마운트 아키텍처 정의. (완료)
* **Do (수행)**:
  - 아톰 서버 크레덴셜(`~/.smbcredentials_nas`) 구축 및 `/etc/fstab` 영구 자동 마운트 완료.
  - 경로 최적화가 적용된 파이프라인 가공 스크립트 이관 및 감시 데몬 기동. (완료)
* **Check (검증)**:
  - `state.json`을 통한 실시간 모니터링 확인.
  - 가상환경 임베딩 모델 CPU 할당을 통한 VRAM OOM 우회 검증.
  - 72B 대형 모델 RAG 연동 질의-답변 결과 확인. (완료)

### 최종 결과물 목록
1. **설정 및 크레덴셜**: `/home/caiser77/.smbcredentials_nas` (NAS 인증 전용 파일)
2. **영구 자동 마운트**: `/etc/fstab` 내 `//100.94.64.83/26Project\0402026` 등록 완료
3. **감시 스크립트 데몬**: `/home/caiser77/dgx_workspace/002. 회사 NAS 분석/scripts/watchdog_pipeline.py` (백그라운드 기동 중)
4. **기동 및 관리 쉘**: [start_nas_watcher.sh](file:///Volumes/caiser77/dgx_workspace/002. 회사 NAS 분석/scripts/start_nas_watcher.sh) (데몬 실행기)

---

## 2. 장애 복구 및 유지 관리 지침 (Maintenance Guide)

### A. NAS 마운트 해제 및 자동 재연동
- **장애 요인**: Tailscale VPN 통신 장애나 시놀로지 NAS 리부팅 시 마운트가 일시 해제될 수 있습니다.
- **예방 설계**: `/etc/fstab`에 `x-systemd.automount` 옵션이 설정되어 있어, 백그라운드 watchdog 데몬이 `/mnt/dgxbackup` 디렉토리에 접근을 시도하는 즉시 OS 레벨에서 삼바 자동 재연결을 시도합니다.
- **수동 재연결**: 만약 자동 연동이 먹통이 될 경우, 아톰 서버 내부에서 아래 명령을 실행합니다.
  ```bash
  # caiser77 패스워드는 'aurum2026!!'
  echo 'aurum2026!!' | sudo -S mount -a
  ```

### B. 감시 데몬 프로세스 관리
- **상태 점검**:
  ```bash
  ps aux | grep watchdog_pipeline
  ```
- **로그 및 이벤트 모니터링**:
  - 실시간 로그: `tail -f "/home/caiser77/dgx_workspace/002. 회사 NAS 분석/logs/watchdog_pipeline.log"`
  - 최종 상태 JSON: `/home/caiser77/dgx_workspace/002. 회사 NAS 분석/data/processed/state.json`

---

## 3. 향후 권장 개선 사항 (Next Action Items)

1. **SlackIncoming Webhook 연동**:
   - 감시 데몬이 파일 가공 실패나 색인 실패 시 사내 슬랙 채널로 즉시 Alert을 송출하도록 `slack_notify.py` 내 Webhook URL 세팅 권장.
2. **증분 색인 지연 시간 튜닝**:
   - NAS에 엑셀이나 문서를 작성하면서 임시 저장을 반복할 때 불필요한 색인 유닛의 잦은 호출을 방지하기 위해, 파일 변경 안정 시간(Watchdog checks)을 3초에서 5~10초 수준으로 문서 용량이 클수록 늘리는 튜닝 권장.
