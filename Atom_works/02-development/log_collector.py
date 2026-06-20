import os
import time
import requests

# 로그 파일 경로
LOG_FILE_PATH = '/mnt/nas2023old/logs/access.log'

# 분석 엔진 엔드포인트
ANALYSIS_ENGINE_ENDPOINT = 'http://localhost:5000/analyze'

def collect_logs():
    """로그 파일을 읽어서 최근 로그를 반환합니다."""
    with open(LOG_FILE_PATH, 'r') as file:
        lines = file.readlines()
        # 최근 100개 로그만 반환
        return lines[-100:]

def send_logs_to_engine(logs):
    """수집된 로그를 분석 엔진으로 전송합니다."""
    response = requests.post(ANALYSIS_ENGINE_ENDPOINT, json={'logs': logs})
    if response.status_code == 200:
        print("Logs sent successfully")
    else:
        print(f"Failed to send logs: {response.status_code}")

def main():
    while True:
        logs = collect_logs()
        send_logs_to_engine(logs)
        time.sleep(60)  # 1분마다 로그 수집

if __name__ == "__main__":
    main()