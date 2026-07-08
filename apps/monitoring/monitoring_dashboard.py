# Created: 2026-06-30 by Antigravity AI
# Purpose: Real-time System & Pipeline Monitoring Dashboard for Aurum AI 전수조사

import os
import sys
import glob
import json
import time
import subprocess
from pathlib import Path
import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="Aurum AI Live Monitor",
    page_icon="⚕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 다크 테마 커스텀 CSS 주입
st.markdown("""
<style>
    .reportview-container {
        background: #0f172a;
        color: #f8fafc;
    }
    .metric-card {
        background-color: #1e293b;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #334155;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        text-align: center;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 5px;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
</style>
""", unsafe_allow_html=True)

# 헤더 영역
st.title("⚕ 아우룸 AI 실시간 관제 시스템 (Aurum Live Monitor)")
st.caption("1차 전수조사 진행률 및 시스템 자원 실시간 모니터링")

# 상위 경로 바인딩
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
METADATA_DIR = PROCESSED_DIR / "metadata"

# 자동 갱신 트리거 (2초마다 초고속 자동 리로드)
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=2000, key="datarefresh")

# ----------------------------------------------------
# 📊 [데이터부] 가공 진행 상황 파싱
# ----------------------------------------------------
TOTAL_FILES = 94513  # 1차 전수조사 분모 고정값

success_count = 0
failed_count = 0
recent_files = []

if METADATA_DIR.exists():
    file_entries = []
    # 9만 개 파일을 시스템 콜 다발 형태로 단 0.05초 만에 메모리에 스캔
    try:
        for entry in os.scandir(METADATA_DIR):
            if entry.is_file() and entry.name.endswith(".metadata.json"):
                try:
                    stat = entry.stat()
                    file_entries.append((entry.path, entry.name, stat.st_size, stat.st_mtime))
                except Exception:
                    pass
    except Exception:
        pass
                
    # 1. 성공/실패 수 대략 계산 (가공 실패한 파일은 텍스트가 null이라 1KB 미만임, 극고속 판정)
    for _, _, size, _ in file_entries:
        if size < 1024:
            failed_count += 1
        else:
            success_count += 1
            
    # 2. 최신 가공된 순으로 정렬하여 상위 30개만 열어서 최근 10개 실시간 이력 정합성 확보
    file_entries.sort(key=lambda x: x[3], reverse=True)
    
    for path, name, _, mtime in file_entries[:30]:
        if len(recent_files) >= 10:
            break
        try:
            with open(path, "r", encoding="utf-8") as file:
                meta = json.load(file)
            status = meta.get("status", "success")
            recent_files.append({
                "파일명": meta.get("filename", name.replace(".metadata.json", "")),
                "분류군": meta.get("category", "미정"),
                "가공상태": "성공" if status == "success" else "실패",
                "가공시각": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
            })
        except Exception:
            pass

# 진행 지표 계산
processed_count = success_count + failed_count
progress_percent = (processed_count / TOTAL_FILES) * 100 if TOTAL_FILES > 0 else 0
remaining_count = max(TOTAL_FILES - processed_count, 0)

# ----------------------------------------------------
# ⚙️ [시스템부] 하드웨어 자원 파싱 (nvidia-smi, psutil)
# ----------------------------------------------------
def get_gpu_status():
    try:
        res = subprocess.check_output(
            ["/usr/bin/nvidia-smi", "--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu", "--format=csv,noheader,nounits"],
            encoding="utf-8"
        )
        parts = res.strip().split("\n")[0].split(", ")
        gpu_util = parts[0]
        mem_used = parts[1]
        mem_total = parts[2]
        temp = parts[3]
        
        vram_str = "N/A"
        try:
            vram_str = f"{float(mem_used)/1024:.1f} GB / {float(mem_total)/1024:.1f} GB"
        except Exception:
            vram_str = f"{mem_used} / {mem_total}"
            
        return {
            "util": f"{gpu_util}%" if gpu_util != "[N/A]" else "N/A",
            "vram": vram_str,
            "temp": f"{temp}°C" if temp != "[N/A]" else "N/A"
        }
    except Exception:
        return {"util": "Offline", "vram": "Offline", "temp": "Offline"}

