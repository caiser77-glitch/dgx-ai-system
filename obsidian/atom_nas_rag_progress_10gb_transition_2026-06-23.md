# 아톰 NAS 큐레이팅 및 RAG 진행도 개선 기록

작성일: 2026-06-23  
대상: DGX Atom, NAS2, Fauna Dashboard, atom-watcher

## 1. 최초 문제 제기

대시보드 `http://localhost:8501/`에서 다음 현상이 확인되었다.

- `누적 가공 인덱스 (RAG)` 값이 변동하지 않음
- `1차 전수 RAG 인덱싱 진행도`가 변동하지 않음
- `최근 파일 가공 이력`은 실시간으로 반영됨
- 외부 접속 설정을 했으나 접속이 되지 않는 것으로 보임

## 2. 원인 판단

### 대시보드 진행도 정체

실제 가공 작업이 멈춘 것이 아니라, 대시보드가 참조하는 집계 소스가 현재 작업 흐름을 정확히 반영하지 못하고 있었다.

- 최근 파일 가공 이력은 metadata 디렉터리를 직접 읽어 갱신되고 있었다.
- `누적 가공 인덱스 (RAG)`와 `1차 전수 RAG 인덱싱 진행도`는 실제 FAISS/state/log 상태와 어긋난 값을 보고 있었다.
- 전수 진행도는 `cron_run.log`의 시작 시점 집계값 위주로 해석되어, 현재 처리 중인 `[n/total] 처리 시작` 및 `가공 완료` 로그가 충분히 반영되지 않았다.

### 외부 접속 문제

Streamlit 자체는 정상 실행 중이었다.

- Streamlit 실행 주소: `0.0.0.0:8501`
- 내부 LAN 접속 주소: `http://192.168.219.100:8501`
- Tailscale 접속 주소: `http://100.98.149.128:8501`

공인 IP 접속은 포트포워딩 또는 방화벽 설정이 없어서 실패하는 상태였다.

## 3. 적용된 개선

### Dashboard 진행도 표시 보정

`Fauna_Dashboard/streamlit_app.py`의 진행도 집계 로직을 수정했다.

변경 내용:

- `누적 가공 인덱스 (RAG)`는 실제 FAISS mapping/state의 `document_count`를 기준으로 표시
- `1차 전수 RAG 인덱싱 진행도`는 `cron_run.log`의 최신 실행 구간을 기준으로 계산
- 현재 처리 위치와 완료 로그를 반영하여 진행률이 움직이도록 보정

당시 검산 예시:

- RAG 인덱스: `84,389건`
- 전수 대상: `194,183개`
- 완료: `4,994개`
- 미처리: `189,189개`
- 진행률: `2.57%`

### 내부 접속 주소 정리

```text
같은 내부망 사용자:
http://192.168.219.100:8501

Tailscale 접속 사용자:
http://100.98.149.128:8501
```

공인 IP 접속 주소는 포트포워딩/방화벽이 준비되지 않아 사용하지 않는 것으로 판단했다.

## 4. 아톰의 주 임무 재정의

아톰의 주 임무는 `hermes-agent` 자체가 아니라 NAS 신규 자료 큐레이팅이다.

공식 감시 데몬:

```text
atom-watcher systemd service
```

공식 감시 대상:

```text
/mnt/nas2023old -> 00Project2023 이전
/mnt/nas2024    -> 24Project 2024
/mnt/nas2025    -> 25Project 2025
/mnt/nas2026    -> 26Project 2026
```

운영 원칙:

- 원본 파일은 DGX로 복사하지 않는다.
- NAS SMB 마운트 경로에서 직접 읽는다.
- atom-watcher는 신규 자료 감시와 큐레이팅의 공식 기준이다.
- Hermes는 필요 시 분류/메타데이터 판단을 보조하는 계층이다.

## 5. NAS2 10Gb SMB 전환

### 기존 상태

전환 전 NAS 공유는 Tailscale IP로 마운트되어 있었다.

```text
//100.94.64.83/00Project2023 이전 -> /mnt/nas2023old
//100.94.64.83/24Project 2024     -> /mnt/nas2024
//100.94.64.83/25Project 2025     -> /mnt/nas2025
//100.94.64.83/26Project 2026     -> /mnt/nas2026
```

이 구성은 SMB/CIFS 마운트는 맞지만, NAS2의 10Gb LAN 경로를 직접 사용하는 구성으로 보기 어려웠다.

