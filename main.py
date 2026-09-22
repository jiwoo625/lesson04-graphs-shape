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
