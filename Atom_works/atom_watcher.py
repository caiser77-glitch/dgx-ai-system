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