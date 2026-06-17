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
    
    .admin-box {
        background-color: #FFF3CD;
        border: 1px solid #FFEBAA;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
"""
st.markdown(local_css, unsafe_allow_html=True)

# ----------------- 🧠 데이터 세션 관리 (파이썬 로직) -----------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

# 정식 승인 부원 목록
if 'approved_members' not in st.session_state:
    st.session_state.approved_members = ["20501", "10101", "30101"]

# 가입 신청 대기 명단
if 'signup_requests' not in st.session_state:
    st.session_state.signup_requests = []

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

# ----------------- 💻 웹페이지 콘텐츠 시작 -----------------

# [상단 헤더 배너]
st.markdown("""
<div class="main-header">
    <h1>D.U.I.T</h1>
    <p>잠실여고 전통적인 컴퓨터공학부</p>
    <div class="binary-body">1000100 1010101 1001001 1010100</div>
</div>
""", unsafe_allow_html=True)

# [좌측 사이드바]
st.sidebar.title("💚 DUIT")
if st.session_state.is_admin:
    st.sidebar.success("👑 DUIT 부장 로그인 중")
    if st.sidebar.button("부장 로그아웃"):
        st.session_state.is_admin = False
        st.session_state.logged_in = False
        st.rerun()
elif st.session_state.logged_in:
    st.sidebar.success("🔒 DUIT 부원 인증 완료")
    if st.sidebar.button("부원 로그아웃"):
        st.session_state.logged_in = False
        st.rerun()
else:
    st.sidebar.warning("🔓 비회원 상태")

# --- 1. 뜻풀이 섹션 ---
st.markdown('<div class="section-title">💡 DUIT 뜻풀이</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-card" style="margin-bottom: 25px;">
    <p>메인 배너의 이진수 <b>1000100 1010101 1001001 1010100</b>는 아스키코드로 변환 시 문자열 <b>DUIT</b>를 의미합니다.</p>
    <p>이는 <b>"Do IT!"</b> 이라는 강력한 슬로건과 결합하여, 끊임없는 열정과 기술적 탐구 정신으로 무엇이든 주도적으로 해결해 나가는 컴퓨터공학부의 의지를 담고 있습니다.</p>
</div>
""", unsafe_allow_html=True)

# --- 2. ABOUT DUIT 섹션 ---
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


# --- 3 & 4. 동아리 게시판 섹션 ---
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

if not st.session_state.logged_in and not st.session_state.is_admin:
    auth_col1, auth_col2 = st.columns([1, 1])
    with auth_col1:
        st.info("💡 6번 '취향 공유' 공간은 DUIT 정식 부원 전용 기능입니다.")
        with st.form("login_form"):
            user_id = st.text_input("학번 (아이디)", placeholder="예: 20501")
            user_pw = st.text_input("비밀번호", type="password")
            submitted = st.form_submit_button("인증하기")
            
            if submitted:
                if user_id == "20401" and user_pw == "2025":
                    st.session_state.is_admin = True
                    st.session_state.logged_in = True
                    st.success("👑 부장님 환영합니다! 관리자 메뉴가 활성화되었습니다.")
                    st.rerun()
                elif user_id in st.session_state.approved_members and user_pw:
                    st.session_state.logged_in = True
                    st.success("🎉 정식 부원 인증 성공!")
                    st.rerun()
                else:
                    st.error("미승인된 학번이거나 비밀번호가 올바르지 않습니다.")
                    
    with auth_col2:
        with st.form("signup_form"):
            st.markdown("### 📝 신규 부원 가입 신청")
            req_id = st.text_input("등록할 본인의 학번을 입력하세요:", placeholder="예: 10522")
            req_submit = st.form_submit_button("신규 부원 등록 신청 발송")
            
            if req_submit:
                if req_id.strip():
                    if req_id in st.session_state.approved_members:
                        st.warning("이미 등록 완료된 학번입니다.")
                    elif req_id in st.session_state.signup_requests:
                        st.warning("이미 승인 대기 중인 신청입니다.")
                    else:
                        st.session_state.signup_requests.append(req_id.strip())
                        st.toast(f"{req_id} 학번의 등록 신청이 발송되었습니다.", icon="📩")
                else:
                    st.error("학번을 입력해주세요.")
else:
    status_msg = "👑 부장 권한으로 로그인 중입니다." if st.session_state.is_admin else "✅ 정식 부원 계정으로 로그인 중입니다."
    st.success(status_msg)


