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


# ── 그래프 3. 총 관객 분포 ──
st.header("3. 총 관객 분포")

fig3 = px.histogram(
    df,
    x="total_audi",
    nbins=15,
    labels={
        "total_audi": "총 관객",
        "count": "영화 편수"
    }
)

fig3.update_traces(
    hovertemplate="총 관객 구간: %{x}<br>영화 편수: %{y}편<extra></extra>"
)

st.plotly_chart(fig3, width="stretch")

most_popular = df.loc[df["total_audi"].idxmax()]

st.write(
    f"**이 그래프로 알 수 있는 것:** "
    f"대부분의 영화가 어느 총 관객 구간에 몰려 있는지 확인할 수 있습니다. "
    f"가장 관객이 많은 영화는 **{most_popular['movieNm']}**이며, "
    f"총 관객은 **{most_popular['total_audi']:,}명**입니다."
)


# ── 그래프 4. 개봉일 스크린수와 총 관객의 관계 ──
st.header("4. 개봉일 스크린수와 총 관객의 관계")

fig4 = px.scatter(
    df,
    x="first_scrn",
    y="total_audi",
    color="장르",
    hover_name="movieNm",
    labels={
        "first_scrn": "개봉일 스크린수",
        "total_audi": "총 관객",
        "장르": "장르"
    }
)

fig4.update_traces(
    hovertemplate=(
        "<b>%{hovertext}</b><br>"
        "개봉일 스크린수: %{x:,}개<br>"
        "총 관객: %{y:,}명"
        "<extra></extra>"
    )
)

st.plotly_chart(fig4, width="stretch")

st.text_input("이 그래프로 알 수 있는 것", key="note4")
