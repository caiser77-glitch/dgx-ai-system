from collections import defaultdict
import os
import zipfile
import io
import json
import random
import xml.etree.ElementTree as ET

class HwpxBuilder:
    def __init__(self, template_dir: str, database_path: str, report_markdown_path: str):
        self.template_dir = template_dir
        self.database_path = database_path
        self.report_markdown_path = report_markdown_path

    def _parse_inline_bold(self, text: str) -> list:
        # ** 기호를 기준으로 볼드체 여부를 분석하여 (is_bold, text_chunk) 튜플 리스트를 반환합니다.
        if not text:
            return []
        
        chunks = []
        parts = text.split("**")
        for idx, part in enumerate(parts):
            if not part:
                continue
            is_bold = (idx % 2 == 1)
            chunks.append((is_bold, part))
        return chunks

    def _parse_markdown(self) -> list:
        # 마크다운 리포트 문서를 파싱하여 한글 문단 속성 목록을 반환합니다.
        parsed = []
        if not os.path.exists(self.report_markdown_path):
            return [("p", "분석 리포트가 존재하지 않습니다.", 0, "0")]

        current_table = []
        in_table = False

        with open(self.report_markdown_path, "r", encoding="utf-8") as f:
            for line in f:
                line_strip = line.strip()
                
                # 1. 마크다운 표 서식 (| 종명 |... 또는 |:---:|) 파싱
                if line_strip.startswith("|") and line_strip.endswith("|"):
                    # 구분선 행 (예: | --- |:---:|) 은 파싱에서 배제
                    if "---" in line_strip:
                        continue
                    
                    # 각 셀의 값 추출
                    cells = [c.strip() for c in line_strip.split("|")[1:-1]]
                    current_table.append(cells)
                    in_table = True
                    continue
                else:
                    # 표 수집이 끝난 상황이면 parsed에 추가
                    if in_table and current_table:
                        parsed.append(("table", current_table, 0, "0"))
                        current_table = []
                        in_table = False
                    
                    if not line_strip:
                        continue
                    
                    # 2. 마크다운 가로 구분선 (--- 또는 ***) 생략 처리 (본문)
                    if line_strip in ["---", "***"] or (line_strip.startswith("---") and line_strip.endswith("---")):
                        continue
                    
                    # 들여쓰기 수준 계산
                    raw_indent = len(line) - len(line.lstrip())
                    
                    # 3. 텍스트 내 백틱 ` 제거하되 볼드체 기호 **는 유지!
                    clean_line = line_strip.replace("`", "")
                    
                    # 4. 제목 서식 및 개요 파싱 지원
                    if clean_line.startswith("===") and clean_line.endswith("==="):
                        parsed.append(("h1", clean_line.replace("===", "").strip(), 0, "0"))
                    elif clean_line.startswith("[") and clean_line.endswith("]"):
                        parsed.append(("h2", clean_line[1:-1].strip(), 0, "0"))
                    elif clean_line.startswith("# "):
                        parsed.append(("h1", clean_line[2:], 0, "0"))
                    elif clean_line.startswith("## "):
                        parsed.append(("h2", clean_line[3:], 0, "0"))
                    elif clean_line.startswith("### "):
                        parsed.append(("h3", clean_line[4:], 0, "0"))
                    elif clean_line.startswith("*   "):
                        # 리스트 항목 (예: *   국명: 삵)
                        text_val = "● " + clean_line[4:].strip()
                        parsed.append(("p", text_val, 0, "0"))
                    elif raw_indent >= 4 and (clean_line.startswith("1)") or clean_line.startswith("2)") or clean_line.startswith("3)") or clean_line.startswith("4)")):
                        # 4대 요소 상세 명세서와 같은 깊은 들여쓰기가 있는 번호 리스트
                        parsed.append(("p", clean_line, 1, "2"))
                    elif clean_line.startswith("- "):
                        text_val = "● " + clean_line[2:].strip()
                        parsed.append(("p", text_val, 0, "0"))
                    elif clean_line.startswith("* "):
                        text_val = "● " + clean_line[2:].strip()
                        parsed.append(("p", text_val, 0, "0"))
                    else:
                        para_pr = "2" if raw_indent >= 4 else "0"
                        parsed.append(("p", clean_line, 1 if raw_indent >= 4 else 0, para_pr))
            
            # 파일이 끝났을 때 마지막 표가 남아 있다면 처리
            if in_table and current_table:
                parsed.append(("table", current_table, 0, "0"))
                
        return parsed

    def _load_database_data(self, survey_id: str, is_cumulative: bool) -> dict:
        # 데이터베이스의 생태 관찰 정보를 읽고 분류군 순서에 맞춰 정렬하여 반환합니다.
        if not os.path.exists(self.database_path):
            return {}
        
        with open(self.database_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        import re
        clean_sid_str = "all"
        if survey_id != "all":
            digits = re.findall(r'\d+', str(survey_id))
            if digits:
                clean_sid_str = digits[0]

        filtered = []
        for item in data:
            if clean_sid_str == "all":
                filtered.append(item)
            else:
                try:
                    s_id = int(clean_sid_str)
                    item_s_id = int(item.get("surveyId", 0))
                    if is_cumulative:
                        if item_s_id <= s_id:
                            filtered.append(item)
                    else:
                        if item_s_id == s_id:
                            filtered.append(item)
                except (ValueError, TypeError):
                    continue

        class_order = {"포유류": 1, "조류": 2, "어류": 3, "양서파충류": 4, "저서무척추": 5}
        
        grouped = defaultdict(list)
        for item in filtered:
            grouped[item.get("class", "미분류")].append(item)
            
        for c_name in grouped:
            grouped[c_name] = sorted(
                grouped[c_name],
                key=lambda x: (x.get("family", ""), x.get("species", ""))
            )
        
        return dict(sorted(grouped.items(), key=lambda x: class_order.get(x[0], 99)))

    def _inject_custom_styles_to_header(self, header_path: str) -> bytes:
        ET.register_namespace('hh', 'http://www.hancom.co.kr/hwpml/2011/head')
        ET.register_namespace('hc', 'http://www.hancom.co.kr/hwpml/2011/core')
        
        tree = ET.parse(header_path)
        root = tree.getroot()
        
        ns = {
            'hh': 'http://www.hancom.co.kr/hwpml/2011/head',
            'hc': 'http://www.hancom.co.kr/hwpml/2011/core'
        }
        
        # 1. charPr 추가
        char_properties = root.find('.//hh:charProperties', ns)
        if char_properties is not None:
            # 기존 id가 50 이상인 것들 지우고 새로 추가 (중복 방지)
            for char_pr in list(char_properties.findall('hh:charPr', ns)):
                if char_pr.attrib.get('id') in ['50', '51', '52', '53', '54', '55', '56']:
                    char_properties.remove(char_pr)
            
            # 스타일 정의
            char_styles = [
                # ID, height, bold, textColor
                ('50', '1600', '1', '#1B365D'), # H1 (16pt, bold, Navy)
                ('51', '1300', '1', '#2E5B88'), # H2 (13pt, bold, SlateBlue)
                ('52', '1100', '1', '#333333'), # H3 (11pt, bold, DarkGray)
                ('53', '1000', '1', '#000000'), # 본문 강조 (10pt, bold)
                ('54', '1000', '0', '#222222'), # 본문 기본 (10pt, normal)
                ('55', '950', '1', '#1B365D'),  # 표 헤더 (9.5pt, bold, Navy)
                ('56', '950', '0', '#333333'),  # 표 바디 (9.5pt, normal)
            ]
            
            for pr_id, height, bold, color in char_styles:
                char_pr = ET.Element('{http://www.hancom.co.kr/hwpml/2011/head}charPr', {
                    'id': pr_id,
                    'height': height,
                    'textColor': color,
                    'shadeColor': 'none',
                    'useFontSpace': '0',
                    'useKerning': '0',
                    'symMark': 'NONE',
                    'borderFillIDRef': '2',
                    'bold': bold
                })
                ET.SubElement(char_pr, '{http://www.hancom.co.kr/hwpml/2011/head}fontRef', {
                    'hangul': '3', 'latin': '3', 'hanja': '2', 'japanese': '3', 'other': '3', 'symbol': '3', 'user': '3'
                })
                ET.SubElement(char_pr, '{http://www.hancom.co.kr/hwpml/2011/head}ratio', {
                    'hangul': '100', 'latin': '100', 'hanja': '100', 'japanese': '100', 'other': '100', 'symbol': '100', 'user': '100'
                })
                ET.SubElement(char_pr, '{http://www.hancom.co.kr/hwpml/2011/head}spacing', {
                    'hangul': '0', 'latin': '0', 'hanja': '0', 'japanese': '0', 'other': '0', 'symbol': '0', 'user': '0'
                })
                ET.SubElement(char_pr, '{http://www.hancom.co.kr/hwpml/2011/head}relSz', {
                    'hangul': '100', 'latin': '100', 'hanja': '100', 'japanese': '100', 'other': '100', 'symbol': '100', 'user': '100'
                })
                ET.SubElement(char_pr, '{http://www.hancom.co.kr/hwpml/2011/head}offset', {
                    'hangul': '0', 'latin': '0', 'hanja': '0', 'japanese': '0', 'other': '0', 'symbol': '0', 'user': '0'
                })
                ET.SubElement(char_pr, '{http://www.hancom.co.kr/hwpml/2011/head}underline', {
                    'type': 'NONE', 'shape': 'SOLID', 'color': '#000000'
                })
                ET.SubElement(char_pr, '{http://www.hancom.co.kr/hwpml/2011/head}strikeout', {
                    'shape': 'NONE', 'color': '#000000'
                })
                ET.SubElement(char_pr, '{http://www.hancom.co.kr/hwpml/2011/head}outline', {
                    'type': 'NONE'
                })
                ET.SubElement(char_pr, '{http://www.hancom.co.kr/hwpml/2011/head}shadow', {
                    'type': 'NONE', 'color': '#C0C0C0', 'offsetX': '10', 'offsetY': '10'
                })
                char_properties.append(char_pr)
            
            char_properties.attrib['itemCnt'] = str(len(char_properties))

        # 2. paraPr 추가
        para_properties = root.find('.//hh:paraProperties', ns)
        if para_properties is not None:
            # 기존 id가 50 이상인 것들 지우고 새로 추가
            for para_pr in list(para_properties.findall('hh:paraPr', ns)):
                if para_pr.attrib.get('id') in ['50', '51', '52', '54', '55', '56', '57']:
                    para_properties.remove(para_pr)
            
            # 파라미터 구조
            # ID, align(LEFT/JUSTIFY/CENTER), prev(위여백), next(아래여백), leftMargin(왼쪽여백), indent(내어쓰기/들여쓰기), lineSpacing(줄간격)
            para_styles = [
                ('50', 'LEFT', '1500', '800', '0', '0', '130'),   # H1
                ('51', 'LEFT', '1000', '500', '0', '0', '130'),   # H2
                ('52', 'LEFT', '800', '400', '0', '0', '130'),    # H3
                ('54', 'JUSTIFY', '0', '300', '0', '0', '160'),   # 본문
                ('55', 'CENTER', '0', '0', '0', '0', '120'),      # 표 헤더
                ('56', 'CENTER', '0', '0', '0', '0', '120'),      # 표 바디
                ('57', 'JUSTIFY', '0', '200', '1500', '-1000', '150'), # 들여쓰기 리스트
            ]
            
            for pr_id, align_val, prev_val, next_val, left_val, indent_val, spacing_val in para_styles:
                para_pr = ET.Element('{http://www.hancom.co.kr/hwpml/2011/head}paraPr', {
                    'id': pr_id,
                    'tabPrIDRef': '0',
                    'condense': '0',
                    'fontLineHeight': '0',
                    'snapToGrid': '1',
                    'suppressLineNumbers': '0',
                    'checked': '0'
                })
                ET.SubElement(para_pr, '{http://www.hancom.co.kr/hwpml/2011/head}align', {
                    'horizontal': align_val, 'vertical': 'BASELINE'
                })
                ET.SubElement(para_pr, '{http://www.hancom.co.kr/hwpml/2011/head}heading', {
                    'type': 'NONE', 'idRef': '0', 'level': '0'
                })
                ET.SubElement(para_pr, '{http://www.hancom.co.kr/hwpml/2011/head}breakSetting', {
                    'breakLatinWord': 'KEEP_WORD', 'breakNonLatinWord': 'KEEP_WORD',
                    'widowOrphan': '0', 'keepWithNext': '0', 'keepLines': '0',
                    'pageBreakBefore': '0', 'lineWrap': 'BREAK'
                })
                ET.SubElement(para_pr, '{http://www.hancom.co.kr/hwpml/2011/head}autoSpacing', {
                    'eAsianEng': '0', 'eAsianNum': '0'
                })
                
                # margin 및 lineSpacing 구조 구성
                switch_el = ET.SubElement(para_pr, '{http://www.hancom.co.kr/hwpml/2011/paragraph}switch')
                
                # Required-namespace 2016
                case_el = ET.SubElement(switch_el, '{http://www.hancom.co.kr/hwpml/2011/paragraph}case', {
                    '{http://www.hancom.co.kr/hwpml/2011/paragraph}required-namespace': 'http://www.hancom.co.kr/hwpml/2016/HwpUnitChar'
                })
                margin_el1 = ET.SubElement(case_el, '{http://www.hancom.co.kr/hwpml/2011/head}margin')
                ET.SubElement(margin_el1, '{http://www.hancom.co.kr/hwpml/2011/core}intent', {'value': indent_val, 'unit': 'HWPUNIT'})
                ET.SubElement(margin_el1, '{http://www.hancom.co.kr/hwpml/2011/core}left', {'value': left_val, 'unit': 'HWPUNIT'})
                ET.SubElement(margin_el1, '{http://www.hancom.co.kr/hwpml/2011/core}right', {'value': '0', 'unit': 'HWPUNIT'})
                ET.SubElement(margin_el1, '{http://www.hancom.co.kr/hwpml/2011/core}prev', {'value': prev_val, 'unit': 'HWPUNIT'})
                ET.SubElement(margin_el1, '{http://www.hancom.co.kr/hwpml/2011/core}next', {'value': next_val, 'unit': 'HWPUNIT'})
                ET.SubElement(case_el, '{http://www.hancom.co.kr/hwpml/2011/head}lineSpacing', {
                    'type': 'PERCENT', 'value': spacing_val, 'unit': 'HWPUNIT'
                })
                
                # Default case
                def_el = ET.SubElement(switch_el, '{http://www.hancom.co.kr/hwpml/2011/paragraph}default')
                margin_el2 = ET.SubElement(def_el, '{http://www.hancom.co.kr/hwpml/2011/head}margin')
                ET.SubElement(margin_el2, '{http://www.hancom.co.kr/hwpml/2011/core}intent', {'value': indent_val, 'unit': 'HWPUNIT'})
                ET.SubElement(margin_el2, '{http://www.hancom.co.kr/hwpml/2011/core}left', {'value': left_val, 'unit': 'HWPUNIT'})
                ET.SubElement(margin_el2, '{http://www.hancom.co.kr/hwpml/2011/core}right', {'value': '0', 'unit': 'HWPUNIT'})
                ET.SubElement(margin_el2, '{http://www.hancom.co.kr/hwpml/2011/core}prev', {'value': prev_val, 'unit': 'HWPUNIT'})
                ET.SubElement(margin_el2, '{http://www.hancom.co.kr/hwpml/2011/core}next', {'value': next_val, 'unit': 'HWPUNIT'})
                ET.SubElement(def_el, '{http://www.hancom.co.kr/hwpml/2011/head}lineSpacing', {
                    'type': 'PERCENT', 'value': spacing_val, 'unit': 'HWPUNIT'
                })
                
                ET.SubElement(para_pr, '{http://www.hancom.co.kr/hwpml/2011/head}border', {
                    'borderFillIDRef': '1', 'offsetLeft': '0', 'offsetRight': '0', 'offsetTop': '0', 'offsetBottom': '0',
                    'connect': '0', 'ignoreMargin': '0'
                })
                para_properties.append(para_pr)
                
            para_properties.attrib['itemCnt'] = str(len(para_properties))
            
        out = io.BytesIO()
        tree.write(out, encoding='utf-8', xml_declaration=False)
        xml_bytes = out.getvalue()
        return b'<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>' + xml_bytes

    def build(self, survey_id: str = "all", is_cumulative: bool = False) -> io.BytesIO:
        # 지정된 조건으로 HWPX 한글 표준 구조 패키지를 메모리 상에 빌드합니다.
        section_path = os.path.join(self.template_dir, "Contents", "section0.xml")
        with open(section_path, encoding="utf-8") as f:
            section_content = f.read()

        ET.register_namespace('ha', 'http://www.hancom.co.kr/hwpml/2011/app')
        ET.register_namespace('hp', 'http://www.hancom.co.kr/hwpml/2011/paragraph')
        ET.register_namespace('hp10', 'http://www.hancom.co.kr/hwpml/2016/paragraph')
        ET.register_namespace('hs', 'http://www.hancom.co.kr/hwpml/2011/section')
        ET.register_namespace('hc', 'http://www.hancom.co.kr/hwpml/2011/core')
        ET.register_namespace('hh', 'http://www.hancom.co.kr/hwpml/2011/head')
        ET.register_namespace('hhs', 'http://www.hancom.co.kr/hwpml/2011/history')
        ET.register_namespace('hm', 'http://www.hancom.co.kr/hwpml/2011/master-page')
        ET.register_namespace('hpf', 'http://www.hancom.co.kr/hwpml/2011/schema')
        ET.register_namespace('hps', 'http://www.hancom.co.kr/hwpml/2011/schema')

        root = ET.fromstring(section_content)
        sec_p = root[0]

        preserved_run = None
        for run in sec_p.findall('{http://www.hancom.co.kr/hwpml/2011/paragraph}run'):
            if run.find('{http://www.hancom.co.kr/hwpml/2011/paragraph}secPr') is not None:
                preserved_run = run
                break

        for child in list(sec_p):
            if child != preserved_run:
                sec_p.remove(child)

        for child in list(root):
            if child != sec_p:
                root.remove(child)

        md_elements = self._parse_markdown()
        NS_HP = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'

        for elem in md_elements:
            elem_type = elem[0]
            if elem_type == "table":
                table_data = elem[1]
                if not table_data:
                    continue
                tbl = self._create_table_node(table_data)
                
                # 표를 삽입할 문단 생성
                table_p = ET.Element(NS_HP + 'p', {
                    'id': str(random.randint(1000000000, 9999999999)),
                    'paraPrIDRef': '54',
                    'styleIDRef': '0',
                    'pageBreak': '0',
                    'columnBreak': '0',
                    'merged': '0'
                })
                table_run = ET.SubElement(table_p, NS_HP + 'run', {'charPrIDRef': '56'})
                table_run.append(tbl)
                root.append(table_p)
                
                # 표 뒤에 빈 한 줄 추가해서 레이아웃 여백 확보
                root.append(self._create_paragraph("", style_id="0", para_pr_id="54", char_pr_id="54"))
                
            elif elem_type == "h1":
                text = elem[1]
                p = self._create_paragraph(f"■ {text}", style_id="0", para_pr_id="50", char_pr_id="50")
                root.append(p)
            elif elem_type == "h2":
                text = elem[1]
                p = self._create_paragraph(f"▶ {text}", style_id="0", para_pr_id="51", char_pr_id="51")
                root.append(p)
            elif elem_type == "h3":
                text = elem[1]
                p = self._create_paragraph(f"  ● {text}", style_id="0", para_pr_id="52", char_pr_id="52")
                root.append(p)
            else: # "p"
                text = elem[1]
                # 리스트 항목 또는 들여쓰기가 필요한 문단
                if text.startswith("● ") or text.startswith("1)") or text.startswith("2)") or text.startswith("3)") or text.startswith("4)"):
                    para_pr_id = "57" # 들여쓰기 리스트용 paraPr
                else:
                    para_pr_id = "54" # 일반 본문 paraPr
                p = self._create_paragraph(text, style_id="0", para_pr_id=para_pr_id, char_pr_id="54")
                root.append(p)

        root.append(self._create_paragraph("", style_id="0", para_pr_id="54", char_pr_id="54"))

        new_section_xml = ET.tostring(root, encoding="utf-8")
        new_section_content = b'<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>' + new_section_xml

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for root_dir, dirs, files in os.walk(self.template_dir):
                for file in files:
                    full_path = os.path.join(root_dir, file)
                    rel_path = os.path.relpath(full_path, self.template_dir)
                    
                    if rel_path == os.path.join("Contents", "section0.xml"):
                        zip_file.writestr(rel_path, new_section_content)
                    elif rel_path == os.path.join("Contents", "header.xml"):
                        header_content = self._inject_custom_styles_to_header(full_path)
                        zip_file.writestr(rel_path, header_content)
                    else:
                        with open(full_path, "rb") as rf:
                            zip_file.writestr(rel_path, rf.read())

        zip_buffer.seek(0)
        return zip_buffer

    def _append_runs_to_paragraph(self, p_elem, text: str, default_char_pr: str):
        NS_HP = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'
        chunks = self._parse_inline_bold(text)
        
        if not chunks:
            run = ET.SubElement(p_elem, NS_HP + 'run', {'charPrIDRef': default_char_pr})
            ET.SubElement(run, NS_HP + 't')
            return
            
        for is_bold, chunk_text in chunks:
            char_pr = default_char_pr
            if is_bold:
                if default_char_pr == '54':
                    char_pr = '53'  # 본문 강조 (10pt, bold)
                elif default_char_pr == '56':
                    char_pr = '55'  # 표 본문 -> 표 헤더/강조 (9.5pt, bold)
                else:
                    char_pr = '53'
            
            run = ET.SubElement(p_elem, NS_HP + 'run', {'charPrIDRef': char_pr})
            t = ET.SubElement(run, NS_HP + 't')
            t.text = chunk_text

    def _create_paragraph(self, text: str, style_id: str = "0", para_pr_id: str = "0", char_pr_id: str = "14") -> ET.Element:
        NS_HP = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'
        p_id = str(random.randint(1000000000, 9999999999))
        p = ET.Element(NS_HP + 'p', {
            'id': p_id,
            'paraPrIDRef': para_pr_id,
            'styleIDRef': style_id,
            'pageBreak': '0',
            'columnBreak': '0',
            'merged': '0'
        })
        self._append_runs_to_paragraph(p, text, char_pr_id)
        return p

    def _create_table_node(self, data_rows: list) -> ET.Element:
        NS_HP = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'
        row_cnt = len(data_rows)
        col_cnt = len(data_rows[0])
        
        tbl_id = str(random.randint(1000000000, 9999999999))
        tbl = ET.Element(NS_HP + 'tbl', {
            'id': tbl_id,
            'zOrder': '0',
            'numberingType': 'TABLE',
            'textWrap': 'TOP_AND_BOTTOM',
            'textFlow': 'BOTH_SIDES',
            'lock': '0',
            'dropcapstyle': 'None',
            'pageBreak': 'CELL',
            'repeatHeader': '1',
            'rowCnt': str(row_cnt),
            'colCnt': str(col_cnt),
            'cellSpacing': '0',
            'borderFillIDRef': '3',
            'noAdjust': '1'
        })
        
        ET.SubElement(tbl, NS_HP + 'sz', {
            'width': '45832',
            'widthRelTo': 'ABSOLUTE',
            'height': str(2737 * row_cnt),
            'heightRelTo': 'ABSOLUTE',
            'protect': '0'
        })
        
        ET.SubElement(tbl, NS_HP + 'pos', {
            'treatAsChar': '1',
            'affectLSpacing': '0',
            'flowWithText': '1',
            'allowOverlap': '0',
            'holdAnchorAndSO': '0',
            'vertRelTo': 'PARA',
            'horzRelTo': 'COLUMN',
            'vertAlign': 'TOP',
            'horzAlign': 'LEFT',
            'vertOffset': '0',
            'horzOffset': '0'
        })
        
        ET.SubElement(tbl, NS_HP + 'outMargin', {'left': '141', 'right': '141', 'top': '141', 'bottom': '141'})
        ET.SubElement(tbl, NS_HP + 'inMargin', {'left': '510', 'right': '510', 'top': '140', 'bottom': '140'})
        
        def get_char_weight(char):
            return 2 if ord(char) > 127 else 1
            
        def get_string_weight(text):
            if not text:
                return 1
            return sum(get_char_weight(c) for c in str(text))

        col_max_weights = [1] * col_cnt
        for row in data_rows:
            for c_idx in range(min(col_cnt, len(row))):
                weight = get_string_weight(row[c_idx])
                if weight > col_max_weights[c_idx]:
                    col_max_weights[c_idx] = weight

        total_weight = sum(col_max_weights)
        total_width = 45832
        col_widths = []
        allocated_width = 0
        
        for c_idx in range(col_cnt - 1):
            w = int(total_width * col_max_weights[c_idx] / total_weight)
            min_w = int(total_width * 0.045)
            if w < min_w:
                w = min_w
            col_widths.append(w)
            allocated_width += w
            
        last_w = total_width - allocated_width
        min_last_w = int(total_width * 0.045)
        if last_w < min_last_w:
            last_w = min_last_w
        col_widths.append(last_w)
        
        for r_idx, row_data in enumerate(data_rows):
            tr = ET.SubElement(tbl, NS_HP + 'tr')
            border_fill = '4' if r_idx == 0 else '6'
            
            for c_idx, cell_value in enumerate(row_data):
                tc = ET.SubElement(tr, NS_HP + 'tc', {
                    'name': '',
                    'header': '1' if r_idx == 0 else '0',
                    'hasMargin': '0',
                    'protect': '0',
                    'editable': '0',
                    'dirty': '0',
                    'borderFillIDRef': border_fill
                })
                
                ET.SubElement(tc, NS_HP + 'cellAddr', {'colAddr': str(c_idx), 'rowAddr': str(r_idx)})
                ET.SubElement(tc, NS_HP + 'cellSpan', {'colSpan': '1', 'ragSpan': '1'})
                ET.SubElement(tc, NS_HP + 'cellSz', {'width': str(col_widths[c_idx]), 'height': '2737'})
                ET.SubElement(tc, NS_HP + 'cellMargin', {'left': '510', 'right': '510', 'top': '140', 'bottom': '140'})
                
                sublist = ET.SubElement(tc, NS_HP + 'subList', {
                    'id': '',
                    'textDirection': 'HORIZONTAL',
                    'lineWrap': 'BREAK',
                    'vertAlign': 'CENTER',
                    'linkListIDRef': '0',
                    'linkListNextIDRef': '0',
                    'textWidth': '0',
                    'textHeight': '0',
                    'hasTextRef': '0',
                    'hasNumRef': '0'
                })
                
                p_style = '55' if r_idx == 0 else '56'
                p = ET.SubElement(sublist, NS_HP + 'p', {
                    'id': str(random.randint(1000000000, 9999999999)),
                    'paraPrIDRef': p_style,
                    'styleIDRef': '0',
                    'pageBreak': '0',
                    'columnBreak': '0',
                    'merged': '0'
                })
                
                c_style = '55' if r_idx == 0 else '56'
                cell_text = str(cell_value) if cell_value is not None else ""
                self._append_runs_to_paragraph(p, cell_text, c_style)
                
        return tbl
