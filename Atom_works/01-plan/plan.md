# 📖 NAS 감시 RAG 시스템 구축 계획서 (PDCA Plan)

본 문서는 아우룸생태연구소의 사내 고성능 AI 서버(아톰)와 회사 NAS 간의 실시간 파일 생성 및 변경을 감지하고, 상태를 주기적으로 아카이빙하기 위한 **PDCA(Plan-Do-Check-Act) 마일스톤 기획 및 실행 상세 정의서**입니다. 

새로운 개발자나 후속 AI 에이전트가 본 프로젝트를 이어서 작업할 때 이 문서를 기준으로 모든 인프라를 이해하고 즉각 런칭할 수 있도록 수립되었습니다.

---

## 📅 1. Plan (계획 단계)

### 1.1. 목표 설정
*   **주요 목표:** NAS 감시 데몬을 통해 실시간 파일 생성 및 갱신을 감지하고, 정제 상태 및 세부 파일 메타데이터 정보를 지정된 상태 파일에 누적 기록하여 RAG 지식베이스 큐레이션을 자동화합니다.
*   **세부 마일스톤:**
    1.  **실시간 감시 대상 경로 지정:** `/mnt/nas2023old`, `/mnt/nas2024`, `/mnt/nas2025`, `/mnt/nas2026` (총 4개 공식 마운트 포인트)
    2.  **이벤트 수집:** 파일 감지 라이브러리(`watchdog`)를 활용한 실시간 이벤트 리스너 구동.
    3.  **상태 기록 자동화:** 파일이 감지될 때마다 메타데이터를 수집하여 `/home/caiser77/dgx_workspace/Atom_works/.pdca-status.json` 파일에 영구 기록.
    4.  **정기 보고 자동화:** 1시간 주기로 크론탭(Cron) 작업을 수행하여 감시 및 분석 결과물을 포맷하여 보고.
    5.  **데몬화(Service):** 리눅스 `systemd` 서비스(`atom-watcher.service`)로 등록하여 백그라운드에서 상시 무중단 구동 보장.

### 1.2. 필요한 시스템 리소스
*   **스크립트 파일:**
    *   `atom_watcher.py`: 실시간 파일 시스템 이벤트를 수신하는 감시 데몬 핵심 스크립트.
    *   `check_status.py`: 정기적으로 상태 파일(`.pdca-status.json`)을 열어 파일 정보를 분석해 콘솔에 보고하는 헬스체크 스크립트.
*   **시스템 설정:**
    *   `/etc/systemd/system/atom-watcher.service`: 데몬 관리를 위한 systemd 설정 파일.
    *   `crontab`: 사용자 정기 스케줄링.
*   **파이썬 의존성 환경:**
    *   에르메스 전용 가상환경의 파이썬 인터프리터 (`/home/caiser77/hermes-agent/venv/bin/python3`) 사용 (전역 pip 패키지 충돌 예방).

---

## 🛠️ 2. Do (실행 및 이식 단계)

### 2.1. 감시 데몬 스크립트 (`atom_watcher.py`)
*   **위치:** `/home/caiser77/dgx_workspace/Atom_works/atom_watcher.py`
*   **기능:** `watchdog` 라이브러리를 이용하여 지정된 NAS 경로의 파일 생성을 비동기로 감지하며, 덮어쓰기 방지 예외 처리가 반영된 JSON 데이터 누적 기능을 제공합니다.

```python
#!/usr/bin/env python3
import os
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NASWatcher(FileSystemEventHandler):
    def __init__(self, paths):
        super().__init__()
        self.paths = paths
        self.status_file = '/home/caiser77/dgx_workspace/Atom_works/.pdca-status.json'
        
        # 기존 기록 불러오기 (기존 기록 덮어쓰기 유실 방지)
        if os.path.exists(self.status_file):
            try:
                with open(self.status_file, 'r') as f:
                    self.status = json.load(f)
            except Exception:
                self.status = {}
        else:
            self.status = {}

    def on_created(self, event):
        if event.is_directory:
            print(f'Directory created: {event.src_path}')
        else:
            print(f'File created: {event.src_path}')
            self.analyze_file(event.src_path)

    def analyze_file(self, file_path):
        try:
            file_info = {
                'path': file_path,
                'type': 'file',
                'size': os.path.getsize(file_path),
                'created': os.path.getctime(file_path)
            }
            self.update_status(file_info)
        except Exception as e:
            print(f"Error analyzing file {file_path}: {e}")

    def update_status(self, file_info):
        self.status[file_info['path']] = file_info
        os.makedirs(os.path.dirname(self.status_file), exist_ok=True)
        with open(self.status_file, 'w') as f:
            json.dump(self.status, f, indent=4)

def main():
    paths = ['/mnt/nas2023old', '/mnt/nas2024', '/mnt/nas2025', '/mnt/nas2026']
    event_handler = NASWatcher(paths)
    observer = Observer()
    for path in paths:
        if os.path.exists(path):
            observer.schedule(event_handler, path, recursive=True)
            print(f"Started watching: {path}")
        else:
            print(f"Warning: path not found, skipped: {path}")
            
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()
```

