import re
import pandas as pd
import os

# 1. 원본 데이터 (실제로는 야장에서 가져온 텍스트라고 가정)
raw_data = [
    {"species": "참매", "entry": "V (1)"},
    {"species": "청개구리", "entry": "D, V (3)"},
    {"species": "너구리", "entry": "F, D, S (2)"},
    {"species": "수달", "entry": "V (1)"}
]

def parse_fauna_entry(raw_string):
    """텍스트에서 흔적 유형과 개체수를 분리하는 함수"""
    # 개체수 추출 (괄호 안의 숫자)
    count_match = re.search(r'\((\d+)\)', raw_string)
    count = int(count_match.group(1)) if count_match else 1
    
    # 흔적 유형 추출 (V, D, F, S 등)
    clean_str = re.sub(r'\(\d+\)', '', raw_string)
    traces = [t.strip() for t in clean_str.split(',') if t.strip()]
    
    return {"traces": ", ".join(traces), "count": count}

# 2. 데이터 변환 로직
processed_rows = []
for item in raw_data:
    parsed = parse_fauna_entry(item['entry'])
    processed_rows.append({
        "species": item['species'],
        "traces": parsed['traces'],
        "count": parsed['count']
    })

# 3. 결과 저장 (CSV 파일로 생성)
df = pd.DataFrame(processed_rows)
output_path = "processed_data.csv"
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"✅ 작업 완료! '{output_path}' 파일이 생성되었습니다.")
print(df)
