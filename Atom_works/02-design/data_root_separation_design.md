# 데이터 루트 분리 설계안

작성일: 2026-07-09

## 목적

코드 트리에는 소스, 설정, 문서만 남기고 대형 생성물과 런타임 산출물은 별도 데이터 루트로 분리한다. VSCode 파일 감시, Git 상태, 백업 범위를 안정화하고, 대량 NAS 처리 중 재색인과 파일 탐색 부하를 낮추는 것이 목표다.

## 현재 확인된 문제

- `watchdog_pipeline.py --auto-index --index-mode immediate` 구형 프로세스가 새 파일 처리 뒤 전체 FAISS 색인을 즉시 재실행하면서 CPU 부하를 크게 올렸다.
- `Fauna_Workspace/System_Engine/Legacy_Pipelines/03_Processed_Data/Papers_Markdown/` 아래에 50MB 초과 Markdown 생성물이 존재한다.
- 기존 `.gitignore`는 `Vector_DB`와 일부 `data/processed`, `data/indexes`를 제외하지만, Legacy `Papers_Markdown` 같은 대형 변환 산출물까지는 포괄하지 못했다.

## 권장 루트

- 코드 루트: `/home/caiser77/dgx_workspace`
- 로컬 런타임 루트: `/home/caiser77/dgx_runtime`
- NAS 파생 데이터 루트: `/mnt/dgxbackup/_AURUM_AI_PROCESSED`
- 임시 작업 루트: `/tmp/aurum_pipeline`

## 디렉터리 매핑

| 데이터 종류 | 현재 예시 | 권장 위치 |
| --- | --- | --- |
| 추출 Markdown | `**/03_Processed_Data/Papers_Markdown/` | `/home/caiser77/dgx_runtime/processed/markdown/` |
| 추출 이미지/첨부 | `**/03_Processed_Data/Images/`, `Attachments/` | `/home/caiser77/dgx_runtime/processed/assets/` |
| FAISS 색인 | `**/data/indexes/faiss/` | `/home/caiser77/dgx_runtime/indexes/faiss/` |
| 상태 DB/JSON | `**/data/processed/state.json` | `/home/caiser77/dgx_runtime/state/` |
| 로그 | `**/logs/` | `/home/caiser77/dgx_runtime/logs/` |

## 단계별 적용

1. 신규 생성물 차단
   - `.gitignore`에서 Legacy `Papers_Markdown`, `Images`, `Attachments`를 제외한다.
   - 감시 스크립트 기본 색인 모드는 `debounced`로 둔다.

2. 파이프라인 경로 변수화
   - `AURUM_DATA_ROOT=/home/caiser77/dgx_runtime`를 공통 기본값으로 둔다.
   - `processed_dir`, `index_dir`, `state_file`, `log_file`은 모두 이 루트 아래에서 파생한다.
   - 기존 CLI 인자는 유지해 수동 실행 호환성을 보존한다.

3. 기존 대형 파일 이관
   - Git 추적 중인 대형 생성물은 별도 커밋에서 `git rm --cached` 후 런타임 루트로 이동한다.
   - Markdown 내부 이미지가 실제 바이너리/비텍스트 바이트를 포함하는 파일은 원본 백업 후 링크 분리 스크립트로 처리한다.

4. 운영 전환
   - 공식 감시는 `atom-watcher` systemd 서비스만 사용한다.
   - 구형 `watchdog_pipeline.py --watch /mnt/dgxbackup --auto-index` 직접 실행 방식은 재기동하지 않는다.

## 검증 기준

- `git status --short`에 런타임 생성물이 나타나지 않는다.
- 신규 파일 유입 시 추출은 즉시 수행되지만 색인은 `debounced` 또는 `batch` 조건에서만 실행된다.
- VSCode 파일 감시 대상에 대형 산출물 디렉터리가 포함되지 않는다.
- 수동 색인은 별도 `index-dir`에서 검증한 뒤 운영 색인을 교체한다.

## 2026-07-09 적용 기록

- `Fauna_Workspace/System_Engine/Legacy_Pipelines/03_Processed_Data/Papers_Markdown/의왕_월암_삵_무인카메라_보고서.md` 계열 NFD 파일을 `/home/caiser77/dgx_runtime/processed/markdown/legacy/Fauna_Workspace/System_Engine/Legacy_Pipelines/03_Processed_Data/Papers_Markdown/` 아래로 이동했다.
- 이동 전후 SHA-256: `13d22f7064bec3e224c1c23594561bbc2bd3bf202935cf9460124c694c4bffc4`.
- 원래 Git 추적 대상이었으므로 `git rm --cached`로 인덱스에서 제거했다.
