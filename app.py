import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="DUIT - 잠실여고 동아리 소개",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- 🎨 스타일 및 색상 디자인 (CSS 통합) -----------------
local_css = """
<style>
    .stApp {
        background-color: #F5F5F5;
        color: #222222;
        font-family: 'Pretendard', -apple-system, sans-serif;
    }
    
    .main-header {
        background-color: #00664F;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        color: #FFFFFF;
        margin-bottom: 25px;
    }
    .main-header h1 {
        color: #FFFFFF !important;
        font-size: 3rem !important;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }
    .main-header p {
        color: #A3D977;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .main-header .binary-body {
        color: #F5F5F5;
        font-size: 1.05rem;
        letter-spacing: 3px;
    }
    
    .section-title {
        color: #00664F;
        font-size: 1.8rem;
        font-weight: bold;
        border-left: 5px solid #A3D977;
        padding-left: 12px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    
    .info-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 100%;
        border-top: 4px solid #00664F;
    }
    .info-card h3 {
        color: #00664F;
        margin-bottom: 12px;
    }
    
    .mini-meaning-box {
        background-color: #E8F5E9;
        border-left: 4px solid #00664F;
        padding: 15px;
        border-radius: 6px;
        margin-bottom: 25px;
        font-size: 0.93rem;
        color: #333333;
        line-height: 1.5;
    }
    
    .jacket-box {
        background-color: #00664F;
        color: #A3D977;
        height: 120px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        font-weight: bold;
        margin-top: 10px;
    }
    
    .schedule-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }
    .schedule-table th {
        background-color: #00664F;
        color: white;
        padding: 10px;
        text-align: left;
    }
    .schedule-table td {
        padding: 10px;
        border-bottom: 1px solid #E0E0E0;
        color: #333333;
    }
    
    .taste-box {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 8px;
        border: 2px dashed #00664F;
        color: #00664F;
        margin-bottom: 10px;
    }
    .taste-tag {
        display: inline-block;
        background-color: #00664F;
        color: white;
        font-size: 0.75rem;
        padding: 2px 8px;
        border-radius: 4px;
        margin-bottom: 8px;
        font-weight: bold;
    }
    .taste-text {
        font-weight: bold;
        font-size: 0.95rem;
        word-break: break-all;
    }
</style>
"""
st.markdown(local_css, unsafe_allow_html=True)

# ----------------- 🧠 데이터 세션 관리 (파이썬 로직) -----------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = ""
if 'boss_verified' not in st.session_state:
    st.session_state.boss_verified = False

# 정식 승인 부원 목록 (학번: 비밀번호)
if 'approved_users' not in st.session_state:
    st.session_state.approved_users = {
        "20501": "1234",
        "10101": "1234",
        "30101": "1234"
    }

# 메인 홈 '이전 활동 보고' 데이터 리스트
if 'boss_log_list' not in st.session_state:
    st.session_state.boss_log_list = [
        "03월: 신입 부원 모집, 면접 및 오리엔테이션",
        "05월: 모의토론, 모둠탐구",
        "06월: 축제, 개인탐구, 홈페이지 만들기"
    ]

# 가입 신청 대기 명단
if 'signup_queue' not in st.session_state:
    st.session_state.signup_queue = []

# 취향 공유 초기 데이터 리스트
if 'tastes_list' not in st.session_state:
    st.session_state.tastes_list = [
        {"id": 0, "category": "🎵 코딩 노동요", "text": "최애 코딩 노동요 플레이리스트 공유해요!"},
        {"id": 1, "category": "💻 IT 장비/팁", "text": "역시 개발 키보드는 기계식 갈축이 최고인 듯"},
        {"id": 2, "category": "🍕 매점 꿀조합", "text": "정보실 뒤편 매점 꿀조합 빵 추천합니다"},
        {"id": 3, "category": "🎤 최애 아이돌", "text": "부실에서 코딩할 때 뉴진스 노래 들으면 능률 대박입니다"}
    ]
if 'taste_id_counter' not in st.session_state:
    st.session_state.taste_id_counter = 4

# ----------------- 💻 사이드바 목차 제어 시스템 -----------------
st.sidebar.title("💚 DUIT 메뉴")

# 기본 목차 구성
menu_options = ["🏠 메인 홈"]

