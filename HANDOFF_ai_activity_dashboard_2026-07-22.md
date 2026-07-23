# 아우룸 관제 대시보드 및 로컬 AI 작업 상태 인계 요약

작성일: 2026-07-22  
대상 저장소: `/home/caiser77/dgx_workspace`  
대시보드: `http://100.80.138.86:8502/`  
대시보드 소스: `apps/monitoring/metrics_server.py`  
협업 파이프라인 루트: `/home/caiser77/AI_BASE`  
맥 파이프라인 루트: `/Users/nams/AI_BASE/AurumPipeline_mohave`

## 사용자 의도

사용자는 아우룸맥과 아톰이 쉬지 않고 계속 일을 하기를 원합니다. 대시보드의 목적은 단순 CPU/RAM 감시가 아니라, 두 로컬 AI가 현재 무엇을 하고 있는지, 왜 멈춰 보이는지, 다음에 무엇을 해야 하는지를 관찰하는 것입니다.

따라서 대시보드는 다음 질문에 답해야 합니다.

- 아톰 AI는 지금 요약/분류/배정 중인가, 아니면 대기 중인가?
- 아우룸맥 AI는 지금 초안/RAG/검토 중인가, 아니면 승인대기 때문에 멈췄는가?
- 자원 사용률이 낮을 때 실제로 유휴인지, 아니면 사람 승인/동기화/후처리 대기인지?
- 다음 작업을 투입할 후보가 있는지?

## 이번 세션에서 확인한 핵심 원인

### 1. `요약대기` 표시는 실제 작업 정체가 아니었음

대시보드의 아톰 가공 이력에 `요약대기`가 많이 보여서 아톰이 일을 안 하는 것처럼 보였지만, 실제 이벤트 큐는 비어 있었습니다.

확인 결과:

- `atom_event_queue_worker` 로그는 `queue=empty` 반복
- SQLite `event_queue`에는 `pending` 없음
- 대시보드의 `요약대기`는 실시간 큐가 아니라 `data/processed/metadata`의 오래된 메타데이터 상태 판정 결과

### 2. 완료 판정 필드가 맞지 않았음

실제 처리기 `extract_data.py`는 `ai_classification.summary`를 생성하고 있었는데, 대시보드는 `ai_summary`만 완료 기준으로 보고 있었습니다.

그 결과 실제로 처리된 파일도 `요약대기`로 표시되었습니다.

수정 후:

- `ai_summary.summary` 또는 `ai_classification.summary`가 있으면 `요약완료`로 판정
- 최근 아톰 이력의 실제 업무 파일들이 `요약완료`로 표시됨
- `summary_done`이 `39,657`에서 `41,691`로 증가

### 3. Git 저장소 내부 파일이 가공 이력을 오염시켰음

최근 이력에 `ae9836e...`, `616eb4...` 같은 해시 파일이 보였는데, 이는 생태조사 문서가 아니라 NAS 내 bare Git 저장소 경로였습니다.

예:

- `/mnt/nas2026/남택우/git/AI_BASE.git/objects/...`

root `atom-watcher`는 이를 skip했지만, `atom_baseline_dryrun_watcher.py --enqueue` 쪽의 ignore rule이 부족해서 큐에 들어간 것으로 판단했습니다.

수정 후:

- `.git`, `*.git`, `.hg`, `.svn` 경로를 감시 제외
- 대시보드 최근 이력에서도 Git/시스템 산출물 경로 제외

### 4. 이벤트 큐 워커가 실패처럼 보인 원인

`atom_event_queue_worker.service`가 `Restart=always`로 되어 있어, 큐가 비어 정상 종료해도 5초마다 다시 실행되었습니다. systemd 상태가 `activating auto-restart`처럼 보여 오류로 오해될 수 있었습니다.

수정 후:

- 서비스는 `Type=oneshot`
- `Restart=always` 제거
- 타이머가 2분마다 실행
- 큐가 비면 정상 종료

## 대시보드 UX 변경

상단에 `AI 작업 현황` 패널을 추가했습니다.

### ATOM AI 작업 현황

표시 항목:

- 상태: `작업중`, `대기중`, `감시중`
- 현재 임무
- 작업명 또는 사업명
- 이벤트/raw/처리중/승인대기 큐
- 다음 조치

현재 API 예시:

```json
"atom": {
  "state": "waiting",
  "headline": "맥 작업 결과 동기화/후처리 대기",
  "job": "과천주암",
  "queue": "이벤트 0 · raw 0 · 처리중 1 · 승인대기 0",
  "next": "맥 상태 회수 또는 중복 아카이브"
}
```

