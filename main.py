# ── 그래프 6. 개봉일 스크린수와 총 관객의 관계 (버블) ──
st.header("6. 개봉일 스크린수와 총 관객의 관계 (버블)")

fig6 = px.scatter(
    df,
    x="first_scrn",
    y="total_audi",
    size="first_week_audi",
    color="장르",
    hover_name="movieNm",
    labels={
        "first_scrn": "개봉일 스크린수",
        "total_audi": "총 관객",
        "first_week_audi": "첫 주 관객",
        "장르": "장르"
    },
    size_max=50
)

fig6.update_traces(
    hovertemplate=(
        "<b>%{hovertext}</b><br>"
        "개봉일 스크린수: %{x:,}개<br>"
        "총 관객: %{y:,}명<br>"
        "첫 주 관객: %{customdata[0]:,}명"
        "<extra></extra>"
    )
)

st.plotly_chart(fig6, width="stretch")

st.text_input("이 그래프로 알 수 있는 것", key="note6")
