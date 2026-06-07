#!/usr/bin/env python3
"""
주말 대용량 배치 인덱싱 및 구조 분석 스크립트.
NAS 내의 기존 보관된 파일들을 순회하며 아직 색인되지 않은 신규 파일을 추출, RAG 인덱스화 및 요약 생성합니다.
배치 모드로 작동하여 텔레그램 알림을 끄고, 기존 처리 완료된 파일은 자동으로 건너뜁니다.
"""
import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import json
import logging
import os
from pathlib import Path
import re
import subprocess
import sys
import time

# 서울 시간대 설정
KST = timezone(timedelta(hours=9))

def now_iso() -> str:
    return datetime.now(KST).isoformat(timespec="seconds")

def setup_logger(log_dir: Path) -> logging.Logger:
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "batch_indexing.log"

    logger = logging.getLogger("batch_indexing")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] %(message)s"
    )
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

def safe_stem(source_path: Path) -> str:
    digest = hashlib.sha1(str(source_path).encode("utf-8")).hexdigest()[:10]
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", source_path.stem).strip("._")
    return f"{cleaned or 'file'}_{digest}"

def is_ignored(path: Path) -> bool:
    """분석 대상에서 완전히 스킵할 시스템 또는 임시 파일인지 판단"""
    parts = path.parts
    # 숨김 폴더, 시스템 폴더, 파이썬 환경 폴더 스킵
    ignore_dirs = {".git", ".venv", ".vscode", "__pycache__", ".smart-env", ".trash", "Backups"}
    if any(d in parts for d in ignore_dirs):
        return True

    # 임시 파일 및 시스템 파일 스킵
    name = path.name
    if name.startswith("._") or name.startswith("~$") or name == ".DS_Store":
        return True

    # 이미 분석 스크립트로 생성된 산출물들(metadata.json, obsidian 요약본 등) 스킵
    if ".metadata.json" in name or path.suffix.lower() == ".log":
        return True

    return False

def get_metadata_path(file_path: Path, output_dir: Path) -> Path:
    stem = safe_stem(file_path)
    return output_dir / "metadata" / f"{stem}.metadata.json"