### Synology DSM에서 확인된 NAS2 10Gb 정보

```text
10Gb 인터페이스 이름: LAN 포트 3 정적 IP
IPv4 주소: 192.168.219.111
서브넷 마스크: 255.255.255.0
연결 속도: 10000 Mbps, 풀 듀플렉스, MTU 1500
기본 게이트웨이: 192.168.219.1
```

DGX 측 확인:

```text
DGX IP: 192.168.219.100
NAS2 10Gb IP: 192.168.219.111
SMB 포트: 445 연결 성공
ping 평균: 약 0.141ms
```

DGX와 NAS2가 같은 10Gb LAN 대역에서 통신 가능한 상태로 확인되었다.

### 전환 후 상태

`/etc/fstab`의 NAS 주소를 `100.94.64.83`에서 `192.168.219.111`로 변경하고 재마운트했다.

현재 마운트:

```text
/mnt/nas2023old -> //192.168.219.111/00Project2023 이전
/mnt/nas2024    -> //192.168.219.111/24Project 2024
/mnt/nas2025    -> //192.168.219.111/25Project 2025
/mnt/nas2026    -> //192.168.219.111/26Project 2026
```

확인된 상태:

```text
FSTYPE: cifs
addr: 192.168.219.111
rsize: 4194304
wsize: 4194304
```

따라서 현재 공식 NAS 경로는 Tailscale IP가 아니라 NAS2 10Gb LAN IP를 사용한다.

## 6. 서비스 상태 정리

### 공식 atom-watcher

전환 후 공식 감시 데몬은 정상 실행 중이다.

```text
atom-watcher.service: active running
```

감시 로그 기준:

```text
watching root: /mnt/nas2023old
watching root: /mnt/nas2024
watching root: /mnt/nas2025
watching root: /mnt/nas2026
polling observer enabled for SMB/CIFS reliability
```

### 구형 watchdog_pipeline.service

사용자 systemd의 `watchdog_pipeline.service`는 비어 있는 `/mnt/dgxbackup`을 감시하고 있었다.

전환 후 `/mnt/dgxbackup`은 더 이상 공식 NAS 마운트 경로가 아니므로, 혼선을 줄이기 위해 해당 사용자 서비스를 중지 및 비활성화했다.

```text
watchdog_pipeline.service: inactive, disabled
```

공식 감시 기준은 `atom-watcher`로 정리한다.

## 7. 현재 남은 정상 작업

전환 후 다음 프로세스가 정상 범위로 남아 있다.

```text
atom-watcher
run_all_slicers.sh
longterm_batch_slicer.py
extract_data.py
```

의미:

- `atom-watcher`: 공식 신규 자료 감시
- `longterm_batch_slicer.py`: 장기 전수 가공/RAG 배치
- `extract_data.py`: 개별 파일 추출 및 메타데이터 생성

## 8. 남은 개선 과제

### 기존 자료 기준선 DB 생성

현재 아톰은 NAS 안에 이미 올라와 있던 자료와 신규 자료를 명확히 구분하기 위한 기준선이 필요하다.

목표:

- 4개 NAS 경로 전체에 대해 기존 파일 목록을 baseline으로 등록
- 파일 복사 없이 `path`, `size`, `mtime`, 필요 시 partial hash만 저장
- 이후 신규/변경 파일만 큐레이팅 대상으로 판정

대상 경로:

```text
/mnt/nas2023old
/mnt/nas2024
/mnt/nas2025
/mnt/nas2026
```

### 신규 큐레이팅과 1차 전수 RAG 분리

운영 역할을 분리한다.

```text
atom-watcher:
  신규 자료 감시 및 큐레이팅

longterm_batch_slicer:
  기존 자료에 대한 1차 전수 가공/RAG 장기 배치
```

이렇게 분리해야 신규 자료가 들어왔을 때 아톰이 본래 임무에 집중할 수 있다.

### RAG 인덱싱 증분화

전수 RAG가 하루 약 1% 수준으로 진행되는 문제를 줄이기 위해 증분화가 필요하다.

개선 방향:

- 매번 전체 FAISS 인덱스를 재빌드하지 않기
- 신규/변경 파일만 임베딩 및 인덱스 반영
- OCR 실패 결과 캐시
- LLM 분류 결과 캐시
- 파일 단위 처리 상태 DB 도입

기대 효과:

- 현재 100일 규모 작업을 수일~수주 단위로 단축할 가능성
- 신규 자료 큐레이팅 지연 감소
- 대시보드 진행도와 실제 작업 상태의 불일치 감소

