# 아톰-모하비-아우룸 파이프라인 점검 — 2026-07-25

## 배경
`005. 아톰-모하비-아우룸 협업 파이프라인` 전반 상태 점검 요청으로 시작. 점검 도중 atom-watcher의 Telegram 알림 폭주(이미 처리한 파일 재통지) 문제를 발견해 원인 수정 및 배포까지 진행.

## 1. 초기 파이프라인 점검 결과

| 항목 | 상태 |
|---|---|
| aurum-pipeline-engine / tracker / deployer | 정상(active) |
| watchdog_pipeline (NAS 감지→hermes 분류) | 정상, 실시간 파일 처리 중 |
| GPU(GB10) | 사용률 96%, 66°C 정상 |
| NAS 마운트(nas2023old~2026, dgxbackup) | 정상 |
| 파이프라인 대기열 | 02_drafting 24건, 03_review_pending 12건, 04_published 288건, 00_error_failed 0건 |
| admin_pending | 8건 — 게이트 정상 동작(종날조 의심 2건, 빈보고서 의심 3건, 중요납품물 3건). 조치 불필요, 정상 흐름 |
| atom_baseline_watcher | 16:48 OOM-kill 1회 발생, 재시작 2회 (당시 스왑 15Gi/15Gi 포화 상태) |
| atom-model-router | BrokenPipeError 502 다수(클라이언트 조기 연결 끊음, 백엔드 자체는 정상) |

## 2. atom-watcher Telegram 폭주 — 근본 원인

- `/opt/atom-watcher/watcher.py`가 `watchdog.observers.polling.PollingObserver`를 `timeout` 인자 없이 생성 → 기본값 **1초 간격**으로 4개 NAS(nas2023old~2026, 28TB급) 전체를 재귀 스캔.
- 중복 방지 로직(`dedupe_recent`)이 **메모리 내, 같은 분(60초) 안에서만** 유효 → 재시작하거나 몇 분만 지나도 무의미.
- 결과: 이미 처리된 파일이 CIFS 리스팅 흔들림 등으로 몇 분~수십 분 간격을 두고 "새로 생성됨"으로 반복 재탐지됨(샘플 파일 1개가 하루 5회 반복 탐지 확인). 실제 Telegram 발송(사진/보고서류)까지 새는 경우도 이론상 가능.

## 3. 적용한 수정

`/opt/atom-watcher/watcher.py`에 **영속 처리 이력(SeenStore)** 추가:
- `/var/log/atom-watcher/seen.sqlite`에 `(상대경로, size+mtime 시그니처)`를 저장
- 이미 동일 시그니처로 기록된 경로는 raw event 단계에서 즉시 스킵 → parse/알림까지 가지 않음
- 파일이 실제로 수정(크기/mtime 변경)되면 시그니처가 달라져 정상적으로 재알림
- 재시작해도 sqlite가 남아있어 재부팅 후 전체 재알림 폭주도 방지

### 배포 중 겪은 이슈
- 최초 배포 시 상태 db 경로를 `/opt/atom-watcher/state/`로 잡았다가 실패 — 유닛 파일의 `ProtectSystem=strict` + `ReadWritePaths=/var/log/atom-watcher`만 허용되는 하드닝 설정 때문. `/var/log/atom-watcher/seen.sqlite`로 경로 변경 후 정상 배포.
- 원본은 타임스탬프 백업(`watcher.py.bak.*`)으로 보존됨.

## 4. vLLM 메모리 여유 확보 시도 — 실패, 원복

atom-watcher 최초 전수 스캔 중 시스템 메모리가 재차 포화(스왑 15Gi/15Gi 거의 소진)되어 여유 확보를 시도.

- 처음엔 "정체불명 100GB+ 메모리"로 보였으나, 계산 결과 vLLM 두 컨테이너의 `--gpu-memory-utilization` 설정(27B=0.44, 35B=0.40, 합계 84%)이 GB10 통합메모리 특성상 원인이었음(사용자가 정확히 짚어냄). 미스터리 아님 — 설계대로 동작.
- `gpu-memory-utilization`을 0.36/0.32로 낮춰 재시작 → **둘 다 기동 실패**(`max_model_len=262144` 기준 KV캐시 부족, `ValueError: No available memory for the cache blocks`).
- 원래 값(0.44/0.40)으로 즉시 원복. 이번엔 두 컨테이너를 거의 동시에 띄워서 **35B가 또 실패**(GPU 메모리 프로파일링 경합 추정).
- 27B를 완전히 healthy 상태로 만든 뒤 35B를 순차적으로 기동 → **둘 다 정상화**.
- 결론: 두 모델을 동시에(병렬로) 기동하면 프로파일링 단계에서 경합이 생겨 실패할 수 있음 — **반드시 순차 기동 필요**. `gpu-memory-utilization`은 현재 설정이 이미 262144 컨텍스트 기준 하한에 가까워 추가로 낮출 여유가 거의 없음.
- 관련 스크립트: `~/dgx_workspace/001. LLM 설정/scripts/start_vllm_qwen36_27b.sh`, `start_vllm_qwen36_35b_nvfp4.sh` (수정 없이 원래 기본값으로 원복 완료).

## 5. 아우룸 슬랙 모델 구성

`~/.hermes/profiles/aurum_slack/config.yaml`:
```yaml
model:
  default: atom-auto
  provider: custom
  base_url: http://127.0.0.1:8088/v1
```
`atom-model-router`(8088)를 경유하며, 내부적으로 코더용 `Qwen/Qwen3.6-27B-FP8`(8090)과 RAG/일반용 `nvidia/Qwen3.6-35B-A3B-NVFP4`(8089)를 요청 성격에 따라 라우터가 자동 선택.

## 6. 최종 상태 (2026-07-25 19:27 기준)

- `atom-watcher.service`: active, 최초 전수 스캔 진행 중. `seen.sqlite` 113,877건 기록, 아직 크래시 없음.
- vLLM `vllm-qwen36-27b`(8090), `vllm-qwen36-35b`(8089): 둘 다 healthy.
- `aurum_slack`: 정상 동작 중(조치 불필요).
- 시스템 메모리: 사용 120Gi/121Gi, 가용 1.2~1.5Gi, 스왑 사실상 소진 — 구조적으로 항상 빠듯한 상태(vLLM 예약 84%가 근본 원인, 별도 조치 없이는 개선 어려움).

## 7. 후속 확인 필요 사항

- [ ] atom-watcher 최초 전수 스캔 완료 시점 확인 — 현재 페이스(분당 약 285건)로는 상당히 오래 걸릴 수 있음. 완료 후 동일 파일 재탐지 시 `skip already-processed` 로그가 실제로 찍히는지 최종 확인 필요.
- [ ] 필요시 `atom-watcher`의 폴링 주기(현재 기본 1초)를 늘리는 방안도 별도로 검토 가능(이번 수정과는 별개, 스캔 부하 자체를 줄이는 방향).
- [ ] 시스템 메모리/스왑 포화는 vLLM 예약량이 원인이라 구조적 이슈 — 재부팅이나 모델 구성 변경 없이는 근본적으로 해소되지 않음.
