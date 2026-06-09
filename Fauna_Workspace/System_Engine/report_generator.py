# -*- coding: utf-8 -*-
"""
🌿 생태조사 결과 보고서 생성기 (수동 파서 표준 표준본)

[안내 및 아키텍처 연계성]
- 이 스크립트는 텍스트 파일 형태의 수동 야장 기록('1_입력_야장기록.txt')을 파싱하여
  최종 마크다운 결과 보고서('2_결과_최종보고서.md')를 로컬에서 그리기 위한 "수동 실행 표준 도구"입니다.
- 실제 프로덕션 대시보드 API 및 연산 파이프라인은 'Fauna_Workspace/System_Engine/swarm_orchestrator.py'가
  중심이 되어 구동되므로, 자동화 파이프라인 수정 시에는 swarm_orchestrator.py를 참조하십시오.
- 이 파일은 과거에 다수 존재하던 'report_generator_*.py' 계열의 과도기 스크립트 중 
  가장 문법적으로 완벽한 'final.py'를 토대로 사소한 날짜 오타를 수정한 최종 통합형 버전입니다.
"""

import os
import re
import pandas as pd
from datetime import datetime

class FieldNoteParser:
    def __init__(self, input_path):
        self.input_path = input_path
        self.data = []

    def parse(self):
        if not os.path.exists(self.input_path):
            print(f"Error: File not found {self.input_path}")
            return None

        with open(self.input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        current_survey = "Unknown"
        current_location = "Unknown"
        
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # 1. Detect Survey Header (e.g., [ 1차 조사: 봄 (4월 15일) ])
            if line.startswith('---') and line.endswith('---'):
                match = re.search(r'\[\s*(.*?)\s*\]', line)
                if match:
                    current_survey = match.group(1)
                continue

            # 2. Detect Location (e.g., 조사 지역: 한강수계 A구역 및 주변 산림)
            if line.startswith("조사 지역:"):
                current_location = line.replace("조사 지역:", "").strip()
                continue

            # 3. Detect Group Data (e.g., - 포유류(10종): 수달(D, 2), ...)
            if line.startswith("-"):
                group_match = re.match(r'-\s*([^\(]+)\((\d+)종\):\s*(.*)', line)
                if group_match:
                    group_name = group_match.group(1).strip()
                    species_count_in_group = int(group_match.group(2))
                    species_str = group_match.group(3)

                    species_list = []
                    # Regex to find: Name(Status, Count)
                    sp_matches = re.findall(r'([^,(]+)\(([^,]+),\s*(\d+)\)', species_str)
                    for sp in sp_matches:
                        species_list.append({
                            "name": sp[0].strip(),
                            "status": sp[1].strip(),
                            "count": int(sp[2].strip())
                        })

                    self.data.append({
                        "survey": current_survey,
                        "location": current_location,
                        "group": group_name,
                        "group_species_count": species_count_in_group,
                        "species_details": species_list
                    })

        return self.data

class ReportGenerator:
    def __init__(self, data, output_path):
        self.data = data
        self.output_path = output_path

    def generate(self):
        if not self.data:
            print("No data to generate report.")
            return

        report = []
        report.append("# 🌿 생태조사 최종 결과 보고서")
        # 오타 수정 완료: %Y-%m_d -> %Y-%m-%d
        report.append(f"**생성 일시:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.append("---\n")

        # Summary Stats
        all_species_set = set()
        total_individuals = 0
        for entry in self.data:
            for sp in entry['species_details']:
                all_species_set.add(sp['name'])
                total_individuals += sp['count']
        
        report.append("## 🔍 조사 요약 (Executive Summary)\n")
        
        # Count how many surveys processed
        surveys_processed = len(set(d['survey'] for d in self.data))
        
        report.append(f"- **총 조사 차수:** {surveys_processed}차")
        report.append(f"- **확인된 총 종 수:** {len(all_species_set)}종")
        report.append(f"- **총 발견 개체수:** {total_individuals}개체\n")
        report.append("---\n")

        # Detailed Section
        report.append("## 📋 차수별 상세 조사 결과\n")
        
        current_survey_name = ""
        for entry in self.data:
            if entry['survey'] != current_survey_name:
                current_survey_name = entry['survey']
                report.append(f"### 📍 {current_survey_name} ({entry['location']})")
            
            report.append(f"**[{entry['group']}]**")
            for sp in entry['species_details']:
                report.append(f"- {sp['name']} ({sp['status']}, {sp['count']}개체)")
            report.append("")

        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(report))
        
        print(f"✅ Report successfully generated: {self.output_path}")

if __name__ == "__main__":
    import sys
    # Use the correct input path provided by the user
    input_f = "/Users/nams/AI_BASE/Fauna_Workspace/1_입력_야장기록.txt"
    output_f = "/Users/nams/AI_BASE/Fauna_Workspace/2_결과_최종보고서.md"
    
    parser = FieldNoteParser(input_f)
    parsed_data = parser.parse()
    
    if parsed_data:
        generator = ReportGenerator(parsed_data, output_f)
        generator.generate()
    else:
        print("Failed to parse.")
