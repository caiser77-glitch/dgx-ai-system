import os
import xml.etree.ElementTree as ET
import time

def run_analysis():
    base_path = "/Users/nams/AI_BASE"
    kml_path = os.path.join(base_path, "한강수계 수달좌표.kml")
    
    print(f"🚀 [System] 분석을 시작합니다...")
    print(f"📍 [Target KML]: {kml_path}")

    if not os.path.exists(kml_path):
        print(f"❌ [Error] KML 파일을 찾을 수 없습니다: {kml_path}")
        return

    # 1. KML 데이터 파싱
    try:
        tree = ET.parse(kml_path)
        root = tree.getroot()
        ns = {'kml': 'http://www.opengis.net/kml/2.2'}
        coords = []
        for coord_text in root.findall('.//kml:coordinates', ns):
            if coord_text is not None:
                parts = coord_text.text.strip().split()
                for p in parts:
                    c = p.split(',')
                    if len(c) >= 2:
                        coords.append((float(c[1]), float(c[0])))
        count = len(coords)
        print(f"✨ [Success] {count}개의 좌표를 추출했습니다.")
    except Exception as e:
        print(f"❌ [Error] KML 파싱 중 오류 발생: {e}")
        return

    # 2. 통계 분석 (Centroid & Density)
    print(f"🧪 [Step 2] 통계 분석 중...")
    time.sleep(1)
    avg_lat = sum(c[0] for c in coords) / count
    avg_lon = sum(c[1] for c in coords) / count
    
    # 3. 결과 보고서 생성 (Markdown)
    output_filename = "analysis_result.md"
    filepath = os.path.join(base_path, output_filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# 📊 [실전 분석 보고서] KML 데이터 기반 통계\n\n")
            f.write(f"## 1. 데이터 규모\n- **관측 지점 수**: {count}개\n\n")
            f.write(f"## 2. 통계적 분석 결과\n")
            f.write(f"| 항목 | 상세 수치 |\n| :--- | :--- |\n")
            f.write(f"| 총 관측 지점 수 | {count}개 |\n")
            f.write(f"| 중심 위도 (Lat) | {avg_lat:.6f} |\n")
            f.write(f"| 중심 경도 (Lon) | {avg_lon:.6f} |\n\n")
            f.write(f"## 3. 결론 및 제언\n")
            f.write(f"- {count}개의 실측 데이터가 성공적으로 분석되었습니다.\n")
            f.write(f"- 이 통계적 근거는 향후 '최적 저감 전략'의 기초가 됩니다.\n")
        print(f"✅ [Success] 보고서가 저장되었습니다: {filepath}")
    except Exception as e:
        print(f"❌ [Error] 파일 저장 중 오류 발생: {e}")

if __name__ == "__main__":
    run_analysis()
