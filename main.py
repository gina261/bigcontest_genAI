import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import requests

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
    
    iframe {
        width: 100% !important;
        height: 100% !important;
        min-height: 400px;
        border: none; /* 검은 테두리 없애기 */
    }

    .full-width-banner {
        position: relative;
        background-image: url('https://github.com/gina261/bigcontest_genAI/blob/main/images/banner.png?raw=true');
        background-size: cover; /* 이미지 크기를 전체 영역에 맞춤 */
        background-position: center bottom;
        height: 450px; /* 배너의 높이 설정 */
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
        margin: 50px 0 20px 0; /* 상단 50px 하단 20px 마진 추가 */
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
        padding-left: 30px;
    }

    /* 새 박스 스타일 */
    .box-2 {
        background-image: url('https://github.com/gina261/bigcontest_genAI/blob/main/images/box2.png?raw=true');
        background-size: 500px;
        background-position: center;
        background-repeat: no-repeat;
        padding: 20px;
        border-radius: 0px;
        margin: 100px 0 20px 0; /* 상단에 80px, 하단에 20px 마진 추가 */
        color: white;
        display: flex;
        justify-content: center;
        align-items: flex-start;
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
        padding-top: 17px;
        padding-left: 40px
    }
    
    .box-2 h4 {
        font-size: 1.2em;
        font-weight: 400;
        margin: 0;
        text-align: center;
        color: white;
        width: 100%;
        padding-top: 17px;
        padding-left: 30px
    }

    /* 레이블 스타일 */
    .custom-label {
        color: black;
        font-family: 'Pretendard', sans-serif;
        font-weight: 300; /* 얇은 글꼴 적용 */
        font-size: 1em;
        margin-bottom: -25px;
    }

    /* Selectbox 크기 조정 */
    .stSelectbox div[data-baseweb="select"] {
        max-width: 250px;  /* selectbox의 최대 너비 설정 */
        margin-bottom: 20px;  /* selectbox와 아래 내용 간의 간격 설정 */
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

# '선택 안함' 옵션을 추가한 selectbox를 사용하여 날짜 선택 유무 결정
with col1:
    st.markdown("<div class='custom-label'>날짜를 선택해주세요.</div>", unsafe_allow_html=True)
    date_option = st.selectbox("", ["선택 안함", "날짜 선택"])

    # 선택한 옵션에 따라 date_input 표시
    if date_option == "날짜 선택":
        selected_date = st.date_input("")
    else:
        selected_date = None

    
with col2:
    st.markdown("<div class='custom-label'>시간대를 선택해주세요.</div>", unsafe_allow_html=True)
    time_slot = st.selectbox(
        "", 
        ("선택 안함", "아침", "점심", "오후", "저녁", "밤")
    )

with col3:
    st.markdown("<div class='custom-label'>인원수를 선택해주세요.</div>", unsafe_allow_html=True)
    members_num = st.selectbox(
        "", 
        ("선택 안함", "혼자", "2명", "3명", "4명 이상")
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


# 중앙에 selectbox를 배치
col_center = st.columns([1, 1, 1])
with col_center[1]:
    visit_purpose = st.selectbox(
        "",
        ("선택 안함", "식사", "카페/디저트")
    )
    

st.markdown(
    """
    <div class="box-2">
        <h4>3. 어디로 가시나요?</h4>
    </div>
    """,
    unsafe_allow_html=True
)

    

# 제주도 중심 좌표
jeju_center = [33.38, 126.6] # 기존 33.4996, 126.5312

mapbox_token = st.secrets["MAPBOX_API_KEY"]

# 커스텀 Mapbox 스타일 URL 적용
mapbox_style = 'mapbox://styles/gina261/cm2f34dvz000g01pygoj0g41c'
custom_style_url = f'https://api.mapbox.com/styles/v1/gina261/cm2f34dvz000g01pygoj0g41c/tiles/{{z}}/{{x}}/{{y}}?access_token={mapbox_token}'

# Folium 지도 객체 생성
jeju_map = folium.Map(
    location=jeju_center, 
    zoom_start=9.8, # 10 => 9.8
    tiles=custom_style_url,
    attr='Mapbox',
    name='Mapbox Custom Style'
)

# Load GeoJSON data from GitHub linkㅌ
geojson_url = 'https://raw.githubusercontent.com/gina261/bigcontest_genAI/main/geojson/jeju_edited.geojson'
geojson_data = requests.get(geojson_url).json()

# Restricting bounds to Jeju Island to avoid showing other regions
# jeju_bounds = [[33.1, 125.9], [34.0, 127.0]]  # Adjust the lat/lon for Jeju boundaries
# jeju_map.fit_bounds(jeju_bounds)

# Add GeoJSON data to the map with interactive features
def on_click(feature):
    return {
        'fillColor': '#ff8015',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.6,
        'highlight': True
    }

geo_json = folium.GeoJson(
    geojson_data,
    name='jeju_districts',
    style_function=lambda feature: {
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0,
    },
    highlight_function=on_click,
    tooltip=folium.GeoJsonTooltip(
        fields=['adm_nm'],  # Ensure that 'adm_nm' is the field name for the region name
        aliases=['Region'],
        localize=True
    )
).add_to(jeju_map)

# Streamlit에서 지도 표시
st_data = st_folium(jeju_map, width=800, height=400)

# Retrieve selected region from folium
if st_data and st_data.get('last_active_drawing'):
    selected_region = st_data['last_active_drawing']['properties']['adm_nm']
    st.write(f"선택한 지역: {selected_region.split(' ')[1]} {selected_region.split(' ')[2]}")
    
    
st.markdown(
    """
    <div class="centered-subtext">
        오늘의 기분이나 상황을 입력해주세요. 그에 맞는 제주의 멋진 곳을 추천해드립니다.
    </div>
    """,
    unsafe_allow_html=True
)