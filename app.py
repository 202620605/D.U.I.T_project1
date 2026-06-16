import streamlit as st

# 페이지 기본 설정 (웹 브라우저 탭에 표시될 정보)
st.set_page_config(
    page_title="DUIT - 잠실여고 동아리 소개",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- 🎨 스타일 및 색상 디자인 (CSS 통합) -----------------
# 메인색상: 이화그린(#00664F) | 글자/배경: 연회색(#F5F5F5) | 포인트: 연두(#A3D977)
local_css = """
<style>
    /* 전체 앱 배경색 및 기본 텍스트 톤 조절 */
    .stApp {
        background-color: #F5F5F5;
        color: #222222;
        font-family: 'Pretendard', -apple-system, sans-serif;
    }
    
    /* 1. 상단 대형 헤더 배너 */
    .main-header {
        background-color: #00664F;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        color: #FFFFFF;
        margin-bottom: 25px;
    }
    .main-header h1 {
        color: #A3D977 !important;
        font-size: 2.5rem !important;
        margin-bottom: 5px;
    }
    .main-header p {
        color: #F5F5F5;
        font-size: 1.1rem;
    }
    
    /* 각 메뉴의 왼쪽 세로 포인트 라인 */
    .section-title {
        color: #00664F;
        font-size: 1.8rem;
        font-weight: bold;
        border-left: 5px solid #A3D977;
        padding-left: 12px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    
    /* 구조 보정용 흰색 박스 카드 */
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
    
    /* 과잠 가상 박스 */
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
    
    /* 게시판 테이블 디자인 */
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
    
    /* 부원들이 등록한 취향 박스 디자인 */
    .taste-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        border: 2px dashed #00664F;
        text-align: center;
        font-weight: bold;
        color: #00664F;
        margin-bottom: 15px;
    }
</style>
"""
st.markdown(local_css, unsafe_allow_html=True)

# ----------------- 🧠 메모리/세션 데이터 관리 (파이썬 기능) -----------------
# 5번 기능: 로그인 상태를 브라우저 세션에 임시 보관
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 6번 기능: 등록된 취향 리스트 배열 (새로고침해도 유지되도록 세션에 저장)
if 'tastes' not in st.session_state:
    st.session_state.tastes = [
        "🎵 최애 코딩 노동요 플레이리스트 공유해요!",
        "💻 역시 개발 키보드는 기계식 갈축이 최고인 듯",
        "🍕 정보실 뒤편 매점 꿀조합 빵 추천합니다"
    ]

# ----------------- 💻 웹페이지 콘텐츠 구현 시작 -----------------

# [상단 헤더 배너]
st.markdown("""
<div class="main-header">
    <h1>1000100 1010101 1001001 1010100</h1>
    <p><b>D . U . I . T</b> | 잠실여자고등학교 최고의 IT 자율동아리</p>
</div>
""", unsafe_allow_html=True)

# [좌측 사이드바 구조 안내]
st.sidebar.title("💚 DUIT")
if st.session_state.logged_in:
    st.sidebar.success("🔒 DUIT 부원 인증 완료")
    if st.sidebar.button("로그아웃"):
        st.session_state.logged_in = False
        st.sidebar.info("로그아웃 되었습니다.")
        st.rerun()
else:
    st.sidebar.warning("🔓 비회원 상태 (6번 메뉴 잠김)")


# --- 2. DUIT 소개글 섹션 ---
st.markdown('<div class="section-title">ABOUT DUIT</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>📍 위치</h3>
        <p><b>잠실여자고등학교 2층 정보실</b></p>
        <p style="color:#666; font-size:0.9rem;">정규 활동 및 방과 후 자율 연구를 위해 주로 모이는 메인 베이스캠프입니다.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🧥 과잠 디자인</h3>
        <p><b>메인 베이스:</b> 깊이감 있는 이화그린 (#00664F)</p>
        <p><b>자수/포인트:</b> 산뜻한 연두색 (#A3D977)</p>
        <div class="jacket-box">과잠 이미지 시각화 준비 중</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>💡 뜻풀이</h3>
        <p>메인 배너의 이진수는 아스키코드로 <b>DUIT</b>를 의미합니다.</p>
        <p><b>"Do IT!"</b> 이라는 슬로건을 결합하여, 열정과 기술로 무엇이든 해결하는 잠실여고 인재들의 모임입니다.</p>
    </div>
    """, unsafe_allow_html=True)


# --- 3 & 4. 게시판 섹션 (부서 수정 완료) ---
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
    <table class="schedule-table">
        <tr><th>월별</th><th>주요 일정 및 계획</th></tr>
        <tr><td>03월</td><td>신입 부원 모집, 면접 및 오리엔테이션</td></tr>
        <tr><td>05월</td><td>부서별 상반기 프로젝트 빌드업 스터디</td></tr>
        <tr><td>10월</td><td>학교 축제 동아리 체험 부스 기획 및 운영</td></tr>
        <tr><td>12월</td><td>최종 성과 공유 아카이빙 및 피드백</td></tr>
    </table>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with b_col3:
    st.markdown("""
    <div class="info-card">
        <h3>🚀 이전 활동 보고</h3>
        <h4 style="color:#222; margin-top:5px; margin-bottom:5px;">[활동로그] 교내 웹 서비스 프로토타입 설계</h4>
        <p style="color:#555; font-size:0.95rem;">잠실여고 학생들이 교내에서 편리하게 사용할 수 있는 기능 중심의 정적 페이지를 설계하고 UI 뼈대를 테스트했습니다.</p>
    </div>
    """, unsafe_allow_html=True)


# --- 5. 로그인 / 회원가입 섹션 ---
st.markdown('<div class="section-title">DUIT 부원 인증</div>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    auth_col1, auth_col2 = st.columns([1, 1])
    with auth_col1:
        st.info("💡 6번 '취향 공유' 공간은 DUIT 정식 부원 전용 기능입니다. 아래 폼에서 로그인해 주세요.")
        with st.form("login_form"):
            user_id = st.text_input("아이디 (학번)", placeholder="예: 20501")
            user_pw = st.text_input("비밀번호", type="password")
            submitted = st.form_submit_button("부원 인증하기")
            
            if submitted:
                if user_id and user_pw: # 아이디/비번 칸이 비어있지 않으면 통과하도록 기본 구현
                    st.session_state.logged_in = True
                    st.success("🎉 인증에 성공했습니다! 스크롤을 내려 취향 공유 기능을 이용하세요.")
                    st.rerun()
                else:
                    st.error("학번과 비밀번호를 정확히 입력해주세요.")
    with auth_col2:
        st.markdown("""
        <div class="info-card" style="border-top: 4px solid #A3D977;">
            <h3>📝 계정 생성 안내</h3>
            <p>DUIT 부원은 동아리 선발 완료 후 담당 선생님을 통해 일괄 계정이 생성됩니다. 로그인이 되지 않는 신입 부원은 아래 버튼을 통해 등록 요청을 접수해주세요.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("신규 부원 등록 신청 발송"):
            st.toast("담당 선생님 확인 후 계정이 활성화됩니다.", icon="ℹ️")
else:
    st.success("✅ 현재 DUIT 부원 계정으로 정상 로그인되어 있습니다.")


# --- 6. 취향 공유 섹션 (로그인 조건부 활성화 및 플러스 버튼 구현) ---
st.markdown('<div class="section-title">✨ 부원 취향 공유 룸</div>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    # 🔐 로그인하지 않은 사용자는 진입 불가 처리 및 블러 연출 대신 경고창 표시
    st.warning("🔒 이 공간은 비공개 상태입니다. 5번 메뉴에서 'DUIT 부원 인증'을 완료해야 접근할 수 있습니다.")
else:
    st.write("동아리 부원들이 서로 좋아하는 IT 장비, 음악, 팁들을 자유롭게 공유하고 실시간으로 추가하는 공간입니다.")
    
    # ➕ 플러스 형태의 취향 등록 인터페이스 구축
    with st.expander("➕ 나의 취향 조각 하나 추가하기", expanded=False):
        new_taste_input = st.text_input("공유할 취향 문장을 적어주세요:", placeholder="예: 저는 파이썬으로 인공지능 모델 다룰 때가 제일 재밌어요!")
        
        # 버튼을 누르면 실시간으로 파이썬 데이터 리스트인 session_state.tastes에 데이터가 누적됩니다.
        if st.button("➕ 등록하기"):
            if new_taste_input.strip():
                st.session_state.tastes.append(f"✨ {new_taste_input.strip()}")
                st.success("새로운 취향 카드가 하단 리스트에 실시간 추가되었습니다!")
                st.rerun()
            else:
                st.error("내용을 한 글자 이상 입력한 후 플러스 버튼을 눌러주세요.")
                
    st.write("") # 간격 띄우기
    
    # 누적된 취향 카드를 화면에 그리드 형태로 렌더링
    t_col1, t_col2 = st.columns(2)
    for index, taste_text in enumerate(st.session_state.tastes):
        if index % 2 == 0:
            with t_col1:
                st.markdown(f'<div class="taste-card">{taste_text}</div>', unsafe_allow_html=True)
        else:
            with t_col2:
                st.markdown(f'<div class="taste-card">{taste_text}</div>', unsafe_allow_html=True)

# [푸터 영역]
st.markdown("""
<div style="background-color: #00664F; color: #F5F5F5; text-align: center; padding: 20px; border-radius: 10px; margin-top: 60px; font-size: 0.9rem;">
    © 2026 DUIT. All rights reserved. | 잠실여자고등학교 2층 정보실
</div>
""", unsafe_allow_html=True)
