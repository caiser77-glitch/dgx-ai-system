# Atom 워크스페이스 Obsidian Vault 설정 기록

## 목표

아톰 서버의 `/home/caiser77/dgx_workspace` 워크스페이스를 Mac에 마운트하고, 해당 경로를 Obsidian Vault로 사용한다.

## 경로

- 아톰 SSH 대상: `caiser77@192.168.219.100:/home/caiser77/dgx_workspace`
- Mac 마운트 위치: `~/Obsidian/atom-workspace`
- Obsidian Vault 경로: `~/Obsidian/atom-workspace`

## 현재 상태

- Mac에는 `sshfs`가 이미 설치되어 있다.
- SSHFS 마운트를 위해 남은 의존성은 macFUSE 설치 및 macOS 보안 승인이다.
- 이전 오류는 명령어 줄바꿈 때문에 `-o` 옵션이 별도 명령처럼 실행된 것이 원인이었다.
- macFUSE 보안 승인을 완료한 뒤에는 Mac을 시스템 종료하거나 재시동해야 정상 적용될 수 있다.

## macFUSE 설치

이번 설정 과정에서 확인한 macFUSE 릴리스는 `macFUSE 5.2.0`이다.

공식 다운로드 URL:

```text
https://github.com/macfuse/macfuse/releases/download/macfuse-5.2.0/macfuse-5.2.0.dmg
```

Mac 터미널에서 다운로드 후 열기:

```bash
curl -L -o "$HOME/Downloads/macfuse-5.2.0.dmg" "https://github.com/macfuse/macfuse/releases/download/macfuse-5.2.0/macfuse-5.2.0.dmg"
open "$HOME/Downloads/macfuse-5.2.0.dmg"
```

열린 디스크 이미지에서 설치 패키지를 실행한다.

macOS가 보안 승인을 요구하면 다음 순서로 처리한다.

1. 시스템 설정을 연다.
2. 개인정보 보호 및 보안으로 이동한다.
3. macFUSE 또는 시스템 확장 로드를 허용한다.
4. macOS가 요구하면 Mac을 시스템 종료하거나 재시동한다.

## 재시동 후 마운트 명령

Mac 터미널에서 아래 명령을 실행한다. `sshfs` 명령은 줄바꿈 없이 한 줄로 실행해야 한다.

```bash
mkdir -p "$HOME/Obsidian/atom-workspace"
sshfs "caiser77@192.168.219.100:/home/caiser77/dgx_workspace" "$HOME/Obsidian/atom-workspace"
ls "$HOME/Obsidian/atom-workspace"
```

`ls` 명령에서 워크스페이스 파일 목록이 보이면 Obsidian에서 아래 경로를 Vault로 연다.

```text
~/Obsidian/atom-workspace
```

## 마운트가 이미 되어 있거나 꼬였을 때

먼저 언마운트한다.

```bash
umount "$HOME/Obsidian/atom-workspace"
```

그다음 `sshfs` 명령을 다시 실행한다.

```bash
sshfs "caiser77@192.168.219.100:/home/caiser77/dgx_workspace" "$HOME/Obsidian/atom-workspace"
```

## Windows 사용자 설정 가이드

Windows 사용자도 `WinFSP`와 `SSHFS-Win` 프로그램을 설치하여 아톰 서버의 워크스페이스 폴더를 네트워크 드라이브(예: `X:`)로 마운트한 뒤 Obsidian으로 열 수 있습니다.

### 1. 필수 프로그램 설치
아래 프로그램들을 다운로드하여 기본 옵션으로 설치합니다.
1. **WinFSP (Windows File System Proxy)**:
   - [WinFSP 공식 다운로드](https://winfsp.dev/)
2. **SSHFS-Win**:
   - [SSHFS-Win 공식 다운로드 (GitHub Releases)](https://github.com/winfsp/sshfs-win/releases)

### 2. SSH 키 설정 (SSH 키 인증 사용 시)
비밀번호가 아닌 SSH 개인 키 파일로 연동하려면 아래 작업을 미리 수행해야 합니다.
1. 사용자 홈 디렉토리 하위의 `.ssh` 폴더(`C:\Users\<사용자이름>\.ssh\`)에 개인 키 파일(예: `id_ed25519_gigabyte_atom`)을 저장합니다.
   * *참고: 패스프레이즈(Passphrase)가 설정되지 않은 비밀번호 없는 OpenSSH 키 규격만 직접 로드할 수 있습니다.*
2. 여러 개의 키를 사용하거나 파일명이 다를 경우 `C:\Users\<사용자이름>\.ssh\config` 파일을 텍스트 에디터로 열어 아래와 같이 호스트 에일리어스를 구성합니다.
   ```text
   Host gigabyte-atom
     HostName 192.168.219.100
     User caiser77
     IdentityFile C:\Users\<사용자이름>\.ssh\id_ed25519_gigabyte_atom
     Port 22
   ```

### 3. 드라이브 마운트 실행
Windows 명령 프롬프트(cmd) 또는 PowerShell을 실행하여 다음 명령어를 입력합니다.

* **비밀번호 인증으로 연결 시**:
  ```cmd
  net use X: \\sshfs\caiser77@192.168.219.100\home\caiser77\dgx_workspace
  ```
  *(비밀번호를 입력하라는 프롬프트가 뜨면 패스워드를 입력합니다.)*

* **SSH 키 인증으로 연결 시 (`\\sshfs.kr\` 접두사 사용)**:
  ```cmd
  net use X: \\sshfs.kr\caiser77@192.168.219.100\home\caiser77\dgx_workspace
  ```
  * `.ssh/config` 설정을 이용해 별칭으로 마운트할 때:
    ```cmd
    net use X: \\sshfs.kr\gigabyte-atom\home\caiser77\dgx_workspace
    ```

### 4. 마운트 해제 및 관리
* **마운트 해제**:
  ```cmd
  net use X: /delete
  ```
* **연결된 전체 드라이브 목록 확인**:
  ```cmd
  net use
  ```

### 5. Obsidian에서 열기
1. Obsidian 앱을 실행합니다.
2. 왼쪽 아래의 **[보관소 열기 (Open folder as vault)]**를 선택합니다.
3. 내 PC에서 새로 마운트된 **`X:` 드라이브**를 선택하여 열어줍니다.

## 참고

- 현재 어시스턴트 세션은 Mac이 아니라 Linux 환경에서 실행 중이므로, 여기서 macFUSE를 직접 설치할 수는 없었다.
- macFUSE는 macOS 보안 설정과 사용자 승인이 필요하므로 Mac에서 직접 설치 및 승인해야 한다.
- 확인에 사용한 공식 참고 자료:
  - `https://github.com/macfuse/macfuse/releases`
  - `https://github.com/macfuse/macfuse/wiki/Getting-Started`
  - `https://macfuse.github.io/2026/04/09/macfuse-5.2.0.html`
