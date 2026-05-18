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

def run_all(file):
    src = Path(file)
    path = BASE / "uploads" / src.name
    shutil.copy(src, path)

    subprocess.run(["python", str(BASE/"scripts/ocr_run.py"), str(path)], check=True)

    ocr_txt_path = BASE / "outputs" / f"{path.stem}_ocr.txt"
    ocr_img_path = BASE / "outputs" / f"{path.stem}_processed.png"

    ocr_text = ocr_txt_path.read_text(encoding="utf-8")
    ai_result = ask_llm(ocr_text)

    ai_file = BASE / "outputs" / f"{path.stem}_ai.txt"
    ai_file.write_text(ai_result, encoding="utf-8")

    ppt_file = BASE / "outputs" / f"{path.stem}_report.pptx"
    create_report_ppt("AI 분석 리포트", ocr_text, ai_result, ppt_file)

    return str(ocr_txt_path), str(ocr_img_path), ai_result, str(ai_file), str(ppt_file)

with gr.Blocks() as app:
    gr.Markdown("# DGX AI 자동 분석 시스템")

    file = gr.File(label="이미지 업로드", type="filepath")
    btn = gr.Button("OCR + AI + PPT 실행")

    ocr_txt = gr.File(label="OCR 결과")
    ocr_img = gr.Image(label="전처리 이미지")
    ai_text = gr.Textbox(label="AI 분석", lines=12)
    ai_file = gr.File(label="AI 결과 파일")
    ppt_file = gr.File(label="PPT 리포트")

    btn.click(run_all, file, [ocr_txt, ocr_img, ai_text, ai_file, ppt_file])

app.launch(server_name="0.0.0.0", server_port=7861)