## 9. 한 줄 결론

대시보드 진행도 정체는 실제 작업 중단이 아니라 집계 소스 문제였고, NAS 통신은 Tailscale SMB에서 NAS2 10Gb LAN SMB로 전환 완료했다. 다음 핵심은 기존 자료 baseline을 만들어 아톰이 신규 자료만 정확히 큐레이팅하도록 정리하는 것이다.

## 10. baseline dry-run watcher 연결

공식 `atom-watcher`는 root/atom 소유의 `/opt/atom-watcher`와 systemd 샌드박스(`ProtectHome=true`) 안에서 실행된다. 따라서 공식 서비스 내부에 baseline DB 판별기를 직접 붙이려면 root 권한으로 `/opt` 배포와 systemd drop-in 수정이 필요하다.

우선 안전한 검증 단계로 사용자 권한의 sidecar dry-run watcher를 연결했다.

실행 세션:

```text
tmux session: atom_baseline_dryrun
```

실행 스크립트:

```text
/home/caiser77/dgx_workspace/scripts/atom_baseline_dryrun_watcher.py
```

감시 대상:

```text
/mnt/nas2023old
/mnt/nas2024
/mnt/nas2025
/mnt/nas2026
```

로그:

```text
/home/caiser77/dgx_workspace/logs/atom_baseline_dryrun_watcher.log
/home/caiser77/dgx_workspace/logs/atom_baseline_dryrun_watcher.console.log
```

현재 모드:

```text
enqueue=False
```

의미:

- 파일 이벤트를 baseline DB와 비교한다.
- `existing`, `ignored`, `new`, `changed`, `deleted` 판정을 로그로 남긴다.
- 아직 큐에는 넣지 않는다.
- dry-run 로그를 보고 오탐 여부를 확인한 뒤 `--enqueue` 모드로 전환한다.

상태 확인:

```bash
tmux list-sessions | grep atom_baseline_dryrun
pgrep -af 'atom_baseline_dryrun_watcher.py'
tail -f /home/caiser77/dgx_workspace/logs/atom_baseline_dryrun_watcher.log
```

중지:

```bash
tmux kill-session -t atom_baseline_dryrun
```

큐 등록 모드로 전환할 때의 실행 예:

```bash
tmux kill-session -t atom_baseline_dryrun

tmux new-session -d -s atom_baseline_dryrun   "PYTHONUNBUFFERED=1 /home/caiser77/dgx_workspace/scripts/atom_baseline_dryrun_watcher.py   --db /home/caiser77/dgx_workspace/data/atom_watcher/atom_baseline.sqlite   --log-file /home/caiser77/dgx_workspace/logs/atom_baseline_dryrun_watcher.log   --enqueue 2>&1 | tee /home/caiser77/dgx_workspace/logs/atom_baseline_dryrun_watcher.console.log"
```

공식 `atom-watcher` 내부 연결은 dry-run 판정이 안정적인 것을 확인한 뒤 진행한다.

## 11. baseline watcher enqueue 서비스 전환

`atom_baseline_dryrun` tmux 세션은 종료했고, baseline 기반 이벤트 판별기를 사용자 systemd 서비스로 전환했다.

서비스:

```text
atom_baseline_watcher.service
```

서비스 파일:

```text
/home/caiser77/.config/systemd/user/atom_baseline_watcher.service
```

실행 명령:

```text
/home/caiser77/dgx_workspace/venv/bin/python   /home/caiser77/dgx_workspace/scripts/atom_baseline_dryrun_watcher.py   --db /home/caiser77/dgx_workspace/data/atom_watcher/atom_baseline.sqlite   --log-file /home/caiser77/dgx_workspace/logs/atom_baseline_dryrun_watcher.log   --enqueue
```

현재 모드:

```text
enqueue=True
```

의미:

- 공식 NAS 4개 루트를 감시한다.
- 이벤트 파일을 baseline DB와 비교한다.
- `ignored`와 `existing`은 로그만 남긴다.
- `new`, `changed`, `deleted`는 `event_queue` 테이블에 등록한다.
- 공식 `atom-watcher` 서비스는 그대로 유지한다.

상태 확인:

```bash
systemctl --user status atom_baseline_watcher.service --no-pager
/home/caiser77/dgx_workspace/scripts/atom_baseline_status.py
tail -f /home/caiser77/dgx_workspace/logs/atom_baseline_dryrun_watcher.log
```