# 🔥 부장 인증 상태일 때만 목차(메뉴) 리스트에 추가됨!
if st.session_state.boss_verified:
    menu_options.append("👑 부장 전용 관리관")

selected_menu = st.sidebar.radio("이동할 페이지를 선택하세요:", menu_options)

st.sidebar.markdown("---")

# 사이드바 하단 부원 인증 및 부장 시크릿 로그인 게이트
if st.session_state.boss_verified:
    st.sidebar.success("👑 부장 마스터 모드 활성화 중")
    if st.sidebar.button("부장 모드 종료"):
        st.session_state.boss_verified = False
        st.rerun()
else:
    # 🔒 부장님은 여기서 비밀번호를 치면 목차(메뉴)에 새 페이지가 열립니다!
    st.sidebar.markdown("### 🔑 부장 인증 게이트")
    boss_pwd_input = st.sidebar.text_input("마스터 패스워드 입력:", type="password", placeholder="비밀번호 입력 시 목차 오픈")
    if boss_pwd_input == "2025":
        st.session_state.boss_verified = True
        st.sidebar.success("부장 인증 완료! 상단 목차를 확인하세요.")
        st.rerun()

st.sidebar.markdown("---")
if st.session_state.logged_in:
    st.sidebar.success(f"🔒 {st.session_state.current_user} 로그인 완료")
    if st.sidebar.button("부원 로그아웃"):
        st.session_state.logged_in = False
        st.session_state.current_user = ""
        st.rerun()
else:
    st.sidebar.warning("🔓 부원 비로그인 상태")


# ==============================================================================
# 🏠 1. [페이지 1] 메인 홈 화면 (기존 레이아웃 완벽 보존)
# ==============================================================================
if selected_menu == "🏠 메인 홈":

    # [상단 헤더 배너]
    st.markdown("""
    <div class="main-header">
        <h1>D.U.I.T</h1>
        <p>잠실여고 전통적인 컴퓨터공학부</p>
        <div class="binary-body">1000100 1010101 1001001 1010100</div>
    </div>
    """, unsafe_allow_html=True)

    # --- 💡 듀잇 뜻풀이 ---
    st.markdown("""
    <div class="mini-meaning-box">
        <b>💡 DUIT 의미 안내:</b> 상단 배너의 이진수 1000100 1010101 1001001 1010100는 아스키코드로 변환 시 문자열 <b>DUIT</b>를 뜻합니다. 이는 슬로건 <b>"Do IT!"</b>과 결합하여 주도적으로 문제를 해결하는 컴퓨터공학부의 정체성을 나타냅니다.
    </div>
    """, unsafe_allow_html=True)

    # --- ABOUT DUIT 섹션 ---
    st.markdown('<div class="section-title">ABOUT DUIT</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>📍 위치</h3>
            <p><b>잠실여자고등학교 2층 정보실</b></p>
            <p style="color:#666; font-size:0.95rem; line-height:1.4;">정규활동 및 동아리 부원들의 프로젝트 연구를 위해 주로 모이는 공간입니다.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🧥 과잠 디자인</h3>
            <p><b>메인 베이스:</b> 깊이감 있는 이화그린</p>
            <p><b>자수/포인트:</b> 산뜻한 연두색</p>
            <div class="jacket-box">과잠 이미지 시각화 준비 중</div>
        </div>
        """, unsafe_allow_html=True)

    # --- 동아리 게시판 섹션 (부서 / 일정 / 이전 활동 보고 내용 유지) ---
    st.markdown('<div class="section-title">동아리 게시판</div>', unsafe_allow_html=True)
    b_col1, b_col2, b_col3 = st.columns(3)

    with b_col1:
        st.markdown("""
        <div class="info-card">
            <h3>👥 부서 소개 (총 인원: 21명)</h3>
            <p style="font-size:0.95rem; color:#444; margin-bottom:8px;">2026학년도 기준 정예 인원으로 운영됩니다.</p>
            <ul>
                <li>💻 <b>프로그래밍부</b>: 웹/앱 서비스 빌드 및 알고리즘 개발</li>
                <li>🛡️ <b>보안부</b>: 웹 해킹 기초 아키텍처 및 시스템 보안 스터디</li>
                <li>🤖 <b>AI부</b>: 인공지능 API 응용 및 빅데이터 수집/분석</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with b_col2:
        st.markdown('<div class="info-card"><h3>📅 동아리 연간 일정</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="schedule-

