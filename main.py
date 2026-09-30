
import io

import streamlit as st
import pandas as pd
import plotly.express as px
import requests


st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    layout="wide"
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"


@st.cache_data
def load_data():
    # 1년간 박스오피스 10위권에 든 영화 216편의 요약표를 불러옵니다
    response = requests.get(
        DATA_URL,
        timeout=20,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response.raise_for_status()

    df = pd.read_csv(io.BytesIO(response.content))

    # 장르가 세로막대 기호(|)로 여러 개 적힌 영화는 첫 번째 장르만 씁니다
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


# ── 그래프 1. 장르별 영화 편수 도넛 ──

st.header("1. 장르별 영화 편수 (도넛)")

genre_count = df["장르"].value_counts().reset_index()
genre_count.columns = ["장르", "편수"]

fig = px.pie(
    genre_count,
    names="장르",
    values="편수",
    hole=0.45,
)

# 조각에 마우스를 올리면 편수와 비율이 보이게 합니다
fig.update_traces(
    hovertemplate="%{label}<br>%{value}편 (%{percent})<extra></extra>"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# '이 그래프로 알 수 있는 것' 한 문장을 적는 자리
st.text_input(
    "이 그래프로 알 수 있는 것",
    key="note1"
)


st.divider()


# 앞으로 그래프를 계속 추가할 구역
st.header("2. (다음 그래프를 여기에 추가)")

