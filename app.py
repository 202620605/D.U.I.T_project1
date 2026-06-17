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

# ----------------- 🧠 데이터 세션 관리 -----------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = ""
if 'boss_verified' not in st.session_state:
    st.session_state.boss_verified = False

# [ABOUT DUIT 기본 데이터]
if 'about_location_title' not in st.session_state:
    st.session_state.about_location_title = "잠실여자고등학교 2층 정보실"
if 'about_location_desc' not in st.session_state:
    st.session_state.about_location_desc = "정규활동 및 동아리 부원들의 프로젝트 연구를 위해 주로 모이는 공간입니다."
if 'about_jacket_base' not in st.session_state:
    st.session_state.about_jacket_base = "깊이감 있는 이화그린"
if 'about_jacket_point' not in st.session_state:
    st.session_state.about_jacket_point = "산뜻한 연두색"
if 'about_jacket_img_text' not in st.session_state:
    st.session_state.about_jacket_img_text = "과잠 이미지 시각화 준비 중"

# [부서 소개 및 연간 일정 기본 데이터]
if 'board_dept_intro' not in st.session_state:
    st.session_state.board_dept_intro = "2026학년도 기준 정예 인원으로 운영됩니다."
if 'board_dept_list' not in st.session_state:
    st.session_state.board_dept_list = [
        "💻 프로그래밍부: 웹/앱 서비스 빌드 및 알고리즘 개발",
        "🛡️ 보안부: 웹 해킹 기초 아키텍처 및 시스템 보안 스터디",
        "🤖 AI부: 인공지능 API 응용 및 빅데이터 수집/분석"
    ]
if 'board_schedule_list' not in st.session_state:
    st.session_state.board_schedule_list = [
        {"month": "03월", "plan": "신입 부원 모집, 면접 및 오리엔테이션"},
        {"month": "05월", "plan": "모의토론, 모둠탐구"},
        {"month": "06월", "plan": "축제, 개인탐구, 홈페이지 만들기"}
    ]

# 👥 정식 승인 부원 목록 (초기에는 오직 부장 계정 20401만 존재)
if 'approved_users' not in st.session_state:
    st.session_state.approved_users = {
        "20401": "2025" 
    }

# 이전 활동 보고 표 데이터 형태로 구조 변경 (연간 일정 표 스타일 요구 반영)
if 'boss_log_list' not in st.session_state:
    st.session_state.boss_log_list = [
        {"month": "03월", "plan": "신입 부원 모집, 면접 및 오리엔테이션 완료"},
        {"month": "05월", "plan": "주제별 모의토론 및 소모둠 탐구 활동 진행"},
        {"month": "06월", "plan": "교내 축제 참여 및 개인별 홈페이지 제작 프로젝트"}
    ]
if 'signup_queue' not in st.session_state:
    st.session_state.signup_queue = []

# 📂 운영 파트(카테고리) 목록
if 'taste_categories' not in st.session_state:
    st.session_state.taste_categories = [
        "🎵 최애 플레이리스트를 공유해요", 
        "🍕 매점 꿀조합", 
        "🎤 최애 아이돌을 공유해요"
    ]

# 취향 공유 등록 데이터 리스트
if 'tastes_list' not in st.session_state:
    st.session_state.tastes_list = [
        {"id": 0, "category": "🎵 최애 플레이리스트를 공유해요", "text": "코딩할 때 듣기 좋은 뉴에이지 추천합니다.", "owner": "20401"},
        {"id": 1, "category": "🍕 매점 꿀조합", "text": "치즈불닭볶음면에 스트링치즈 추가해보세요!", "owner": "20401"}
    ]
if 'taste_id_counter' not in st.session_state:
    st.session_state.taste_id_counter = 2


# ----------------- 💻 사이드바 목차 및 인증 제어 -----------------
st.sidebar.title("💚 DUIT 메뉴")

menu_options = ["🏠 메인 홈"]

if st.session_state.boss_verified:
    menu_options.append("👑 부장 전용 관리 페이지")

selected_menu = st.sidebar.radio("이동할 페이지를 선택하세요:", menu_options)
st.sidebar.markdown("---")

if st.session_state.boss_verified:
    st.sidebar.success("👑 부장 전권 관리 모드 활성화 중")
    if st.sidebar.button("부장 모드 종료"):
        st.session_state.boss_verified = False
        st.rerun()
