#!/usr/bin/env python3
"""Extract text, table outputs, and metadata from uploaded local files."""
import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request
import uuid


TEXT_EXTENSIONS = {".txt", ".md"}
CSV_EXTENSIONS = {".csv"}
XLSX_EXTENSIONS = {".xlsx"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
PDF_EXTENSIONS = {".pdf"}


def now_iso() -> str:
    kst = timezone(timedelta(hours=9))
    return datetime.now(kst).isoformat(timespec="seconds")


def safe_stem(source_path: Path) -> str:
    digest = hashlib.sha1(str(source_path).encode("utf-8")).hexdigest()[:10]
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", source_path.stem).strip("._")
    return f"{cleaned or 'file'}_{digest}"


def ensure_dirs(output_dir: Path) -> dict[str, Path]:
    paths = {
        "text": output_dir / "text",
        "tables": output_dir / "tables",
        "metadata": output_dir / "metadata",
    }
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
    return paths


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def read_text_file(source_path: Path) -> str:
    try:
        return source_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return source_path.read_text(encoding="utf-8", errors="replace")


def extract_text(source_path: Path, dirs: dict[str, Path], stem: str) -> dict:
    output_path = dirs["text"] / f"{stem}.txt"
    write_text(output_path, read_text_file(source_path))
    return {"text": str(output_path), "tables": []}


def extract_csv(source_path: Path, dirs: dict[str, Path], stem: str) -> dict:
    table_path = dirs["tables"] / f"{stem}.csv"
    rows = []
    with source_path.open("r", encoding="utf-8-sig", newline="") as src:
        reader = csv.reader(src)
        for row in reader:
            rows.append(row)

    with table_path.open("w", encoding="utf-8", newline="") as dst:
        writer = csv.writer(dst)
        writer.writerows(rows)

    text_path = dirs["text"] / f"{stem}.txt"
    row_count = max(len(rows) - 1, 0)
    headers = rows[0] if rows else []
    summary = [
        f"source_name: {source_path.name}",
        f"source_type: csv",
        f"row_count: {row_count}",
        f"columns: {', '.join(headers)}",
    ]
    write_text(text_path, "\n".join(summary) + "\n")
    return {"text": str(text_path), "tables": [str(table_path)]}


def extract_xlsx(source_path: Path, dirs: dict[str, Path], stem: str) -> dict:
    try:
        from openpyxl import load_workbook
    except ImportError as exc:
        raise RuntimeError("openpyxl is required for .xlsx extraction") from exc

    workbook = load_workbook(source_path, read_only=True, data_only=True)
    table_paths = []
    summaries = [
        f"source_name: {source_path.name}",
        "source_type: xlsx",
    ]
    for worksheet in workbook.worksheets:
        sheet_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", worksheet.title).strip("._")
        table_path = dirs["tables"] / f"{stem}.{sheet_name or 'sheet'}.csv"
        rows = list(worksheet.iter_rows(values_only=True))
        with table_path.open("w", encoding="utf-8", newline="") as dst:
            writer = csv.writer(dst)
            writer.writerows(
                ["" if cell is None else cell for cell in row]
                for row in rows
            )
        table_paths.append(str(table_path))
        summaries.append(
            f"sheet: {worksheet.title}, rows: {len(rows)}, columns: {worksheet.max_column}"
        )

    text_path = dirs["text"] / f"{stem}.txt"
    write_text(text_path, "\n".join(summaries) + "\n")
    return {"text": str(text_path), "tables": table_paths}


def extract_image(source_path: Path, dirs: dict[str, Path], stem: str) -> dict:
    image_info = {
        "source_name": source_path.name,
        "source_type": source_path.suffix.lower().lstrip("."),
        "size_bytes": source_path.stat().st_size,
    }
    try:
        from PIL import Image

        with Image.open(source_path) as image:
            image_info.update(
                {
                    "width": image.width,
                    "height": image.height,
                    "mode": image.mode,
                    "format": image.format,
                }
            )
    except ImportError:
        image_info["note"] = "Pillow not installed; image dimensions not extracted."
    except Exception as exc:
        image_info["error"] = str(exc)

    table_path = dirs["tables"] / f"{stem}.image.json"
    table_path.write_text(
        json.dumps(image_info, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    text_path = dirs["text"] / f"{stem}.txt"
    lines = [f"{key}: {value}" for key, value in image_info.items()]
    write_text(text_path, "\n".join(lines) + "\n")
    return {"text": str(text_path), "tables": [str(table_path)]}

def extract_basic_metadata(source_path: Path, dirs: dict[str, Path], stem: str) -> dict:
    text_path = dirs["text"] / f"{stem}.txt"
    details = [
        f"source_name: {source_path.name}",
        f"source_type: {source_path.suffix.lower().lstrip('.') or 'unknown'}",
        f"size_bytes: {source_path.stat().st_size}",
        "content_extraction: unsupported_file_type",
    ]
    write_text(text_path, "\n".join(details) + "\n")
    return {"text": str(text_path), "tables": []}


def send_multipart_file(url: str, file_path: Path, extra_fields: dict | None = None) -> bytes:
    boundary = f"----WebKitFormBoundary{uuid.uuid4().hex}"
    parts = []
    
    if extra_fields:
        for name, value in extra_fields.items():
            parts.append(f"--{boundary}")
            parts.append(f'Content-Disposition: form-data; name="{name}"')
            parts.append('')
            parts.append(str(value))
            
    parts.append(f"--{boundary}")
    filename = file_path.name
    suffix = file_path.suffix.lower()
    content_type = "application/octet-stream"
    if suffix in {".jpg", ".jpeg"}:
        content_type = "image/jpeg"
    elif suffix == ".png":
        content_type = "image/png"
    elif suffix == ".pdf":
        content_type = "application/pdf"
        
    parts.append(f'Content-Disposition: form-data; name="file"; filename="{filename}"')
    parts.append(f'Content-Type: {content_type}')
    parts.append('')
    
    body_header = "\n".join(parts).replace("\n", "\r\n").encode("utf-8") + b"\r\n"
    body_footer = f"\r\n--{boundary}--\r\n".encode("utf-8")
    
    file_content = file_path.read_bytes()
    body = body_header + file_content + body_footer
    
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Content-Length": str(len(body))
        },
        method="POST"
    )
    
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def extract_via_ocr(source_path: Path, dirs: dict[str, Path], stem: str, ocr_endpoint: str, is_pdf: bool) -> dict:
    if is_pdf:
        url = f"{ocr_endpoint.rstrip('/')}/tools/pdf-ocr"
        extra = {"pages": "1"}
    else:
        url = f"{ocr_endpoint.rstrip('/')}/tools/image-ocr"
        extra = {}

    try:
        resp_bytes = send_multipart_file(url, source_path, extra)
        resp_json = json.loads(resp_bytes.decode("utf-8"))
        
        if resp_json.get("status") != "ok" or "url" not in resp_json:
            raise RuntimeError(f"OCR API failed: {resp_json}")
            
        file_url_path = resp_json["url"]
        download_url = f"{ocr_endpoint.rstrip('/')}{file_url_path}"
        
        excel_path = dirs["tables"] / f"{stem}_ocr.xlsx"
        with urllib.request.urlopen(download_url, timeout=30) as resp:
            excel_path.write_bytes(resp.read())
            
        from openpyxl import load_workbook
        workbook = load_workbook(excel_path, read_only=True, data_only=True)
        summaries = [
            f"source_name: {source_path.name}",
            f"source_type: {source_path.suffix.lower().lstrip('.')}",
            f"ocr_engine: gigabyte-atom-ocr",
            f"ocr_excel_source: {download_url}",
        ]
        
        for worksheet in workbook.worksheets:
            summaries.append(f"\n--- Sheet: {worksheet.title} ---")
            for row in worksheet.iter_rows(values_only=True):
                row_str = ", ".join(
                    ["" if cell is None else str(cell).strip() for cell in row]
                ).strip(", ")
                if row_str:
                    summaries.append(row_str)
                    
        text_path = dirs["text"] / f"{stem}.txt"
        write_text(text_path, "\n".join(summaries) + "\n")
        
        return {"text": str(text_path), "tables": [str(excel_path)]}
        
    except Exception as exc:
        if not is_pdf:
            fallback_res = extract_image(source_path, dirs, stem)
            t_path = Path(fallback_res["text"])
            t_content = t_path.read_text(encoding="utf-8")
            write_text(t_path, t_content + f"ocr_error: {exc}\n")
            return fallback_res
        else:
            fallback_res = extract_basic_metadata(source_path, dirs, stem)
            t_path = Path(fallback_res["text"])
            t_content = t_path.read_text(encoding="utf-8")
            write_text(t_path, t_content + f"ocr_error: {exc}\n")
            return fallback_res


def run_extraction(source_path: Path, output_dir: Path, no_ocr: bool = False, ocr_endpoint: str | None = None) -> dict:
    dirs = ensure_dirs(output_dir)
    stem = safe_stem(source_path)
    suffix = source_path.suffix.lower()

    if suffix in TEXT_EXTENSIONS:
        outputs = extract_text(source_path, dirs, stem)
    elif suffix in CSV_EXTENSIONS:
        outputs = extract_csv(source_path, dirs, stem)
    elif suffix in XLSX_EXTENSIONS:
        outputs = extract_xlsx(source_path, dirs, stem)
    elif suffix in IMAGE_EXTENSIONS:
        if no_ocr or not ocr_endpoint:
            outputs = extract_image(source_path, dirs, stem)
        else:
            outputs = extract_via_ocr(source_path, dirs, stem, ocr_endpoint, is_pdf=False)
    elif suffix in PDF_EXTENSIONS:
        if no_ocr or not ocr_endpoint:
            outputs = extract_basic_metadata(source_path, dirs, stem)
        else:
            outputs = extract_via_ocr(source_path, dirs, stem, ocr_endpoint, is_pdf=True)
    else:
        outputs = extract_basic_metadata(source_path, dirs, stem)

    metadata_path = dirs["metadata"] / f"{stem}.metadata.json"
    outputs["metadata"] = str(metadata_path)
    return outputs


def build_metadata(
    source_path: Path,
    device_name: str,
    detected_at: str | None,
    status: str,
    outputs: dict,
    error: dict | None,
) -> dict:
    return {
        "source_path": str(source_path),
        "source_name": source_path.name,
        "source_type": source_path.suffix.lower().lstrip(".") or "unknown",
        "device_name": device_name,
        "detected_at": detected_at or now_iso(),
        "processed_at": now_iso(),
        "status": status,
        "outputs": outputs,
        "error": error,
    }


def write_metadata(metadata: dict, output_dir: Path, source_path: Path) -> Path:
    dirs = ensure_dirs(output_dir)
    output_metadata = metadata.get("outputs", {}).get("metadata")
    metadata_path = Path(
        output_metadata or dirs["metadata"] / f"{safe_stem(source_path)}.metadata.json"
    )
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    metadata_path.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return metadata_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("legacy_input", nargs="?", help="이전 형식의 입력 파일 경로")
    parser.add_argument("--input", dest="input_path", help="처리할 입력 파일 경로")
    parser.add_argument("--device-name", default="unknown", help="장비명")
    parser.add_argument("--output-dir", default="data/processed", help="추출 결과 저장 루트")
    parser.add_argument("--detected-at", help="감지 시각 ISO 문자열")
    parser.add_argument("--ocr-endpoint", default="http://192.168.219.100:7870", help="기가바이트 OCR API 엔드포인트")
    parser.add_argument("--no-ocr", action="store_true", help="원격 OCR 연동을 생략하고 로컬 추출만 수행")
    args = parser.parse_args()

    input_value = args.input_path or args.legacy_input
    if not input_value:
        parser.error("--input is required")

    source_path = Path(input_value).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser()
    if not output_dir.is_absolute():
        output_dir = Path.cwd() / output_dir

    if not source_path.exists():
        error = {
            "type": "FileNotFoundError",
            "message": f"input file not found: {source_path}",
            "return_code": 1,
        }
        metadata = build_metadata(
            source_path,
            args.device_name,
            args.detected_at,
            "failed",
            {"text": None, "tables": [], "metadata": None},
            error,
        )
        write_metadata(metadata, output_dir, source_path)
        print(error["message"], file=sys.stderr)
        return 1

    try:
        outputs = run_extraction(source_path, output_dir, args.no_ocr, args.ocr_endpoint)
        metadata = build_metadata(
            source_path,
            args.device_name,
            args.detected_at,
            "success",
            outputs,
            None,
        )
        metadata_path = write_metadata(metadata, output_dir, source_path)
        print(f"metadata={metadata_path}")
        return 0
    except Exception as exc:
        error = {
            "type": exc.__class__.__name__,
            "message": str(exc),
            "return_code": 1,
        }
        metadata = build_metadata(
            source_path,
            args.device_name,
            args.detected_at,
            "failed",
            {"text": None, "tables": [], "metadata": None},
            error,
        )
        metadata_path = write_metadata(metadata, output_dir, source_path)
        print(f"extraction failed; metadata={metadata_path}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
