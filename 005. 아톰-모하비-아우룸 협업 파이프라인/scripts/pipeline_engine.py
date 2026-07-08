import os
import json
import time
import logging
import shutil
import re
import unicodedata
from datetime import datetime

READY_STATUSES = {"raw_analyzed", "completed"}

class NFCGuard:
    """macOS(NFD)와 Linux/Windows(NFC) 간의 한글 깨짐을 방지하기 위한 유틸리티."""
    @staticmethod
    def normalize(path: str) -> str:
        if not isinstance(path, str):
            return path
        return unicodedata.normalize('NFC', path)

class StageManager:
    """작업 단계를 물리적 폴더 이동으로 관리하는 매니저."""
    def __init__(self, base_dir: str):
        # 인코딩 안전을 위해 NFD/NFC 정규화 적용
        self.base_dir = os.path.abspath(NFCGuard.normalize(base_dir))
        self.stages = {
            "raw": os.path.join(self.base_dir, "01_raw_analyzed"),
            "drafting": os.path.join(self.base_dir, "02_drafting"),
            "review": os.path.join(self.base_dir, "03_review_pending"),
            "error": os.path.join(self.base_dir, "00_error_failed")
        }
        self._setup_directories()

    def _setup_directories(self):
        for stage in self.stages.values():
            os.makedirs(NFCGuard.normalize(stage), exist_ok=True)

    def get_stage_path(self, stage_name: str) -> str:
        return NFCGuard.normalize(self.stages[stage_name])

