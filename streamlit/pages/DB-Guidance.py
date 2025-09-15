import streamlit as st

st.header("당신의 프로젝트가 해결하려는 가장 중요한 문제는 무엇인가요?")

left, middle, right = st.columns(3)

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)

if left.button("sql 안정적인 데이터 관리 및 거래 처리", width="stretch"):
    left.markdown("안정적인 데이터 관리 및 거래 처리")  

    if left.button("정형 데이터", width="stretch"):
        left.markdown("?")  

if middle.button("nosql 빠른 속도와 대규모 트래픽 처리", icon="😃", width="stretch"):
    middle.markdown("빠른 속도와 대규모 트래픽 처리")

    if middle.button("문서 데이터", width="stretch"):
        middle.markdown("?")
    if middle.button("키값 데이터", width="stretch"):
        middle.markdown("?")       

if right.button("vector AI 기반의 의미 검색 및 추천", icon=":material/mood:", width="stretch"):
    right.markdown("AI 기반의 의미 검색 및 추천")

    if right.button("벡터 데이터", width="stretch"):
        right.markdown("?")