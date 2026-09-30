
import streamlit as st
import pandas as pd
import plotly.express as px


# ─────────────────────────────────────────────
# 페이지 설정
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    layout="wide",
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")


# ─────────────────────────────────────────────
# 데이터 불러오기
# ─────────────────────────────────────────────
DATA_URL = (
    "https://raw.githubusercontent.com/greatsong/modudata/"
    "main/data/kobis_movies.csv"
)


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 여러 장르가 있으면 첫 번째 장르만 사용
    df["장르"] = (
        df["genre"]
        .fillna("미상")
        .astype(str)
        .str.split("|")
        .str[0]
        .str.strip()
    )

    return df


df = load_data()


# ─────────────────────────────────────────────
# 그래프 1. 장르별 영화 편수
# ─────────────────────────────────────────────
st.header("1. 장르별 영화 편수")

genre_count = (
    df["장르"]
    .value_counts()
    .reset_index()
)

genre_count.columns = [
    "장르",
    "영화 편수",
]

fig1 = px.pie(
    genre_count,
    names="장르",
    values="영화 편수",
    hole=0.5,
)

fig1.update_traces(
    hovertemplate=(
        "장르 %{label}"
        "<br>영화 편수 %{value}편"
        "<br>비율 %{percent}"
        "<extra></extra>"
    )
)

fig1.update_layout(
    legend_title_text="장르",
)

st.plotly_chart(
    fig1,
    width="stretch",
)

st.caption(
    "이 그래프로 알 수 있는 것: __________________________________"
)


# ─────────────────────────────────────────────
# 그래프 2
# ─────────────────────────────────────────────
# 다음 그래프를 이곳에 추가


# ─────────────────────────────────────────────
# 그래프 3
# ─────────────────────────────────────────────
# 다음 그래프를 이곳에 추가

