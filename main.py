import streamlit as st
import pandas as pd
import plotly.express as px

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"

st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    page_icon="🎬",
    layout="wide",
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")
st.write("1년간 박스오피스 10위권에 든 영화 가운데 해당 기간에 개봉한 216편의 데이터를 살펴봅니다.")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    # 세로막대(|)로 여러 장르가 적힌 경우 첫 번째 장르만 사용
    df["genre"] = df["genre"].fillna("미상").astype(str).str.split("|").str[0].str.strip()
    return df

try:
    df = load_data()
except Exception as e:
    st.error("데이터를 불러오지 못했습니다. 인터넷 연결과 데이터 주소를 확인해 주세요.")
    st.exception(e)
    st.stop()

# 숫자형 열 정리
numeric_cols = [
    "first_scrn",
    "first_show",
    "first_week_audi",
    "total_audi",
    "days_in_top10",
]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# -------------------------
# 그래프 1: 장르별 영화 편수
# -------------------------
st.subheader("① 장르별 영화 편수")

genre_counts = (
    df["genre"]
    .value_counts()
    .rename_axis("genre")
    .reset_index(name="count")
)

fig = px.pie(
    genre_counts,
    names="genre",
    values="count",
    hole=0.48,
    title="장르별 영화 편수",
)
fig.update_traces(
    textinfo="percent",
    hovertemplate="<b>%{label}</b><br>편수: %{value}편<br>비율: %{percent}<extra></extra>",
)
fig.update_layout(
    legend_title_text="장르",
    margin=dict(t=60, l=20, r=20, b=20),
)

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    <div style="
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 14px 18px;
        margin-top: 4px;
        background-color: #fafafa;
    ">
        <b>이 그래프로 알 수 있는 것</b><br>
        <span style="color:#666;">여기에 이 그래프에서 발견한 특징을 한 문장으로 적어 보세요.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

st.caption(f"전체 영화 수: {len(df)}편")