### AURUM MAC AI 작업 현황

표시 항목:

- 상태: `작업중`, `대기중`, `감시중`
- 현재 임무
- 작업 ID
- 초안작성/승인대기/여유슬롯
- 다음 조치

현재 API 예시:

```json
"mac": {
  "state": "waiting",
  "headline": "초안/검토 완료, 운영자 승인 대기",
  "job": "doc_e5aa23c021db",
  "queue": "초안작성 0 · 승인대기 1 · 여유슬롯 2",
  "next": "대시보드 승인/거절 또는 아톰 회수"
}
```

## 현재 실제 파이프라인 상태

마지막 확인 시점 기준:

- 아톰 raw: `0`
- 아톰 02_drafting: `1`
- 아톰 승인대기: `0`
- 맥 초안작성: `0`
- 맥 승인대기: `1`
- 배포 완료: `12`
- 코퍼스: `19`
- 이벤트 큐 pending: `0`

현재 핵심 작업:

- `doc_e5aa23c021db`
- 아톰에는 `02_drafting/status: drafting`으로 남아 있음
- 맥에는 `02_drafting/status: admin_pending`으로 존재
- 맥 draft에는 아우룸 자동 검토 의견이 붙어 있음
- 즉 맥은 초안/검토를 끝내고 사람 승인 대기 상태

## 커밋/푸시 내역

### 1. 대시보드 UI 개선

커밋:

```text
d0adad950 Improve monitoring dashboard operations UI
```

내용:

- 운영 관제형 compact dark UI
- 레이아웃/색상 반전/카드 밀도 조정

### 2. 파이프라인 승인 컨트롤

커밋:

```text
b958c2654 Add dashboard pipeline approval controls
```

내용:

- 파이프라인 카드 클릭 가능
- 승인대기/처리중/배포완료/코퍼스 상세 모달
- 승인/거절 API 추가
- 맥 승인대기 회수 액션 추가

### 3. 밸런서 및 stale 후처리

커밋:

```text
1f3739b96 Add pipeline balancer and stale job cleanup
```

내용:

- `pipeline_balancer.py` 추가
- RAM 사용률 대신 `MemAvailable`, memory PSI, swap, 큐 상태 기준
- stale Atom `02_drafting` 중복 정리
- 맥 published 후처리
- systemd timer 추가

### 4. 아톰 가공 이력 상태 보정

커밋:

```text
2d1b56d72 Fix Atom processing history status
```

내용:

- `ai_classification.summary`를 요약 완료로 인정
- Git 저장소 내부 파일을 이력/감시에서 제외
- 이벤트 큐 워커를 타이머 실행형으로 정리

### 5. 두 로컬 AI 작업 현황 표시

커밋:

```text
727d7e512 Show local AI activity on dashboard
```

내용:

- `ai_activity` API 필드 추가
- 상단 `ATOM AI 작업 현황`, `AURUM MAC AI 작업 현황` 패널 추가
- 밸런서가 맥 작업 목록, 활성 작업, 대기 이유, 여유 슬롯을 상태 파일에 기록
- 대시보드가 두 로컬 AI의 현재 임무와 다음 조치를 표시

위 커밋들은 모두 `origin/main`에 푸시 완료되었습니다.

## 현재 변경되지 않은/주의할 점

### 승인대기는 자동 승인하지 말 것

`admin_pending`은 사람이 승인/거절해야 하는 단계입니다. 사용자가 “일하게 만들자”고 했더라도 문서 내용을 검토하지 않고 자동 승인하는 것은 위험합니다.

현재 가능한 자동 조치:

- 맥 승인대기 항목을 아톰 승인대기함으로 회수
- stale duplicate 정리
- 새 raw 작업 투입
- 밸런서로 맥에 신규 작업 배정

수동 판단이 필요한 조치:

- 승인
- 거절
- 검토 의견에 따른 수정 지시

### 상태 파일 형식 주의

`pipeline_balancer.py`를 수정해 `pipeline_mac_status.json`에 다음 필드를 쓰도록 했습니다.

- `jobs`
- `active_jobs`
- `idle_reason`
- `last_action`
- `available_slots`

그러나 마지막 사용자 중단 직전 확인에서 `pipeline_mac_status.json`이 다시 옛 형식처럼 보였습니다.

예:

```json
{"admin_pending":1,"drafting":0,"launchd":"active","updated":"2026-07-22 12:33:52"}
```

가능성:

- systemd 타이머가 수정 전/다른 경로의 밸런서를 실행 중
- 사용자가 중단한 명령이 일부 실행되다가 상태 파일만 갱신
- 배포본/실행본과 편집본 차이

