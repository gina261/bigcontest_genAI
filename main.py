import streamlit as st

# CSS for adding a full-width background image with transparency
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

    .full-width-banner {
        position: relative;
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://ifh.cc/g/tyYadc.jpg'); /* 반투명 검정색 오버레이와 이미지 */
        background-size: cover; /* 이미지 크기를 전체 영역에 맞춤 */
        background-position: center; /* 이미지 중앙 정렬 */
        height: 500px; /* 배너의 높이 설정 */
        width: 100vw; /* 페이지의 전체 너비를 사용 */
        margin-left: calc(-50vw + 50%); /* 페이지 중앙 정렬 후 왼쪽으로 이동 */
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        z-index: 1;
        flex-direction: column; /* 세로 방향 정렬을 위한 추가 */
    }

    /* 텍스트 스타일 */
    .full-width-banner h1 {
        font-size: 3em;
        font-family: 'Nanum Gothic', sans-serif;
        margin: 0;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 텍스트에 그림자 추가 */
    }

    .full-width-banner h2 {
        font-size: 2em;
        font-family: 'Nanum Gothic', sans-serif;
        margin: 0;
        color: white;
        margin-top: 10px; /* 상단 마진 추가 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the full-width banner
st.markdown(
    """
    <div class="full-width-banner">
        <h1>Welcome to team 예쁘DA</h1>
    </div>
    """,
    unsafe_allow_html=True
)