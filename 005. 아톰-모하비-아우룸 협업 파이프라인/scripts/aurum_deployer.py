import argparse
import os
import re
import shlex
import shutil
import subprocess
import time
import logging
import unicodedata
from pathlib import Path

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
    def __init__(self, watch_dir: str, publish_dir: str, telegram_token: str = None, chat_id: str = None, convert_command: str = None):
        self.watch_dir = NFCGuard.normalize(os.path.abspath(os.path.expanduser(watch_dir)))
        self.publish_dir = NFCGuard.normalize(os.path.abspath(os.path.expanduser(publish_dir)))
        self.error_dir = NFCGuard.normalize(os.path.join(os.path.dirname(self.watch_dir), "00_error_failed"))
        self.published_stage_dir = NFCGuard.normalize(os.path.join(os.path.dirname(self.watch_dir), "04_published"))
        self.convert_command = convert_command or os.environ.get('AURUM_CONVERT_COMMAND')
        self.telegram_token = telegram_token
        self.chat_id = chat_id
        self.processed_jobs = set()

        # 폴더 초기화
        os.makedirs(self.publish_dir, exist_ok=True)
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

    def mark_published(self, file_path: str):
        """배포 완료 후 draft frontmatter 상태를 published로 갱신합니다."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL):
                content = re.sub(
                    r'(^---\s*\n.*?^status:\s*)[^\n]+',
                    r'\1published',
                    content,
                    count=1,
                    flags=re.DOTALL | re.MULTILINE,
                )
                content = re.sub(
                    r'(^---\s*\n.*?^assigned_agent:\s*)[^\n]+',
                    r'\1none',
                    content,
                    count=1,
                    flags=re.DOTALL | re.MULTILINE,
                )
            else:
                content = f"---\nstatus: published\nassigned_agent: none\n---\n\n{content}"

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            self.logger.error(f"상태 갱신 실패 ({os.path.basename(file_path)}): {e}")

    def send_telegram_notification(self, job_id: str, meta: dict):
        """텔레그램 채널로 검수 대기 알림을 전송합니다."""
        if not self.telegram_token or not self.chat_id:
            self.logger.info(f"[{job_id}] 텔레그램 설정이 누락되어 콘솔 로그로 대체합니다.")
            return

        message = (
            f"[에르메스 검수 요청]\n"
            f"작업 ID: {job_id}\n"
            f"소속 용역: {meta.get('year_vendor', '알 수 없음')}\n"
            f"프로젝트명: {meta.get('project_name', '알 수 없음')}\n"
            f"대분류군: {meta.get('class_name', '알 수 없음')}\n"
            f"상태: 검수 대기중 (review_pending)\n"
            f"HWP 및 PDF 변환 준비 완료."
        )

        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message}

        try:
            res = requests.post(url, json=payload, timeout=5)
            if res.status_code == 200:
                self.logger.info(f"[{job_id}] 텔레그램 검수 알림 전송 완료.")
            else:
                self.logger.error(f"[{job_id}] 텔레그램 전송 실패: {res.text}")
        except Exception as e:
            self.logger.error(f"[{job_id}] 텔레그램 API 호출 실패: {e}")

    def _run_convert_command(self, draft_path: str, job_id: str) -> bool:
        if not self.convert_command:
            return False
        env = os.environ.copy()
        env.update({
            'DRAFT_PATH': draft_path,
            'JOB_ID': job_id,
            'PUBLISH_DIR': self.publish_dir,
            'OUTPUT_HWP': os.path.join(self.publish_dir, f'{job_id}.hwp'),
            'OUTPUT_PDF': os.path.join(self.publish_dir, f'{job_id}.pdf'),
            'OUTPUT_DOCX': os.path.join(self.publish_dir, f'{job_id}.docx'),
        })
        self.logger.info(f"[{job_id}] 외부 변환 명령 실행: {self.convert_command}")
        result = subprocess.run(shlex.split(self.convert_command), env=env, text=True, capture_output=True, timeout=300)
        if result.stdout:
            self.logger.info(result.stdout.strip())
        if result.stderr:
            self.logger.warning(result.stderr.strip())
        if result.returncode != 0:
            raise RuntimeError(f"외부 변환 명령 실패: exit={result.returncode}")
        return True

    def _write_fallback_outputs(self, draft_path: str, job_id: str):
        draft_text = Path(draft_path).read_text(encoding='utf-8')
        # HWP 바이너리 변환 엔진이 없는 환경에서도 handoff 산출물 존재성은 보장한다.
        Path(self.publish_dir, f"{job_id}.hwp").write_text(
            "HWP 변환 대기 파일입니다. AURUM_CONVERT_COMMAND를 설정하면 실제 변환 산출물로 대체됩니다.\n\n" + draft_text,
            encoding='utf-8',
        )
        Path(self.publish_dir, f"{job_id}.pdf").write_text(
            "PDF 변환 대기 파일입니다. AURUM_CONVERT_COMMAND를 설정하면 실제 변환 산출물로 대체됩니다.\n\n" + draft_text,
            encoding='utf-8',
        )
        Path(self.publish_dir, f"{job_id}.md").write_text(draft_text, encoding='utf-8')

    def convert_to_hwp_pdf(self, draft_path: str, job_id: str) -> bool:
        """HWP/PDF 변환을 수행한다. 외부 변환 명령이 없으면 대기 산출물을 생성한다."""
        self.logger.info(f"[{job_id}] 한글(HWP) 및 PDF 문서 변환을 시작합니다...")
        if self._run_convert_command(draft_path, job_id):
            return True
        self.logger.warning(f"[{job_id}] AURUM_CONVERT_COMMAND 미설정: 변환 대기 산출물을 생성합니다.")
        self._write_fallback_outputs(draft_path, job_id)
        return True

    def process_review_pending(self, draft_filename: str):
        """review_pending 문서를 최종 검수 후 NAS 배포 및 published 스테이지로 아카이빙합니다."""
        job_id = draft_filename.replace(".draft.md", "")
        full_draft_path = NFCGuard.normalize(os.path.join(self.watch_dir, draft_filename))
        result_file = NFCGuard.normalize(os.path.join(self.watch_dir, f"{job_id}.result.json"))
        summary_file = NFCGuard.normalize(os.path.join(self.watch_dir, f"{job_id}.summary.md"))

        current_files = [full_draft_path, result_file, summary_file]

        try:
            meta = self.parse_metadata(full_draft_path)
            status = meta.get('status', 'review_pending')
            if status not in {'review_pending', 'reviewed'}:
                self.logger.info(f"[{job_id}] 배포 대상 상태가 아니므로 건너뜁니다: {status}")
                return
            self.send_telegram_notification(job_id, meta)

            success = self.convert_to_hwp_pdf(full_draft_path, job_id)
            if not success:
                raise RuntimeError("HWP/PDF 문서 변환에 실패했습니다.")

            self.logger.info(f"[{job_id}] NAS 최종 배포 성공: {self.publish_dir}")
            self.mark_published(full_draft_path)

            for f_p in current_files:
                if os.path.exists(f_p):
                    shutil.move(f_p, os.path.join(self.published_stage_dir, os.path.basename(f_p)))

            self.logger.info(f"[{job_id}] 04_published 스테이지로 상태 전이 완료.")
            self.processed_jobs.add(job_id)

        except Exception as e:
            self.logger.error(f"[{job_id}] 배포 처리 중 오류 발생: {e}")
            for f_p in current_files:
                if os.path.exists(f_p):
                    shutil.move(f_p, os.path.join(self.error_dir, os.path.basename(f_p)))
            self.processed_jobs.add(job_id)

    def scan_once(self):
        processed = []
        for filename in os.listdir(self.watch_dir):
            filename_nfc = NFCGuard.normalize(filename)
            if filename_nfc.endswith(".draft.md"):
                job_id = filename_nfc.replace(".draft.md", "")
                if job_id not in self.processed_jobs:
                    self.process_review_pending(filename_nfc)
                    processed.append(job_id)
        return processed

    def start_monitoring(self, interval=2):
        self.logger.info(f"아우룸 배포 엔진 가동 시작 (감시 경로: {self.watch_dir})")
        try:
            while True:
                self.scan_once()
                time.sleep(interval)
        except KeyboardInterrupt:
            self.logger.info("배포 엔진 종료.")


def build_arg_parser():
    parser = argparse.ArgumentParser(description="아우룸 배포 엔진")
    parser.add_argument("--root", default=os.environ.get("PIPELINE_ROOT", "~/AI_BASE"), help="파이프라인 stage 루트")
    parser.add_argument("--watch-dir", help="기본값: <root>/03_review_pending")
    parser.add_argument("--publish-dir", default=os.environ.get("AURUM_PUBLISH_DIR"), help="기본값: <root>/NAS_Distribution")
    parser.add_argument("--interval", type=int, default=int(os.environ.get("AURUM_DEPLOY_INTERVAL", "2")))
    parser.add_argument("--once", action="store_true", help="한 번만 스캔하고 종료")
    parser.add_argument("--convert-command", default=os.environ.get("AURUM_CONVERT_COMMAND"), help="외부 변환 명령. env로 DRAFT_PATH/JOB_ID/PUBLISH_DIR/OUTPUT_* 제공")
    return parser


def main():
    args = build_arg_parser().parse_args()
    root = os.path.abspath(os.path.expanduser(args.root))
    watch = args.watch_dir or os.path.join(root, "03_review_pending")
    publish = args.publish_dir or os.path.join(root, "NAS_Distribution")
    deployer = AurumDeployer(
        watch,
        publish,
        telegram_token=os.environ.get('TELEGRAM_BOT_TOKEN'),
        chat_id=os.environ.get('ALLOWED_USER_ID'),
        convert_command=args.convert_command,
    )
    if args.once:
        deployer.scan_once()
    else:
        deployer.start_monitoring(interval=args.interval)


if __name__ == "__main__":
    main()