다음 세션에서는 먼저 아래를 확인해야 합니다.

```bash
systemctl --user cat aurum-pipeline-balancer.service aurum-pipeline-balancer.timer
cd "/home/caiser77/dgx_workspace/005. 아톰-모하비-아우룸 협업 파이프라인" && /usr/bin/python3 scripts/pipeline_balancer.py --execute
cat /home/caiser77/AI_BASE/pipeline_mac_status.json
```

## 마지막 사용자 요청과 중단 지점

사용자 요청:

```text
일을 하게 만들자
```

진행 중 판단:

- 현재 승인대기 1건 때문에 맥은 다음 작업이 없어 보임
- 이벤트 큐는 비어 있음
- 아톰/맥을 쉬지 않게 하려면 승인대기를 임의 처리하기보다, 처리 완료된 metadata 중 아직 005 파이프라인에 들어가지 않은 항목을 raw로 2-3건 신규 투입하는 것이 안전함

진행하려던 작업:

1. 현재 파이프라인 job ID 목록 수집
2. `data/processed/metadata`에서 아직 005에 export되지 않은 성공 metadata 후보 찾기
3. `export_processed_to_pipeline.py --metadata-file ...`로 2-3건을 `01_raw_analyzed`에 투입
4. `pipeline_engine.py`가 `02_drafting`으로 넘기는지 확인
5. `pipeline_balancer.py --execute`로 맥에 배정
6. 필요 시 맥 launchd 수동 시작

사용자가 중단한 명령:

```bash
cd "/home/caiser77/dgx_workspace/005. 아톰-모하비-아우룸 협업 파이프라인" && /usr/bin/python3 scripts/pipeline_balancer.py --execute
```

중단 후에는 해당 명령이 일부 실행되었을 수 있으므로, 다음 세션에서는 먼저 상태 파일과 큐 상태를 다시 확인해야 합니다.

## 다음 추천 작업

### 1. 밸런서 상태 파일 형식 확인

새 필드가 유지되는지 확인합니다.

### 2. 승인대기 항목을 대시보드에서 열어 검토

`doc_e5aa23c021db`는 맥에서 이미 `admin_pending`입니다. 사용자가 승인하거나 거절해야 다음 단계로 넘어갑니다.

### 3. 새 일감 2-3건 투입

승인대기를 건드리지 않고 아톰과 맥을 일하게 하려면, 미투입 metadata를 찾아 `01_raw_analyzed`로 export합니다.

주의:

- `export_processed_to_pipeline.py --limit`은 기존 항목 skip도 count에 포함할 수 있으므로, 가능하면 특정 metadata 파일을 직접 지정하는 방식이 안전합니다.
- Git 저장소 내부 경로, `_AURUM_AI_PROCESSED`, recycle 경로는 제외해야 합니다.

### 4. 자동 투입 정책 설계

운영 목표가 “두 로컬 AI를 쉬지 않게 하기”라면 별도 feeder가 필요합니다.

권장 정책:

- 맥 `admin_pending`이 있어도 active drafting이 0이고 여유 슬롯이 있으면 새 raw 후보를 계속 투입
- 단, 전체 승인대기 상한을 둠. 예: 5건 이상이면 추가 투입 중지
- 낮에는 1-2건, 야간에는 4-8건까지 자동 투입
- 대시보드에는 “왜 투입/보류했는지”를 표시

## 주요 파일

- `/home/caiser77/dgx_workspace/apps/monitoring/metrics_server.py`
- `/home/caiser77/dgx_workspace/scripts/atom_ignore_rules.py`
- `/home/caiser77/dgx_workspace/scripts/atom_event_queue_worker.py`
- `/home/caiser77/dgx_workspace/scripts/atom_baseline_dryrun_watcher.py`
- `/home/caiser77/dgx_workspace/005. 아톰-모하비-아우룸 협업 파이프라인/scripts/pipeline_balancer.py`
- `/home/caiser77/dgx_workspace/005. 아톰-모하비-아우룸 협업 파이프라인/scripts/export_processed_to_pipeline.py`
- `/home/caiser77/AI_BASE/pipeline_mac_status.json`

## 라이브 대시보드 재시작 명령

```bash
kill <metrics_pid>
setsid /bin/bash -c 'cd /home/caiser77/dgx_workspace/apps/monitoring && exec /home/caiser77/dgx_workspace/venv/bin/python3 metrics_server.py </dev/null >dashboard.log 2>&1' >/dev/null 2>&1 &
```

`</dev/null`이 없으면 프로세스가 죽을 수 있으므로 반드시 포함합니다.
