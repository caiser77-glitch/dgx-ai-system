# Aurum NAS 분석 저장 구조 정리

작성일: 2026-06-14

## 배경

아우룸 맥북은 평소 회사 네트워크에 있고, 주말이나 출장 시에는 우리집 또는 외부 네트워크에 있다. 아톰 서버는 회사 네트워크에 있으며, 회사 NAS는 아톰 서버에서 `/mnt/dgxbackup`으로 마운트된다. 외부에서는 Tailscale을 통해 아우룸 맥북, 아톰 서버, NAS에 접근한다.

초기 목적은 NAS 원본 데이터와 AI 정리 산출물을 아톰 서버 로컬 디스크에 계속 누적하지 않고 NAS에 저장하는 것이다. 따라서 아톰 서버의 로컬 워크스페이스는 장기 정본 저장소가 아니라 처리 실행 환경과 검색 캐시로만 사용해야 한다.

## 권장 원칙

1. 원본 데이터 정본은 NAS에 둔다.
2. AI 정리 산출물 정본도 NAS에 둔다.
3. 아톰 서버에는 빠른 RAG 검색을 위한 FAISS 로컬 캐시만 둔다.
4. 아우룸 맥북은 분석 결과를 복사받는 방식이 아니라 회사 LAN 또는 Tailscale/SMB로 NAS 또는 아톰 공유를 열람한다.
5. 같은 산출물이 `002. 회사 NAS 분석/data`와 `/home/caiser77/dgx_workspace/data`에 나뉘어 쌓이지 않도록 신규 파이프라인 경로를 통일한다.

## 최종 구조

```text
NAS 신규 투입함: /mnt/dgxbackup/_AURUM_AI_INBOX

NAS 정리 산출물: /mnt/dgxbackup/_AURUM_AI_PROCESSED
├── processed/
│   ├── text/
│   ├── tables/
│   ├── metadata/
│   ├── obsidian_notes/
│   └── state.json
└── logs/

아톰 로컬 캐시: /home/caiser77/dgx_workspace/cache/faiss_current
├── index.faiss
└── mapping.json
```

## 역할 분담

### NAS

- 대용량 원본 파일 저장
- AI 추출 텍스트, 표, 메타데이터, Obsidian 노트 저장
- 장기 보존 대상

### 아톰 서버

- Watchdog 실시간 감시 실행: `/mnt/dgxbackup/_AURUM_AI_INBOX` 전용
- 장기 배치 실행: `/mnt/dgxbackup` 전체를 cron으로 처리
- OCR, Hermes, vLLM, 임베딩 처리
- RAG 질의용 FAISS 인덱스 캐시 유지

### 아우룸 맥북

- 평소 회사에서는 회사 LAN/SMB로 NAS 또는 아톰 공유를 열람
- 주말/출장/외부에서는 Tailscale 경로로 동일 산출물을 열람
- 텔레그램 피드백으로 에르메스 분류 규칙 교정

## 맥북 접속 방식

맥북 위치에 따라 접속 IP는 달라질 수 있으나, 맥북 안의 마운트 지점은 하나로 맞추는 것이 좋다.

```text
맥북 공통 마운트 지점: ~/AURUM_NAS_AI

회사 내부: 회사 LAN SMB 주소로 NAS 또는 아톰 공유 마운트
외부/우리집: Tailscale SMB 주소로 NAS 또는 아톰 공유 마운트
```

이렇게 하면 Obsidian Vault와 파일 링크가 네트워크 위치 변화에 덜 흔들린다.

## 적용 경로

신규 Watchdog 투입 경로:

```text
/mnt/dgxbackup/_AURUM_AI_INBOX
```

신규 Watchdog 및 장기 배치 산출물:

```text
/mnt/dgxbackup/_AURUM_AI_PROCESSED/processed
```

신규 RAG 인덱스 캐시:

```text
/home/caiser77/dgx_workspace/cache/faiss_current
```

텔레그램 RAG 봇은 위 로컬 캐시를 조회한다. 이 캐시는 NAS 정리본을 기반으로 재생성할 수 있으므로 장애 시 삭제 후 재빌드해도 된다.

## 운영상 주의

- `/home/caiser77/dgx_workspace/002. 회사 NAS 분석/data`와 `/home/caiser77/dgx_workspace/data`는 기존 산출물 보존 영역으로만 취급한다.
- 신규 자동 처리의 정본 산출물은 NAS `_AURUM_AI_PROCESSED` 아래에 저장한다.
- FAISS 인덱스는 조회 성능 때문에 아톰 로컬 캐시를 사용한다.
- 맥북으로 분석 결과를 별도 복사하지 않는다. 맥북은 NAS/아톰 공유를 원격 열람한다.
- NAS 전체를 recursive Watchdog로 감시하면 초기 등록 단계에서 I/O 대기가 발생하므로 사용하지 않는다. 신규 파일을 즉시 처리해야 하면 `_AURUM_AI_INBOX`에 넣고, 기존 프로젝트 폴더 전체는 cron 배치가 처리한다.

## 2026-06-14 적용 결과

1. 기존 `002. 회사 NAS 분석/data/processed` 산출물을 NAS 정본 폴더로 병합했다.
2. 기존 `/home/caiser77/dgx_workspace/data/processed` 산출물을 NAS 정본 폴더로 병합했다.
3. 기존 FAISS 인덱스를 `/home/caiser77/dgx_workspace/cache/faiss_current`로 복사했다.
4. `cron_daily_pipeline.sh` 실행권한을 복구했고, crontab에는 매일 00:00 실행 항목이 있다.
5. Watchdog는 `/mnt/dgxbackup/_AURUM_AI_INBOX`만 감시하도록 재기동했다.
6. Watchdog 재부팅 자동시작을 위해 crontab에 `@reboot start_nas_watcher.sh` 항목을 추가했다.
7. `start_nas_watcher.sh`에는 PID 기반 중복 실행 방지 로직을 추가했다.
8. 텔레그램 피드백 봇 시작 스크립트 `004. 에르메스 NAS 분류기/scripts/start_telegram_feedback_bot.sh`를 만들었다. 이 스크립트는 `/home/caiser77/.hermes/.env`의 `TELEGRAM_BOT_TOKEN`과 `TELEGRAM_ALLOWED_USERS`를 읽어 실행한다.
9. 텔레그램 피드백 봇을 실행했고, 재부팅 자동시작을 위해 crontab에 `@reboot start_telegram_feedback_bot.sh` 항목을 추가했다.

## 후속 정리 후보

1. NAS 정본 폴더에 생긴 중첩 `processed/processed` 구조를 검토 후 정리
2. NAS 정본 기준으로 FAISS 캐시를 재빌드
3. 텔레그램 피드백 봇은 `/home/caiser77/.hermes/.env`의 `TELEGRAM_ALLOWED_USERS` 첫 번째 사용자 ID를 허용 사용자로 사용한다. 허용 사용자를 늘릴 때는 이 값을 쉼표 구분으로 관리한다.
4. 텔레그램 봇별 토큰/허용 사용자 키가 분리될 경우, 각 봇 시작 스크립트에서 명시적으로 어떤 env 키를 읽는지 고정한다.
