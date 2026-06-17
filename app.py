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
    .main-header .binary-sub {
        color: #A3D977;
        font-size: 1.3rem;
        font-weight: bold;
        letter-spacing: 4px;
        margin-bottom: 15px;
    }
    .main-header p {
        color: #F5F5F5;
        font-size: 1.1rem;
    }
    
    .section-title {
        color: #00664F;
        font-size: 1.8rem;
        font-weight: bold;
        border-left: 5px solid #A3D977;
        padding-left: 12px;
        margin-top: 40px;
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
    
    /* 부원들이 등록한 취향 박스 디자인 */
    .taste-box {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 8px;
        border: 2px dashed #00664F;
        color: #00664F;
        margin-bottom: 15px;
        position: relative;
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

# ----------------- 🧠 메모리/세션 데이터 관리 (파이썬 기능) -----------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 취향 데이터를 딕셔너리 구조(id, 카테고리, 내용)로 관리하여 삭제 및 정렬이 가능하도록 개선
if 'tastes_list' not in st.session_state:
    st.session_state.tastes_list = [
        {"id": 0, "category": "🎵 코딩 노동요", "text": "최애 코딩 노동요 플레이리스트 공유해요!"},
        {"id": 1, "category": "💻 IT 장비/팁", "text": "역시 개발 키보드는 기계식 갈축이 최고인 듯"},
        {"id": 2, "category": "🍕 매점 꿀조합", "text": "정보실 뒤편 매점 꿀조합 빵 추천합니다"},
        {"id": 3, "category": "🎤 최애 아이돌", "text": "부실에서 코딩할 때 뉴진스 노래 들으면 능률 대박입니다"}
    ]
if 'taste_id_counter' not in st.session_state:
    st.session_state.taste_id_counter = 4

# ----------------- 💻 웹페이지 콘텐츠 구현 시작 -----------------

# [상단 헤더 배너]
st.markdown("""
<div class="main-header">
    <h1>D.U.I.T</h1>
    <div class="binary-sub">1000100 1010101 1001001 1010100</div>
    <p><b>D . U . I . T</b> | 잠실여고 전통적인 컴퓨터공학부</p>
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
        <p style="color:#666; font-size:0.95rem; line-height:1.4;">정규활동를 위해 주로 모이는 공간입니다.</p>
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

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>💡 뜻풀이</h3>
        <p>메인 배너의 이진수는 아스키코드로 <b>DUIT</b>를 의미합니다.</p>
        <p><b>"Do IT!"</b> 이라는 슬로건을 결합하여, 열정과 기술로 무엇이든 해결하는 모임입니다.</p>
    </div>
    """, unsafe_allow_html=True)


# --- 3 & 4. 게시판 섹션 (10월, 12월 삭제 및 문구 수정) ---
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
        <tr><td>05월</td><td>모의토론, 모둠탐구</td></tr>
        <tr><td>06월</td><td>축제, 개인탐구, 홈페이지 만들기</td></tr>
    </table>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with b_col3:
    st.markdown("""
    <div class="info-card">
        <h3>🚀 이전 활동 보고</h3>
        <h4 style="color:#222; margin-top:5px; margin-bottom:8px;">[활동로그] 연간 핵심 일정 기록</h4>
        <p style="color:#555; font-size:0.93rem; line-height:1.5;">
            • <b>03월</b>: 신입 부원 모집, 면접 및 오리엔테이션<br>
            • <b>05월</b>: 모의토론, 모둠탐구<br>
            • <b>06월</b>: 축제, 개인탐구, 홈페이지 만들기
        </p>
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
                if user_id and user_pw:
                    st.session_state.logged_in = True
                    st.success("🎉 인증에 성공했습니다! 스크롤을 내려 취향 공유 기능을 이용하세요.")
                    st.rerun()
                else:
                    st.error("학번과 비밀번호를 정확히 입력해주세요.")
    with auth_col2:
        st.markdown("""
        <div class="info-card" style="border-top: 4px solid #A3D977;">
            <h3>📝 계정 생성 안내</h3>
            <p>DUIT 부원은 동아리 선발 완료 후 <b>동아리 부장</b>을 통해 일괄 계정이 생성됩니다. 로그인이 되지 않는 신입 부원은 아래 버튼을 통해 등록 요청을 접수해주세요.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("신규 부원 등록 신청 발송"):
            st.toast("동아리 부장 확인 후 계정이 활성화됩니다.", icon="ℹ️")
else:
    st.success("✅ 현재 DUIT 부원 계정으로 정상 로그인되어 있습니다.")


# --- 6. 취향 공유 섹션 (파트 선택, 최애 아이돌 추가 및 삭제 기능 구현) ---
st.markdown('<div class="section-title">✨ 부원 취향 공유 룸</div>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    st.warning("🔒 이 공간은 비공개 상태입니다. 5번 메뉴에서 'DUIT 부원 인증'을 완료해야 접근할 수 있습니다.")
else:
    st.write("동아리 부원들이 파트별 관심사(노동요, 장비, 매점 메뉴, 최애 아이돌 목록 등)를 공유하고 관리하는 공간입니다.")
    
    # ➕ 취향 등록 인터페이스 (파트 선택 및 추가할 관심사 세분화)
    with st.expander("➕ 나의 취향 조각 하나 추가하기", expanded=False):
        # 1. 파트(카테고리) 선택 상자
        select_category = st.selectbox(
            "어느 파트에 넣을 건지 선택해주세요:",
            ["🎵 코딩 노동요", "💻 IT 장비/팁", "🍕 매점 꿀조합", "🎤 최애 아이돌"]
        )
        
        # 2. 추가 버튼과 연동되는 내용 입력 폼
        new_taste_input = st.text_input(
            "추가하고 싶은 구체적인 관심사를 적어주세요:", 
            placeholder="예: 최애 아이돌 멤버 이름, 매점 빵 이름, 추천 플레이리스트 등"
        )
        
        if st.button("➕ 등록하기"):
            if new_taste_input.strip():
                # 세션 데이터에 고유 ID값과 함께 딕셔너리로 저장
                st.session_state.tastes_list.append({
                    "id": st.session_state.taste_id_counter,
                    "category": select_category,
                    "text": new_taste_input.strip()
                })
                st.session_state.taste_id_counter += 1
                st.success(f"[{select_category}] 파트에 새로운 취향 카드가 실시간 추가되었습니다!")
                st.rerun()
            else:
                st.error("내용을 한 글자 이상 입력한 후 플러스 버튼을 눌러주세요.")
                
    st.write("") 
    
    # 누적된 취향 카드를 화면에 그리드 형태로 렌더링하고 각각 삭제 버튼 배치
    if len(st.session_state.tastes_list) == 0:
        st.info("현재 등록된 취향 카드가 없습니다. 첫 번째 카드를 추가해 보세요!")
    else:
        # 카드를 2열(Grid) 구조로 배치
        t_col1, t_col2 = st.columns(2)
        
        for index, taste_item in enumerate(st.session_state.tastes_list):
            # 홀짝 분기 처리로 열 분리
            target_col = t_col1 if index % 2 == 0 else t_col2
            
            with target_col:
                # 카드 외형 디자인 렌더링
                st.markdown(f"""
                <div class="taste-box">
                    <span class="taste-tag">{taste_item['category']}</span>
                    <div class="taste-text">✨ {taste_item['text']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # 삭제 기능을 위한 고유 키값 할당 버튼 배치
                if st.button(f"🗑️ 이 취향 삭제", key=f"del_{taste_item['id']}"):
                    # 해당 ID 아이템을 리스트에서 제거
                    st.session_state.tastes_list = [item for item in st.session_state.tastes_list if item['id'] != taste_item['id']]
                    st.toast("선택하신 취향 카드가 삭제되었습니다.", icon="🗑️")
                    st.rerun()

# [푸터 영역]
st.markdown("""
<div style="background-color: #00664F; color: #F5F5F5; text-align: center; padding: 20px; border-radius: 10px; margin-top: 60px; font-size: 0.9rem;">
    © 2026 DUIT. All rights reserved. | 잠실여자고등학교 2층 정보실
</div>
""", unsafe_allow_html=True)
