# 🤖 코덱스 워크스페이스 지침 - 회사 NAS 분석 및 RAG 파이프라인 (Sub-project)

이 파일은 `002. 회사 NAS 분석` 서브 프로젝트를 담당하는 개발자 및 AI 에이전트를 위한 핵심 규칙과 운영 가이드를 담고 있습니다. 이 폴더 내에서 작업을 수행할 때 이 지침을 최우선으로 준수하십시오.

---

## 🔌 연동 인프라 환경 매핑 (Infrastructure Details)

* **아톰(Atom) 서버 IP**: **`100.98.149.127`** (Tailscale) / **`192.168.219.100`** (사무실 내부)
  - SSH 사용자 계정: `caiser77` (sudo 패스워드: `별도 보안 채널 보관`)
  - 로컬 가상환경 경로: `/home/caiser77/dgx_workspace/venv`
* **회사 NAS (Synology) IP**: **`100.94.64.83`** (Tailscale)
  - 삼바(SMB) 전용 계정: `aurum-rag` / 패스워드: `Aurum2026!!`
  - 마운트 대상 공유 폴더:
    - `00Project2023 이전` → `/mnt/nas2023old`
    - `24Project 2024` → `/mnt/nas2024`
    - `25Project 2025` → `/mnt/nas2025`
    - `26Project 2026` → `/mnt/nas2026`
* **마운트 세부 사항**:
  - 아톰 서버 내 공식 감시 마운트 경로: `/mnt/nas2023old`, `/mnt/nas2024`, `/mnt/nas2025`, `/mnt/nas2026`
  - 아톰 서버 크레덴셜 파일: `/home/caiser77/.smbcredentials_nas`
  - 자동 마운트 설정: `/etc/fstab`에 위 4개 SMB 공유 자동 연동 등록 완료
  - 이전 감시 경로 명칭은 신규 운영 설명이나 감시 대상으로 사용하지 않습니다.
* **운영 원칙**:
  - NAS 원본 파일은 DGX 로컬로 복사하지 않고, SMB 마운트 경로에서 직접 읽습니다.
  - DGX 로컬에는 로그, 상태파일, 색인, 메타데이터 등 작은 파생 데이터만 저장합니다.
  - 현재 공식 감시 데몬은 `atom-watcher` systemd 서비스이며, 이전 watchdog_pipeline 직접 감시 방식은 사용하지 않습니다.

---

## 🛠️ 빌드, 실행 및 검증 명령어 (Operation Command Line)

### 1. 실시간 감시 데몬 기동 및 프로세스 체크
아톰 서버 내부에서 NAS 폴더 감시 데몬을 systemd 서비스로 실행하고 확인하는 명령입니다.
```bash
# 감시 서비스 재시작
sudo systemctl restart atom-watcher

# 감시 프로세스 생존 여부 확인
ps aux | grep -E 'atom-watcher|watcher.py' | grep -v grep

# 실시간 감시 로그 확인
tail -f /var/log/atom-watcher/atom-watcher.log
```

### 2. 파이프라인 수동 수집 및 색인(FAISS) 검증
* **텍스트 가공 추출**:
  ```bash
  ./venv/bin/python scripts/extract_data.py \
    --input "/mnt/nas2026/경로/파일명.xlsx" \
    --device-name "atom-watcher" \
    --output-dir "data/processed"
  ```
* **FAISS 지식베이스 인덱싱**:
  ```bash
  ./venv/bin/python scripts/index_documents.py \
    --processed-dir "data/processed" \
    --index-dir "data/indexes/faiss"
  ```

### 3. vLLM 72B API 연동 RAG 질의 처리
```bash
./venv/bin/python scripts/rag_query.py \
  --query "질문 내용 입력" \
  --index-dir "data/indexes/faiss" \
  --llm-endpoint "http://localhost:8088/v1/chat/completions" \
  --model "Qwen/Qwen2.5-72B-Instruct-AWQ"
```

---

## 📋 코딩 지침 및 주의사항 (Coding Rules)

1. **임베딩 모델 CPU 고정 (OOM 방지)**:
   * 아톰 서버의 GPU 메모리(VRAM)는 72B 대형 모델(`vllm-server` 컨테이너)이 90% 이상 점유하고 있습니다.
   * 따라서 [index_documents.py](file:///Volumes/caiser77/dgx_workspace/002. 회사 NAS 분서ך/scripts/index_documents.py) 등에서 `SentenceTransformer` 모델을 로드할 때는 반드시 **`device='cpu'`** 인자를 지정하여 GPU 메모리 충돌을 예방해야 합니다.
2. **한글 자모분리(NFC/NFD) 방지**:
   * macOS 사용자가 SMB/NAS에 업로드한 파일은 한글 자모가 분리(NFD 방식)되어 저장되어, 리눅스 파일시스템 단에서 파일 경로 접근 시 인식 오류가 빈번합니다.
   * 파일 및 디렉터리 경로를 수집하여 접근하는 로직 초입에서는 반드시 `unicodedata.normalize('NFC', path)` 처리를 거치도록 설계하십시오.
3. **임시 테스트 파일 잔여 금지**:
   * 네트워크 연동 검증이나 자격증명 브루트포스 테스트를 위해 생성된 임시 스크립트(예: `crack_nas_auth.py`, `list_nas_shares.py` 등)는 세션 종료 전에 즉각 삭제하여, 원격 및 로컬 워크스페이스에 불필요한 파일을 남겨두지 마십시오.
4. **결과물 언어**:
   * 본 프로젝트의 보고서 및 코드 내 주석, 최종 결과물 작성 언어는 **한국어**로 통일합니다.
