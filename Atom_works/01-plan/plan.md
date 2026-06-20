# NAS 감시 시스템 계획

## 1. Plan (계획)

### 1.1. 목표 설정
- 주요 목표: NAS 감시 스크립트와 상태 확인 스크립트를 통해 파일 생성 및 변경을 감지하고, 이를 로그로 기록하여 RAG 지식베이스 구축을 효율적으로 수행한다.
- 세부 목표:
  - NAS 디렉토리 (/mnt/nas2023old, /mnt/nas2024, /mnt/nas2025, /mnt/nas2026)를 실시간으로 감시한다.
  - 파일 생성 및 변경 이벤트를 로그 파일 (/home/caiser77/dgx_workspace/Atom_works/.pdca-status.json)에 기록한다.
  - 1시간마다 상태를 확인하고 로그를 기록하는 Cron 작업을 등록한다.
  - atom-watcher 서비스를 실행하여 감시 스크립트가 무중단으로 상시 백그라운드 구동되도록 한다.

### 1.2. 필요한 리소스
- 스크립트:
  - atom_watcher.py: watchdog을 활용한 NAS 디렉토리 비동기 실시간 감시 스크립트
  - check_status.py: 상태 데이터의 정규 검증 및 리포팅 스크립트 (Type Guard 적용)
- 서비스 파일:
  - /etc/systemd/system/atom-watcher.service: 에르메스 가상환경 venv 파이썬으로 안전 구동하는 systemd 데몬 파일
- Cron 작업:
  - 1시간 주기 check_status.py 구동 cron 스케줄

### 1.3. 계획 단계 문서화
- 문서 위치: /home/caiser77/dgx_workspace/Atom_works/01-plan/plan.md
- 문서 내용:
  1. 목표
    - NAS 디렉토리 (/mnt/nas2023old, /mnt/nas2024, /mnt/nas2025, /mnt/nas2026)를 실시간으로 감시한다.
    - 파일 생성 및 변경 이벤트를 로그 파일 (.pdca-status.json)에 누적 기록한다.
    - 1시간마다 상태를 확인하는 Cron 작업을 등록한다.
    - atom-watcher 서비스를 가동하여 감시 스크립트가 계속 실행되도록 한다.
  2. 필요한 리소스
    - 스크립트 (atom_watcher.py, check_status.py)
    - 서비스 파일 (atom-watcher.service)
    - Cron 작업 등록 (1시간 주기)

## 2. Do (실행)

### 2.1. 감시 스크립트 생성
- 파일 위치: /home/caiser77/dgx_workspace/Atom_works/atom_watcher.py
- 파일 내용:
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
          
          # 기존 기록 불러오기 (덮어쓰기 방지)
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

### 2.2. 상태 확인 스크립트 생성
- 파일 위치: /home/caiser77/dgx_workspace/Atom_works/check_status.py
- 파일 내용:
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

### 2.3. systemd 서비스 파일 생성
- 파일 위치: /etc/systemd/system/atom-watcher.service
- 파일 내용:
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

### 2.4. 서비스 시작 및 활성화
- 명령어:
  ```bash
  sudo systemctl daemon-reload
  sudo systemctl enable atom-watcher
  sudo systemctl start atom-watcher
  sudo systemctl status atom-watcher
  ```

### 2.5. Cron 작업 등록
- 명령어:
  ```bash
  (crontab -l 2>/dev/null | grep -v 'check_status.py'; echo "0 * * * * /home/caiser77/hermes-agent/venv/bin/python3 /home/caiser77/dgx_workspace/Atom_works/check_status.py") | crontab -
  ```

## 3. Check (확인)
- 로그 확인:
  - .pdca-status.json 파일을 주기적으로 확인하여 감시 결과를 검증한다.
  - check_status.py 스크립트의 출력을 확인하여 정상적으로 우회 필터링 및 조회가 되는지 검증한다.
- 시스템 상태 확인:
  - systemctl status atom-watcher 명령어를 사용하여 서비스가 active (running) 상태인지 검증한다.

## 4. Act (조치)
- 개선 사항 적용:
  - 감시 스크립트와 상태 확인 스크립트의 안정성을 최적화한다.
  - 파일 검출 시 예외 상황(파일 잠금 등)에 대한 복구 메커니즘을 튜닝한다.
- 문서 업데이트:
  - 기획서 문서(plan.md)를 상시 갱신하고 버전 관리를 실시한다.