class PipelineEngine:
    """아톰의 데이터를 감시하고 Obsidian으로 배포하는 핵심 엔진."""
    def __init__(self, entry_point: str):
        entry_point = NFCGuard.normalize(entry_point)
        # 1. 스마트 생성자: JSON 설정 파일 혹은 디렉토리 경로 판별
        if entry_point.endswith(".json"):
            actual_config_path = os.path.abspath(entry_point)
            try:
                with open(actual_config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                self.watch_dir = NFCGuard.normalize(os.path.expanduser(config['paths']['watch_dir']))
                self.dest_dir = NFCGuard.normalize(os.path.expanduser(config['paths'].get('dest_dir', '')))
                self.poll_interval = config['settings'].get('poll_interval', 2)
                self.max_retries = config['settings'].get('max_retry_attempts', 3)
            except Exception as e:
                raise RuntimeError(f"설정 파일 파싱 실패 ({actual_config_path}): {e}")
        else:
            # 설정 파일이 없을 경우의 Fallback 경로
            self.watch_dir = NFCGuard.normalize(os.path.abspath(entry_point))
            self.dest_dir = "" # 명시적 주입 필요
            self.poll_interval = 2
            self.max_retries = 3

        # 2. 스테이지 매니저 초기화 (watch_dir의 상위 경로를 기준으로 설정)
        self.stages = StageManager(os.path.dirname(self.watch_dir))
        self.processed_jobs = set()

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger("PipelineEngine")

    def _handle_error(self, job_id: str, files_to_isolate: list):
        """DLQ (Dead Letter Queue) 로직: 에러 발생 시 파일을 에러 스테이지로 격리."""
        error_dir = self.stages.get_stage_path("error")
        self.logger.error(f"!!! [{job_id}] 치명적 오류 감지 - 데이터 격리 수행 ({error_dir})")
        for f_path in files_to_isolate:
            if os.path.exists(f_path):
                try:
                    shutil.move(f_path, os.path.join(error_dir, os.path.basename(f_path)))
                except Exception as e:
                    self.logger.error(f"[{job_id}] 격리 이동 중 에러 발생: {e}")

    def parse_status(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            match = re.search(r'status:\s*["\']?(\w+)["\']?', content)
            return match.group(1) if match else "unknown"
        except Exception as e:
            self.logger.error(f"Status 파싱 오류 ({os.path.basename(file_path)}): {e}")
            return "unknown"

    def _generate_markdown(self, data: dict, job_id: str) -> str:
        metadata = data.get('metadata', {})
        payload = data.get('payload', {})
        content = (
            "---\n"
            "status: drafting\n"
            "assigned_agent: Mohave\n"
            f"job_id: \"{metadata.get('job_id', job_id)}\"\n"
            f"last_updated: \"{datetime.now().isoformat(timespec='seconds')}\"\n"
            "---\n\n"
        )
        content += f"# [DRAFT] 생태 조사 결과 보고서 ({job_id})\n\n"
        content += f"## 1. 기초 정보\n- 작업 ID: {metadata.get('job_id', job_id)}\n- 생성 시각: {metadata.get('timestamp', '')}\n\n"
        content += "## 2. 주요 정밀 지표 (Metrics)\n"
        for k, v in payload.get('metrics', {}).items():
            name = k.replace("_", " ").title()
            content += f"- {name}: {v}\n"
        content += "\n## 3. 공간적 관측 데이터\n"
        for obs in payload.get('spatial_observations', []):
            content += f"- 위치: ({obs['lat']}, {obs['lon']}) | 개체수: {obs['count']} | 비고: {obs.get('note', '')}\n"
        return content

    def process_job(self, summary_filename: str):
        job_id = summary_filename.replace(".summary.md", "")
        full_summary_path = os.path.join(self.watch_dir, summary_filename)
        # 에러 역추적을 위한 추적 리스트 초기화
        current_files_to_track = []

        try:
            status = self.parse_status(full_summary_path)
            if status not in READY_STATUSES:
                return

            self.logger.info(f"[{job_id}] 작업 감지 - 상태 확인 완료.")
            result_file = os.path.join(self.watch_dir, f"{job_id}.result.json")
            current_files_to_track.append(full_summary_path)

            # 1. 데이터 파일 존재 여부 및 재시도 체크 (Retry-after-delay)
            found_data = False
            for attempt in range(self.max_retries):
                if os.path.exists(result_file):
                    found_data = True
                    break
                self.logger.warning(f"[{job_id}] 결과 파일 대기 중... ({attempt+1}/{self.max_retries})")
                time.sleep(2)

            if not found_data:
                raise FileNotFoundError(f"{result_file} 파일을 찾을 수 없습니다.")

            current_files_to_track.append(result_file)

            # 2. 데이터 로딩 및 드래프트 생성
            with open(result_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            temp_draft_path = os.path.join(self.watch_dir, f"{job_id}.draft.md")
            with open(temp_draft_path, 'w', encoding='utf-8') as f:
                f.write(self._generate_markdown(data, job_id))
            current_files_to_track.append(temp_draft_path)

            # 3. Stage Transition (Hand-off to drafting)
            target_dir = self.stages.get_stage_path("drafting")
            self.logger.info(f"[{job_id}] 스테이지 전이 중: {os.path.basename(target_dir)}")

            for f_p in current_files_to_track:
                shutil.move(f_p, os.path.join(target_dir, os.path.basename(f_p)))

            self.logger.info(f"[{job_id}] 성공적으로 전이되었습니다.")
            self.processed_jobs.add(job_id)

        except Exception as e:
            self.logger.error(f"[{job_id}] 프로세스 오류 발생: {e}")
            self._handle_error(job_id, current_files_to_track)

    def start_monitoring(self):
        self.logger.info(f"엔진 가동 시작 (감시 경로: {self.watch_dir})")
        try:
            while True:
                for filename in os.listdir(self.watch_dir):
                    filename_nfc = NFCGuard.normalize(filename)
                    if filename_nfc.endswith(".summary.md"):
                        job_id = filename_nfc.replace(".summary.md", "")
                        if job_id not in self.processed_jobs:
                            self.process_job(filename_nfc)
                time.sleep(self.poll_interval)
        except KeyboardInterrupt:
            self.logger.info("운영자 요청에 의해 종료되었습니다.")

if __name__ == "__main__":
    import sys
    # 인자 전달 (config.json 우선 처리)
    ENTRY = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/AI_BASE/config.json")
    engine = PipelineEngine(ENTRY)
    engine.start_monitoring()
