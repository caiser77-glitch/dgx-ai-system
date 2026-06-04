import shutil
import subprocess
import requests
from pathlib import Path

import gradio as gr

BASE = Path("/home/caiser77/dgx_workspace")
OLLAMA_URL = "http://localhost:11434/api/generate"
OPEN_WEBUI_URL = "http://100.98.149.128:3000/"

MODEL_SIMPLE = "llama3.1:8b"
MODEL_WORK = "qwen2.5:14b"
MODEL_BIG = "qwen2.5:72b"
MODEL_REVIEW = "llama3.1:70b"
MODEL_IMAGE = "llava:latest"
MODEL_LIGHT = "mistral:latest"
MODEL_WRITE = "gemma2:27b"
MODEL_POLISH = "gemma2:9b"
MODEL_SMALL = "gemma:7b"


def call_ollama(model, prompt, temperature=0.2, timeout=600):
    print(f"[AURUM DEBUG] Ollama 호출 모델: {model}")

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "top_p": 0.8,
            },
        },
        timeout=timeout,
    )

    print(f"[AURUM DEBUG] Ollama 상태코드: {r.status_code}")
    r.raise_for_status()
    return r.json().get("response", "")


def get_weather():
    try:
        r = requests.get("https://wttr.in/Seoul?format=3", timeout=20)
        r.raise_for_status()
        return r.text
    except Exception as e:
        return f"날씨 정보를 가져오지 못했습니다: {e}"


def select_model(question):
    q = question.lower()
    length = len(question)

    if any(k in q for k in ["날씨", "기온", "비", "눈", "weather"]):
        return "WEATHER_API", "날씨 질문"

    if any(k in q for k in ["이미지", "사진", "그림", "ocr", "캡처", "스캔"]):
        return MODEL_IMAGE, "이미지/OCR 질문"

    if any(k in q for k in ["간단", "짧게", "빠르게", "한줄", "한 줄"]):
        return MODEL_SIMPLE, "간단 응답"

    if any(k in q for k in ["문장", "다듬", "부드럽게", "표현", "이메일", "메일", "문체"]):
        return MODEL_POLISH, "문장 다듬기/문체 작업"

    if any(k in q for k in ["초안", "작성", "기획서", "제안서", "공문", "보고서 작성"]):
        return MODEL_WRITE, "문서 작성 작업"

    if any(k in q for k in ["검증", "반박", "다른 관점", "재검토", "비판"]):
        return MODEL_REVIEW, "대형 검토/재검토"

    if any(k in q for k in ["보고서", "분석", "요약", "환경영향평가", "논리", "전략", "긴 문서"]) or length > 1200:
        return MODEL_BIG, "긴 문서/복잡 분석"

    if any(k in q for k in ["코드", "python", "에러", "오류", "스크립트", "터미널", "docker", "git", "vscode"]):
        return MODEL_WORK, "코드/시스템 작업"

    if length < 80:
        return MODEL_SMALL, "짧은 일반 대화"

    return MODEL_WORK, "일반 업무"


def build_chat_context(history, max_turns=8):
    if not history:
        return ""

    lines = []
    for msg in history[-max_turns:]:
        role = msg.get("role", "")
        content = msg.get("content", "")

        if role == "user":
            lines.append(f"사용자: {content}")
        elif role == "assistant":
            lines.append(f"AURUM: {content}")

    return "\n".join(lines)


def aurum_chat(message, history):
    if history is None:
        history = []

    if not message or not message.strip():
        yield history, "", "대기 중"
        return

    model, reason = select_model(message)
    print(f"[AURUM DEBUG] 질문: {message}")
    print(f"[AURUM DEBUG] 선택 모델: {model} / 이유: {reason}")

    history.append({"role": "user", "content": message})
    history.append({
        "role": "assistant",
        "content": f"⏳ AURUM 응답 생성 중...\n\n선택 모델/도구: {model}\n선택 이유: {reason}"
    })

    yield history, "", "⏳ 응답 생성 중"

    try:
        if model == "WEATHER_API":
            answer = get_weather()
            final_answer = f"[AURUM]\n선택 도구: WEATHER_API\n선택 이유: {reason}\n\n{answer}"
        else:
            context = build_chat_context(history[:-2])

            prompt = f"""
너는 AURUM(아우룸) 통합 AI 시스템이다.
DGX 로컬 서버에서 여러 LLM을 목적별로 선택해 사용한다.

현재 선택 모델: {model}
선택 이유: {reason}

이전 대화:
{context}

답변 원칙:
- 반드시 한국어로만 답변
- 영어로 답하지 말 것
- 실무 중심
- 초보자도 따라할 수 있게 설명
- 명령어는 복붙 가능하게 제공
- 불확실하면 단정하지 않기
- 너무 장황하지 않게 핵심부터 답변

사용자 질문:
{message}
"""

            answer = call_ollama(model, prompt)

            if not answer.strip():
                answer = "모델 응답이 비어 있습니다. Ollama 모델 상태를 확인해야 합니다."

            final_answer = f"[AURUM]\n선택 모델: {model}\n선택 이유: {reason}\n\n{answer}"

        history[-1] = {"role": "assistant", "content": final_answer}
        yield history, "", "✅ 응답 완료"

    except Exception as e:
        err = f"❌ 오류 발생:\n{type(e).__name__}: {e}"
        print(f"[AURUM ERROR] {err}")

        history[-1] = {
            "role": "assistant",
            "content": f"[AURUM 오류]\n{err}\n\n터미널 로그를 확인하세요."
        }

        yield history, "", "❌ 오류 발생"


