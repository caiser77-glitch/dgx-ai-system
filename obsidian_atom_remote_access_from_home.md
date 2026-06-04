# 🏠 집(외부)에서 사무실 Mac 및 아톰(Atom) 서버 원격 접속 가이드

이 문서는 외부(집)에서 별도의 하드웨어 VPN 장비나 공유기 포트포워딩 설정 없이, **Tailscale** 보안 가상 네트워크망을 활용하여 사무실의 Mac 클라이언트 및 고성능 AI 서버 아톰(Atom)에 안전하게 접속하는 방법을 설명합니다.

---

## 1. 핵심 개념 (Tailscale)

* **Tailscale**은 회사 방화벽이나 공유기 설정을 변경할 필요 없이, 로그인만으로 각 기기(집 컴퓨터, 사무실 Mac, 아톰 서버)를 암호화된 가상의 하나의 사설 네트워크망(`100.xxx.xxx.xxx` 대역)으로 묶어주는 무료 가상 네트워크 서비스입니다.
* 외부 노출 포트가 없으므로 보안성이 매우 뛰어나며, 인터넷만 연결되어 있으면 세계 어디서든 사무실 내부망처럼 통신할 수 있습니다.

---

## 2. 현재 네트워크 정보

* **아톰(Atom) 서버 Tailscale IP**: **`100.98.149.128`** (이미 서버 내 설치 및 기동 완료)
* **아톰 SSH 사용자 계정**: `caiser77`

---

## 3. 원격 접속 세팅 순서

### 1단계: 각 기기에 Tailscale 설치 및 로그인
1. **집 컴퓨터 (Mac 또는 Windows)**와 **사무실 Mac**에 각각 Tailscale 앱을 설치합니다.
   * **Mac**: [Mac App Store에서 Tailscale 설치](https://apps.apple.com/kr/app/tailscale/id1475387162)
   * **Windows**: [Tailscale 공식 다운로드 페이지](https://tailscale.com/download/windows)
2. 앱 실행 후 **아톰 서버에 등록된 것과 동일한 계정**(Google, Microsoft 등)으로 로그인합니다.
3. 모든 기기가 로그인 완료되면 Tailscale 가상 네트워크망에 서로 연결됩니다.

### 2단계: 사무실 Mac의 외부 접속 허용 (선택 사항)
집에서 아톰 서버뿐만 아니라 **사무실 Mac**에도 원격으로 SSH 접속하고 싶다면 아래 설정을 켜둡니다.
1. 사무실 Mac에서 **[시스템 설정 > 일반 > 공유]**로 이동합니다.
2. **원격 로그인 (Remote Login)** 옵션을 활성화(ON)합니다.

---

## 4. 기기별 실제 접속 방법

### A. 집 ➡️ 아톰(Atom) 서버 바로 접속하기
집 컴퓨터 터미널(또는 CMD/PowerShell)에서 아톰 서버의 Tailscale IP를 사용하여 접속합니다.

* **일반 SSH 접속 명령어**:
  ```bash
  ssh caiser77@100.98.149.128
  ```

* **SSH Config 구성 (권장)**:
  집 컴퓨터의 SSH 설정 파일(`~/.ssh/config` 또는 Windows의 `C:\Users\<사용자이름>\.ssh\config`)에 아래 내용을 추가해두면 간단하게 `ssh gigabyte-atom` 명령어로 바로 접속할 수 있습니다.
  ```sshconfig
  Host gigabyte-atom
    HostName 100.98.149.128
    User caiser77
    IdentityFile ~/.ssh/id_ed25519_gigabyte_atom
    IdentitiesOnly yes
  ```

### B. 집 ➡️ 사무실 Mac 접속하기
1. 집 컴퓨터의 Tailscale 트레이 아이콘이나 관리 콘솔에서 **사무실 Mac의 Tailscale IP**(예: `100.11.22.33`)를 확인합니다.
2. 집 컴퓨터 터미널에서 사무실 Mac의 계정명을 사용해 접속합니다:
  ```bash
  ssh <사무실_맥_계정명>@<사무실_맥_Tailscale_IP>
  ```

---

## 5. 연결 확인 및 문제 해결

* **연결 상태 점검 (Ping 테스트)**:
  집 컴퓨터 터미널에서 아래 명령을 실행해 응답이 오는지 확인합니다.
  ```bash
  ping 100.98.149.128
  ```
* **마운트 연동**:
  집 Mac에서도 동일하게 아래 명령어로 아톰 서버의 워크스페이스를 로컬에 마운트하여 옵시디언으로 열어볼 수 있습니다.
  ```bash
  mkdir -p ~/Obsidian/atom-workspace
  sshfs gigabyte-atom:/home/caiser77/dgx_workspace ~/Obsidian/atom-workspace -o local,allow_other,reconnect,defer_permissions
  ```
