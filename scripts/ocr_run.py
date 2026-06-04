import sys
from pathlib import Path
import cv2
import pytesseract
import easyocr

if len(sys.argv) < 2:
    print("사용법: python scripts/ocr_run.py uploads/이미지파일.png")
    sys.exit(1)

input_path = Path(sys.argv[1])
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

img = cv2.imread(str(input_path))
if img is None:
    raise FileNotFoundError(f"이미지를 읽을 수 없습니다: {input_path}")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
binary = cv2.medianBlur(binary, 3)

processed_path = output_dir / f"{input_path.stem}_processed.png"
cv2.imwrite(str(processed_path), binary)

# 1) Tesseract OCR
tess_text = pytesseract.image_to_string(
    binary,
    lang="kor+eng",
    config="--psm 6"
).strip()

# 2) EasyOCR
reader = easyocr.Reader(["ko", "en"], gpu=False)
easy_results = reader.readtext(binary)

easy_lines = []
for bbox, text, prob in easy_results:
    if prob >= 0.25:
        easy_lines.append(text)

easy_text = "\n".join(easy_lines).strip()

# 3) 둘 다 저장
tess_out = output_dir / f"{input_path.stem}_ocr_tesseract.txt"
easy_out = output_dir / f"{input_path.stem}_ocr_easyocr.txt"
final_out = output_dir / f"{input_path.stem}_ocr.txt"

tess_out.write_text(tess_text, encoding="utf-8")
easy_out.write_text(easy_text, encoding="utf-8")

combined = f"""[TESSERACT_RESULT]
{tess_text}

[EASYOCR_RESULT]
{easy_text}
"""

final_out.write_text(combined, encoding="utf-8")

print(f"전처리 이미지: {processed_path}")
print(f"Tesseract 결과: {tess_out}")
print(f"EasyOCR 결과: {easy_out}")
print(f"하이브리드 OCR 결과: {final_out}")