def clear_chat():
    return [], "", "대화 초기화 완료"


def run_taxa_image_ocr(file):
    src = Path(file)
    path = BASE / "uploads" / src.name
    shutil.copy(src, path)

    subprocess.run(
        ["python", str(BASE / "scripts/taxa_table_ocr.py"), str(path)],
        check=True,
    )

    return str(BASE / "outputs" / f"{path.stem}_taxa.xlsx")


def safe_page_name(pages):
    p = pages.strip() if pages and pages.strip() else "all"
    return p.replace(",", "_").replace("-", "to").replace(" ", "")


def run_taxa_pdf_ocr(file, pages):
    src = Path(file)
    path = BASE / "uploads" / src.name
    shutil.copy(src, path)

    page_text = pages.strip() if pages and pages.strip() else ""

    subprocess.run(
        ["python", str(BASE / "scripts/taxa_pdf_ocr.py"), str(path), page_text],
        check=True,
    )

    out_name = f"{path.stem}_pages_{safe_page_name(page_text)}_taxa.xlsx"
    return str(BASE / "outputs" / out_name)


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
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    log = f"변환 완료: {path.name} → {out.name}\n\n{result.stdout}"
    return str(out), log


def run_excel(file):
    src = Path(file)
    path = BASE / "uploads" / src.name
    shutil.copy(src, path)

    subprocess.run(
        ["python", str(BASE / "scripts/excel_summary.py"), str(path)],
        check=True,
    )

    return str(BASE / "outputs" / f"{path.stem}_summary.xlsx")


with gr.Blocks(title="AURUM") as app:
    gr.Markdown("# AURUM / 아우룸")
    gr.Markdown("### DGX 통합 AI 작업 콘솔")

    with gr.Tab("AURUM Chat"):
        chatbot = gr.Chatbot(
            label="AURUM 대화",
            height=600,
        )

        status = gr.Textbox(
            label="상태",
            value="대기 중",
            interactive=False,
        )

        chat_input = gr.Textbox(
            label="메시지 입력",
            lines=1,
            placeholder="메시지 입력 후 Enter",
        )

        with gr.Row():
            send_btn = gr.Button("전송")
            clear_btn = gr.Button("대화 초기화")

        send_btn.click(
            aurum_chat,
            [chat_input, chatbot],
            [chatbot, chat_input, status],
        )

        chat_input.submit(
            aurum_chat,
            [chat_input, chatbot],
            [chatbot, chat_input, status],
        )

        clear_btn.click(
            clear_chat,
            None,
            [chatbot, chat_input, status],
        )

    with gr.Tab("분류군 조사표 OCR"):
        gr.Markdown("## 이미지 조사표 OCR")
        taxa_file = gr.File(label="조사표 이미지 업로드", type="filepath")
        taxa_btn = gr.Button("이미지 표 OCR → Excel 생성")
        taxa_out = gr.File(label="결과 Excel")
        taxa_btn.click(run_taxa_image_ocr, taxa_file, taxa_out)

        gr.Markdown("---")
        gr.Markdown("## PDF 조사표 OCR")
        pdf_file = gr.File(label="PDF 업로드", type="filepath")
        page_input = gr.Textbox(
            label="OCR할 페이지",
            value="1",
            placeholder="예: 1,3-5,8 / 전체 페이지는 빈칸",
        )
        pdf_btn = gr.Button("지정 페이지 OCR → Excel 생성")
        pdf_out = gr.File(label="결과 Excel")
        pdf_btn.click(run_taxa_pdf_ocr, [pdf_file, page_input], pdf_out)

    with gr.Tab("CAD / KML 자동 변환"):
        cad_kml_file = gr.File(label="KML 또는 DXF 파일 업로드", type="filepath")
        cad_kml_btn = gr.Button("자동 변환")
        cad_kml_out = gr.File(label="변환 결과 파일")
        cad_kml_log = gr.Textbox(label="처리 로그", lines=6)
        cad_kml_btn.click(auto_convert_cad_kml, cad_kml_file, [cad_kml_out, cad_kml_log])

    with gr.Tab("Excel"):
        excel_file = gr.File(label="엑셀 파일 업로드", type="filepath")
        excel_btn = gr.Button("엑셀 분석 실행")
        excel_out = gr.File(label="엑셀 분석 결과")
        excel_btn.click(run_excel, excel_file, excel_out)

    with gr.Tab("Open WebUI"):
        gr.Markdown("## Open WebUI")
        gr.Markdown(f"[Open WebUI 새 창에서 열기]({OPEN_WEBUI_URL})")
        gr.HTML(f"""
        <iframe src="{OPEN_WEBUI_URL}" width="100%" height="800"
        style="border:1px solid #ccc; border-radius:8px;"></iframe>
        """)


app.launch(server_name="0.0.0.0", server_port=7861)
