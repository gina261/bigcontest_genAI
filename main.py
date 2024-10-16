import streamlit as st

# CSS for styling the page
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

    body {
        margin: 0;
        padding: 0;
    }

    .full-width-banner {
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://i.ibb.co/0tVV9zh'); /* 반투명 검정색 오버레이와 이미지 */
        background-size: cover;
        background-position: center;
        height: 100vh; /* 배너의 높이를 화면 전체 높이로 설정 */
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        position: relative;
        z-index: 1;
        flex-direction: column;
    }

    /* 텍스트 스타일 */
    .full-width-banner h1 {
        font-size: 3em;
        font-family: 'Nanum Gothic', sans-serif;
        margin: 0;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    .reveal-text {
        font-size: 1.5em;
        font-family: 'Nanum Gothic', sans-serif;
        margin: 20px 0;
        color: white;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 1s ease-out, transform 1s ease-out;
        text-align: center;
    }

    .show {
        opacity: 1;
        transform: translateY(0);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the banner and the text
st.markdown(
    """
    <div class="full-width-banner">
        <h1>Welcome to team 예쁘DA</h1>
        <div class="reveal-text" id="scroll-text">반갑습니다. 오늘 어떤 하루를 보내고 계신가요?</div>
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
    unsafe_allow_html=True
)

# Sample content to create scroll space
st.write("\n" * 10)  # Create enough space to scroll
st.write("This is the content of the app below the banner.")
st.write("Scroll down to see the animation effect when the text appears.")
st.write("\n" * 50)  # Create enough space to scroll