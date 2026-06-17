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
    
    /* 작게 수정한 뜻풀이 전용 박스 */
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
    
    .admin-box {
        background-color: #FFF3CD;
        border: 1px solid #FFEBAA;
        padding: 25px;
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
if 'current_user' not in st.session_state:
    st.session_state.current_user = ""

# 정식 승인 부원 목록 (학번: 비밀번호)
if 'approved_users' not in st.session_state:
    st.session_state.approved_users = {
        "20501": "1234",
        "10101": "1234",
        "30101": "1234"
    }

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

# ----------------- 💻 사이드바 메뉴 및 권한 분리 -----------------
st.sidebar.title("💚 DUIT 메뉴")

menu_options = ["🏠 메인 홈"]

# 부장 로그인 시에만 사이드바 전용 메뉴 노출
if st.session_state.is_admin:
    menu_options.append("👑 부장 전용 관리관")

selected_menu = st.sidebar.radio("이동할 페이지를 선택하세요:", menu_options)

st.sidebar.markdown("---")
if st.session_state.is_admin:
    st.sidebar.success(f"👑 부장님 ({st.session_state.current_user}) 로그인 중")
    if st.sidebar.button("부장 로그아웃"):
        st.session_state.is_admin = False
        st.session_state.logged_in = False
        st.session_state.current_user = ""
        st.rerun()
elif st.session_state.logged_in:
    st.sidebar.success(f"🔒 부원 ({st.session_state.current_user}) 인증 완료")
    if st.sidebar.button("부원 로그아웃"):
        st.session_state.logged_in = False
        st.session_state.current_user = ""
        st.rerun()
else:
    st.sidebar.warning("🔓 비회원 상태")


# ==============================================================================
# 🏠 1. 메인 홈 페이지 화면
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


    # --- 동아리 게시판 섹션 (복구 완료 및 [활동로그] 글자 제거 완료) ---
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
            <h4 style="color:#222; margin-top:5px; margin-bottom:8px;">연간 핵심 일정 기록</h4>
            <p style="color:#555; font-size:0.93rem; line-height:1.5;">
                • <b>03월</b>: 신입 부원 모집, 면접 및 오리엔테이션<br>
                • <b>05월</b>: 모의토론, 모둠탐구<br>
                • <b>06월</b>: 축제, 개인탐구, 홈페이지 만들기
            </p>
        </div>
        """, unsafe_allow_html=True)


    # --- 로그인 / 회원가입 섹션 ---
    st.markdown('<div class="section-title">DUIT 부원 인증</div>', unsafe_allow_html=True)

    if not st.session_state.logged_in:
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
                        st.session_state.current_user = "부장"
                        st.success("👑 부장님 환영합니다! 왼쪽 메뉴에서 관리자 페이지를 이용하실 수 있습니다.")
                        st.rerun()
                    elif user_id in st.session_state.approved_users and st.session_state.approved_users[user_id] == user_pw:
                        st.session_state.logged_in = True
                        st.session_state.current_user = user_id
                        st.success(f"🎉 {user_id} 부원님 인증 성공!")
                        st.rerun()
                    else:
                        st.error("등록되지 않은 학번이거나 비밀번호가 올바르지 않습니다.")
                        
        with auth_col2:
            with st.form("signup_form"):
                st.markdown("### 📝 신규 부원 가입 신청")
                req_id = st.text_input("가입할 본인의 학번을 입력하세요:", placeholder="예: 10522")
                req_pw = st.text_input("사용할 비밀번호를 입력하세요:", type="password", placeholder="최소 4자리 이상")
                req_submit = st.form_submit_button("신규 부원 등록 신청 발송")
                
                if req_submit:
                    if req_id.strip() and req_pw.strip():
                        if req_id in st.session_state.approved_users or req_id == "20401":
                            st.warning("이미 등록 완료된 학번입니다.")
                        elif any(item['id'] == req_id.strip() for item in st.session_state.signup_queue):
                            st.warning("이미 부장님의 승인을 대기 중인 신청입니다.")
                        else:
                            st.session_state.signup_queue.append({
                                "id": req_id.strip(),
                                "pw": req_pw.strip()
                            })
                            st.toast(f"{req_id} 학번의 등록 신청이 발송되었습니다.", icon="📩")
                    else:
                        st.error("학번과 비밀번호를 모두 기입한 후 신청해주세요.")
else:
    status_msg = "👑 부장 권한으로 로그인 중입니다. 사이드바 메뉴에서 관리관으로 진입할 수 있습니다." if st.session_state.is_admin else f"✅ {st.session_state.current_user} 정식 부원 계정으로 로그인 중입니다."
    st.success(status_msg)


    # --- 취향 공유 섹션 ---
    st.markdown('<div class="section-title">✨ 부원 취향 공유 룸</div>', unsafe_allow_html=True)

    if not st.session_state.logged_in:
        st.warning("🔒 이 공간은 비공개 상태입니다. 위 메뉴에서 'DUIT 부원 인증'을 완료해야 접근할 수 있습니다.")
    else:
        st.write("동아리 부원들이 파트별 관심사를 공유하고 관리하는 공간입니다.")
        
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
                    st.error("내용을 입력해주세요.")
                    
        st.write("") 
        
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
                    
                    if st.button(f"🗑️ 이 취향 삭제", key=f"del_{taste_item['id']}"):
                        st.session_state.tastes_list = [item for item in st.session_state.tastes_list if item['id'] != taste_item['id']]
                        st.rerun()


# ==============================================================================
# 👑 2. 부장 전용 비밀 관리 페이지 화면
# ==============================================================================
elif selected_menu == "👑 부장 전용 관리관":
    
    st.title("👑 DUIT 부장 마스터 대시보드")
    st.write("부장전용 독립 메뉴입니다. 이곳에서 신규 가입 제어 및 취향 편집 마스터 권한을 행사할 수 있습니다.")
    st.markdown("---")
    
    # [파트 1: 신규 가입 회원 신청 목록]
    st.subheader("📩 신규 회원 가입 및 비밀번호 승인 관리")
    
    if not st.session_state.signup_queue:
        st.info("현재 대기 중인 신규 가입 신청자가 없습니다.")
    else:
        for req_user in st.session_state.signup_queue:
            with st.container():
                r_col1, r_col2, r_col3 = st.columns([2, 1, 1])
                with r_col1:
                    st.warning(f"👤 신청 학번: **{req_user['id']}** | 설정 비밀번호: ` {req_user['pw']} `")
                with r_col2:
                    if st.button(f"✅ 회원 등록 승인", key=f"admin_app_{req_user['id']}"):
                        st.session_state.approved_users[req_user['id']] = req_user['pw']
                        st.session_state.signup_queue.remove(req_user)
                        st.toast(f"{req_user['id']} 학생이 정식 데이터베이스에 부원으로 합류했습니다.")
                        st.rerun()
                with r_col3:
                    if st.button(f"❌ 신청 즉시 삭제", key=f"admin_rej_{req_user['id']}"):
                        st.session_state.signup_queue.remove(req_user)
                        st.toast("가입 요청서가 폐기되었습니다.")
                        st.rerun()
                        
    st.markdown("---")
    
    # [파트 2: 모든 부원들의 취향 총괄 수정/삭제]
    st.subheader("🛠️ 전체 부원 취향 게시글 마스터 편집기")
    st.write("현재 학생들이 작성해 둔 모든 카드를 실시간으로 강제 수정하거나 검열하여 삭제할 수 있습니다.")
    
    if len(st.session_state.tastes_list) == 0:
        st.write("수정할 카드가 존재하지 않습니다.")
    else:
        for t_item in st.session_state.tastes_list:
            with st.expander(f"⚙️ [{t_item['category']}] 카드 ID: {t_item['id']} - 편집창"):
                edit_input = st.text_input(f"내용 수정창 (ID: {t_item['id']})", value=t_item['text'], key=f"master_edit_{t_item['id']}")
                
                if edit_input != t_item['text'] and edit_input.strip():
                    t_item['text'] = edit_input.strip()
                    st.toast("부장 권한으로 텍스트가 강제 수정되었습니다.")
                
                if st.button("🗑️ 이 카드 완전 삭제", key=f"master_del_{t_item['id']}"):
                    st.session_state.tastes_list = [item for item in st.session_state.tastes_list if item['id'] != t_item['id']]
                    st.success("해당 부원의 글을 완전히 삭제처리 했습니다.")
                    st.rerun()


# [공통 푸터 영역]
st.markdown("""
<div style="background-color: #00664F; color: #F5F5F5; text-align: center; padding: 20px; border-radius: 10px; margin-top: 60px; font-size: 0.9rem;">
    © 2026 DUIT. All rights reserved. | 잠실여자고등학교 2층 정보실
</div>
""", unsafe_allow_html=True)

