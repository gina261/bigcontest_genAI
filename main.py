import streamlit as st

# CSS and JavaScript for scroll animation
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

    .full-width-banner {
        background-image: url('https://ifh.cc/g/lD0gY1.jpg'); /* 배경으로 사용할 이미지 URL */
        background-size: cover; /* 이미지 크기를 전체 영역에 맞춤 */
        background-position: center; /* 이미지 중앙 정렬 */
        height: 500px; /* 배너의 높이 설정 */
        width: 100vw; /* 페이지의 전체 너비를 사용 */
        margin-left: calc(-50vw + 50%); /* 페이지 중앙 정렬 후 왼쪽으로 이동 */
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        position: relative;
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
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 텍스트에 그림자 추가 */
        margin-top: 10px; /* 상단 마진 추가 */
        opacity: 0; /* 초기 상태에서 숨김 */
        transform: translateY(20px); /* 애니메이션 효과를 위해 아래로 이동 */
        transition: opacity 1s ease-out, transform 1s ease-out; /* 애니메이션 설정 */
    }

    .show {
        opacity: 1; /* 보이도록 설정 */
        transform: translateY(0); /* 원래 위치로 이동 */
    }
    </style>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // 요소를 감지하여 클래스 추가하는 함수
        function revealOnScroll() {
            var element = document.querySelector('.full-width-banner h2');
            var position = element.getBoundingClientRect().top;
            var windowHeight = window.innerHeight;

            // 요소가 보이면 'show' 클래스 추가
            if (position < windowHeight) {
                element.classList.add('show');
            }
        }

        // 스크롤 이벤트 리스너 추가
        window.addEventListener('scroll', revealOnScroll);

        // 초기 실행
        revealOnScroll();
    });
    </script>
    """,
    unsafe_allow_html=True
)

# HTML for the full-width banner
st.markdown(
    """
    <div class="full-width-banner">
        <h1>Welcome to team 예쁘DA</h1>
        <h2>제주 맛집 추천 챗봇</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Sample content to create scroll space
st.write("This is the content of the app below the banner.")
st.write("You can add more Streamlit components here.")
st.write("Scroll down to see the animation effect when the text appears.")
st.write("\n" * 50)  # Create enough space to scroll