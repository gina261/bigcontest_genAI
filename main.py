import streamlit as st

# CSS and JavaScript for scroll animation
st.components.v1.html(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

    .full-width-banner {
        position: relative;
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://i.ibb.co/0tVV9zh'); /* 반투명 검정색 오버레이와 이미지 */
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

    .reveal-text {
        font-size: 2em;
        font-family: 'Nanum Gothic', sans-serif;
        margin: 0;
        color: white;
        margin-top: 20px; /* 상단 마진 추가 */
        opacity: 0; /* 초기 상태에서 숨김 */
        transform: translateY(20px); /* 애니메이션 효과를 위해 아래로 이동 */
        transition: opacity 1s ease-out, transform 1s ease-out; /* 애니메이션 설정 */
    }

    .show {
        opacity: 1; /* 보이도록 설정 */
        transform: translateY(0); /* 원래 위치로 이동 */
    }
    </style>

    <div class="full-width-banner">
        <h1>Welcome to team 예쁘DA</h1>
    </div>
    <div class="reveal-text" id="scroll-text">
        반갑습니다. 오늘 어떤 하루를 보내고 계신가요?
    </div>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        function revealOnScroll() {
            var element = document.getElementById('scroll-text');
            if (element) {
                var position = element.getBoundingClientRect().top;
                var windowHeight = window.innerHeight;
                
                if (position < windowHeight) {
                    element.classList.add('show');
                }
            }
        }

        window.addEventListener('scroll', revealOnScroll);
        revealOnScroll();
    });
    </script>
    """,
    height=800,
)

# Sample content to create scroll space
st.write("This is the content of the app below the banner.")
st.write("Scroll down to see the animation effect when the text appears.")
st.write("\n" * 50)  # Create enough space to scroll