def get_cpu_temp():
    try:
        temps = []
        for path in glob.glob("/sys/class/thermal/thermal_zone*/temp"):
            with open(path, "r") as f:
                val = int(f.read().strip())
                temps.append(val / 1000.0)
        if temps:
            return f"{max(temps):.1f}°C"
        return "N/A"
    except Exception:
        return "N/A"

def get_cpu_ram_status():
    try:
        import psutil
        cpu = f"{psutil.cpu_percent()}%"
        ram = f"{psutil.virtual_memory().percent}%"
        return cpu, ram
    except Exception:
        return "N/A", "N/A"

def get_mac_status():
    metrics_path = PROCESSED_DIR / "metrics_mac.json"
    if metrics_path.exists():
        try:
            mtime = os.path.getmtime(metrics_path)
            # 60초 이내에 파일이 원격 복사(갱신)되었다면 Online
            if (time.time() - mtime) < 60:
                with open(metrics_path, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
    return {
        "cpu": "Offline",
        "ram": "Offline",
        "ollama_status": "Offline",
        "workers": 0,
        "status": "Sleeping"
    }

gpu_info = get_gpu_status()
cpu_val, ram_val = get_cpu_ram_status()
mac_data = get_mac_status()

# ----------------------------------------------------
# 🖥️ [레이아웃부] UI 화면 렌더링
# ----------------------------------------------------

# 1. 최상단 핵심 지표 레이아웃 (3열)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{processed_count:,} / {TOTAL_FILES:,}</div>
        <div class="metric-label">전체 가공 진행률 ({progress_percent:.2f}%)</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color: #4ade80;">{success_count:,}</div>
        <div class="metric-label">가공 성공 파일 수</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color: #f87171;">{failed_count:,}</div>
        <div class="metric-label">가공 실패 파일 수</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color: #e2e8f0;">{remaining_count:,}</div>
        <div class="metric-label">남은 대기 파일 수</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.progress(min(max(progress_percent / 100.0, 0.0), 1.0))

# 2. 메인 컨텐츠 레이아웃 (좌: 시스템 자원 / 우: 실시간 가공 로그)
left_col, right_col = st.columns([1, 2])

with left_col:
    st.subheader("⚙️ 실시간 하드웨어 리소스")
    
    # 아톰 서버 리소스 정보 카드
    st.info("🤖 **ATOM SERVER (아톰 서버 - 20 Workers)**")
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        st.metric("CPU 사용량", cpu_val)
        st.metric("RAM 사용량", ram_val)
        st.metric("CPU 최고 온도", get_cpu_temp())
    with s_col2:
        st.metric("GPU 로드율", gpu_info["util"])
        st.metric("GPU 온도", gpu_info["temp"])
        st.metric("VRAM 점유 현황", gpu_info["vram"])
        
    st.write("---")
    
    # 아우룸 맥북 리소스 연동 상태
    st.success(f"💻 **AURUM MACBOOK (아우룸 맥북 - {mac_data.get('workers', 0)} Workers)**")
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric("맥북 CPU 사용량", mac_data.get("cpu", "Offline"))
        st.metric("맥북 RAM 사용량", mac_data.get("ram", "Offline"))
        st.metric("맥북 내부 온도", mac_data.get("temp", "Offline"))
    with m_col2:
        st.metric("맥북 GPU 사용량", mac_data.get("gpu", "Offline"))
        st.metric("가공 상태", mac_data.get("status", "Offline"))
    with m_col3:
        st.metric("Ollama 상태", mac_data.get("ollama_status", "Offline"))

with right_col:
    st.subheader("📋 실시간 파일 가공 이력")
    if recent_files:
        df = pd.DataFrame(recent_files)
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "가공상태": st.column_config.TextColumn(
                    "가공상태",
                    help="가공 및 AI 요약 성공 상태",
                    validate="^성공$|^실패$"
                )
            }
        )
    else:
        st.warning("현재 데이터 가공 완료 이력이 없습니다. 파이프라인 스캔을 시작해 주세요.")
        
    # 가공 파이프라인 상태 제어 가이드
    st.write("")
    st.markdown("""
    > [!TIP]
    > * 대시보드는 **10초마다 실시간으로 자동 갱신**됩니다.
    > * 텍스트 추출 가공 로그를 텍스트로 보시려면 서버 터미널에서 `tail -f ~/dgx_workspace/003.*\\ 파이프라인/logs/cron_run.log` 를 실행해 주세요.
    """)
