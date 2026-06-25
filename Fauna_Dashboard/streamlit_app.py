import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
import json
import re
import subprocess
from pathlib import Path
import time

# 1. 페이지 설정 및 경로 정의
st.set_page_config(
    page_title="Fauna Ecological Dashboard",
    layout="wide",
    page_icon="🌿",
    initial_sidebar_state="collapsed"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DATA_PATH = os.path.join(BASE_DIR, "data", "species_search_index.json")
METADATA_DIR = os.path.join(PROJECT_ROOT, "data", "processed", "metadata")
PENDING_FILE = os.path.join(PROJECT_ROOT, "scratch", "pending_queue.json")
CRON_LOG_FILE = os.path.join(PROJECT_ROOT, "003. NAS 장기 배치 파이프라인", "logs", "cron_run.log")
PRIMARY_RAG_STATE_FILE = os.path.join(PROJECT_ROOT, "002. 회사 NAS 분석", "data", "processed", "state.json")
PRIMARY_RAG_MAPPING_FILE = os.path.join(PROJECT_ROOT, "002. 회사 NAS 분석", "data", "indexes", "faiss", "mapping.json")
BATCH_RAG_MAPPING_FILE = os.path.join(PROJECT_ROOT, "data", "indexes", "faiss", "mapping.json")

# 2. 전역 스타일링 인젝션 (Warm Beige 테마 및 상태 색상 복원)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

    :root {
        --background-color: #faf8f5;     /* Warm beige */
        --card-bg: #ffffff;              /* Clean white cards */
        --text-color: #3c3c3c;           /* Charcoal dark grey */
        --border-color: #e1dad0;         /* Soft warm grey border */
        --primary-color: #7c7267;        /* Muted warm bronze */

        /* Restored status colors for clear visual distinction */
        --success-color: #059669;        /* Success green */
        --success-bg: #ecfdf5;
        --success-border: #a7f3d0;

        --error-color: #dc2626;          /* Failure red */
        --error-bg: #fef2f2;
        --error-border: #fca5a5;

        --warning-color: #d97706;        /* Pending amber */
        --warning-bg: #fffbeb;
        --warning-border: #fde68a;
    }

    html, body, [class*="css"], .stApp {
        background-color: var(--background-color) !important;
        color: var(--text-color) !important;
        font-family: 'Pretendard', -apple-system, sans-serif;
        font-size: 14px;
    }

    .stApp { background-color: var(--background-color); }

    h1, h2, h3, h4, h5, h6 {
        color: #4a4238 !important;
        font-weight: 700 !important;
        margin-bottom: 8px !important;
    }

    hr { border-color: var(--border-color) !important; margin: 12px 0 !important; }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* Streamlit Tab Customization */
    div[data-baseweb="tab-list"] {
        background-color: #f3ece0 !important;
        padding: 4px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        gap: 4px;
    }
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        color: #7c7267 !important;
        border: none !important;
        font-weight: 600;
        padding: 6px 14px;
        border-radius: 6px;
        font-size: 0.9rem;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #ffffff !important;
        color: #2c251e !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* KPI metric glass cards */
    .kpi-wrapper {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-bottom: 15px;
    }
    .kpi-glass-card {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 10px;
        padding: 12px 16px;
        position: relative;
        transition: transform 0.2s, box-shadow 0.2s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .kpi-glass-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .kpi-lbl {
        font-size: 0.75rem;
        font-weight: 700;
        color: #7c7267;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }
    .kpi-val {
        font-size: 1.8rem;
        font-weight: 800;
        color: var(--text-color);
        line-height: 1.1;
    }
    .kpi-unit {
        font-size: 0.85rem;
        color: #7c7267;
        font-weight: 400;
        margin-left: 2px;
    }

    /* Collaborative Agent online status cards */
    .agent-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 8px;
    }
    .agent-card {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 10px 14px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.01);
    }

    /* Process status badges */
    .badge-running {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: var(--success-bg);
        color: var(--success-color);
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 700;
        font-size: 0.7rem;
        border: 1px solid var(--success-border);
    }
    .badge-stopped {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: var(--error-bg);
        color: var(--error-color);
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 700;
        font-size: 0.7rem;
        border: 1px solid var(--error-border);
    }
    .badge-idle {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: var(--warning-bg);
        color: var(--warning-color);
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 700;
        font-size: 0.7rem;
        border: 1px solid var(--warning-border);
    }

    .pulse-green { color: var(--success-color); font-weight: 900; }
    .pulse-red { color: var(--error-color); font-weight: 900; }
    .pulse-amber { color: var(--warning-color); font-weight: 900; }

    /* Hardware monitor cards */
    .hw-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 8px;
        margin-top: 5px;
    }
    .hw-card {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 8px 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.01);
    }
    .hw-title {
        font-size: 0.75rem;
        color: #7c7267;
        font-weight: 600;
        margin-bottom: 2px;
    }
    .hw-value {
        font-size: 1.25rem;
        font-weight: 800;
        color: var(--text-color);
    }
    .hw-temp-badge {
        font-size: 0.7rem;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 700;
        display: inline-block;
    }
    .temp-cool { background: var(--success-bg); color: var(--success-color); border: 1px solid var(--success-border); }
    .temp-warm { background: var(--warning-bg); color: var(--warning-color); border: 1px solid var(--warning-border); }
    .temp-hot { background: var(--error-bg); color: var(--error-color); border: 1px solid var(--error-border); }

    /* Streamlit overrides */
    div[data-testid="stDataFrame"] {
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        padding: 4px;
    }

    div[data-testid="stForm"] {
        background: #ffffff !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }

    .info-box {
        background-color: #ffffff;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 8px 12px;
        color: #7c7267;
        font-size: 0.8rem;
    }

    button[kind="secondary"] {
        background-color: #ffffff !important;
        color: var(--text-color) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        padding: 4px 10px !important;
    }
    button[kind="secondary"]:hover {
        background-color: #fcfbf9 !important;
        border-color: #7c7267 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 생태 종 사전 인덱스 로드 함수
@st.cache_resource
def load_index():
    if os.path.exists(DATA_PATH):
        try:
            with open(DATA_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            st.warning(f"종 사전 인덱스 로드 실패: {e}")
            return {}
    return {}

species_index = load_index()

# 4. 세션 상태 초기화
if 'survey_log' not in st.session_state:
    st.session_state.survey_log = pd.DataFrame(columns=['Type', 'Species', 'Count', 'Status', 'Location', 'Class', 'Order', 'Family'])

# 5. 1차 전수조사 RAG 인덱싱 진행 현황 로깅 파서
def get_full_scan_progress():
    import glob
    log_dir = os.path.join(PROJECT_ROOT, "003. NAS 장기 배치 파이프라인", "logs")
    log_paths = glob.glob(os.path.join(log_dir, "slicer_*.log"))
    
    # 활성 슬라이서 로그들 취득 (크기 > 0)
    active_logs = [p for p in log_paths if os.path.exists(p) and os.path.getsize(p) > 0]
    if not active_logs:
        active_logs = [CRON_LOG_FILE]

    combined_total = 0
    combined_completed = 0
    combined_pending = 0
    current_files = []

    for log_path in active_logs:
        if os.path.exists(log_path):
            try:
                with open(log_path, 'r', encoding='utf-8', errors='replace') as f:
                    f.seek(0, os.SEEK_END)
                    size = f.tell()
                    read_size = min(size, 2000000)
                    f.seek(size - read_size)
                    content = f.read()

                marker = "=== NAS 장기 배치 파이프라인 스캔 개시 ==="
                marker_pos = content.rfind(marker)
                current_run = content[marker_pos:] if marker_pos >= 0 else content

                totals = re.findall(r"발견된 지원 포맷 파일 수:\s*(\d+)개", current_run)
                skips = re.findall(r"가공 완료 스킵 파일 수:\s*(\d+)개", current_run)
                pendings = re.findall(r"남은 미처리 가공 대상 수:\s*(\d+)개", current_run)
                positions = re.findall(r"\[(\d+)/(\d+)\]\s*처리 시작:\s*(.*)", current_run)
                successes = len(re.findall(r"✅\s*가공 완료", current_run))

                sub_total = 0
                sub_completed = 0
                sub_pending = 0
                sub_current_file = ""

                if totals:
                    sub_total = int(totals[-1])
                skipped = int(skips[-1]) if skips else 0
                if positions:
                    current_pos = int(positions[-1][0])
                    sub_completed = skipped + max(successes, current_pos - 1)
                    sub_current_file = positions[-1][2].strip()
                else:
                    sub_completed = skipped
                if pendings:
                    sub_pending = int(pendings[-1])

                if sub_total > 0:
                    sub_completed = min(sub_completed, sub_total)
                    sub_pending = max(sub_total - sub_completed, 0)

                combined_total += sub_total
                combined_completed += sub_completed
                combined_pending += sub_pending
                if sub_current_file:
                    label = os.path.basename(log_path).replace('slicer_', '').replace('.log', '')
                    current_files.append(f"{label}: {sub_current_file}")
            except Exception:
                pass

    if combined_total > 0:
        combined_completed = min(combined_completed, combined_total)
        combined_pending = max(combined_total - combined_completed, 0)
    
    progress_rate = (combined_completed / combined_total * 100) if combined_total > 0 else 0.0
    combined_current_file = " | ".join(current_files) if current_files else ""
    return combined_total, combined_completed, combined_pending, progress_rate, combined_current_file


def get_rag_index_info():
    best_count = 0
    best_model_name = "미정"

    # 1. mapping.json 파일들 우선 탐색하여 실 데이터 기준으로 확인
    for mapping_file in (PRIMARY_RAG_MAPPING_FILE, BATCH_RAG_MAPPING_FILE):
        if os.path.exists(mapping_file):
            try:
                with open(mapping_file, "r", encoding="utf-8") as f:
                    header = f.read(4096)
                count_match = re.search(r'"document_count":\s*(\d+)', header)
                model_match = re.search(r'"model_name":\s*"([^"]+)"', header)
                if count_match:
                    count = int(count_match.group(1))
                    if count > best_count:
                        best_count = count
                        if model_match:
                            best_model_name = model_match.group(1)
            except Exception:
                pass

    # 2. state.json 도 비교하여 최대치 반영
    if os.path.exists(PRIMARY_RAG_STATE_FILE):
        try:
            with open(PRIMARY_RAG_STATE_FILE, "r", encoding="utf-8") as f:
                state = json.load(f)
            if "index" in state and isinstance(state["index"], dict):
                count = state["index"].get("document_count", 0)
                model_name = state["index"].get("model_name", "미정")
                if count > best_count:
                    best_count = count
                    best_model_name = model_name
        except Exception:
            pass

    return best_count, best_model_name

# 6. 실시간 시스템 자원 파싱 함수 (psutil 연동)
def get_system_resources():
    import psutil
    cpu_usage = psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory()
    mem_used_gb = memory.used / (1024 ** 3)
    mem_total_gb = memory.total / (1024 ** 3)
    mem_usage = memory.percent

    cpu_temp = None
    try:
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps:
            cpu_temp = np.mean([t.current for t in temps['coretemp']])
        elif 'cpu_thermal' in temps:
            cpu_temp = temps['cpu_thermal'][0].current
        else:
            for k, v in temps.items():
                if v:
                    cpu_temp = v[0].current
                    break
    except Exception:
        pass

    return {
        "cpu_usage": cpu_usage,
        "cpu_temp": cpu_temp,
        "mem_used": mem_used_gb,
        "mem_total": mem_total_gb,
        "mem_usage": mem_usage
    }

# 7. 실시간 GPU 모니터링 파싱 함수 (NVIDIA UMA/Grace-Blackwell 대응)
def get_gpu_status():
    try:
        res = subprocess.run([
            "nvidia-smi",
            "--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu,name",
            "--format=csv,noheader,nounits"
        ], capture_output=True, text=True, check=True)

        gpu_stats = []
        lines = res.stdout.strip().splitlines()
        for idx, line in enumerate(lines):
            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 5:
                mem_used = None
                mem_total = None
                try:
                    mem_used = float(parts[1]) / 1024.0
                    mem_total = float(parts[2]) / 1024.0
                except (ValueError, TypeError):
                    pass

                util = 0
                try:
                    util = int(parts[0])
                except (ValueError, TypeError):
                    pass

                temp = 0
                try:
                    temp = int(parts[3])
                except (ValueError, TypeError):
                    pass

                gpu_stats.append({
                    "id": idx,
                    "name": parts[4],
                    "util": util,
                    "mem_used": mem_used,
                    "mem_total": mem_total,
                    "temp": temp
                })
        return gpu_stats
    except Exception:
        return []

# 8. 개별 에이전트 자원 점유율 실시간 감지 함수 (Dummy 틱 + 0.1s 누적 버그 극복버전)
def get_agent_resources():
    import psutil
    agents = {
        "slicer": {"name": "🤖 아톰 RAG 슬라이서", "pattern": "longterm_batch_slicer.py", "pid": None, "cpu": 0.0, "mem_mb": 0.0},
        "extractor": {"name": "📷 아톰 이미지 스캐너", "pattern": "extract_data.py", "pid": None, "cpu": 0.0, "mem_mb": 0.0},
        "watcher": {"name": "⏱️ 아톰 Watchdog 데몬", "pattern": "watchdog_pipeline.py", "pid": None, "cpu": 0.0, "mem_mb": 0.0},
        "indexer": {"name": "⚡ 아톰 RAG 인덱서 (FAISS 빌드)", "pattern": "index_documents.py", "pid": None, "cpu": 0.0, "mem_mb": 0.0},
        "hermes_gateway": {"name": "💬 에르메스 게이트웨이", "pattern": "hermes_cli.main gateway", "pid": None, "cpu": 0.0, "mem_mb": 0.0},
        "hermes_chat": {"name": "🗣️ 에르메스 대화 쉘 (Atom)", "pattern": "hermes_cli.main chat", "pid": None, "cpu": 0.0, "mem_mb": 0.0},
        "telegram_bot": {"name": "📢 아우룸 텔레그램 피드백 봇", "pattern": "telegram_feedback_bot.py", "pid": None, "cpu": 0.0, "mem_mb": 0.0},
        "dashboard": {"name": "📊 아우룸 대시보드 (Streamlit)", "pattern": "Fauna_Dashboard/streamlit_app.py", "pid": None, "cpu": 0.0, "mem_mb": 0.0}
    }

    # PID 매핑
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = proc.info.get('cmdline')
            if not cmdline: continue
            cmdline_str = " ".join(cmdline)

            for key, agent in agents.items():
                if agent["pattern"] in cmdline_str:
                    agents[key]["pid"] = proc.info['pid']
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Dummy 틱을 통해 cpu 클럭 수치 누적 개시
    processes_to_measure = {}
    for key, agent in agents.items():
        if agent["pid"] is not None:
            try:
                p = psutil.Process(agent["pid"])
                p.cpu_percent(interval=None)
                processes_to_measure[key] = p
            except Exception:
                pass

    # 0.1초 동안 cpu 점유율 누적 대기
    time.sleep(0.1)

    # 실제 수치 추출
    for key, p in processes_to_measure.items():
        try:
            agents[key]["cpu"] = p.cpu_percent(interval=None)
            agents[key]["mem_mb"] = p.memory_info().rss / (1024 * 1024)
        except Exception:
            agents[key]["pid"] = None

    return agents

# 9. 메타데이터 가공 인덱싱 성공/실패율 통계 파서
def get_metadata_stats():
    success_count = 0
    failed_count = 0
    total_files = 0
    recent_files = []

    if os.path.exists(METADATA_DIR):
        metadata_paths = list(Path(METADATA_DIR).glob("*.metadata.json"))
        total_files = len(metadata_paths)

        sorted_paths = sorted(metadata_paths, key=lambda p: p.stat().st_mtime, reverse=True)
        for path in metadata_paths:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if data.get("status") == "success":
                    success_count += 1
                else:
                    failed_count += 1
            except Exception:
                pass

        for path in sorted_paths[:10]:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                mtime = pd.Timestamp(path.stat().st_mtime, unit='s', tz='Asia/Seoul').strftime('%m-%d %H:%M:%S')
                recent_files.append({
                    "파일명": data.get("source_name", path.name),
                    "가공시간": mtime,
                    "상태": data.get("status", "unknown").upper(),
                    "분류군": data.get("ai_classification", {}).get("class_name", "미정")
                })
            except Exception:
                pass

    return success_count, failed_count, total_files, recent_files

# 10. 모하비/아우룸 보류 검수 목록 로더
def load_pending_queue():
    pending_list = []
    if os.path.exists(PENDING_FILE):
        try:
            with open(PENDING_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        pending_list.append(json.loads(line))
        except Exception:
            pass
    return pending_list

# --- 상단 타이틀 및 자동 갱신 제어 ---
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
col_title, col_refresh = st.columns([4, 1.2])
with col_title:
    st.markdown('<h1 style="margin:0; font-size:1.8rem; color:#4a4238; font-weight:800; line-height:1.2;">🌿 Fauna Ecological Swarm Dashboard</h1>', unsafe_allow_html=True)
with col_refresh:
    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
    auto_refresh = st.checkbox("🔄 실시간 자동 갱신 (1분)", value=True)

# --- 탭 구성 (RAG & 에이전트 모니터를 메인으로 배치) ---
tab1, tab2 = st.tabs(["💻 실시간 시스템 자원 & RAG 파이프라인", "🌿 현지조사 & 생태분석"])

# ──────────────────────────────────────────────────────────
# 💻 TAB 1: 실시간 시스템 자원 & RAG 파이프라인
# ──────────────────────────────────────────────────────────
with tab1:
    st.markdown('<h2 style="margin-top:0; color:#4a4238;">💻 RAG Pipeline & System Monitor</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.9rem; color:#7c7267; margin-bottom:15px;">아톰(Atom)·모하비(Mohave)·아우룸(Aurum) 3단 에이전트 구동 현황 및 Grace-Blackwell 실시간 자원 소비율</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    agent_res = get_agent_resources()
    indexer_running = agent_res.get("indexer", {}).get("pid") is not None
    indexer_status_html = ""
    if indexer_running:
        cpu_val = agent_res["indexer"]["cpu"]
        indexer_status_html = f'<div style="font-size:0.75rem; color:#059669; font-weight:700; margin-top:2px;">⚡ 색인 빌드 중 (CPU: {cpu_val:.1f}%)</div>'
    else:
        indexer_status_html = '<div style="font-size:0.75rem; color:#7c7267; margin-top:2px;">✓ 대기 완료 상태</div>'

    success_cnt, failed_cnt, total_cnt, recent_events = get_metadata_stats()
    rag_index_count, rag_model_name = get_rag_index_info()
    rag_index_count = rag_index_count or total_cnt
    pending_queue = load_pending_queue()

    # KPI 대시보드 카드 영역
    st.markdown(f"""
        <div class="kpi-wrapper">
            <div class="kpi-glass-card" style="border-top: 4px solid #7c7267;">
                <div class="kpi-lbl">누적 가공 인덱스 (RAG)</div>
                <div class="kpi-val">{rag_index_count:,}<span class="kpi-unit">건</span></div>
                <div style="font-size:0.7rem; color:#7c7267; margin-top:2px; word-break:break-all;">🏷️ {rag_model_name}</div>
                {indexer_status_html}
            </div>
            <div class="kpi-glass-card" style="border-top: 4px solid var(--success-color);">
                <div class="kpi-lbl" style="color: var(--success-color);">정상 가공 성공</div>
                <div class="kpi-val" style="color: var(--success-color);">{success_cnt}<span class="kpi-unit" style="color: var(--success-color);">건</span></div>
            </div>
            <div class="kpi-glass-card" style="border-top: 4px solid var(--error-color);">
                <div class="kpi-lbl" style="color: var(--error-color);">가공 오류 실패</div>
                <div class="kpi-val" style="color: var(--error-color);">{failed_cnt}<span class="kpi-unit" style="color: var(--error-color);">건</span></div>
            </div>
            <div class="kpi-glass-card" style="border-top: 4px solid var(--warning-color);">
                <div class="kpi-lbl" style="color: var(--warning-color);">모하비/아우룸 검수 대기</div>
                <div class="kpi-val" style="color: var(--warning-color);">{len(pending_queue)}<span class="kpi-unit" style="color: var(--warning-color);">건</span></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 1차 전수조사 RAG 인덱싱 진행도 바
    total_files, completed_files, pending_files, progress_rate, current_file = get_full_scan_progress()

    current_file_html = ""
    if current_file:
        current_file_html = f'<div style="font-size:0.8rem; color:#7c7267; margin-top:8px; font-style:italic; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">🕒 현재 가공 중: {current_file}</div>'

    st.markdown(f"""
        <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 10px; padding: 16px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 0.9rem; font-weight: 700; color: var(--text-color); display: flex; align-items: center; gap: 8px;">📊 1차 전수조사 RAG 인덱싱 진행도 (Full Indexing Progress)</span>
                <span style="font-size: 1.15rem; font-weight: 800; color: var(--success-color);">{progress_rate:.4f}%</span>
            </div>
            <div style="width: 100%; background-color: #e5e7eb; border-radius: 9999px; height: 12px; overflow: hidden; margin-bottom: 12px; border: 1px solid #e1dad0;">
                <div style="width: {progress_rate}%; background: linear-gradient(90deg, var(--success-color) 0%, #059669 100%); height: 100%; border-radius: 9999px; transition: width 0.5s ease-in-out;"></div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; text-align: center;">
                <div style="border-right: 1px solid var(--border-color);">
                    <div style="font-size: 0.75rem; color: #7c7267; text-transform: uppercase;">전수조사 대상 파일 수</div>
                    <div style="font-size: 1.1rem; font-weight: 800; color: var(--text-color); margin-top: 2px;">{total_files:,} <span style="font-size: 0.75rem; font-weight: 400; color:#7c7267;">개</span></div>
                </div>
                <div style="border-right: 1px solid var(--border-color);">
                    <div style="font-size: 0.75rem; color: var(--success-color); text-transform: uppercase;">1차 가공 완료</div>
                    <div style="font-size: 1.1rem; font-weight: 800; color: var(--success-color); margin-top: 2px;">{completed_files:,} <span style="font-size: 0.75rem; font-weight: 400; color:var(--success-color);">개</span></div>
                </div>
                <div>
                    <div style="font-size: 0.75rem; color: var(--error-color); text-transform: uppercase;">남은 미처리 대상</div>
                    <div style="font-size: 1.1rem; font-weight: 800; color: var(--error-color); margin-top: 2px;">{pending_files:,} <span style="font-size: 0.75rem; font-weight: 400; color:var(--error-color);">개</span></div>
                </div>
            </div>
            {current_file_html}
        </div>
    """, unsafe_allow_html=True)

    # 본문 2분할 레이아웃
    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.markdown("<h3 style='margin-top:0; color:#4a4238; font-size:1.1rem;'>💡 협업 에이전트 구동 현황 (Online Status)</h3>", unsafe_allow_html=True)
        # agent_res는 이미 상단에서 선언 및 사용됨 (중복 측정 방지를 위해 호출 생략)

        st.markdown("<div class='agent-grid'>", unsafe_allow_html=True)
        for key, agent in agent_res.items():
            if agent["pid"] is not None:
                status_badge = f'<div class="badge-running"><span class="pulse-green">●</span> RUNNING</div>'
                details = f'<span style="color: #4b5563;">PID: <b>{agent["pid"]}</b></span> | <span style="color: var(--success-color);">CPU: <b>{agent["cpu"]:.1f}%</b></span> | <span style="color: #4b5563;">RAM: <b>{agent["mem_mb"]:.1f} MB</b></span>'
            else:
                status_badge = '<div class="badge-stopped"><span class="pulse-red">■</span> STOPPED</div>'
                details = '<span style="color: #9ca3af;">프로세스가 활성화되어 있지 않습니다.</span>'

            card_html = (
                f'<div class="agent-card">'
                f'<div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">'
                f'<div style="font-weight: 700; color: var(--text-color); font-size: 0.85rem;">{agent["name"]}</div>'
                f'{status_badge}'
                f'</div>'
                f'<div style="margin-top: 4px; font-size: 0.75rem;">{details}</div>'
                f'</div>'
            )
            st.markdown(card_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#4a4238; font-size:1.1rem;'>⚠️ 모하비 & 아우룸 피드백 검수 대기 목록</h3>", unsafe_allow_html=True)
        if pending_queue:
            pending_df = pd.DataFrame(pending_queue)
            st.dataframe(
                pending_df[["created_at", "source_name", "project_name", "inferred_class", "status"]].rename(
                    columns={
                        "created_at": "등록시간",
                        "source_name": "파일명",
                        "project_name": "사업명",
                        "inferred_class": "추론분류",
                        "status": "상태"
                    }
                ),
                use_container_width=True,
                height=220
            )
        else:
            st.markdown('<div class="info-box">현재 모하비 및 아우룸의 피드백 검수를 대기 중인 보류 파일이 없습니다. (상태 양호)</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown("<h3 style='margin-top:0; color:#4a4238; font-size:1.1rem;'>💻 실시간 시스템 자원 소비율 (System Resources)</h3>", unsafe_allow_html=True)
        sys_res = get_system_resources()
        gpu_res = get_gpu_status()

        cpu_temp_val = f"{sys_res['cpu_temp']:.1f}°C" if sys_res['cpu_temp'] is not None else "N/A"
        cpu_temp_class = "temp-cool" if sys_res['cpu_temp'] is None or sys_res['cpu_temp'] < 65 else ("temp-warm" if sys_res['cpu_temp'] < 80 else "temp-hot")

        st.markdown(f"""
            <div class="hw-grid">
                <div class="hw-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="hw-title">🖥️ 전체 CPU 사용률</span>
                        <span class="hw-temp-badge {cpu_temp_class}">🌡️ {cpu_temp_val}</span>
                    </div>
                    <div class="hw-value" style="text-align: left; margin-top: 3px;">{sys_res["cpu_usage"]:.1f}%</div>
                </div>
                <div class="hw-card">
                    <div class="hw-title" style="text-align: left;">💾 전체 메모리 (RAM)</div>
                    <div class="hw-value" style="text-align: left; margin-top: 3px;">{sys_res["mem_usage"]:.1f}%</div>
                    <div style="font-size:0.7rem; color:#7c7267; margin-top:3px; text-align: left;">{sys_res["mem_used"]:.1f} / {sys_res["mem_total"]:.1f} GB</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if gpu_res:
            for gpu in gpu_res:
                gpu_temp_class = "temp-cool" if gpu["temp"] < 65 else ("temp-warm" if gpu["temp"] < 80 else "temp-hot")
                if gpu["mem_used"] is None or gpu["mem_total"] is None:
                    mem_val = "Unified"
                    mem_desc = "호스트 RAM 공유 (통합 메모리)"
                else:
                    mem_val = f"{(gpu['mem_used']/gpu['mem_total'])*100:.1f}%"
                    mem_desc = f"{gpu['mem_used']:.1f} / {gpu['mem_total']:.1f} GB"

                st.markdown(f"""
                    <div class="hw-grid" style="grid-template-columns: 1fr 1fr; margin-top: 10px;">
                        <div class="hw-card" style="grid-column: span 2; display: flex; justify-content: space-between; align-items: center; padding: 6px 10px;">
                            <div style="text-align: left;">
                                <div class="hw-title" style="margin-bottom:0; font-weight:700;">📟 GPU #{gpu["id"]} - {gpu["name"]}</div>
                            </div>
                            <div class="hw-temp-badge {gpu_temp_class}">🔥 {gpu["temp"]}°C</div>
                        </div>
                        <div class="hw-card">
                            <div class="hw-title" style="text-align: left;">🎨 GPU 코어 사용률</div>
                            <div class="hw-value" style="text-align: left; margin-top: 3px;">{gpu["util"]}%</div>
                        </div>
                        <div class="hw-card">
                            <div class="hw-title" style="text-align: left;">📼 GPU 메모리 (VRAM)</div>
                            <div class="hw-value" style="text-align: left; margin-top: 3px;">{mem_val}</div>
                            <div style="font-size:0.7rem; color:#7c7267; margin-top:3px; text-align: left;">{mem_desc}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="background:#ffffff; border: 1px solid var(--border-color); border-radius:8px; padding:10px; margin-top:8px; font-size:0.75rem; color:#7c7267;">
                    📟 GPU 정보 비활성화 (NVIDIA 드라이버 확인 필요)
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#4a4238; font-size:1.1rem;'>📋 최근 10개 파일 가공 이력</h3>", unsafe_allow_html=True)
        if recent_events:
            recent_df = pd.DataFrame(recent_events)
            st.dataframe(
                recent_df[["가공시간", "파일명", "상태", "분류군"]],
                use_container_width=True,
                height=260
            )
        else:
            st.markdown('<div class="info-box">최근 가공된 내역이 없습니다.</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# 🌿 TAB 2: 현지조사 & 생태분석 (원래 대시보드 뷰)
# ──────────────────────────────────────────────────────────
with tab2:
    st.markdown('<h2 style="margin-top:0; color:#4a4238;">🌿 Fauna Ecological Survey & Analysis</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.9rem; color:#7c7267; margin-bottom:15px;">정밀 생태 조사 기록 및 실시간 생태적 다양성 수치 계산 시스템 (Shannon-Wiener, Pielou Evenness)</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.subheader("📝 현장 조사 기록 입력")
    with st.form("entry_form", clear_on_submit=True):
        c1, c2, c3, c4 = st.columns([1.5, 3, 1, 1.5])
        with c1:
            status = st.radio("출현 상태", ["당회(○)", "누적(●)"], horizontal=True)
        with c2:
            species = st.selectbox("종명 검색 (분류체계 자동 매핑)", options=[""] + list(species_index.keys()), index=0)
        with c3:
            count = st.number_input("개체수", min_value=1, value=1)
        with c4:
            location = st.text_input("조사 지역", value="현장")

        submitted = st.form_submit_button("기록 추가", use_container_width=True)

        if submitted:
            if species and species != "":
                info = species_index.get(species, {})
                new_row = {
                    'Type': '현지조사',
                    'Species': species,
                    'Count': count,
                    'Status': status,
                    'Location': location,
                    'Class': info.get('Class', '미상'),
                    'Order': info.get('Order', '미상'),
                    'Family': info.get('Family', '미상')
                }
                st.session_state.survey_log = pd.concat([st.session_state.survey_log, pd.DataFrame([new_row])], ignore_index=True)
                st.success(f"'{species}' 기록이 성공적으로 추가되었습니다. (분류군: {info.get('Order', '미상')} / {info.get('Family', '미상')})")
                st.rerun()
            else:
                st.error("종명을 정확히 선택해 주세요.")

    st.markdown("<br>", unsafe_allow_html=True)
    log_df = st.session_state.survey_log

    if not log_df.empty:
        st.subheader("📊 실시간 생태 분석 결과")

        total_individuals = log_df['Count'].sum()
        species_counts = log_df.groupby('Species')['Count'].sum()
        total_species = len(species_counts)

        proportions = species_counts / total_individuals
        shannon_h = -np.sum(proportions * np.log(proportions)) if total_individuals > 0 else 0
        pielou_j = shannon_h / np.log(total_species) if total_species > 1 else 0

        # KPI Metrics for Shannon Index
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("총 관찰 종수 (S)", f"{total_species} 종")
        m2.metric("전체 개체수 (N)", f"{total_individuals} 개체")
        m3.metric("우점 분류군", log_df['Order'].mode()[0] if not log_df['Order'].empty else "-")
        m4.metric("종다양도 (H')", f"{shannon_h:.3f}")
        m5.metric("균등도 (J')", f"{pielou_j:.3f}")

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.markdown("**🌱 분류군별 개체수 분포 (Sunburst Chart)**")
            fig = px.sunburst(
                log_df,
                path=['Status', 'Class', 'Order', 'Species'],
                values='Count',
                color='Status',
                color_discrete_map={"당회(○)": "#a7c957", "누적(●)": "#6a994e"},
                template="plotly_white",
                height=450
            )
            fig.update_layout(
                margin=dict(t=10, l=10, r=10, b=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Pretendard, Outfit", color="#3c3c3c")
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("**📋 조사 데이터 원본**")
            st.dataframe(log_df[['Status', 'Species', 'Count', 'Location', 'Order']], height=380, use_container_width=True)

            csv = log_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 분석 데이터 CSV 내보내기",
                data=csv,
                file_name='fauna_ecological_analysis.csv',
                mime='text/csv',
                use_container_width=True
            )

        st.markdown("---")
        st.subheader("📊 추가 시각화: 종 구성 비율 (Pie Chart)")
        fig_pie = px.pie(
            log_df,
            values='Count',
            names='Species',
            color_discrete_sequence=px.colors.qualitative.Pastel,
            hole=0.4,
            template="plotly_white"
        )
        fig_pie.update_layout(
            margin=dict(t=20, b=20, l=20, r=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Pretendard, Outfit", color="#3c3c3c"),
            legend=dict(orientation="h", y=-0.1)
        )
        st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("---")
        st.subheader("📄 최종 생태 분석 결과 보고서 (Text Summary)")
        report_text = f"""
### 🌿 생태계 조사 분석 보고서
**조사 일시:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}
**데이터 상태:** {status} (누적/단일 기반)

#### 1. 생태 지표 요약
- **종 풍부도 (Species Richness):** {total_species} 종
- **총 개체수 (Total Abundance):** {total_individuals} 개체
- **Shannon-Wiener 지수 (H'):** {shannon_h:.3f}
- **Pielou 균등도 (J'):** {pielou_j:.3f}

#### 2. 주요 분석 내용
- **우점 분류군:** {log_df['Order'].mode()[0] if not log_df['Order'].empty else '-'}
- **최근 관찰 기록:** {', '.join(log_df['Species'].tail(3).tolist())}

#### 3. 종합 결론
본 조사 지역의 생태적 다양성은 Shannon 지수 {shannon_h:.3f}로 측정되었습니다.
균등도({pielou_j:.3f})를 고려할 때, 특정 종에 의한 우점 현상이 {'관찰됨' if pielou_j < 0.6 else '미미함'}을 나타냅니다.
"""
        st.text_area("보고서 전문 (복사 가능)", report_text, height=300)
    else:
        st.markdown('<div class="info-box">💡 위의 폼에서 조사 기록을 입력하면, 실시간으로 생태 통계 분석(H\', J\') 및 시각화 결과가 나타납니다.</div>', unsafe_allow_html=True)

# 11. 자동 갱신 루프 처리
if auto_refresh:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=60000, key="datarefresh")
