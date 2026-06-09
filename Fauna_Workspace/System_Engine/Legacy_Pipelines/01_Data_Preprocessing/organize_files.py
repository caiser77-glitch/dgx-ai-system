import os
import shutil
from pathlib import Path

def organize_data():
    # 1. 경로 설정
    source_root = Path('~/AI_BASE/Raw_Data').expanduser()
    target_root = Path('~/AI_BASE/Work_In_Progress/Organized_Data').expanduser()

    # 2. 목적지 폴더 생성
    sub_folders = ['Papers', 'Reports', 'Data']
    for folder in sub_folders:
        (target_root / folder).mkdir(parents=True, exist_ok=True)

    print(f"🚀 작업 시작: {source_root} -> {target_root}")

    # 3. 파일 탐색 및 분류
    count = {'Papers': 0, 'Reports': 0, 'Data': 0, 'Other': 0}

    # rglob('*')를 사용하여 모든 하위 파일 탐색
    for file_path in source_root.rglob('*'):
        if file_path.is_dir():
            continue
        
        # 확장자 확인
        ext = file_path.suffix.lower()

        # 분류 로직
        target_subfolder = 'Other'
        
        if ext in ['.pdf', '.docx', '.doc']:
            target_subfolder = 'Papers'
        elif ext in ['.hwp', '.hwpx']:
            target_subfolder = 'Reports'
        elif ext in ['.xlsx', '.xls', '.kml', '.zip', '.txt']:
            target_subfolder = 'Data'

        # 파일 복사 실행
        if target_subfolder != 'Other':
            dest_path = target_root / target_subfolder / file_path.name
            
            # 파일명 중복 방지 (동일 이름이 있을 경우 숫자 추가)
            if dest_path.exists():
                dest_path = target_root / target_subfolder / f"copy_{file_path.name}"
            
            try:
                shutil.copy2(file_path, dest_path)
                count[target_subfolder] += 1
            except Exception as e:
                print(f"❌ 오류 발생 ({file_path.name}): {e}")
        else:
            count['Other'] += 1

    print("\n✅ 작업 완료 보고서:")
    for folder, num in count.items():
        print(f" - {folder}: {num}개 파일 복사됨")
    print(f" - 기타(제외): {count['Other']}개 파일")
    print("\n💡 다음 단계: 'Papers' 폴더의 PDF를 마크다운으로 변환할 준비가 되었습니다.")

if __name__ == "__main__":
    organize_data()

