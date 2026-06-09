# -*- coding: utf-8 -*-
"""
Intelligent Report Generation Engine
This engine enhances raw species data with natural language summaries,
providing semantic insights (dominance, richness, etc.) for ecological reports.
"""

import os
import sys
import json
import pandas as pd
from datetime import datetime

class IntelligentReportEngine:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.data = None
        self.report_content = ""

    def load_data(self):
        """Load the structured JSON data."""
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input JSON not found: {self.input_path}")
        
        with open(self.input_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        print(f"✅ Loaded structured data from: {os.path.basename(self.input_path)}")

    def generate_semantic_summary(self) -> str:
        """
        The 'Brain' of the engine: Transforms raw numbers into human-readable narratives.
        """
        if not self.data or 'summary_hierarchy' not in self.data:
            return "No summary data available to interpret."

        summary_list = self.data['summary_hierarchy']
        total_species = self.data['metadata']['total_species_count']
        
        narratives = []
        narrative_header = "## 🔍 조사 요 약 (Executive Summary)\n"
        narr_list = [narrative_header]
        narr_list.append(f"이번 조사를 통해 총 **{total_species:,}종**의 생물 종이 확인되었습니다.")

        # 1. Dominance Analysis
        if summary_list:
            # Find the group with the maximum species count
            max_group = max(summary_list, key=lambda x: x.get('species_count', 0))
            
            # Identify which key contains the name
            group_name = max_group.get('Tax_Name', max_group.get('Taxon_Name', '미분류군'))
            count = max_group.get('species_count', 0)
            
            narr_list.append(f"- **주요 분류군 발견:** 조사된 종 중 가장 높은 빈도를 보인 분류군은 **{group_name}**으로, 총 **{count:,}종**이 관찰되었습니다.")

        # 2. Diversity Analysis
        if len(summary_list) > 1:
            narr_list.append(f"- **분류군 다양성:** 총 {len(summary_list)}개의 주요 분류군 단위가 확인되었습니다.")
        
        return "\n".join(narr_list)

    def generate_full_report(self):
        """Orchestrates the generation of the final Markdown report."""
        if not self.data:
            raise RuntimeError("No data loaded. Call load_data() first.")

        report = []
        report.append("# 🌿 지능형 생태조사 분석 보고서 (Intelligent Analysis Report)")
        report.append(f"**데이터 원본:** `{os.path.basename(self.input_path)}`")
        report.append(f"**분석 일시:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("\n---\n")

        # 1. Semantic Summary Section
        report.append(self.generate_semantic_summary())
        report_sep = "\n---\n"
        report.append(report_sep)

        # 2. Structured Table Section
        report.append("## 📊 Table 1: 분류군별 종 수 상세 요약 (Hierarchical Summary)")
        summary_df = pd.DataFrame(self.data['summary_hierarchy'])
        if not summary_df.empty:
            report.append(summary_df.to_markdown(index=False))
        else:
            report.append("*집계된 요약 데이터가 없습니다.*")

        # 3. Detailed Species List Section
        report.append("\n## 📋 Table 2: 상세 종 목록 (Detailed Species List)")
        report_count_str = f"*총 {self.data['metadata']['total_species_count']:,}종 중 상위 500개를 출력합니다.*"
        report.append(report_count_str)
        
        species_list = self.data['species_list']
        if species_list:
            detailed_df = pd.DataFrame(species_list).head(500)
            cols_to_show = [c for c in ['scientific_name', 'common_name_kr', 'ktsn'] if c in detailed_df.columns]
            if cols_to_show:
                report.append(detailed_df[cols_to_show].to_markdown(index=False))
            else:
                report.append(detailed_df.to_markdown(index=False))
        else:
            report.append("*상세 종 목록 데이터가 비어있습니다.*")

        self.report_content = "\n".join(report)
        
        # Final Write
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(self.report_content)
        
        print(f"🚀 [SUCCESS] Intelligent Report Generated: {self.output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python intelligent_engine.py <input_json_path> <output_md_path>")
    else:
        engine = IntelligentReportEngine(sys.argv[1], sys.argv[2])
        engine.load_data()
        engine.generate_full_report()
        print("✨ Report generation completed successfully.")
