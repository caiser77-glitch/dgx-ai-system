import pandas as pd
import os
import json
import numpy as np

# 통합된 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, 'data', '2025년 국가생물종목록_v1.0.xlsx')
OUTPUT_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_CSV = os.path.join(OUTPUT_DIR, 'fauna_master_final.csv')
OUTPUT_JSON = os.path.join(OUTPUT_DIR, 'species_search_index.json')

def refine_master_database():
    print(f"🔍 마스터 데이터 정밀 가공 시작 (통합 폴더 구조)...")
    if not os.path.exists(INPUT_FILE):
        print(f"❌ 원본 파일을 찾을 수 없습니다: {INPUT_FILE}")
        return

    try:
        xl = pd.ExcelFile(INPUT_FILE)
        target_sheets = [s for s in xl.sheet_names if s not in ['개요', '통계', '62,604종']]

        full_list = []
        for sheet in target_sheets:
            print(f"📂 가공 중: {sheet}")
            df = pd.read_excel(INPUT_FILE, sheet_name=sheet)
            mapping = {'강': 'Class', '목': 'Order', '과': 'Family', '국명': 'Korean_Name', '학명': 'Scientific_Name'}

            # Rename columns based on mapping
            new_cols = {}
            for col in df.columns:
                for k, v in mapping.items():
                    if k in str(col):
                        new_cols[col] = v
            df.rename(columns=new_cols, inplace=True)

            cols = [c for c in ['Class', 'Order', 'Family', 'Korean_Name', 'Scientific_Name'] if c in df.columns]
            temp_df = df[cols].copy()
            if 'Class' not in temp_df.columns:
                temp_df['Class'] = sheet
            full_list.append(temp_df)

        if not full_list:
            print("❌ 가공할 시트가 없습니다.")
            return

        final_df = pd.concat(full_list, ignore_index=True)
        final_df = final_df.dropna(subset=['Korean_Name'])
        final_df['Korean_Name'] = final_df['Korean_Name'].astype(str).str.strip()
        final_df = final_df.drop_duplicates(subset=['Korean_Name'])

        # --- [CRITICAL FIX] JSON-safe handling: Replace NaN with None (becomes null in JSON) ---
        # This prevents the "Unexpected token 'N' (NaN)" error in JavaScript.
        final_df = final_df.replace({np.nan: None})

        if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
        final_df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')

        search_index = final_df.set_index('Korean_Name').to_dict('index')
        with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
            json.dump(search_index, f, ensure_ascii=False, indent=2)

        print("-" * 4_000)
        print(f"✅ 통합 가공 완료: {len(final_df)} 종 인덱싱됨")
        print("-" * 4_000)

    except Exception as e:
        print(f"❌ 오류: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    refine_master_database()