### 2.2. 상태 보고 스크립트 (`check_status.py`)
*   **위치:** `/home/caiser77/dgx_workspace/Atom_works/check_status.py`
*   **기능:** 수집된 파일들을 정규 검사합니다. 프로젝트 메타데이터 문자열 키가 섞여 있어도 정상 파싱하도록 타입 가드(`isinstance`) 처리가 적용된 크래시 프리 버전입니다.

```python
#!/usr/bin/env python3
import json
import os
import time

status_file = '/home/caiser77/dgx_workspace/Atom_works/.pdca-status.json'

def check_status():
    if not os.path.exists(status_file):
        print("Status file not found.")
        return

    try:
        with open(status_file, 'r') as f:
            status = json.load(f)
    except Exception as e:
        print(f"Error reading status file: {e}")
        return

    if not status:
        print("No files have been analyzed yet.")
        return

    for file_path, file_info in status.items():
        # 파일 정보 딕셔너리가 아닌 메타데이터 키는 건너뜁니다 (TypeError 크래시 방지)
        if not isinstance(file_info, dict):
            continue
        print(f"File: {file_path}")
        print(f"Type: {file_info.get('type', 'unknown')}")
        print(f"Size: {file_info.get('size', 0)} bytes")
        print(f"Created: {time.ctime(file_info.get('created', time.time()))}")
        print()

if __name__ == '__main__':
    check_status()
```

### 2.3. Systemd 서비스 구성 (`atom-watcher.service`)
*   **위치:** `/etc/systemd/system/atom-watcher.service`
*   **기능:** 데몬이 뻗어도 영구 복구(`Restart=always`)하고 가상환경 파이썬을 타겟팅합니다.

```ini
[Unit]
Description=Atom Watcher Service
After=network.target

[Service]
User=caiser77
# 에르메스 venv 내의 파이썬으로 가동하여 모듈 누락 방지
ExecStart=/home/caiser77/hermes-agent/venv/bin/python3 /home/caiser77/dgx_workspace/Atom_works/atom_watcher.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### 2.4. 서비스 및 스케줄 런칭 가이드
터미널에서 아래 명령어를 순서대로 실행하여 전체 인프라를 활성화합니다.
```bash
# 1. 스크립트 실행 권한 부여
chmod +x /home/caiser77/dgx_workspace/Atom_works/atom_watcher.py /home/caiser77/dgx_workspace/Atom_works/check_status.py

# 2. 서비스 데몬 리로드 및 구동
sudo systemctl daemon-reload
sudo systemctl enable atom-watcher
sudo systemctl restart atom-watcher
sudo systemctl status atom-watcher

# 3. 1시간 정기 크론(Cron) 스케줄 추가 등록 (중복 제거 포함)
(crontab -l 2>/dev/null | grep -v 'check_status.py'; echo "0 * * * * /home/caiser77/hermes-agent/venv/bin/python3 /home/caiser77/dgx_workspace/Atom_works/check_status.py") | crontab -
```

---

## 📊 3. Check (검증 단계)

*   **상태 파일 모니터링:** `.pdca-status.json` 파일의 감시 기록을 열어 신규 감지된 파일들이 정확하게 누적되고 있는지 확인합니다.
*   **수동 리포트 검사:** `python3 check_status.py`를 수동 구동하여 정상적으로 파싱된 감지 텍스트가 뿌려지는지 확인합니다.
*   **시스템 로그 감사:** `sudo journalctl -u atom-watcher -f` 명령어로 watchdog 감시자가 뿜어내는 파일 탐지 로그를 실시간 관찰합니다.

---

## 🔄 4. Act (개선 및 조치 단계)

*   **성능 최적화:** 감시 대상인 NAS의 파일 용량이 수십 TB 수준이므로, 향후 성능 정체가 발생할 시 watchdog 감시 대상 서브디렉토리를 화이트리스트 기반으로 필터링하는 파싱 로직을 추가 반영합니다.
*   **계획서 지속 갱신:** 감시 대상 경로의 추가/제거 등의 하드웨어적인 토폴로지 변경 시 본 계획서 문서(`plan.md`)를 즉각 업데이트하여 에이전트 간의 설정 싱크를 유지합니다.