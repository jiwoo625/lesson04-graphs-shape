import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    layout="wide"
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    df["장르"] = df["genre"].str.split("|").str[0]
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
    hole=0.45
)

fig.update_traces(
    hovertemplate="%{label}<br>%{value}편 (%{percent})<extra></extra>"
)

st.plotly_chart(fig, width="stretch")

st.text_input("이 그래프로 알 수 있는 것", key="note1")


# ── 그래프 2. 장르 안의 영화 (트리맵) ──
st.header("2. 장르 안의 영화 (트리맵)")

fig2 = px.treemap(
    df,
    path=["장르", "movieNm"],
    values="total_audi"
)

fig2.update_traces(
    textfont=dict(color="black"),
    hovertemplate="<b>%{label}</b><br>총 관객: %{value:,}명<extra></extra>"
)

st.plotly_chart(fig2, width="stretch")

st.text_input("이 그래프로 알 수 있는 것", key="note2")
