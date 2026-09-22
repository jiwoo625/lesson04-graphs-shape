from pathlib import Path

main_py = r'''import streamlit as st
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
    "1년간 박스오피스 10위권에 든 영화 가운데 해당 기간에 개봉한 216편의 데이터를 살펴봅니다."
)


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 여러 장르가 세로막대(|)로 구분되어 있으면 첫 번째 장르만 사용
    df["genre"] = (
        df["genre"]
        .fillna("미상")
        .astype(str)
        .str.split("|")
        .str[0]
        .str.strip()
    )

    # 숫자형 열 변환
    numeric_cols = [
        "first_scrn",
        "first_show",
        "first_week_audi",
        "total_audi",
        "days_in_top10",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


try:
    df = load_data()
except Exception as e:
    st.error("데이터를 불러오지 못했습니다. 인터넷 연결과 데이터 주소를 확인해 주세요.")
    st.exception(e)
    st.stop()


# =========================================================
# 그래프 1. 장르별 영화 편수
# =========================================================
st.subheader("① 장르별 영화 편수")

genre_counts = (
    df["genre"]
    .value_counts()
    .rename_axis("genre")
    .reset_index(name="count")
)

fig1 = px.pie(
    genre_counts,
    names="genre",
    values="count",
    hole=0.48,
    title="장르별 영화 편수",
)

fig1.update_traces(
    textinfo="percent",
    hovertemplate=(
        "<b>%{label}</b><br>"
        "편수: %{value}편<br>"
        "비율: %{percent}<extra></extra>"
    ),
)

fig1.update_layout(
    legend_title_text="장르",
    margin=dict(t=60, l=20, r=20, b=20),
)

st.plotly_chart(fig1, use_container_width=True)

with st.container(border=True):
    st.markdown("**이 그래프로 알 수 있는 것**")
    st.write("여기에 이 그래프에서 발견한 특징을 한 문장으로 적어 보세요.")


st.divider()


# =========================================================
# 그래프 2. 장르 안에 영화가 들어 있는 트리맵
# =========================================================
st.subheader("② 장르별 영화 총 관객 트리맵")

treemap_df = df[["genre", "movieNm", "total_audi"]].copy()

treemap_df["movieNm"] = (
    treemap_df["movieNm"]
    .fillna("영화명 미상")
    .astype(str)
)

treemap_df["total_audi"] = (
    pd.to_numeric(treemap_df["total_audi"], errors="coerce")
    .fillna(0)
)

# total_audi가 0인 행도 표시할 수 있도록 최소값을 주지 않고 그대로 사용
fig2 = px.treemap(
    treemap_df,
    path=["genre", "movieNm"],
    values="total_audi",
    title="장르 안의 영화별 총 관객",
)

# 영화 칸에 마우스를 올리면 영화명과 총 관객을 표시
fig2.update_traces(
    hovertemplate=(
        "<b>영화명: %{label}</b><br>"
        "총 관객: %{value:,.0f}명<extra></extra>"
    ),
    root_color="lightgrey",
)

fig2.update_layout(
    margin=dict(t=60, l=10, r=10, b=10),
)

st.plotly_chart(fig2, use_container_width=True)

with st.container(border=True):
    st.markdown("**이 그래프로 알 수 있는 것**")
    st.write("여기에 이 그래프에서 발견한 특징을 한 문장으로 적어 보세요.")


st.divider()

st.caption(f"전체 영화 수: {len(df)}편")
'''

requirements_txt = """streamlit
pandas
plotly
"""

Path("/mnt/data/main.py").write_text(main_py, encoding="utf-8")
Path("/mnt/data/requirements.txt").write_text(requirements_txt, encoding="utf-8")

print("main.py와 requirements.txt를 수정했습니다.")
