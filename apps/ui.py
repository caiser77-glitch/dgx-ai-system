import shutil
import subprocess
import requests
from pathlib import Path
import gradio as gr
from pptx import Presentation

BASE = Path("/home/caiser77/dgx_workspace")
OLLAMA_URL = "http://localhost:11434/api/generate"
LLM_MODEL = "qwen2.5:14b"

def ask_llm(text):
    prompt = f"""
너는 회사 업무용 문서 분석 전문가다.
OCR 결과를 보고 실무 보고서처럼 작성해라.

[문서 유형]
- 이 문서가 무엇인지 한 줄로 설명

[보정된 핵심 내용]
- OCR 오류를 자연스럽게 수정해서 정리

[핵심 요약]
1.
2.
3.

[상세 분석]
- 의미 설명

[실행할 작업]
1.
2.
3.

[주의할 점]
- OCR 오류 가능성

OCR 원문:
{text}
"""
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.2}
        },
        timeout=300
    )
    r.raise_for_status()
    return r.json().get("response", "")

def create_report_ppt(title, ocr_text, ai_result, out_path):
    prs = Presentation()

    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = title
    slide.placeholders[1].text = "DGX 자동 리포트"

    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "OCR 원문"
    slide.placeholders[1].text = ocr_text[:1000]

    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "AI 분석"
    slide.placeholders[1].text = ai_result[:1000]

    prs.save(out_path)

def run_ocr_ai_ppt(file):
    src = Path(file)
    path = BASE / "uploads" / src.name
    shutil.copy(src, path)

    subprocess.run(["python", str(BASE / "scripts/ocr_run.py"), str(path)], check=True)

    ocr_txt_path = BASE / "outputs" / f"{path.stem}_ocr.txt"
    ocr_img_path = BASE / "outputs" / f"{path.stem}_processed.png"

    ocr_text = ocr_txt_path.read_text(encoding="utf-8")
    ai_result = ask_llm(ocr_text)

    ai_file = BASE / "outputs" / f"{path.stem}_ai.txt"
    ai_file.write_text(ai_result, encoding="utf-8")

    ppt_file = BASE / "outputs" / f"{path.stem}_report.pptx"
    create_report_ppt("AI 분석 리포트", ocr_text, ai_result, ppt_file)

    return str(ocr_txt_path), str(ocr_img_path), ai_result, str(ai_file), str(ppt_file)

def run_excel(file):
    src = Path(file)
    path = BASE / "uploads" / src.name
    shutil.copy(src, path)

    subprocess.run(["python", str(BASE / "scripts/excel_summary.py"), str(path)], check=True)

    out = BASE / "outputs" / f"{path.stem}_summary.xlsx"
    return str(out)

def run_ppt():
    subprocess.run(["python", str(BASE / "scripts/ppt_create.py")], check=True)
    return str(BASE / "outputs" / "test_presentation.pptx")

def run_cad_test():
    subprocess.run(["python", str(BASE / "scripts/cad_create_dxf.py")], check=True)
    return str(BASE / "outputs" / "test_drawing.dxf")

def auto_convert_cad_kml(file):
    src = Path(file)
    path = BASE / "uploads" / src.name
    shutil.copy(src, path)

    ext = path.suffix.lower()

    if ext == ".kml":
        mode = "kml_to_dxf"
        out = BASE / "outputs" / f"{path.stem}.dxf"
    elif ext == ".dxf":
        mode = "dxf_to_kml"
        out = BASE / "outputs" / f"{path.stem}.kml"
    else:
        raise ValueError("지원하지 않는 파일입니다. .kml 또는 .dxf 파일만 업로드하세요.")

    result = subprocess.run(
        ["python", str(BASE / "scripts/cad_kml_convert.py"), mode, str(path), str(out)],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    log = f"변환 완료: {path.name} → {out.name}\n\n{result.stdout}"
    return str(out), log

with gr.Blocks() as app:
    gr.Markdown("# DGX 작업 콘솔")

    with gr.Tab("OCR → AI → PPT"):
        file = gr.File(label="이미지 업로드", type="filepath")
        btn = gr.Button("OCR + AI 분석 + PPT 생성")

        ocr_txt = gr.File(label="OCR 결과")
        ocr_img = gr.Image(label="전처리 이미지")
        ai_text = gr.Textbox(label="AI 분석", lines=12)
        ai_file = gr.File(label="AI 결과 파일")
        ppt_file = gr.File(label="PPT 리포트")

        btn.click(run_ocr_ai_ppt, file, [ocr_txt, ocr_img, ai_text, ai_file, ppt_file])

    with gr.Tab("Excel"):
        excel_file = gr.File(label="엑셀 파일 업로드", type="filepath")
        excel_btn = gr.Button("엑셀 분석 실행")
        excel_out = gr.File(label="엑셀 분석 결과")
        excel_btn.click(run_excel, excel_file, excel_out)

    with gr.Tab("CAD / KML 자동 변환"):
        cad_kml_file = gr.File(label="KML 또는 DXF 파일 업로드", type="filepath")
        cad_kml_btn = gr.Button("자동 변환")
        cad_kml_out = gr.File(label="변환 결과 파일")
        cad_kml_log = gr.Textbox(label="처리 로그", lines=6)
        cad_kml_btn.click(auto_convert_cad_kml, cad_kml_file, [cad_kml_out, cad_kml_log])

    with gr.Tab("PPT 테스트"):
        ppt_btn = gr.Button("PPT 생성")
        ppt_out = gr.File(label="생성된 PPT")
        ppt_btn.click(run_ppt, None, ppt_out)

    with gr.Tab("CAD 테스트"):
        cad_btn = gr.Button("DXF 테스트 도면 생성")
        cad_out = gr.File(label="생성된 DXF")
        cad_btn.click(run_cad_test, None, cad_out)

app.launch(server_name="0.0.0.0", server_port=7861)
