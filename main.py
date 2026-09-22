from pathlib import Path

path = Path("/mnt/data/main.py")
text = path.read_text(encoding="utf-8")

insert = r'''
# -------------------------
# 그래프 2: 장르별 영화 트리맵
# -------------------------
st.subheader("② 장르별 영화 트리맵")

treemap_df = df[["genre", "movieNm", "total_audi"]].copy()
treemap_df["movieNm"] = treemap_df["movieNm"].fillna("영화명 미상")
treemap_df["total_audi"] = pd.to_numeric(treemap_df["total_audi"], errors="coerce").fillna(0)

fig2 = px.treemap(
    treemap_df,
    path=["genre", "movieNm"],
    values="total_audi",
    title="장르 안의 영화별 총 관객",
)

fig2.update_traces(
    hovertemplate="<b>%{label}</b><br>총 관객: %{value:,.0f}명<extra></extra>",
)

fig2.update_layout(
    margin=dict(t=60, l=10, r=10, b=10),
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown(
    """
    <div style="
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 14px 18px;
        margin-top: 4px;
        background-color: #fafafa;
    ">
        <b>이 그래프로 알 수 있는 것</b><br>
        <span style="color:#666;">여기에 이 그래프에서 발견한 특징을 한 문장으로 적어 보세요.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()
'''

# 기존 마지막 st.caption 앞에 그래프 2 삽입
marker = 'st.caption(f"전체 영화 수: {len(df)}편")'
if marker in text and '그래프 2: 장르별 영화 트리맵' not in text:
    text = text.replace(marker, insert + '\n' + marker)

path.write_text(text, encoding="utf-8")
print(f"Updated: {path}")