# --- 👑 부장 전용 마스터 관리자 메뉴 ---
if st.session_state.is_admin:
    st.markdown('<div class="section-title">👑 부장 전용 관리자 메뉴</div>', unsafe_allow_html=True)
    st.markdown('<div class="admin-box">', unsafe_allow_html=True)
    st.subheader("📩 신규 회원 가입 요청 관리")
    
    if not st.session_state.signup_requests:
        st.write("현재 대기 중인 신규 가입 신청이 없습니다.")
    else:
        for req_member in st.session_state.signup_requests:
            r_col1, r_col2, r_col3 = st.columns([2, 1, 1])
            with r_col1:
                st.write(f"학번 **{req_member}** 학생이 가입을 요청했습니다.")
            with r_col2:
                if st.button(f"✅ 승인", key=f"app_{req_member}"):
                    st.session_state.approved_members.append(req_member)
                    st.session_state.signup_requests.remove(req_member)
                    st.toast(f"{req_member} 학번이 정식 부원으로 등록되었습니다!")
                    st.rerun()
            with r_col3:
                if st.button(f"❌ 거절", key=f"rej_{req_member}"):
                    st.session_state.signup_requests.remove(req_member)
                    st.toast("요청을 거절했습니다.")
                    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# --- 6. 취향 공유 섹션 ---
st.markdown('<div class="section-title">✨ 부원 취향 공유 룸</div>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    st.warning("🔒 이 공간은 비공개 상태입니다. 5번 메뉴에서 'DUIT 부원 인증'을 완료해야 접근할 수 있습니다.")
else:
    st.write("동아리 부원들이 파트별 관심사를 공유하고 관리하는 공간입니다.")
    
    # ➕ 취향 등록 인터페이스
    with st.expander("➕ 나의 취향 조각 하나 추가하기", expanded=False):
        select_category = st.selectbox(
            "어느 파트에 넣을 건지 선택해주세요:",
            ["🎵 코딩 노동요", "💻 IT 장비/팁", "🍕 매점 꿀조합", "🎤 최애 아이돌"]
        )
        new_taste_input = st.text_input(
            "추가하고 싶은 구체적인 관심사를 적어주세요:", 
            placeholder="추천 내용을 입력해 주세요"
        )
        
        if st.button("➕ 등록하기"):
            if new_taste_input.strip():
                st.session_state.tastes_list.append({
                    "id": st.session_state.taste_id_counter,
                    "category": select_category,
                    "text": new_taste_input.strip()
                })
                st.session_state.taste_id_counter += 1
                st.success("취향 카드가 추가되었습니다!")
                st.rerun()
            else:
                st.error("내용을 한 글자 이상 입력해주세요.")
                
    st.write("") 
    
    # 카드 렌더링 화면
    if len(st.session_state.tastes_list) == 0:
        st.info("현재 등록된 취향 카드가 없습니다.")
    else:
        t_col1, t_col2 = st.columns(2)
        
        for index, taste_item in enumerate(st.session_state.tastes_list):
            target_col = t_col1 if index % 2 == 0 else t_col2
            
            with target_col:
                st.markdown(f"""
                <div class="taste-box">
                    <span class="taste-tag">{taste_item['category']}</span>
                    <div class="taste-text">✨ {taste_item['text']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # --- 부장 전용 수정/삭제 기능 ---
                if st.session_state.is_admin:
                    edit_col, del_col = st.columns([3, 1])
                    with edit_col:
                        edited_text = st.text_input(
                            f"✏️ 내용 수정 (ID: {taste_item['id']})", 
                            value=taste_item['text'], 
                            key=f"edit_val_{taste_item['id']}"
                        )
                        if edited_text != taste_item['text'] and edited_text.strip():
                            taste_item['text'] = edited_text.strip()
                            st.toast("내용이 수정되었습니다.")
                    with del_col:
                        st.write("<div style='height:28px;'></div>", unsafe_allow_html=True)
                        if st.button("🗑️ 삭제", key=f"admin_del_{taste_item['id']}"):
                            st.session_state.tastes_list = [item for item in st.session_state.tastes_list if item['id'] != taste_item['id']]
                            st.rerun()
                
                # --- 일반 회원 전용 삭제 기능 ---
                else:
                    if st.button(f"🗑️ 이 취향 삭제", key=f"del_{taste_item['id']}"):
                        st.session_state.tastes_list = [item for item in st.session_state.tastes_list if item['id'] != taste_item['id']]
                        st.rerun()

# [푸터 영역]
st.markdown("""
<div style="background-color: #00664F; color: #F5F5F5; text-align: center; padding: 20px; border-radius: 10px; margin-top: 60px; font-size: 0.9rem;">
    © 2026 DUIT. All rights reserved. | 잠실여자고등학교 2층 정보실
</div>
""", unsafe_allow_html=True)