else:
    st.sidebar.markdown("### 🔑 부장 인증 관리")
    boss_pwd_input = st.sidebar.text_input("마스터 패스워드 입력:", type="password", placeholder="비밀번호 입력 시 목차 오픈")
    if boss_pwd_input == "2025":
        st.session_state.boss_verified = True
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
# 🏠 1. 메인 홈 화면 렌더링 영역
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
        st.markdown(f"""
        <div class="info-card">
            <h3>📍 위치</h3>
            <p><b>{st.session_state.about_location_title}</b></p>
            <p style="color:#666; font-size:0.95rem; line-height:1.4;">{st.session_state.about_location_desc}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="info-card">
            <h3>🧥 과잠 디자인</h3>
            <p><b>메인 베이스:</b> {st.session_state.about_jacket_base}</p>
            <p><b>자수/포인트:</b> {st.session_state.about_jacket_point}</p>
            <div class="jacket-box">{st.session_state.about_jacket_img_text}</div>
        </div>
        """, unsafe_allow_html=True)

    # --- 동아리 게시판 섹션 ---
    st.markdown('<div class="section-title">동아리 게시판</div>', unsafe_allow_html=True)
    b_col1, b_col2, b_col3 = st.columns(3)

    with b_col1:
        st.markdown(f"""
        <div class="info-card">
            <h3>👥 부서 소개</h3>
            <p style="font-size:0.95rem; color:#444; margin-bottom:8px;">{st.session_state.board_dept_intro}</p>
            <ul>
        """, unsafe_allow_html=True)
        for dept in st.session_state.board_dept_list:
            st.markdown(f"<li>{dept}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)

    with b_col2:
        st.markdown('<div class="info-card"><h3>📅 동아리 연간 일정</h3>', unsafe_allow_html=True)
        st.markdown('<table class="schedule-table"><thead><tr><th>월별</th><th>주요 일정 및 계획</th></tr></thead><tbody>', unsafe_allow_html=True)
        for sched in st.session_state.board_schedule_list:
            st.markdown(f"<tr><td>{sched['month']}</td><td>{sched['plan']}</td></tr>", unsafe_allow_html=True)
        st.markdown('</tbody></table></div>', unsafe_allow_html=True)

    with b_col3:
        # [요청 반영 디자인 변경]: '이전 활동 보고' 칸 디자인을 연간 일정 표 스타일과 100% 동일하게 구현
        st.markdown('<div class="info-card"><h3>🚀 이전 활동 보고</h3>', unsafe_allow_html=True)
        st.markdown('<table class="schedule-table"><thead><tr><th>월별</th><th>활동 기록 내용</th></tr></thead><tbody>', unsafe_allow_html=True)
        for log_item in st.session_state.boss_log_list:
            st.markdown(f"<tr><td>{log_item['month']}</td><td>{log_item['plan']}</td></tr>", unsafe_allow_html=True)
        st.markdown('</tbody></table></div>', unsafe_allow_html=True)

    # --- 로그인 / 회원가입 섹션 ---
    st.markdown('<div class="section-title">DUIT 부원 인증</div>', unsafe_allow_html=True)

    if not st.session_state.logged_in:
        auth_col1, auth_col2 = st.columns([1, 1])
        with auth_col1:
            st.info("💡 '취향 공유' 공간은 DUIT 정식 부원 전용 기능입니다.")
            with st.form("login_form"):
                user_id = st.text_input("학번 (아이디)", placeholder="예: 20401")
                user_pw = st.text_input("비밀번호", type="password")
                submitted = st.form_submit_button("인증하기")
                
                if submitted:
                    if user_id in st.session_state.approved_users and st.session_state.approved_users[user_id] == user_pw:
                        st.session_state.logged_in = True
                        st.session_state.current_user = str(user_id)
                        st.success(f"🎉 {user_id} 부원님 인증 성공!")
                        st.rerun()
                    else:
                        st.error("학번이 없거나 비밀번호가 올바르지 않습니다.")
                        
        with auth_col2:
            with st.form("signup_form"):
                st.markdown("### 📝 신규 부원 가입 신청")
                req_id = st.text_input("가입할 본인의 학번을 입력하세요:", placeholder="예: 10522")
                req_pw = st.text_input("사용할 비밀번호를 입력하세요:", type="password", placeholder="최소 4자리 이상")
                req_submit = st.form_submit_button("신규 부원 등록 신청 발송")
                
                if req_submit:
                    if req_id.strip() and req_pw.strip():
                        if req_id in st.session_state.approved_users:
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
                        st.error("학번과 비밀번호를 완벽히 입력해주세요.")
    else:
        st.success(f"✅ 현재 {st.session_state.current_user} 계정으로 로그인되어 있습니다.")

    # [요청 반영 완료]: 일반 메인 홈 화면에서는 부원 명단 리스트 컴포넌트를 완전히 삭제했습니다.

    # --- 취향 공유 섹션 ---
    st.markdown('<div class="section-title">✨ 부원 취향 공유 공간</div>', unsafe_allow_html=True)

    if not st.session_state.logged_in:
        st.warning("🔒 이 공간은 비공개 상태입니다. 위 메뉴에서 'DUIT 부원 인증'을 완료해야 접근할 수 있습니다.")
    else:
        st.write("동아리 부원들이 파트별 관심사를 자유롭게 공유하는 소통 공간입니다.")
        
        with st.expander("➕ 나의 취향 조각 하나 추가하기", expanded=False):
            # [요청 반영 완료]: 부장 페이지에서 새로 생성한 커스텀 파트들이 여기에 자동 연동되어 나타납니다.
            select_category = st.selectbox(
                "어느 파트에 넣을 건지 선택해주세요:",
                st.session_state.taste_categories
            )
            new_taste_input = st.text_input("추가하고 싶은 구체적인 관심사 내용을 적어주세요:")
            
            if st.button("➕ 등록하기"):
                if new_taste_input.strip():
                    st.session_state.tastes_list.append({
                        "id": st.session_state.taste_id_counter,
                        "category": select_category,
                        "text": new_taste_input.strip(),
                        "owner": st.session_state.current_user
                    })
                    st.session_state.taste_id_counter += 1
                    st.success("취향 카드가 추가되었습니다!")
                    st.rerun()
                    
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
                        <span class="taste-tag">{taste_item['category']}</span> (작성자: {taste_item['owner']})
                        <div class="taste-text">✨ {taste_item['text']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if taste_item['owner'] == st.session_state.current_user:
                        if st.button(f"🗑️ 내가 쓴 글 삭제", key=f"del_{taste_item['id']}"):
                            st.session_state.tastes_list = [item for item in st.session_state.tastes_list if item['id'] != taste_item['id']]
                            st.rerun()


# ==============================================================================
# 👑 2. 부장 전용 단독 관리 페이지
# ==============================================================================
elif selected_menu == "👑 부장 전용 관리 페이지" and st.session_state.boss_verified:
    
    st.title("👑 DUIT 부장 전용 전권 관리 대시보드")
    st.write("메인 홈 화면에 노출되는 모든 콘텐츠와 파트, 전체 부원들의 상태를 마스터 통제합니다.")
    st.markdown("---")

    # 👥 [요청 반영 완료]: 부원 명단 조회는 오직 이곳 부장용 페이지에서만 가능합니다.
    st.subheader("👥 동아리 가입 인원 상태 현황판")
    user_list_text = ", ".join([f"**{uid} 부원**" for uid in st.session_state.approved_users.keys()])
    st.info(f"현재 정식 승인 부원 목록: {user_list_text}")
    st.markdown("---")
    
    # 🛠️ [1] ABOUT DUIT 칸 수정 (위치 & 과잠)
    st.subheader("📍 [ABOUT DUIT] 위치 및 과잠 칸 콘텐츠 수정")
    with st.form("about_edit_form"):
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### **위치 정보 컴포넌트**")
            loc_title = st.text_input("위치 메인 제목", value=st.session_state.about_location_title)
            loc_desc = st.text_area("위치 세부 설명", value=st.session_state.about_location_desc)
        with c2:
            st.markdown("#### **과잠 디자인 컴포넌트**")
            jkt_base = st.text_input("메인 베이스 색상", value=st.session_state.about_jacket_base)
            jkt_point = st.text_input("자수/포인트 색상", value=st.session_state.about_jacket_point)
            jkt_img_text = st.text_input("이미지 박스 대체 문구", value=st.session_state.about_jacket_img_text)
            
        if st.form_submit_button("💾 ABOUT DUIT 내용 일괄 업데이트"):
            st.session_state.about_location_title = loc_title
            st.session_state.about_location_desc = loc_desc
            st.session_state.about_jacket_base = jkt_base
            st.session_state.about_jacket_point = jkt_point
            st.session_state.about_jacket_img_text = jkt_img_text
            st.success("ABOUT DUIT 정보가 완전히 업데이트 되었습니다.")
            st.rerun()

    st.markdown("---")

    # 🛠️ [2] 부서 소개 칸 수정
    st.subheader("👥 [동아리 게시판] 부서 소개 칸 수정")
    with st.form("dept_edit_form"):
        dept_intro = st.text_input("부서 설명 요약문", value=st.session_state.board_dept_intro)
        st.write("**현재 등록된 하위 부서 리스트:**")
        
        d0 = st.text_input("부서 1", value=st.session_state.board_dept_list[0])
        d1 = st.text_input("부서 2", value=st.session_state.board_dept_list[1])
        d2 = st.text_input("부서 3", value=st.session_state.board_dept_list[2])
        
        if st.form_submit_button("💾 부서 소개 정보 업데이트"):
            st.session_state.board_dept_intro = dept_intro
            st.session_state.board_dept_list = [d0, d1, d2]
            st.success("부서 소개 내용이 업데이트되었습니다!")
            st.rerun()

    st.markdown("---")

    # 🛠️ [3] 연간 일정 칸 수정
    st.subheader("📅 [동아리 게시판] 연간 일정 표 데이터 수정")
    with st.form("schedule_edit_form"):
        st.write("메인 홈 연간 일정 표에 노출할 월별 데이터를 수정합니다.")
        updated_schedules = []
        for idx, sched in enumerate(st.session_state.board_schedule_list):
            sc_c1, sc_c2 = st.columns([1, 4])
            m_val = sc_c1.text_input(f"월 정보 ({idx+1}행)", value=sched['month'], key=f"m_key_{idx}")
            p_val = sc_c2.text_input(f"계획 및 일정 ({idx+1}행)", value=sched['plan'], key=f"p_key_{idx}")
            updated_schedules.append({"month": m_val, "plan": p_val})
            
        if st.form_submit_button("💾 연간 일정 표 즉시 변경"):
            st.session_state.board_schedule_list = updated_schedules
            st.success("연간 일정 내부 표 데이터가 전면 수정되었습니다!")
            st.rerun()

    st.markdown("---")
    
    # 🚀 [4] 이전 활동 보고 표 데이터 관리소 (표 디자인 맞춤 반영 수정)
    st.subheader("🚀 [이전 활동 보고] 표 데이터 수정 및 행 추가")
    with st.form("boss_log_edit_form"):
        st.write("메인 홈 이전 활동 보고 표에 노출할 월별 데이터를 제어합니다.")
        updated_logs = []
        for idx, log_item in enumerate(st.session_state.boss_log_list):
            l_c1, l_c2 = st.columns([1, 4])
            lm_val = l_c1.text_input(f"기록 월 ({idx+1}행)", value=log_item['month'], key=f"lm_key_{idx}")
            lp_val = l_c2.text_input(f"활동 내역 ({idx+1}행)", value=log_item['plan'], key=f"lp_key_{idx}")
            updated_logs.append({"month": lm_val, "plan": lp_val})
            
        if st.form_submit_button("💾 이전 활동 보고 표 전체 갱신"):
            st.session_state.boss_log_list = updated_logs
            st.success("이전 활동 보고 데이터 표가 실시간 반영 완료되었습니다!")
            st.rerun()

    with st.form("boss_log_add_row_form"):
        st.write("**➕ 새로운 기록 행 한 줄 추가하기**")
        add_m = st.text_input("활동 월 입력 (예: '07월')")
        add_p = st.text_input("상세 활동 내용 입력")
        if st.form_submit_button("➕ 새로운 활동 행 추가"):
            if add_m.strip() and add_p.strip():
                st.session_state.boss_log_list.append({"month": add_m.strip(), "plan": add_p.strip()})
                st.success("활동 기록 행이 한 줄 신설되었습니다!")
                st.rerun()

    st.write("**현재 등록된 활동 리스트 삭제 관리:**")
    for idx, log_item in enumerate(st.session_state.boss_log_list):
        cl1, cl2 = st.columns([6, 1])
        cl1.info(f"[{log_item['month']}] {log_item['plan']}")
        if cl2.button("🗑️ 행 삭제", key=f"remove_log_row_{idx}"):
            st.session_state.boss_log_list.pop(idx)
            st.rerun()
            
    st.markdown("---")
    
    # 📩 [5] 신규 부원 가입 신청 관리소
    st.subheader("📩 부원 가입 신청 수락/반려 제어기")
    if not st.session_state.signup_queue:
        st.info("현재 대기 중인 신규 가입 신청서가 없습니다.")
    else:
        for req_user in st.session_state.signup_queue:
            with st.container():
                r_col1, r_col2, r_col3 = st.columns([2, 1, 1])
                with r_col1:
                    st.warning(f"👤 신청 학생 학번: **{req_user['id']}** | 패스워드: `{req_user['pw']}`")
                with r_col2:
                    if st.button(f"✅ 최종 승인", key=f"final_app_{req_user['id']}"):
                        st.session_state.approved_users[req_user['id']] = req_user['pw']
                        st.session_state.signup_queue.remove(req_user)
                        st.success(f"{req_user['id']} 학번이 정식 부원으로 승인 추가되었습니다!")
                        st.rerun()
                with r_col3:
                    if st.button(f"❌ 가입 거절", key=f"final_rej_{req_user['id']}"):
                        st.session_state.signup_queue.remove(req_user)
                        st.rerun()
                        
    st.markdown("---")
    
    # 🛠️ [6] 부원 게시물 마스터 통제소
    st.subheader("🛠️ 전체 부원 취향 조각 마스터 통제소")
    if len(st.session_state.tastes_list) == 0:
        st.info("부원들이 등록한 취향 카드가 비어있습니다.")
    else:
        for t_item in st.session_state.tastes_list:
            with st.expander(f"⚙️ [{t_item['category']}] 작성자: {t_item['owner']} 글 통제 편집창"):
                edit_input = st.text_input("내용 강제 변경", value=t_item['text'], key=f"final_edit_{t_item['id']}")
                
                if edit_input != t_item['text'] and edit_input.strip():
                    t_item['text'] = edit_input.strip()
                    st.toast("부장 권한으로 글 내용이 수정되었습니다.")
                
                if st.button("🗑️ 해당 카드 영구 파기", key=f"final_del_{t_item['id']}"):
                    st.session_state.tastes_list = [item for item in st.session_state.tastes_list if item['id'] != t_item['id']]
                    st.rerun()

    st.markdown("---")

    # 📂 [요청 반영 완료]: 파트 관리 컴포넌트 레이아웃의 '가장 마지막' 순서로 이동 배치
    st.subheader("📂 [파트 관리] 새로운 취향 공유 파트 개설 및 추가")
    with st.form("add_category_form"):
        new_cat_name = st.text_input("새로 개설하고 싶은 파트 명을 입력하세요 (예: 🎮 추천 보드게임):")
        if st.form_submit_button("➕ 새로운 파트 추가 개설"):
            if new_cat_name.strip():
                if new_cat_name.strip() not in st.session_state.taste_categories:
                    st.session_state.taste_categories.append(new_cat_name.strip())
                    st.success(f"'{new_cat_name.strip()}' 파트가 새롭게 추가되어 실시간 연동됩니다!")
                    st.rerun()
                else:
                    st.warning("이미 존재하는 파트 이름입니다.")
            else:
                st.error("추가할 파트명을 입력해 주세요.")

    st.write("**현재 운영 중인 공유 파트 목록:**")
    st.code(", ".join(st.session_state.taste_categories))


# ----------------- 🌐 시스템 공통 하단 푸터 -----------------
st.markdown("""
<div style="background-color: #00664F; color: #F5F5F5; text-align: center; padding: 20px; border-radius: 10px; margin-top: 60px; font-size: 0.9rem;">
    © 2026 DUIT. All rights reserved. | 잠실여자고등학교 2층 정보실
</div>
""", unsafe_allow_html=True)

