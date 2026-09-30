
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    layout="wide",
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"


@st.cache_data
def load_data():
    # 1년간 박스오피스 10위권에 든 영화 216편의 요약표를 불러옵니다.
    df = pd.read_csv(DATA_URL)

    # 장르가 여러 개 적힌 영화는 첫 번째 장르만 사용합니다.
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


# ─────────────────────────────────────
# 그래프 1. 장르별 영화 편수 도넛
# ─────────────────────────────────────

st.header("1. 장르별 영화 편수")

genre_count = (
    df["장르"]
    .value_counts()
    .reset_index()
)

genre_count.columns = ["장르", "편수"]

fig = px.pie(
    genre_count,
    names="장르",
    values="편수",
    hole=0.45,
)

# 마우스를 올리면 편수와 비율 표시
fig.update_traces(
    hovertemplate="%{label}<br>%{value}편 (%{percent})<extra></extra>"
)

fig.update_layout(
    margin=dict(t=20, b=20, l=20, r=20),
)

st.plotly_chart(fig, width="stretch")


# 그래프 설명 영역
st.markdown("#### 이 그래프로 알 수 있는 것")

st.text_input(
    "한 문장으로 작성해 보세요.",
    key="note1",
    placeholder="예: 이 기간에는 ○○ 장르의 영화가 가장 많았다.",
)


# ─────────────────────────────────────
# 다음 그래프 영역
# ─────────────────────────────────────

st.divider()

st.header("2. 다음 그래프")
st.info("다음 그래프를 여기에 추가할 수 있습니다.")

