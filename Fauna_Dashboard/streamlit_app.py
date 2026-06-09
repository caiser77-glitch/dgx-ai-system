import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
import json

# 1. 페이지 설정 및 경로 정의
st.set_page_config(page_title="Fauna Unified Dashboard", layout="wide", page_icon="🌿")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'species_search_index.json')

# 🎨 파스텔톤 라이트 테마 커스텀 CSS (미니멀 원페이지 디자인)
st.markdown("""
    <style>
    :root {
        --primary-color: #8bb2a5;
        --background-color: #fcfcfc;
        --card-bg: #ffffff;
        --text-color: #4a4a4a;
    }
    html, body, [class*="css"] { 
        font-size: 15px; 
        background-color: var(--background-color); 
        color: var(--text-color);
        font-family: 'Pretendard', -apple-system, sans-serif;
    }
    .stApp { background-color: var(--background-color); }
    .css-1d391kg { background-color: var(--card-bg); border-radius: 12px; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    
    /* Metrics Styling */
    [data-testid="stMetricValue"] { color: #5c7f71; font-weight: 700; font-size: 1.8rem; }
    [data-testid="stMetricLabel"] { color: #7a9c90; font-weight: 600; font-size: 1.0rem; }
    div[data-testid="metric-container"] { 
        background-color: #f5f8f7; 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 5px solid var(--primary-color);
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    h1, h2, h3 { color: #5c7f71; font-weight: 600; }
    div[data-testid="stForm"] { background-color: #fdfdfd; border: 1px solid #e1e8e5; border-radius: 10px; padding: 20px; }
    button[kind="primary"] { background-color: var(--primary-color); color: white; border: none; border-radius: 8px; font-weight: 600; }
    button[kind="primary"]:hover { background-color: #7a9c90; }
    hr { border-color: #e1e8e5; }
    </style>
    """, unsafe_allow_html=True)

# 2. 데이터 로드
@st.cache_resource
def load_index():
    if os.path.exists(DATA_PATH):
        try:
            with open(DATA_PATH, 'r', encoding='utf-8') as f: 
                return json.load(f)
        except Exception as e:
            st.warning(f"인덱스 로드 실패: {e}")
            return {}
    return {}

species_index = load_index()

# 3. 세션 상태 초기화
if 'survey_log' not in st.session_state:
    st.session_state.survey_log = pd.DataFrame(columns=['Type', 'Species', 'Count', 'Status', 'Location', 'Class', 'Order', 'Family'])

# --- UI 레이아웃 (미니멀 원페이지) ---
st.title("🌿 Fauna Ecological Dashboard")
st.markdown("**정밀 조사 기록 및 실시간 생태 통계 분석 시스템 (Shannon-Wiener, Pielou)**")
st.markdown("---")

# 1단 레이아웃: 데이터 입력 폼
st.subheader("📝 현장 조사 기록 입력")
with st.form("entry_form", clear_on_submit=True):
    c1, c2, c3, c4 = st.columns([1.5, 3, 1, 1.5])
    with c1: 
        status = st.radio("출현 상태", ["당회(○)", "누적(●)"], horizontal=True)
    with c2: 
        # 검색 자동 완성
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
            # 데이터프레임에 추가
            st.session_state.survey_log = pd.concat([st.session_state.survey_log, pd.DataFrame([new_row])], ignore_index=True)
            st.success(f"'{species}' 기록이 성공적으로 추가되었습니다. (분류군: {info.get('Order', '미상')} / {info.get('Family', '미상')})")
            st.rerun()
        else:
            st.error("종명을 정확히 선택해 주세요.")

st.markdown("<br>", unsafe_allow_html=True)

# 2단 레이아웃: 통계 지표 및 시각화 (데이터가 있을 때만 표시)
log_df = st.session_state.survey_log

if not log_df.empty:
    st.subheader("📊 실시간 생태 분석 결과")
    
    # 지표 계산 로직 (Shannon-Wiener, Pielou)
    total_individuals = log_df['Count'].sum()
    species_counts = log_df.groupby('Species')['Count'].sum()
    total_species = len(species_counts)
    
    # H' (Shannon-Wiener Index)
    proportions = species_counts / total_individuals
    shannon_h = -np.sum(proportions * np.log(proportions)) if total_individuals > 0 else 0
    
    # J' (Pielou's Evenness)
    pielou_j = shannon_h / np.log(total_species) if total_species > 1 else 0

    # 주요 지표 표시
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("총 관찰 종수 (S)", f"{total_species} 종")
    m2.metric("전체 개체수 (N)", f"{total_individuals} 개체")
    m3.metric("우점 분류군", log_df['Order'].mode()[0] if not log_df['Order'].empty else "-")
    m4.metric("종다양도 (H')", f"{shannon_h:.3f}")
    m5.metric("균등도 (J')", f"{pielou_j:.3f}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 시각화 및 데이터 표 (2분할)
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown("**🌱 분류군별 개체수 분포 (Sunburst Chart)**")
        fig = px.sunburst(
            log_df, 
            path=['Status', 'Class', 'Order', 'Species'], 
            values='Count', 
            color='Status',
            color_discrete_map={"당회(○)": "#a8d5c2", "누적(●)": "#8bb2a5"},
            height=450
        )
        fig.update_layout(
            margin=dict(t=10, l=10, r=10, b=10), 
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("**📋 조사 데이터 원본**")
        st.dataframe(log_df[['Status', 'Species', 'Count', 'Location', 'Order']], height=380, use_container_width=True)
        
        # 내보내기 기능
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
            color_discrete_sequence=px.colors.sequential.RdPu_r,
            hole=0.4
        )
        fig_pie.update_layout(margin=dict(t=0, b=0, l=0, r=0), legend=dict(orientation="h", y=-0.2))
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
    st.info("💡 위의 폼에서 조사 기록을 입력하면, 실시간으로 생태 통계 분석(H', J') 및 시각화 결과가 나타납니다.")
