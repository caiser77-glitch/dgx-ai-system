# 집(외부)에서 아우룸 맥북 & 아톰 서버 원격 접속 가이드

이 문서는 외부(재택 등)에서 **Tailscale VPN**망을 거쳐 **아우룸 맥북** 및 **아톰 서버**에 안전하게 화면 공유(GUI) 및 IDE(VS Code/Cursor 등)로 접속하는 설정과 실행 방법을 다룹니다.

---

## 🌐 0. 대상 기기 정보 및 접속 요약

외부 기기(예: 재택용 개인 노트북/데스크톱)에 **Tailscale이 켜져 있는 상태**에서만 아래 접속이 유효합니다.

| 대상 장비 | 역할 / 환경 | Tailscale IP | 로그인 계정 (ID) |
| :--- | :--- | :--- | :--- |
| **아우룸 맥북** | 클라이언트 / macOS | `100.115.9.49` | `nams` |
| **아톰 서버** | AI 연산 서버 / Linux | `100.98.149.127` | `caiser77` |

---

## 🖥️ 1. 아우룸 맥북 (`100.115.9.49`) 원격 접속 방법

### ① 화면 공유 (GUI 제어)
맥북의 화면을 그대로 제어하고 싶을 때 사용합니다.
- **접속 방식:** macOS 기본 **화면 공유(Screen Sharing)** 앱
- **접속 주소:** `vnc://100.115.9.49`
- **로그인 ID / PW:** `nams` / 별도 보안 채널에 보관
- **사용 방법:**
  1. 재택 맥북의 터미널이나 Safari 주소창에 `open vnc://100.115.9.49`를 입력합니다.
  2. 로그인 이름에 `nams`, 비밀번호는 별도 보안 채널의 값을 입력합니다. (키체인 저장 시 다음부터 클릭 한 번으로 자동 진입)

### ② IDE (VS Code / Cursor) 원격 코딩 및 SSH 제어
맥북 내부의 파일 수정이나 터미널 제어 시 사용합니다.
- **터미널 접속:**
  ```bash
  ssh nams@100.115.9.49
  ```
- **IDE 접속 (VS Code):**
  재택 맥북의 터미널에서 다음 명령어를 실행하여 원격으로 VS Code를 실행합니다.
  ```bash
  code --remote ssh-remote+aurum-macbook
  ```
  *(비밀번호 없이 즉시 접속하기 위해 아래 3번 항목의 SSH 키 및 Config 설정을 재택 기기에 추가하시는 것을 권장합니다.)*

---

## 🏢 2. 아톰 서버 (`100.98.149.127`) 원격 접속 방법

### ① 화면 공유 (GUI 제어 - RDP)
우분투 데스크톱 화면을 그대로 보며 GUI 작업을 할 때 사용합니다.
- **접속 방식:** RDP (원격 데스크톱)
- **접속 주소:** `100.98.149.127:3389`
- **로그인 ID / PW:** `caiser77` / 별도 보안 채널에 보관
- **사용 방법:**
  1. Mac App Store에서 **Microsoft Remote Desktop** 앱을 다운로드 및 설치합니다.
  2. `PCs > Add PC`를 선택하여 PC name에 `100.98.149.127:3389`를 추가합니다.
  3. 등록된 PC를 더블클릭하여 아이디 `caiser77`와 별도 보안 채널의 암호를 입력해 접속합니다.

### ② IDE (VS Code / Cursor) 원격 코딩 및 SSH 제어
아톰 서버 내부의 dgx_workspace로 진입해 코딩하고 개발 환경을 사용할 때 사용합니다.
- **터미널 접속:**
  ```bash
  ssh caiser77@100.98.149.127
  ```
- **IDE 접속 (VS Code):**
  재택 맥북 터미널에서 아래 명령어로 VS Code를 실행하여 아톰 서버 워크스페이스에 즉시 진입합니다.
  ```bash
  code --remote ssh-remote+gigabyte-atom /home/caiser77/dgx_workspace
  ```

### ③ 웹 브라우저 서비스 직접 접속
아톰 서버에서 가동 중인 로컬 AI 관련 웹 서비스들을 집에서 바로 접속할 수 있습니다.
- **Open-WebUI (로컬 ChatGPT):** [http://100.98.149.127:3000](http://100.98.149.127:3000)
- **아우룸 Frontend (대시보드):** [http://100.98.149.127:5173](http://100.98.149.127:5173)
- **아우룸 UI (Gradio 화면):** [http://100.98.149.127:7861](http://100.98.149.127:7861)

---

## ⚙️ 3. [추천] 재택 PC 편의성 설정 (SSH Config)

집에서 사용하는 노트북/데스크톱의 터미널에서 비밀번호 입력 없이 `ssh aurum-macbook` 혹은 `ssh gigabyte-atom` 명령어로 1초 만에 진입할 수 있도록 설정하는 방법입니다.

### 1단계: SSH 개인키 파일 복사
현재 이 맥북의 `~/.ssh/id_ed25519_gigabyte_atom` (개인키) 파일을 집에서 사용하는 PC의 `~/.ssh/` 폴더 안으로 복사하여 붙여넣습니다.

### 2단계: 집 PC의 `~/.ssh/config` 설정 수정
집 PC의 `~/.ssh/config` 파일을 텍스트 편집기 등으로 열어 아래 블록을 추가해 줍니다.

```sshconfig
# 1. 아톰 AI 서버 연결 설정
Host gigabyte-atom
    HostName 100.98.149.127
    User caiser77
    IdentityFile ~/.ssh/id_ed25519_gigabyte_atom
    StrictHostKeyChecking no

# 2. 아우룸 맥북 연결 설정
Host aurum-macbook
    HostName 100.115.9.49
    User nams
    IdentityFile ~/.ssh/id_ed25519_gigabyte_atom
    StrictHostKeyChecking no
```

설정이 완료되면 집 PC의 터미널에서 다음 명령어로 비밀번호 없이 즉시 접속 및 작업이 가능합니다.
- `ssh aurum-macbook` (맥북 원격 접속)
- `ssh gigabyte-atom` (아톰 서버 원격 접속)
