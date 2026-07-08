# 아톰-모하비-아우룸 협업 파이프라인 완성 보고

## 1. 구현 완료 범위

2026-07-08 기준으로 3단 협업 파이프라인의 기본 실행 골격을 완성했다.

- `scripts/pipeline_engine.py`: `01_raw_analyzed`의 `*.summary.md`와 `*.result.json`을 감지해 `*.draft.md`를 만들고 `02_drafting`으로 이동한다.
- `scripts/track_pipeline_status.py`: 모하비가 초안을 `status: review_pending` 또는 `status: reviewed`로 바꾸면 관련 파일 세트를 `03_review_pending`으로 이동한다.
- `scripts/aurum_deployer.py`: `03_review_pending`의 draft를 배포 처리하고 HWP/PDF 산출물을 만든 뒤 `04_published`로 아카이빙한다.
- `scripts/sync_obsidian_notes.sh`: 아톰, 모하비, 아우룸 간 stage 디렉터리와 피드백 DB를 rsync로 교환한다.
- `scripts/simulate_pipeline_e2e.py`: 임시 디렉터리에서 전체 상태 전이를 검증한다.
- `scripts/pipeline_config.example.json`: 운영 경로 설정 예시를 제공한다.

## 2. 표준 상태 전이

```text
01_raw_analyzed/status: raw_analyzed
  -> pipeline_engine.py
02_drafting/status: drafting
  -> 모하비 작성 완료 후 status: review_pending
  -> track_pipeline_status.py
03_review_pending/status: review_pending 또는 reviewed
  -> aurum_deployer.py
04_published/status: published
```

## 3. 운영 명령

stage 디렉터리 초기화:

```bash
PIPELINE_ROOT=~/AI_BASE python3 scripts/track_pipeline_status.py --root ~/AI_BASE init
```

아톰 1단계 감시:

```bash
python3 scripts/pipeline_engine.py ~/AI_BASE/01_raw_analyzed
```

모하비 handoff 감시:

```bash
python3 scripts/track_pipeline_status.py --root ~/AI_BASE watch --interval 5
```

아우룸 배포 감시:

```bash
TELEGRAM_BOT_TOKEN=... ALLOWED_USER_ID=... python3 scripts/aurum_deployer.py
```

동기화 예시:

```bash
ATOM_PIPELINE_ROOT=~/AI_BASE MOHAVE_PIPELINE_ROOT=user@mac:/Users/user/Obsidian/AurumPipeline AURUM_PIPELINE_ROOT=user@aurum:/srv/aurum-pipeline scripts/sync_obsidian_notes.sh all
```

로컬 E2E 검증:

```bash
PYTHONDONTWRITEBYTECODE=1 scripts/simulate_pipeline_e2e.py
```

## 4. 검증 결과

`simulate_pipeline_e2e.py`로 아래 흐름을 확인했다.

- `raw_analyzed` summary/result 생성
- draft 생성 및 `02_drafting` 이동
- `review_pending` 승격 및 `03_review_pending` 이동
- 아우룸 배포 모의 HWP/PDF 생성
- draft frontmatter `status: published` 갱신
- `04_published` 아카이빙

## 5. 남은 프로덕션 연동 과제

- 현재 HWP/PDF 변환은 `MOCK HWP`, `MOCK PDF` 파일 생성이다. 실제 운영에서는 Pandoc, Weasyprint, 한글 OLE Automation 중 하나로 `convert_to_hwp_pdf()`를 교체해야 한다.
- 모하비의 실제 RAG 초안 작성 엔진은 외부 에이전트/옵시디언 워크플로에 연결해야 한다. 현재 트래커는 완료된 draft의 상태 전이를 담당한다.
- rsync 원격 경로와 인증키, macOS 자모 변환 옵션(`RSYNC_ICONV`)은 운영 장비별로 환경변수에서 확정해야 한다.
