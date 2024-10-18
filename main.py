import streamlit as st
import folium
from streamlit_folium import st_folium

# CSS for changing the entire background color and styling the page
st.markdown(
    """
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

    /* 기본 마진과 패딩 제거 */
    body {
        margin: 0;
        padding: 0;
    }
    
    /* Streamlit 전체 페이지의 배경을 변경하기 위한 설정 */
    .stApp {
        background-color: #ffefcc;
        font-family: 'Pretendard', sans-serif; /* 폰트 적용 */
        color: black; /* 기본 텍스트 색상 */
        padding: 0; /* 추가적인 패딩 제거 */
    }
    
    /* 상단 여백 제거 */
    .block-container {
        padding-top: 0;
        padding-bottom: 0;
        padding-right: 0;
    }
    
    /* 상단 여백 제거를 위한 추가 설정 */
    .css-18e3th9 {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-right: 0 !important;
    }

    .full-width-banner {
        position: relative;
        background-image: url('https://github.com/gina261/bigcontest_genAI/blob/main/images/banner_edited.png?raw=true');
        background-size: cover; /* 이미지 크기를 전체 영역에 맞춤 */
        background-position: center; /* 이미지 중앙 정렬 */
        height: 600px; /* 배너의 높이 설정 */
        width: 100vw; /* 페이지의 전체 너비를 사용 */
        margin-left: calc(-50vw + 50%); /* 페이지 중앙 정렬 후 왼쪽으로 이동 */
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        z-index: 1;
        flex-direction: column; /* 세로 방향 정렬을 위한 추가 */
    }

    /* 배너 텍스트 스타일 */
    .full-width-banner h1 {
        font-size: 3em;
        margin: 0;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 텍스트에 그림자 추가 */
    }

    /* 배경 큰 글씨 */
    .centered-text {
        font-size: 1.5em;
        margin: 0px 0 20px 0; /* 위쪽에 0px, 아래쪽에 20px 마진 추가 */
        text-align: center; /* 텍스트 중앙 정렬 */
        color: black;
    }

    /* 배경 중간 글씨 */
    .centered-subtext {
        font-size: 1.2em;
        margin: 20px 0 20px 0; /* 위쪽과 아래쪽에 20px 마진 추가 */
        text-align: center; /* 텍스트 중앙 정렬 */
        color: black;
    }

    .centered-subtext.last {
        margin-bottom: 50px; /* 마지막 텍스트와 박스 사이의 간격을 추가 */
    }

    /* 박스 스타일 */
    .box {
        background-image: url('https://github.com/gina261/bigcontest_genAI/blob/main/images/box1.png?raw=true');
        background-size: 500px;
        background-position: center; /* 이미지 중앙 정렬 */
        background-repeat: no-repeat; /* 이미지 반복 방지 */
        padding: 50px 0 20px 0; /* 상단 50px 여백, 하단 20px */
        border-radius: 0px;
        margin: 50px 0; /* 상단과 하단에 50px 마진 추가 */
        color: white;
        display: flex;
        justify-content: center;
        align-items: flex-start; /* 텍스트를 박스 상단에서부터 정렬 */
        height: 250px; /* 박스 높이 설정 */
        text-align: center;
    }
    
    .box h3 {
        font-size: 1.2em;
        font-weight: 400;
        margin: 0;
        text-align: center;
        color: white;
        width: 100%;
        padding-top: 113px; /* 텍스트와 상단 간격 설정 */
        padding-left: 60px;
    }

    /* 새 박스 스타일 */
    .box-2 {
        background-image: url('https://github.com/gina261/bigcontest_genAI/blob/main/images/box2.png?raw=true');
        background-size: 500px;
        background-position: center;
        background-repeat: no-repeat;
        padding: 20px;
        border-radius: 0px;
        margin: 100px 0 50px 0; /* 상단에 50px, 하단에 50px 마진 추가 */
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
        text-align: center;
    }
    
    .box-2 h3 {
        font-size: 1.2em;
        font-weight: 400;
        margin: 0;
        text-align: center;
        color: white;
        width: 100%;
    }

    /* 레이블 스타일 */
    .custom-label {
        color: black;
        font-family: 'Pretendard', sans-serif;
        font-weight: 300; /* 얇은 글꼴 적용 */
        font-size: 1em;
        margin-bottom: -25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the full-width banner and the centered texts below it
st.markdown(
    """
    <div class="full-width-banner">
        <h1></h1>
    </div>
    <div class="centered-text">
        반갑습니다. 오늘 어떤 하루를 보내고 계신가요?
    </div>
    <div class="centered-subtext">
        당신의 기분에 맞는 제주 맛집을 추천해드리겠습니다.
    </div>
    <div class="centered-subtext last">
        추천을 위해 몇 가지 질문에 답해주세요.
    </div>
    """,
    unsafe_allow_html=True
)

# 날짜, 시간대, 인원수 선택 위젯을 한 행에 배치
st.markdown(
    """
    <div class="box">
        <h3>1. 언제, 누구와 방문할 예정이신가요?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# 3개의 열을 생성하여 위젯을 한 행에 배치
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='custom-label'>날짜를 선택해주세요.</div>", unsafe_allow_html=True)
    selected_date = st.date_input("")
    
with col2:
    st.markdown("<div class='custom-label'>시간대를 선택해주세요.</div>", unsafe_allow_html=True)
    time_slot = st.selectbox(
        "", 
        ("아침", "점심", "오후", "저녁", "밤", "선택 안함")
    )

with col3:
    st.markdown("<div class='custom-label'>인원수를 선택해주세요.</div>", unsafe_allow_html=True)
    members_num = st.selectbox(
        "", 
        ("혼자", "2명", "3명", "4명 이상", "선택 안함")
    )


# 새 박스를 추가
st.markdown(
    """
    <div class="box-2">
        <h3>2. 방문 목적이 무엇인가요?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# 제주도 중심 좌표
jeju_center = [33.4996, 126.5312]

# Folium 지도 객체 생성
jeju_map = folium.Map(location=jeju_center, zoom_start=10)

# 마커 추가 예시
folium.Marker(
    location=[33.4996, 126.5312],
    popup="제주시",
    icon=folium.Icon(color="blue")
).add_to(jeju_map)

# Streamlit에서 지도 표시
st_data = st_folium(jeju_map, width=700, height=500)