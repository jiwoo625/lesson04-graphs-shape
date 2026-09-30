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
st.write(
    "1년간 박스오피스 10위권에 든 영화 가운데 이 기간에 개봉한 216편의 데이터를 살펴봅니다."
)

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    # 장르가 여러 개 적힌 경우 첫 번째 장르만 사용
    df["genre"] = df["genre"].fillna("미상").astype(str).str.split("|").str[0].str.strip()
    return df

try:
    df = load_data()
except Exception as e:
    st.error("데이터를 불러오는 중 오류가 발생했습니다.")
    st.exception(e)
    st.stop()

# ---------------------------------------------------------
# 그래프 1. 장르별 영화 편수
# ---------------------------------------------------------
st.subheader("1. 장르별 영화 편수")

genre_counts = (
    df["genre"]
    .value_counts()
    .rename_axis("장르")
    .reset_index(name="영화 편수")
)

fig = px.pie(
    genre_counts,
    names="장르",
    values="영화 편수",
    hole=0.55,
    title="장르별 영화 편수",
)

fig.update_traces(
    hovertemplate="<b>%{label}</b><br>편수: %{value}편<br>비율: %{percent}<extra></extra>"
)

fig.update_layout(
    margin=dict(t=60, b=20, l=20, r=20),
    legend_title_text="장르",
)

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    <div style="
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 16px;
        margin-top: 8px;
        margin-bottom: 28px;
        background-color: #fafafa;
    ">
        <b>이 그래프로 알 수 있는 것</b><br>
        어떤 장르의 영화가 이 기간에 개봉한 박스오피스 10위권 영화에서 많이 나타났는지 한눈에 비교할 수 있습니다.
    </div>
    """,
    unsafe_allow_html=True,
)

# 이후 그래프를 추가할 수 있도록 구역을 미리 분리
st.divider()
st.subheader("2. 다음 그래프")
st.info("여기에 다음 분포·관계 그래프를 추가할 수 있습니다.")

st.markdown(
    """
    <div style="
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 16px;
        margin-top: 8px;
        background-color: #fafafa;
    ">
        <b>이 그래프로 알 수 있는 것</b><br>
        이 그래프에서 발견한 특징을 한 문장으로 정리하는 공간입니다.
    </div>
    """,
    unsafe_allow_html=True,
)
