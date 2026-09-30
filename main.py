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
    df["장르"] = df["genre"].fillna("미상").str.split("|").str[0]
    return df


try:
    df = load_data()

except Exception:
    st.error("데이터를 불러오지 못했습니다.")
    st.write("현재 지정된 GitHub CSV 주소에 접근할 수 없습니다.")
    st.stop()


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

fig.update_traces(
    hovertemplate="%{label}<br>%{value}편 (%{percent})<extra></extra>"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.text_input(
    "이 그래프로 알 수 있는 것",
    key="note1"
)

st.divider()

st.header("2. (다음 그래프를 여기에 추가)")
