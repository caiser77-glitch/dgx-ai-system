# 보고서 파일(.docx, .hwp)을 마크다운 형식으로 변환하는 스크립트입니다.
import os
from pathlib import Path

def convert_docs_to_md(source_dir, target_dir):
    """
    문서 파일을 읽어 마크다운 형식으로 저장합니다.
    """
    source_path = Path(source_dir).expanduser()
    target_path = Path(target_dir).expanduser()
    target_path.mkdir(parents=True, exist_ok=True)

    print(f"🚀 보고서 변환 시작: {source_path} -> {target_path}")
    
    # 대상 확장자 설정
    extensions = ['*.docx', '*.doc', '*.hwp', '*.hwpx']
    files_to_process = []
    for ext in extensions:
        files_to_process.extend(list(source_path.glob(ext)))

    total = len(files_to_process)
    print(f"📂 총 {total}개의 파일을 발견했습니다.")

    success_count = 0
    error_count = 0

    for i, file_path in enumerate(files_to_process):
        try:
            # 1. 파일명 생성 (원본이름.md)
            md_filename = file_path.stem + ".md"
            dest_file = target_path / md_filename

            # 2. 파일 내용 추출 (간이 방식: 텍스트 기반)
            # 주의: HWP는 별도의 라이브러리나 시스템 명령어가 필요할 수 있습니다.
            # 여기서는 구조적 틀을 잡는 데 집중합니다.
            with open(file_path, 'rb') as f:
                content = f.read().decode('utf-8', errors='ignore')

            # 3. 마크다운 파일로 저장
            with open(dest_file, "w", encoding="utf-8") as f:
                f.write(f"--- \n")
                f.write(f"source: {file_path.name}\n")
                f.write(f"--- \n\n")
                f.write(content)

            success_count += 1
            print(f"[{i+1}/{total}] ✅ 성공: {file_path.name}")

        except Exception as e:
            print(f"[{i+1}/{total}] ❌ 실패: {file_path.name} | 오류: {e}")
            error_count += 1

    print("\n" + "="*30)
    print(f"📊 최종 결과 보고서")
    print(f" - 성공: {success_count}개")
    print(f" - 실패: {error_count}개")
    print("="*30)

if __name__ == "__main__":
    # 경로 설정
    SOURCE = "~/AI_BASE/Work_In_Progress/Organized_Data/Reports"
    TARGET = "~/AI_BASE/03_Processed_Data/Papers_Markdown"
    
    convert_docs_to_md(SOURCE, TARGET)
