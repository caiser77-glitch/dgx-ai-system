# 야장 데이터를 마크다운(MD)으로 변환하는 스크립트
import re
import sys
import os

def convert(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return False

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    md_content = []
    current_survey = ""
    
    # 분류군 매핑 (한글 -> 알파벳 순서)
    sub_map = {
        "포유류": "가",
        "조류": "나",
        "어류": "다",
        "양서파충류": "라",
        "저서무척추": "마"
    }

    for line in lines:
        line = line.strip()
        if not line or line.startswith('---'):
            continue

        # 차수 추출 (예: --- [ 1차 조사: 봄 (4월 15일) ] ---)
        survey_match = re.search(r'\[ (.*?) \]', line)
        if survey_match:
            current_survey = survey_match.group(1)
            # 차수 번호 부여 (1차, 2차...)
            idx = re.search(r'(\d)차', current_survey)
            survey_num = idx.group(1) if idx else "0"
            md_content.append(f"**{survey_num})** {current_survey}")
            continue

        # 분류군 추출 (예: |- 포유류(10종): ...)
        group_match = re.search(r'\|\- (.*?)\((\d+)종\): (.*)', line)
        if group_match:
            group_name = group_match.group(1)
            count = group_match.group(2)
            species_data = group_match.group(3)
            
            alpha = sub_map.get(group_name, "ㅎ")
            md_content.append(f"**{alpha})** {group_name} ({count}종)")
            
            # 특이사항(Note) 처리: 만약 줄 끝에 *가 있다면 먼저 추출
            note_match = re.search(r'\* (.*)', species_data)
            if note_match:
                note_text = note_match.group(1)
                species_data = species_data.replace(f"* {note_text}", "").strip()
                md_content.append(f"※ {note_text}")

            # 종 목록을 ◦ 기호로 변환
            # 데이터 예시: 수달(D, 2), 고라니(V, 3)
            species_list = species_data.split(', ')
            for species in species_list:
                if species.strip():
                    md_content.append(f"◦ {species.strip()}")
            continue

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_content))
    
    print(f"[+] Converted: {input_path} -> {output_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv)  3:
        print("Usage: python3 convert_field_to_md.py input_txt output_md")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
