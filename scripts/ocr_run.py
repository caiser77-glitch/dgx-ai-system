import sys
from pathlib import Path
import pytesseract
from PIL import Image
import cv2
import numpy as np

if len(sys.argv) < 2:
    print("사용법: python scripts/ocr_run.py uploads/이미지파일.png")
    sys.exit(1)

input_path = Path(sys.argv[1])
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

img = cv2.imread(str(input_path))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 확대
gray = cv2.resize(gray, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

# 이진화
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# 노이즈 제거
gray = cv2.medianBlur(gray, 3)

processed = output_dir / f"{input_path.stem}_processed.png"
cv2.imwrite(str(processed), gray)

text = pytesseract.image_to_string(gray, lang="kor+eng", config="--psm 6")

out = output_dir / f"{input_path.stem}_ocr.txt"
out.write_text(text, encoding="utf-8")

print(f"전처리 이미지: {processed}")
print(f"OCR 완료: {out}")
