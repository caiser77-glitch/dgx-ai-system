import sys
from pathlib import Path
import pandas as pd

if len(sys.argv) < 2:
    print("사용법: python scripts/excel_summary.py uploads/파일.xlsx")
    sys.exit(1)

input_path = Path(sys.argv[1])
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

df = pd.read_excel(input_path)
summary = df.describe(include="all")

out = output_dir / f"{input_path.stem}_summary.xlsx"
summary.to_excel(out)

print(f"Excel 요약 완료: {out}")
