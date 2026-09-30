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
st.caption("1년간 박스오피스 10위권에 든 영화 가운데 해당 기간에 개봉한 216편의 데이터를 살펴봅니다.")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 장르가 '|'로 여러 개 적힌 경우 첫 번째 장르만 사용
    df["genre_first"] = (
        df["genre"]
        .fillna("미상")
        .astype(str)
        .str.split("|")
        .str[0]
        .str.strip()
    )
    df.loc[df["genre_first"].eq(""), "genre_first"] = "미상"

    return df

try:
    df = load_data()
except Exception as e:
    st.error("데이터를 불러오지 못했습니다.")
    st.exception(e)
    st.stop()

st.subheader("1. 장르별 영화 편수")

genre_counts = (
    df["genre_first"]
    .value_counts()
    .rename_axis("장르")
    .reset_index(name="편수")
)

genre_counts["비율"] = genre_counts["편수"] / genre_counts["편수"].sum() * 100

fig = px.pie(
    genre_counts,
    names="장르",
    values="편수",
    hole=0.5,
    custom_data=["편수", "비율"],
)

fig.update_traces(
    hovertemplate="<b>%{label}</b><br>편수: %{customdata[0]}편<br>비율: %{customdata[1]:.1f}%<extra></extra>"
)

fig.update_layout(
    margin=dict(t=30, b=20, l=20, r=20),
    legend_title_text="장르",
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("### 이 그래프로 알 수 있는 것")
st.info("장르별로 1년간 박스오피스 10위권에 든 영화가 몇 편씩 분포했는지 한눈에 비교할 수 있습니다.")

st.caption(f"데이터 행 수: {len(df):,}편")
