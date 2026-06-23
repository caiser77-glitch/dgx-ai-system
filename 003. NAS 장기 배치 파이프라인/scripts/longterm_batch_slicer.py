#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
003. NAS 장기 배치 파이프라인 - 일자별 슬라이싱 및 일괄 처리 엔진
1. 대규모 NAS 디렉토리(10개년 자료)를 스캔하여 핵심 문서 파일 식별
2. 이미 성공적으로 처리(AI 요약 포함)된 파일은 건너뜀 (Incremental Processing)
3. 지정된 개수 한도(--limit)만큼만 하루 밤에 순차 처리하여 리소스 과부하 예방
4. 가공 성공한 파일들이 존재하면 최종적으로 FAISS 인덱스 빌드 트리거
"""

import os
import sys
import json
import argparse
import subprocess
import hashlib
import re
import urllib.request
import urllib.error
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from datetime import datetime, timezone, timedelta

# KST 시간 획득
def now_iso() -> str:
    kst = timezone(timedelta(hours=9))
    return datetime.now(kst).isoformat(timespec="seconds")

def safe_stem(source_path: Path) -> str:
    """
    파일의 고유 해시와 정제된 파일명 조합으로 고유 ID stem을 생성합니다.
    (기존 extract_data.py 및 batch_process.py와의 정합성 100% 유지)
    """
    digest = hashlib.sha1(str(source_path).encode("utf-8")).hexdigest()[:10]
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", source_path.stem).strip("._")
    return f"{cleaned or 'file'}_{digest}"

def call_vllm_for_summary(text: str, endpoint: str, model_name: str) -> dict:
    """vLLM API를 호출하여 핵심 요약 3줄, 카테고리, 키워드 태그를 생성합니다."""
    truncated_text = text[:6000] # 성능 및 컨텍스트 한계 고려

    prompt = (
        "당신은 아우룸생태연구소의 문서 분석 및 요약 전문가입니다. "
        "다음 문서 내용을 분석하여 반드시 지정된 JSON 형식으로만 응답해 주세요. "
        "JSON 마크다운 코드 블록(```json ... ```)이나 추가 텍스트 없이 순수 JSON 문자열만 출력해야 합니다.\n\n"
        "출력 JSON 스키마:\n"
        "{\n"
        '  "summary": [\n'
        '    "핵심 요약 3줄 중 첫 번째 줄",\n'
        '    "핵심 요약 3줄 중 두 번째 줄",\n'
        '    "핵심 요약 3줄 중 세 번째 줄"\n'
        '  ],\n'
        '  "category": "분류 카테고리 (예: 장비, 연구보고서, 현장조사, 행정문서, 기타 등)",\n'
        '  "keywords": ["키워드1", "키워드2", "키워드3"]\n'
        "}\n\n"
        f"문서 내용:\n{truncated_text}\n"
    )

    data_dict = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "You are a helpful document analysis assistant. You must respond in valid JSON format only."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1,
        "max_tokens": 512,
        "stream": False,
    }

    payload = json.dumps(data_dict).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            resp_data = json.loads(response.read().decode("utf-8"))
            choices = resp_data.get("choices", [])
            if choices:
                content = choices[0].get("message", {}).get("content", "").strip()
                if content.startswith("```"):
                    lines = content.splitlines()
                    if lines[0].startswith("```json"):
                        content = "\n".join(lines[1:-1])
                    elif lines[0].startswith("```"):
                        content = "\n".join(lines[1:-1])
                return json.loads(content)
    except urllib.error.URLError as e:
        print(f"[오류] vLLM API 호출 실패: {e}", file=sys.stderr)
    except json.JSONDecodeError as e:
        print(f"[오류] JSON 파싱 실패: {e}\n응답 내용: {content if 'content' in locals() else 'None'}", file=sys.stderr)
    except Exception as e:
        print(f"[예외] 요약 생성 중 예외 발생: {e}", file=sys.stderr)

    return {
        "summary": ["요약을 생성하지 못했습니다.", "", ""],
        "category": "기타",
        "keywords": []
    }

def update_text_file_with_summary(text_path: Path, ai_summary: dict) -> None:
    """텍스트 파일 상단에 AI 요약 헤더를 추가/치환합니다."""
    original_content = text_path.read_text(encoding="utf-8", errors="replace")
    separator = "=========================================\n"
    if separator in original_content:
        parts = original_content.split(separator, 1)
        original_content = parts[1]

    summary_lines = ai_summary.get("summary", [])
    summary_str = "\n".join(f"- {line}" for line in summary_lines if line)
    keywords_str = ", ".join(ai_summary.get("keywords", []))
    category = ai_summary.get("category", "기타")

    header = (
        "[AI 기반 사전 요약 및 메타데이터]\n"
        f"● 분류 카테고리: {category}\n"
        f"● 핵심 키워드: {keywords_str}\n"
        f"● 3줄 요약:\n{summary_str}\n"
        f"{separator}"
    )
    text_path.write_text(header + original_content, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="NAS 장기 분할 배치 가공 및 색인기")
    parser.add_argument("--input-dir", required=True, help="스캔 대상 NAS 마운트 디렉토리")
    parser.add_argument("--processed-dir", required=True, help="추출 텍스트 및 메타데이터 저장 경로")
    parser.add_argument("--index-dir", required=True, help="FAISS 인덱스 빌드 경로")
    parser.add_argument("--limit", type=int, default=300, help="하루 밤에 처리할 파일 최대 개수")
    parser.add_argument("--extensions", default=".pdf,.docx,.txt,.pptx,.xlsx,.csv,.hwp,.hwpx,.xls", help="대상 확장자 목록 (콤마 구분)")
    parser.add_argument("--device-name", default="overnight_batch", help="장비 식별 식별자")
    parser.add_argument("--vllm-endpoint", default="http://localhost:8088/v1/chat/completions", help="vLLM API 엔드포인트")
    parser.add_argument("--vllm-model", default="Qwen/Qwen2.5-72B-Instruct-AWQ", help="vLLM 모델명")
    parser.add_argument("--embedding-model", default="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", help="FAISS 인덱싱에 사용할 임베딩 모델명")
    parser.add_argument("--embedding-device", default="cpu", help="FAISS 인덱싱 임베딩 실행 장치(cpu, cuda 등)")
    parser.add_argument("--embedding-batch-size", type=int, default=32, help="FAISS 인덱싱 임베딩 배치 크기")
    parser.add_argument("--skip-current-index", action="store_true", help="입력/모델이 기존 인덱스와 같으면 최종 FAISS 재빌드를 건너뜀")
    parser.add_argument("--ocr-endpoint", default="http://localhost:7870", help="OCR API 엔드포인트")
    parser.add_argument("--no-ocr", action="store_true", help="OCR 처리 비활성화")
    parser.add_argument("--mtime-days", type=int, default=0, help="N일 이내에 수정된 파일만 대상 (0이면 제한 없음)")
    parser.add_argument("--sort-newest", action="store_true", help="최신 수정 파일부터 순차 가공 (미설정 시 오래된 파일부터)")
    parser.add_argument("--report-file", default="", help="일일 배치 결과 리포트 파일 경로")
    parser.add_argument("--workers", type=int, default=2, help="병렬 가공을 위한 스레드 워커 수 (디폴트: 2)")

    args = parser.parse_args()

    input_dir = Path(args.input_dir).expanduser().resolve()
    processed_dir = Path(args.processed_dir).expanduser().resolve()
    index_dir = Path(args.index_dir).expanduser().resolve()

    # 의존 스크립트 경로 획득 (프로젝트 루트 내 scripts 및 002 폴더 등 참조)
    project_root = Path(__file__).resolve().parent.parent.parent
    extract_script = project_root / "002. 회사 NAS 분석" / "scripts" / "extract_data.py"
    index_script = project_root / "002. 회사 NAS 분석" / "scripts" / "index_documents.py"

    if not extract_script.exists():
        # Fallback: 로컬 스크립트 디렉토리 탐색
        extract_script = Path(__file__).resolve().parent / "extract_data.py"
        index_script = Path(__file__).resolve().parent / "index_documents.py"

    if not input_dir.exists():
        print(f"[오류] 입력 경로가 존재하지 않습니다: {input_dir}")
        return 1

    allowed_exts = {ext.strip().lower() for ext in args.extensions.split(",") if ext.strip()}

    print(f"[{now_iso()}] === NAS 장기 배치 파이프라인 스캔 개시 ===")
    print(f"- 입력 경로: {input_dir}")
    print(f"- 가공 경로: {processed_dir}")
    print(f"- 하루 처리 한도: {args.limit} 개")
    print(f"- 병렬 워커 수: {args.workers} 개")

    # 1. 파일 목록 순회 및 스캔
    raw_files = []
    for root, dirs, files in os.walk(input_dir):
        # 숨김 폴더 제외
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.startswith('.'):
                continue
            file_path = Path(root) / file
            ext = file_path.suffix.lower()
            if ext in allowed_exts:
                raw_files.append(file_path)

    print(f"발견된 지원 포맷 파일 수: {len(raw_files)}개")

    # 2. 증분 필터링 (이미 가공 완료된 파일 스킵)
    target_files = []
    skipped_count = 0

    for file_path in raw_files:
        # 시간 제한이 설정되어 있으면 확인
        if args.mtime_days > 0:
            mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            age = datetime.now() - mtime
            if age.days > args.mtime_days:
                continue

        stem = safe_stem(file_path)
        metadata_path = processed_dir / "metadata" / f"{stem}.metadata.json"

        # 메타데이터가 정상적이고 ai_summary가 존재하면 완료된 것으로 판단
        if metadata_path.exists():
            try:
                meta = json.loads(metadata_path.read_text(encoding="utf-8"))
                if meta.get("status") == "success" and "ai_summary" in meta:
                    skipped_count += 1
                    continue
            except Exception:
                pass

        # 가공 대상 리스트에 추가 (파일 경로, 수정 시각)
        target_files.append((file_path, file_path.stat().st_mtime))

    print(f"가공 완료 스킵 파일 수: {skipped_count}개")
    print(f"남은 미처리 가공 대상 수: {len(target_files)}개")

    if not target_files:
        print("모든 파일의 지식 가공이 이미 완료되었습니다. 작업을 종료합니다.")
        return 0

    # 3. 수정 시간 기준 정렬
    target_files.sort(key=lambda x: x[1], reverse=args.sort_newest)

    # 4. Limit 슬라이싱
    sliced_targets = [item[0] for item in target_files[:args.limit]]
    print(f"금일 가공할 슬라이스 범위: {len(sliced_targets)}개 파일")

    success_count = 0
    failed_count = 0
    python_exe = sys.executable or "python3"

    # 동시성 처리를 위한 락 생성
    print_lock = threading.Lock()
    counter_lock = threading.Lock()

    # 5. 병렬 가공 파일 처리 함수
    def process_file(idx, file_path):
        nonlocal success_count, failed_count

        with print_lock:
            print(f"\n[{idx + 1}/{len(sliced_targets)}] 처리 시작: {file_path.name}")

        stem = safe_stem(file_path)
        metadata_path = processed_dir / "metadata" / f"{stem}.metadata.json"

        # A. 텍스트 추출 실행
        cmd = [
            python_exe,
            str(extract_script),
            "--input", str(file_path),
            "--device-name", args.device_name,
            "--output-dir", str(processed_dir),
            "--ocr-endpoint", args.ocr_endpoint
        ]
        if args.no_ocr:
            cmd.append("--no-ocr")

        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            with print_lock:
                print(f"❌ 텍스트 추출 실패 ({file_path.name}): {res.stderr.strip()}")
            with counter_lock:
                failed_count += 1
            return

        if not metadata_path.exists():
            with print_lock:
                print(f"❌ 메타데이터 없음 ({file_path.name})")
            with counter_lock:
                failed_count += 1
            return

        try:
            meta = json.loads(metadata_path.read_text(encoding="utf-8"))
        except Exception as e:
            with print_lock:
                print(f"❌ 메타데이터 파싱 실패: {e}")
            with counter_lock:
                failed_count += 1
            return

        if meta.get("status") != "success":
            with print_lock:
                print(f"❌ 추출 프로세스 실패 마킹: {meta.get('error', {}).get('message', 'unknown')}")
            with counter_lock:
                failed_count += 1
            return

        text_output = meta.get("outputs", {}).get("text")
        if not text_output or not Path(text_output).exists():
            with print_lock:
                print(f"❌ 추출된 텍스트 결과 파일 부재: {text_output}")
            with counter_lock:
                failed_count += 1
            return

        text_path = Path(text_output)
        text_content = text_path.read_text(encoding="utf-8", errors="replace").strip()

        # B. vLLM 요약 및 메타 주입
        with print_lock:
            print(f"-> AI 요약 및 분류 생성 중 ({args.vllm_model}) [{file_path.name}]...")
        ai_summary = call_vllm_for_summary(text_content, args.vllm_endpoint, args.vllm_model)

        meta["ai_summary"] = ai_summary
        meta["processed_at"] = now_iso()
        metadata_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

        update_text_file_with_summary(text_path, ai_summary)

        with print_lock:
            print(f"✅ 가공 완료 (카테고리: {ai_summary.get('category')}) [{file_path.name}]")
        with counter_lock:
            success_count += 1

    # ThreadPoolExecutor를 이용한 멀티스레드 병렬 실행
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(process_file, idx, file_path) for idx, file_path in enumerate(sliced_targets)]
        # 모든 스레드가 완료될 때까지 동기 대기 및 결과 처리
        for fut in futures:
            try:
                fut.result()
            except Exception as e:
                print(f"[예외] 스레드 실행 중 치명적 오류 발생: {e}", file=sys.stderr)
                with counter_lock:
                    failed_count += 1

    print(f"\n[{now_iso()}] === 일일 배치 가공 완료 ===")
    print(f"- 성공: {success_count}개, 실패: {failed_count}개")

    # 6. FAISS 인덱스 일괄 빌드
    if success_count > 0:
        print(f"\n[{now_iso()}] === FAISS 인덱스 업데이트 빌드 개시 ===")
        cmd_index = [
            python_exe,
            str(index_script),
            "--processed-dir", str(processed_dir),
            "--index-dir", str(index_dir),
            "--model-name", args.embedding_model,
            "--device", args.embedding_device,
            "--batch-size", str(args.embedding_batch_size),
        ]
        if args.skip_current_index:
            cmd_index.append("--skip-if-current")
        res_index = subprocess.run(cmd_index, capture_output=True, text=True)
        if res_index.returncode == 0:
            print(f"✅ FAISS 인덱스 빌드 완료: {index_dir}")
            print(res_index.stdout.strip())
        else:
            print(f"❌ FAISS 인덱스 빌드 실패: {res_index.stderr.strip()}")

    # 7. 일일 리포트 작성
    if args.report_file:
        report_path = Path(args.report_file).expanduser().resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_lines = [
            f"날짜: {now_iso()[:10]}",
            f"스캔 시간: {now_iso()}",
            f"총 미처리 타겟: {len(target_files)}개",
            f"금일 가공 범위: {len(sliced_targets)}개",
            f"성공: {success_count}개",
            f"실패: {failed_count}개",
            "----------------------------------------"
        ]
        with report_path.open("a", encoding="utf-8") as rf:
            rf.write("\n".join(report_lines) + "\n")

    return 0

if __name__ == "__main__":
    sys.exit(main())
