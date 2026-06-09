# 분류군별 생물종 통계 및 상세 보고서 생성 엔진
# 이 스크립트는 2025년 국가생물종목록 엑셀 데이터를 읽어 분류군별(포유류, 조류 등)로 통계(목, 과, 종 수)를 산출하고, 상세 종 목록을 분류군별로 분리된 표 형식으로 생성합니다.

import pandas as pd
import os

class TaxonomyReportEngine:
    def __init__(self, excel_path):
        self.excel_path = excel_path
        self.df = None
        self.summary_df = None
        self.group_tables = {}

    def load_data(self):
        print(f"🚀 [Step 1] 데이터 로드 중: {self.excel_path}")
        try:
            # '62,604종' 시트 로드
            self.df = pd.read_excel(self.excel_path, sheet_name='62,604종')
            
            # 컬럼명 정규화 (Unnamed 컬럼 제거 및 의미 있는 이름으로 매핑)
            # 분석 결과에 기반하여 핵심 컬럼만 추출
            column_map = {
                '관리분류군': 'group',
                'Order': 'order',
                'Family': 'family',
                'Species': 'species',
                '대표국명': 'common_name'
            }
            
            # 필요한 컬럼만 필터링 (존재하는 컬럼만)
            existing_cols = [c for c in column_map.keys() if c in self.df.columns]
            self.df = self.df[existing_cols].copy()
            self.df.rename(columns=column_map, inplace=True)
            
            # 결측치 처리 (분류 정보가 없는 경우 '미분류'로 처리)
            self.df.fillna('미분류', inplace=True)
            
            print(f"✅ 데이터 로드 완료. 총 {len(self.df)}개 종 확인.")
        except Exception as e:
            print(f"❌ 데이터 로드 실패: {s}")
            raise e

    def process_taxonomy(self):
        print("📊 [Step 2] 분류군별 통계 산출 및 그룹화 중...")
        
        # 1. 전체 요약 통계 생성 (목, 과, 종 수)
        summary = self.df.groupby('group').agg({
            'order': 'nunique',
            'family': 'nunique',
            'species': 'nunique'
        }).rename(columns={
            'order': '목 수',
            'family': '과 수',
            'species': '종 수'
        })
        self.summary_df = summary.reset_index()

        # 2. 분류군별 상세 테이블 생성
        groups = self.df['group'].unique()
        for group in groups:
            group_data = self.df[self.df['group'] == group][['common_name', 'family', 'order', 'species']]
            self.group_tables[group] = group_data
            
        print(f"✅ {len(self.group_tables)}개 분류군별 데이터 분리 완료.")

    def generate_markdown_report(self, output_path):
        print(f"📝 [Step 3] 마크다운 보고서 생성 중: {output_php}")
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("# 📋 2025 국가생물종 분포 및 분류군 통계 보고서\n\n")
                
                # 1. 전체 요약 표
                f.write("## 1. 분류군별 통계 요약\n")
                f.write("| 분류군 | 목 수 | 과 수 | 종 수 |\n")
                f.write("| :--- | :---: | :---: | :---: |\n")
                for _, row in self.summary_df.iterrows():
                    f.write(f"| {row['group']} | {row['목 수']} | {row['과 수']} | {row['종 수']} |\n")
                f.write("\n")

                # 2. 분류군별 상세 표
                f.write("## 2. 분류군별 상세 종 목록\n")
                for group, table in self.group_tables.items():
                    f.write(f"### 📍 {group} 분류군\n")
                    f.write("| 종명 (대표국명) | 과 | 목 | 종 |\n")
                    f.append_line("| :--- | :--- | :--- | :--- |\n") # Note: pseudo-code logic
                    
                    # 실제 구현에서는 table를 마크다운으로 변란
                    md_table = table.to_markdown(index=False)
                    f.write(md_table + "\n\n")
            
            print(f"✅ 보고서 생성 완료: {output_path}")
        except Exception as e:
            print(f"❌ 보고서 생성 실패: {e}")

if __name__ == "__main__":
    # 실행 테스트
    INPUT_EXCEL = "/Users/nams/AI_BASE/Fauna_Workspace/System_Engine/Legacy_Pipelines/02_Knowledge_DB/2025년 국가생물종목록_v1.0.xlsx"
    OUTPUT_MD = "/Users/nams/AI_BASE/Fauna_Workspace/System_Engine/Legacy_Pipelines/06_Visual_Reporting/taxonomy_report_final.md"
    
    engine = TaxonomyReportEngine(INPUT_EXCEL)
    try:
        engine.load_data()
        engine.process_taxonomy()
        engine.generate_markdown_report(OUTPUT_MD)
    except Exception as err:
        print(f"💥 미완성 엔진 에러: {err}")