중지:

```bash
systemctl --user stop atom_baseline_watcher.service
```

재시작:

```bash
systemctl --user restart atom_baseline_watcher.service
```

비활성화:

```bash
systemctl --user disable --now atom_baseline_watcher.service
```

현재 확인 상태:

```text
atom_baseline_watcher.service: active running
baseline_present_files: 1,159,434
scan_errors: 0
queue: empty
```

다음 작업은 `event_queue`에 들어온 신규/변경/삭제 이벤트를 처리하는 worker를 만드는 것이다. 이 worker는 신규 파일을 큐레이팅 대상으로 넘기고, 처리 성공/실패/재시도 상태를 관리해야 한다.

## 12. event_queue worker 준비

baseline watcher가 `new`, `changed`, `deleted` 이벤트를 `event_queue`에 넣으면, 이를 처리할 worker를 준비했다.

스크립트:

```text
/home/caiser77/dgx_workspace/scripts/atom_event_queue_worker.py
```

현재 상태:

```text
자동 실행 서비스로는 아직 등록하지 않음
수동 실행 및 dry-run 검증 완료
현재 queue=empty
```

큐 상태 확인:

```bash
/home/caiser77/dgx_workspace/scripts/atom_event_queue_worker.py --summary
```

큐 dry-run 처리:

```bash
/home/caiser77/dgx_workspace/scripts/atom_event_queue_worker.py --dry-run --limit 5
```

실제 처리 실행 예:

```bash
/home/caiser77/dgx_workspace/scripts/atom_event_queue_worker.py --limit 5
```

처리 동작:

- `new`, `changed`: 기존 `extract_data.py`를 호출해 `/home/caiser77/dgx_workspace/data/processed`로 가공한다.
- `deleted`: `skipped_deleted`로 상태를 정리한다.
- 실패 시 `failed`와 `last_error`를 기록한다.
- 성공 시 `done`으로 기록한다.

아직 자동 서비스로 켜지 않은 이유:

- 신규 이벤트가 실제로 들어와 큐에 쌓이는지 먼저 관찰해야 한다.
- 큐 처리량과 OCR/LLM 부하를 확인한 뒤 worker를 timer 또는 service로 승격하는 것이 안전하다.

## 13. event_queue worker 안전 승격

신규 이벤트 큐가 아직 비어 있는 상태에서 watcher가 `--enqueue`로 정상 실행 중임을 확인했다. 이후 worker를 상시 프로세스가 아니라 user systemd timer로 승격했다. 큐가 없으면 즉시 종료하고, 큐가 있으면 한 번에 최대 3건만 처리한다.

등록된 unit:

```text
/home/caiser77/.config/systemd/user/atom_event_queue_worker.service
/home/caiser77/.config/systemd/user/atom_event_queue_worker.timer
```

실행 방식:

```text
ExecStart=/home/caiser77/dgx_workspace/venv/bin/python /home/caiser77/dgx_workspace/scripts/atom_event_queue_worker.py --limit 3
OnBootSec=2min
OnUnitActiveSec=2min
AccuracySec=30s
```

승격 직후 확인 결과:

```text
atom_event_queue_worker.timer: active waiting
첫 실행 결과: queue=empty, status=0/SUCCESS
다음 실행: 2분 주기
```

운영 확인 명령:

```bash
systemctl --user status atom_baseline_watcher.service --no-pager
systemctl --user status atom_event_queue_worker.timer --no-pager
systemctl --user status atom_event_queue_worker.service --no-pager
systemctl --user list-timers --all atom_event_queue_worker.timer --no-pager
/home/caiser77/dgx_workspace/venv/bin/python /home/caiser77/dgx_workspace/scripts/atom_baseline_status.py
/home/caiser77/dgx_workspace/venv/bin/python /home/caiser77/dgx_workspace/scripts/atom_event_queue_worker.py --summary
```

안전 중지 명령:

```bash
systemctl --user disable --now atom_event_queue_worker.timer
systemctl --user stop atom_event_queue_worker.service
```

현재 구조에서 신규 NAS 파일이 감지되면 `event_queue`에 `new` 또는 `changed`로 들어가고, timer가 최대 3건씩 기존 `extract_data.py` 파이프라인으로 넘긴다. 대량 처리 전환은 처리 성공률과 OCR/LLM 부하를 확인한 뒤 `--limit`과 주기를 늘리는 방식으로 진행한다.

