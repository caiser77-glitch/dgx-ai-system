import sys
import subprocess
from pathlib import Path
import pandas as pd
import fitz  # PyMuPDF


BASE = Path("/home/caiser77/dgx_workspace")
TMP_DIR = BASE / "outputs" / "_pdf_pages"
TMP_DIR.mkdir(parents=True, exist_ok=True)


def parse_pages(page_text, total_pages):
    """
    입력 예:
    1
    1,3,5
    2-4
    1,3-5,8
    """
    pages = set()

    if not page_text.strip():
        return list(range(1, total_pages + 1))

    for part in page_text.split(","):
        part = part.strip()

        if "-" in part:
            a, b = part.split("-")
            for p in range(int(a), int(b) + 1):
                if 1 <= p <= total_pages:
                    pages.add(p)
        else:
            p = int(part)
            if 1 <= p <= total_pages:
                pages.add(p)

    return sorted(pages)


def render_pdf_pages(pdf_path, pages, dpi=300):
    doc = fitz.open(pdf_path)
    image_paths = []

    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)

    for page_num in pages:
        page = doc[page_num - 1]
        pix = page.get_pixmap(matrix=mat, alpha=False)

        out_img = TMP_DIR / f"{Path(pdf_path).stem}_page_{page_num}.png"
        pix.save(out_img)

        image_paths.append((page_num, out_img))

    return image_paths


def run_taxa_ocr_on_image(image_path):
    subprocess.run(
        ["python", str(BASE / "scripts" / "taxa_table_ocr.py"), str(image_path)],
        check=True,
    )

    return BASE / "outputs" / f"{Path(image_path).stem}_taxa.xlsx"


def combine_excels(results, output_xlsx):
    all_rows = []

    for page_num, xlsx_path in results:
        if not xlsx_path.exists():
            continue

        df = pd.read_excel(xlsx_path)
        df.insert(0, "페이지", page_num)
        df.insert(1, "원본파일", output_xlsx.stem)
        all_rows.append(df)

    if not all_rows:
        raise RuntimeError("OCR 결과가 없습니다.")

    final_df = pd.concat(all_rows, ignore_index=True)
    final_df.to_excel(output_xlsx, index=False)


def main():
    if len(sys.argv) < 3:
        print("사용법:")
        print('python scripts/taxa_pdf_ocr.py uploads/sample.pdf "1,3-5"')
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    page_text = sys.argv[2]

    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    doc.close()

    pages = parse_pages(page_text, total_pages)

    if not pages:
        raise RuntimeError("선택된 페이지가 없습니다.")

    print(f"선택 페이지: {pages}")

    rendered = render_pdf_pages(pdf_path, pages)

    results = []
    for page_num, image_path in rendered:
        print(f"OCR 처리 중: page {page_num}")
        xlsx = run_taxa_ocr_on_image(image_path)
        results.append((page_num, xlsx))

    output_xlsx = BASE / "outputs" / f"{pdf_path.stem}_pages_{page_text.replace(',', '_').replace('-', 'to')}_taxa.xlsx"
    combine_excels(results, output_xlsx)

    print(f"PDF 분류군 OCR 완료: {output_xlsx}")


if __name__ == "__main__":
    main()
