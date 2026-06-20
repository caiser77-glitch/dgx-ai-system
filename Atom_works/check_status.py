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
        # 파일 정보 딕셔너리가 아닌 메타데이터 키는 건너뜁니다.
        if not isinstance(file_info, dict):
            continue
        print(f"File: {file_path}")
        print(f"Type: {file_info.get('type', 'unknown')}")
        print(f"Size: {file_info.get('size', 0)} bytes")
        print(f"Created: {time.ctime(file_info.get('created', time.time()))}")
        print()

if __name__ == '__main__':
    check_status()