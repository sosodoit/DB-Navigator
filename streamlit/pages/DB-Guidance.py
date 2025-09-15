import streamlit as st

# 페이지 설정
st.set_page_config(layout="centered")

# --- session_state 초기화 ---
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.choices = {}

# --- 1단계: 핵심 목표 ---
if st.session_state.step == 1:
    st.header("🎯 기준 1: 프로젝트 핵심 목표")
    st.subheader("당신의 프로젝트가 해결하려는 가장 중요한 문제는 무엇인가요?")

    # SQL 버튼
    if st.button("안정적인 데이터 관리 및 거래 처리", type="primary", use_container_width=True):
        st.session_state.choices['goal'] = 'SQL'
        st.session_state.step = 2
        st.rerun() # 다음 단계로 이동


# --- 2단계: 데이터 모델  ---
elif st.session_state.step == 2:
    st.header("💾 기준 2: 데이터 모델")
    st.subheader("주로 다루게 될 데이터는 어떤 형태에 가장 가깝나요?")
    st.info("SQL은 정형 데이터를 다루는 데 최적화되어 있습니다.")
    
    if st.button("정형 데이터 (엑셀 표)", use_container_width=True):
        st.session_state.choices['model'] = '정형 데이터' # sql은 정형데이터만
        st.session_state.step = 3
        st.rerun()

# --- 3단계: 최우선 가치 ---
elif st.session_state.step == 3:
    st.header("🥇 기준 3: 최우선 가치")
    st.subheader("여러 가치 중, 절대로 포기할 수 없는 3가지는 무엇인가요?")

    choices = st.multiselect(
        "중요시 여기는 3가지를 선택해주세요.",
        ["데이터 무결성 및 안정성", "수평 확장성", "응답 속도", "검색 정확도", "개발 편의성 및 커뮤니티"],
        max_selections = 3
    )
    
    if st.button("다음 단계로 가기", type="primary"):
        st.session_state.choices['priority'] = choices
        st.session_state.step = 4
        st.rerun()
    
    
        
# --- 4단계: 운영 환경 및 비용 (SQL 경로) ---
elif st.session_state.step == 4:
    st.header("🛠️ 기준 4: 운영 환경 및 비용")
    st.subheader("선호하는 운영 방식과 비용 모델은 무엇인가요?")

    choices = st.multiselect(
        "해당하는 것을 모두 선택해주세요.",
        ["클라우드 관리형 서비스 선호", "서버에 직접 설치 선호", "오픈소스 선호"]
    )
    
    if st.button("결과 보기", type="primary"):
        st.session_state.choices['operation'] = choices
        st.session_state.step = 5
        st.rerun()

# --- 5단계: 결과 표시 ---
elif st.session_state.step == 5:
    st.header("✨ 당신의 프로젝트를 위한 DB 추천")

    with st.expander("내가 선택한 내용 보기"):
        st.write(st.session_state.choices)

    # --- 추천 로직 (함수 대신 if문으로 직접 작성) ---
    dbms = "미정"
    reason = "추천 내용을 생성하지 못했습니다."
    
    priority = st.session_state.choices.get('priority')
    operation = st.session_state.choices.get('operation')

    if '데이터 무결성 및 안정성' in priority:
        if "클라우드 관리형 서비스 선호" in operation and "오픈소스 선호" in operation:
            dbms = "PostgreSQL"
            reason = "데이터의 무결성과 정합성을 최우선으로 하는 프로젝트에 가장 적합한 오픈소스 RDBMS입니다."
        elif "서버에 직접 설치 선호" in operation and "오픈소스 선호" in operation:
            dbms = "PostgreSQL"
            reason = "데이터의 무결성과 정합성을 최우선으로 하는 프로젝트에 가장 적합한 오픈소스 RDBMS입니다."
    elif '개발 편의성 및 커뮤니티' in priority:
        if "클라우드 관리형 서비스 선호" in operation and "오픈소스 선호" in operation:
            dbms = "MySQL / MariaDB"
            reason = "가장 대중적이고 자료가 많아, 빠른 개발과 안정적인 운영이 중요한 웹 프로젝트에 적합합니다."
        elif "서버에 직접 설치 선호" in operation and "오픈소스 선호" in operation:
            dbms = "MySQL / MariaDB"
            reason = "가장 대중적이고 자료가 많아, 빠른 개발과 안정적인 운영이 중요한 웹 프로젝트에 적합합니다."
        
        
    
    st.success(f"### 🥇 추천 DBMS: {dbms}")
    st.info(reason)

    if st.button("다시 시작하기"):
        # st.session_state 초기화
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

# --- 99단계: 준비 중 페이지 ---
elif st.session_state.step == 99:
    st.warning("### 🚧 준비 중인 기능입니다.")
    st.info(f"선택하신 **{st.session_state.choices.get('goal')}** DB 추천 기능은 현재 개발 중입니다.")
    
    if st.button("뒤로 가기"):
        # st.session_state 초기화
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()