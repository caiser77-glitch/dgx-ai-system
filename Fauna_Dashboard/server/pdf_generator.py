# pdf_generator.py: 생태 조사 데이터를 기반으로 전문가용 PDF 보고서를 생성하는 모듈입니다.
import json
from fpdf import FPDF
import os

class EcologicalReport(FPDF):
    def __init__(self, font_name):
        super().__init__()
        self.font_name = font_name

    def header(self):
        try:
            self.set_font(self.font_name, "B", 10)
        except:
            self.set_font("Arial", "B", 10)
        self.set_text_color(100)
        self.cell(0, 10, "Ecological Survey Analysis Report", ln=True, align="R")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        try:
            self.set_font(self.font_name, "", 8)
        except:
            self.set_font("Arial", "", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section_title(self, title):
        try:
            self.set_font(self.font_name, "B", 16)
        except:
            self.set_font("Arial", "B", 16)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 12, f" {title}", ln=True, fill=True)
        self.ln(5)

    def section_subtitle(self, title):
        try:
            self.set_font(self.font_name, "B", 12)
        except:
            self.set_font("Arial", "B", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

def generate_report(json_path, output_path):
    if not os.path.exists(json_path):
        print(f"Error: JSON file not found at {json_path}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # macOS 시스템 폰트 경로
    font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
    
    pdf = EcologicalReport("Koreafont")
    
    # 폰트 등록 시도 (실패해도 프로그램이 중단되지 않도록 처리)
    try:
        if os.path.exists(font_path):
            pdf.add_font("Koreafont", "", font_path)
            pdf.add_font("Koreafont", "B", font_path) # 동일 폰트를 Bold 스타일로 등록
            print(f"Font loaded successfully: {font_path}")
        else:
            print(f"Warning: Font not found at {font_path}. Using fallback.")
    except Exception as e:
        print(f"Warning: Font loading failed ({e}). Using fallback.")

    pdf.add_page()
    
    # Title Page
    try:
        pdf.set_font("Koreafont", "B", 24)
    except:
        pdf.set_font("Arial", "B", 24)
    
    pdf.cell(0, 30, data['metadata']['title'], ln=True, align="C")
    
    try:
        pdf.set_font("Koreafont", "", 12)
    except:
        pdf.set_font("Arial", "", 12)
        
    pdf.cell(0, 10, f"Total Records: {data['metadata']['total_records']}", ln=True, align="C")
    pdf.ln(20)

    # 1. Protected Species Section
    pdf.section_title("1. 법적 보호종 현황 (Protected Species)")
    pdf.section_subtitle("분류별 보호종 목록")
    
    ps = data['protected_species']
    for cls, species in ps['by_class'].items():
        try:
            pdf.set_font("Koreafont", "B", 11)
        except:
            pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 8, f"• {cls}", ln=True)
        
        try:
            pdf.set_font("Koreafont", "", 10)
        except:
            pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 6, ", ".join(species))
        pdf.ln(2)
    pdf.ln(5)

    # 2. Biodiversity Section
    pdf.section_title("2. 생물 다양성 분석 (Biodiversity)")
    pdf.section_subtitle("분류군별 종 구성")
    
    # Table Header
    try:
        pdf.set_font("Koreafont", "B", 10)
    except:
        pdf.set_font("Arial", "B", 10)
        
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(50, 8, "Group", 1, 0, "C", True)
    pdf.cell(40, 8, "Count", 1, 0, "C", True)
    pdf.cell(40, 8, "Species", 1, 1, "C", True)

    try:
        pdf.set_font("Koreafont", "", 10)
    except:
        pdf.set_font("Arial", "", 10)

    for group, info in data['diversity'].items():
        pdf.cell(50, 8, group, 1, 0, "C")
        pdf.cell(40, 8, str(info['total_count']), 1, 0, "C")
        pdf.cell(40, 8, str(info['species_count']), 1, 1, "C")
    pdf.ln(10)

    # 3. Methodology Section
    pdf.section_title("3. 조사 방법론 및 신뢰도 (Methodology)")
    pdf.section_subtitle("증거 유형별 데이터 분포")
    
    try:
        pdf.set_font("Koreafont", "", 10)
    except:
        pdf.set_font("Arial", "", 10)
        
    for key, val in data['traces'].items():
        label = val['label']
        count = val['species_count']
        pdf.cell(0, 8, f"- {label}: {count} species", ln=True)
    
    pdf.output(output_path)
    print(f"Successfully generated report: {output_path}")

if __name__ == "__main__":
    input_json = "/Users/nams/AI_BASE/Fauna_Dashboard/server/injection_payload.json"
    output_pdf = "/Users/nams/AI_BASE/Fauna_Dashboard/server/Ecological_Report.pdf"
    generate_report(input_json, output_pdf)
