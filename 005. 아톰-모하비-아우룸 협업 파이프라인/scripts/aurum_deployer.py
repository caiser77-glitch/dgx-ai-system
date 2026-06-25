import os
import json
import time
import logging
import shutil
import re
import unicodedata
import requests

class NFCGuard:
    """한글 자모분리(NFD) 방지를 위한 NFC 정규화 유틸리티."""
    @staticmethod
    def normalize(path: str) -> str:
        if not isinstance(path, str):
            return path
        return unicodedata.normalize('NFC', path)

class AurumDeployer:
    """3단계 아우룸(Aurum) 최종 배포 및 텔레그램 알림 제어 엔진."""
    def __init__(self, watch_dir: str, publish_dir: str, telegram_token: str = None, chat_id: str = None):
        self.watch_dir = NFCGuard.normalize(os.path.abspath(watch_dir))
        self.publish_dir = NFCGuard.normalize(os.path.abspath(publish_dir))
        self.error_dir = NFCGuard.normalize(os.path.join(os.path.dirname(self.watch_dir), "00_error_failed"))
        self.published_stage_dir = NFCGuard.normalize(os.path.join(os.path.dirname(self.watch_dir), "04_published"))
        
        self.telegram_token = telegram_token
        self.chat_id = chat_id
        self.processed_jobs = set()

        # 폴더 초기화
        os.makedirs(self.published_stage_dir, exist_ok=True)
        os.makedirs(self.error_dir, exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger("AurumDeployer")

    def parse_metadata(self, file_path: str) -> dict:
        """마크다운 Frontmatter에서 메타데이터를 추출합니다."""
        meta = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Frontmatter 매칭
            fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if fm_match:
                fm_text = fm_match.group(1)
                for line in fm_text.split('\n'):
                    if ':' in line:
                        k, v = line.split(':', 1)
                        meta[k.strip()] = v.strip().strip('"').strip("'")
        except Exception as e:
            self.logger.error(f"메타데이터 파싱 실패 ({os.path.basename(file_path)}): {e}")
        return meta

    def send_telegram_notification(self, job_id: str, meta: dict):
        """텔레그램 채널로 검수 대기 알림을 전송합니다."""
        if not self.telegram_token or not self.chat_id:
            self.logger.info(f"[{job_id}] 텔레그램 설정이 누락되어 콘솔 로그로 대체합니다.")
            return

        message = (
            f"🔔 *[에르메스 검수 요청]*\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"• *작업 ID:* `{job_id}`\n"
            f"• *소속 용역:* `{meta.get('year_vendor', '알 수 없음')}`\n"
            f"• *프로젝트명:* `{meta.get('project_name', '알 수 없음')}`\n"
            f"• *대분류군:* `{meta.get('class_name', '알 수 없음')}`\n"
            f"• *상태:* `검수 대기중 (review_pending)`\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"👉 HWP 및 PDF 변환 준비 완료."
        )
        
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        
        try:
            res = requests.post(url, json=payload, timeout=5)
            if res.status_code == 200:
                self.logger.info(f"[{job_id}] 텔레그램 검수 알림 전송 완료.")
            else:
                self.logger.error(f"[{job_id}] 텔레그램 전송 실패: {res.text}")
        except Exception as e:
            self.logger.error(f"[{job_id}] 텔레그램 API 호출 실패: {e}")

    def convert_to_hwp_pdf(self, draft_path: str, job_id: str) -> bool:
        """[Placeholder] 실제 한글(HWP) 및 PDF 정식 규격 변환을 수행합니다."""
        self.logger.info(f"[{job_id}] 한글(HWP) 및 PDF 문서 변환을 시작합니다...")
        # TODO: 아우룸 OS 환경에 맞춰 변환 엔진(Pandoc, Weasyprint 또는 Windows HWP OLE) 연동
        time.sleep(2) # 변환 시간 시뮬레이션
        return True

    def process_review_pending(self, draft_filename: str):
        """review_pending 문서를 최종 검수 후 NAS 배포 및 published 스테이지로 아카이빙합니다."""
        job_id = draft_filename.replace(".draft.md", "")
        full_draft_path = NFCGuard.normalize(os.path.join(self.watch_dir, draft_filename))
        result_file = NFCGuard.normalize(os.path.join(self.watch_dir, f"{job_id}.result.json"))
        summary_file = NFCGuard.normalize(os.path.join(self.watch_dir, f"{job_id}.summary.md"))

        current_files = [full_draft_path, result_file, summary_file]

        try:
            # 1. 메타 파싱 및 알림
            meta = self.parse_metadata(full_draft_path)
            self.send_telegram_notification(job_id, meta)

            # 2. HWP/PDF 변환 수행
            success = self.convert_to_hwp_pdf(full_draft_path, job_id)
            if not success:
                raise RuntimeError("HWP/PDF 문서 변환에 실패했습니다.")

            # 3. NAS 배포 및 published 폴더로 이동 (Hand-off)
            # 배포 파일 모의 생성
            nas_hwp = os.path.join(self.publish_dir, f"{job_id}.hwp")
            nas_pdf = os.path.join(self.publish_dir, f"{job_id}.pdf")
            
            with open(nas_hwp, 'w', encoding='utf-8') as f: f.write("MOCK HWP")
            with open(nas_pdf, 'w', encoding='utf-8') as f: f.write("MOCK PDF")
            self.logger.info(f"[{job_id}] NAS 최종 배포 성공: {self.publish_dir}")

            # 파일들 04_published 스테이지로 격리 이동
            for f_p in current_files:
                if os.path.exists(f_p):
                    shutil.move(f_p, os.path.join(self.published_stage_dir, os.path.basename(f_p)))

            self.logger.info(f"[{job_id}] 04_published 스테이지로 상태 전이 완료.")
            self.processed_jobs.add(job_id)

        except Exception as e:
            self.logger.error(f"[{job_id}] 배포 처리 중 오류 발생: {e}")
            # 에러 발생 시 DLQ로 격리 이동
            for f_p in current_files:
                if os.path.exists(f_p):
                    shutil.move(f_p, os.path.join(self.error_dir, os.path.basename(f_p)))
            self.processed_jobs.add(job_id)

    def start_monitoring(self, interval=2):
        self.logger.info(f"아우룸 배포 엔진 가동 시작 (감시 경로: {self.watch_dir})")
        try:
            while True:
                for filename in os.listdir(self.watch_dir):
                    filename_nfc = NFCGuard.normalize(filename)
                    if filename_nfc.endswith(".draft.md"):
                        job_id = filename_nfc.replace(".draft.md", "")
                        if job_id not in self.processed_jobs:
                            self.process_review_pending(filename_nfc)
                time.sleep(interval)
        except KeyboardInterrupt:
            self.logger.info("배포 엔진 종료.")

if __name__ == "__main__":
    # 테스트 구동 설정
    BASE = os.path.expanduser("~/AI_BASE")
    WATCH = os.path.join(BASE, "03_review_pending")
    PUBLISH = os.path.join(BASE, "NAS_Distribution")
    
    os.makedirs(PUBLISH, exist_ok=True)
    
    deployer = AurumDeployer(WATCH, PUBLISH)
    # deployer.start_monitoring()