def check_already_indexed(file_path: Path, output_dir: Path, logger: logging.Logger) -> bool:
    """이미 성공적으로 인덱싱되었는지 여부 확인"""
    meta_path = get_metadata_path(file_path, output_dir)
    if not meta_path.exists():
        return False

    try:
        data = json.loads(meta_path.read_text(encoding="utf-8"))
        if data.get("status") == "success":
            return True
    except Exception as e:
        logger.warning("Failed to parse existing metadata for %s: %s", file_path.name, e)

    return False

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--watch', default='/mnt/dgxbackup', help='분석 및 인덱싱할 NAS 루트 폴더 경로')
    p.add_argument('--output-dir', default='/home/caiser77/dgx_workspace/002. 회사 NAS 분석/data/processed', help='결과 저장 루트')
    p.add_argument('--ocr-endpoint', default='http://localhost:7870', help='기가바이트 OCR API 엔드포인트')
    p.add_argument('--no-ocr', action='store_true', help='원격 OCR 연동 생략')
    p.add_argument('--no-telegram', action='store_true', default=True, help='텔레그램 승인 요청 발송 생략 (기본 활성)')
    p.add_argument('--send-telegram', action='store_false', dest='no_telegram', help='모호성 발생 시 텔레그램을 즉시 발송하도록 변경')
    p.add_argument('--device-name', default='atom-batch', help='메타데이터에 기록할 분석 장치명')
    p.add_argument('--no-ai', action='store_true', help='Hermes AI 분류 생략 — 경로 파싱으로 대체 (배치 고속 모드)')
    p.add_argument('--sleep', type=float, default=0.5, help='파일 처리간 CPU/GPU 대기 시간(초)')
    p.add_argument('--limit', type=int, default=0, help='최대 처리할 파일 개수 제한 (0은 무제한)')
    p.add_argument('--extensions', default='.pdf,.png,.jpg,.jpeg,.xlsx,.csv,.txt,.hwp', help='분석 대상 확장자 목록 (콤마 구분)')
    args = p.parse_args()

    watch_path = Path(args.watch).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    log_dir = Path("/home/caiser77/dgx_workspace/002. 회사 NAS 분석/logs")

    logger = setup_logger(log_dir)

    logger.info("=== 배치 인덱싱 시작 ===")
    logger.info("감시 대상 경로: %s", watch_path)
    logger.info("결과 저장 경로: %s", output_dir)
    logger.info("OCR 서버: %s (no-ocr=%s)", args.ocr_endpoint, args.no_ocr)
    logger.info("텔레그램 발송 생략 여부: %s", args.no_telegram)

    if not watch_path.exists():
        logger.error("Error: 감시 대상 경로가 존재하지 않습니다: %s", watch_path)
        sys.exit(1)

    target_exts = {ext.strip().lower() for ext in args.extensions.split(",")}
    logger.info("대상 확장자: %s", target_exts)

    # 1. 대상 파일 리스트업
    logger.info("파일 스캔 중...")
    all_files = []
    for root, _, files in os.walk(str(watch_path)):
        for file in files:
            file_path = Path(root) / file
            if is_ignored(file_path):
                continue
            if file_path.suffix.lower() in target_exts:
                all_files.append(file_path)

    total_found = len(all_files)
    logger.info("스캔 완료: 총 %d개의 대상 파일 발견", total_found)

    # 2. 기인덱싱 여부 필터링 (중복 제거)
    to_process = []
    skipped_count = 0
    for f in all_files:
        if check_already_indexed(f, output_dir, logger):
            skipped_count += 1
        else:
            to_process.append(f)

    total_to_process = len(to_process)
    logger.info("스킵된 파일(이미 완료됨): %d개", skipped_count)
    logger.info("새로 처리할 파일: %d개", total_to_process)

    if args.limit > 0:
        logger.info("처리 제한 적용: %d개 파일만 처리합니다.", args.limit)
        to_process = to_process[:args.limit]
        total_to_process = len(to_process)

    if total_to_process == 0:
        logger.info("처리할 신규 파일이 없습니다. 작업을 종료합니다.")
        return

    # 3. 배치 루프 처리 시작
    started_at = time.time()
    success_count = 0
    fail_count = 0
    processed_files = []
    failed_files = []

    extractor_script = Path("/home/caiser77/dgx_workspace/002. 회사 NAS 분석/scripts/extract_data.py")
    python_bin = sys.executable  # 현재 가상환경의 python3 런타임

    for idx, file_path in enumerate(to_process, 1):
        percent = (idx / total_to_process) * 100
        logger.info("[%d/%d - %.1f%%] 처리 중: %s", idx, total_to_process, percent, file_path.relative_to(watch_path))

        cmd = [
            python_bin,
            str(extractor_script),
            "--input", str(file_path),
            "--device-name", args.device_name,
            "--output-dir", str(output_dir),
            "--ocr-endpoint", args.ocr_endpoint
        ]
        if args.no_ocr:
            cmd.append("--no-ocr")
        if args.no_telegram:
            cmd.append("--no-telegram")
        if args.no_ai:
            cmd.append("--no-ai")

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=120, encoding="utf-8")
            if res.returncode == 0:
                success_count += 1
                processed_files.append(str(file_path))
                logger.info("처리 성공: %s", file_path.name)
            else:
                fail_count += 1
                err_msg = res.stderr.strip() if res.stderr else "알 수 없는 에러"
                failed_files.append({"path": str(file_path), "error": err_msg})
                logger.error("처리 실패: %s (반환 코드: %d)\nStderr: %s", file_path.name, res.returncode, err_msg)
        except subprocess.TimeoutExpired:
            fail_count += 1
            failed_files.append({"path": str(file_path), "error": "시간 초과 (120초)"})
            logger.error("처리 실패(시간 초과): %s", file_path.name)
        except Exception as e:
            fail_count += 1
            failed_files.append({"path": str(file_path), "error": str(e)})
            logger.error("처리 실패(예외 발생): %s - %s", file_path.name, e)

        if args.sleep > 0:
            time.sleep(args.sleep)

    # 4. 보고서 및 결과 통계 작성
    elapsed = time.time() - started_at
    logger.info("=== 배치 인덱싱 완료 ===")
    logger.info("소요 시간: %.2f초 (%.2f분)", elapsed, elapsed / 60)
    logger.info("성공: %d개, 실패: %d개", success_count, fail_count)

    # 마크다운 보고서 저장
    report_path = log_dir / "batch_indexing_report.md"
    report_lines = [
        "# 📊 주말 배치 인덱싱 작업 결과 보고서",
        f"\n* **작업 일시**: {now_iso()} (KST)",
        f"* **분석 장치**: {args.device_name}",
        f"* **소요 시간**: {elapsed/60:.2f}분 ({elapsed:.1f}초)",
        f"* **총 대상 파일**: {total_found}개",
        f"* **기존 완료 파일 (스킵)**: {skipped_count}개",
        f"* **새로 시도한 파일**: {total_to_process}개",
        f"  - **성공**: {success_count}개 ✅",
        f"  - **실패**: {fail_count}개 ❌",
        "\n---",
        "\n## ❌ 실패 목록 및 원인 분석"
    ]

    if failed_files:
        for f in failed_files:
            report_lines.append(f"\n### 📄 {Path(f['path']).name}")
            report_lines.append(f"* **경로**: `{f['path']}`")
            report_lines.append(f"* **원인**: `{f['error']}`")
    else:
        report_lines.append("\n* 실패한 파일이 없습니다. 모든 파일이 정상적으로 인덱싱되었습니다! 🎉")

    try:
        report_path.write_text("\n".join(report_lines), encoding="utf-8")
        logger.info("결과 보고서 작성 완료: %s", report_path)
    except Exception as e:
        logger.error("Failed to write report file: %s", e)

if __name__ == '__main__':
    main()
