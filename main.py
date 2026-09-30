import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    layout="wide"
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")


@st.cache_data
def load_data():
    # main.py와 같은 폴더에 있는 CSV 파일을 불러옵니다.
    df = pd.read_csv("kobis_movies.csv")

    # 여러 장르가 |로 구분되어 있으면 첫 번째 장르만 사용
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

st.header("2. (다음 그래프를 여기에 추가)")
