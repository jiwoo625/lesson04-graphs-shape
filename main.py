# ── 그래프 3. 총 관객 히스토그램 ──

st.header("3. 총 관객 분포")

fig3 = px.histogram(
df,
x="total_audi",
nbins=15,
title="영화별 총 관객 분포",
labels={"total_audi": "총 관객", "count": "영화 편수"}
)

fig3.update_traces(
hovertemplate="총 관객 구간: %{x}<br>영화 편수: %{y}편<extra></extra>"
)

st.plotly_chart(fig3, use_container_width=True)

# 가장 관객이 많은 영화 찾기

most_popular = df.loc[df["total_audi"].idxmax()]
most_popular_name = most_popular["movieNm"]
most_popular_audi = most_popular["total_audi"]

with st.container(border=True):
st.subheader("이 그래프로 알 수 있는 것")
st.write(
"대부분의 영화가 어느 관객 구간에 몰려 있는지 히스토그램에서 확인할 수 있습니다. "
f"가장 관객이 많은 영화는 **{most_popular_name}**으로, "
f"총 관객은 **{most_popular_audi:,}명**입니다."
)

st.divider()
