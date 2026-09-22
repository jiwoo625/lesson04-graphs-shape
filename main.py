```python
# ── 그래프 2. 장르 안의 영화 (트리맵) ──
st.header("2. 장르 안의 영화")

fig2 = px.treemap(
    df,
    path=["장르", "movieNm"],
    values="total_audi",
)

# 마우스를 올리면 영화명과 총 관객이 보이게 합니다
fig2.update_traces(
    hovertemplate=(
        "<b>%{label}</b><br>"
        "총 관객: %{value:,}명"
        "<extra></extra>"
    )
)

st.plotly_chart(fig2, use_container_width=True)

with st.container(border=True):
    st.subheader("이 그래프로 알 수 있는 것")
    st.write("여기에 이 그래프를 보고 알 수 있는 내용을 한 문장으로 적어 보세요.")

st.divider()
```
