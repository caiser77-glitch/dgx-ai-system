import sys
import os
import zipfile

# server 디렉토리를 path에 추가합니다.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.hwpx_builder import HwpxBuilder

def test_hwpx_generation():
    template_dir = "/Users/nams/AI_BASE/Fauna_Dashboard/server/utils/hwpx_templates"
    database_path = "/Users/nams/AI_BASE/Fauna_Dashboard/server/database.json"
    report_markdown_path = "/Users/nams/AI_BASE/Fauna_Workspace/2_결과_최종보고서.md"

    print("HWPX 빌더 테스트를 시작합니다.")
    builder = HwpxBuilder(
        template_dir=template_dir,
        database_path=database_path,
        report_markdown_path=report_markdown_path
    )

    try:
        # 모든 조사 데이터를 기준으로 HWPX 스트림을 빌드합니다.
        hwpx_stream = builder.build(survey_id="all", is_cumulative=False)
        data = hwpx_stream.getvalue()
        
        # 실물 파일로 디스크에 저장합니다.
        output_file_path = "/Users/nams/AI_BASE/Fauna_Dashboard/server/fauna_report_test.hwpx"
        with open(output_file_path, "wb") as out_f:
            out_f.write(data)
        print(f"실물 HWPX 파일 저장 완료: {output_file_path}")
        
        print(f"생성된 파일 크기: {len(data)} 바이트.")
        assert len(data) > 0, "생성된 데이터 크기가 0바이트입니다."

        # ZIP 파일 유효성 검증
        is_zip = zipfile.is_zipfile(hwpx_stream)
        print(f"유효한 ZIP 압축 구조 검증 결과: {is_zip}.")
        assert is_zip, "유효한 ZIP 파일 구조가 아닙니다."

        # 내부에 들어있는 핵심 XML 파일 구조가 깨지지 않았는지 zipfile을 열어서 확인합니다.
        hwpx_stream.seek(0)
        with zipfile.ZipFile(hwpx_stream, 'r') as z:
            namelist = z.namelist()
            print("ZIP 내부 파일 목록:")
            for name in namelist:
                print(f" - {name}")
            
            assert "Contents/section0.xml" in namelist, "Contents/section0.xml 파일이 존재하지 않습니다."
            assert "Contents/header.xml" in namelist, "Contents/header.xml 파일이 존재하지 않습니다."

            # section0.xml 파싱에 오류가 없는지 검증합니다.
            sec_content = z.read("Contents/section0.xml")
            import xml.etree.ElementTree as ET
            ET.fromstring(sec_content)
            print("section0.xml 파싱 성공.")

        print("모든 HWPX 빌더 무결성 검증 테스트를 성공적으로 통과하였습니다.")
    except Exception as e:
        print(f"테스트 실패: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_hwpx_generation()
