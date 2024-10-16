import os
import numpy as np
import pandas as pd

# from transformers import AutoTokenizer, AutoModel
# import torch
# from tqdm import tqdm
# import faiss

import streamlit as st

# Gemini 설정
# import google.generativeai as genai

# gemini 설정
# GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
# genai.configure(api_key=GOOGLE_API_KEY)

# Gemini 모델 선택
# model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="예쁘DA🍊")



# CSS for adding a full-width background image with gradient
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap" rel="stylesheet">
    <style>
    /* 페이지 전체를 감싸는 상위 컨테이너의 패딩을 없애기 위한 CSS */
    .css-18e3th9, .css-1d391kg {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    
    /* 배너 영역 설정 */
    .full-width-banner {
        background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0)), 
                    url('https://ifh.cc/g/lD0gY1.jpg'); /* 배경으로 사용할 이미지 URL */
        background-size: cover; /* 이미지 크기를 전체 영역에 맞춤 */
        background-repeat: no-repeat; /* 반복 없이 한 번만 이미지 사용 */
        background-position: center; /* 이미지 중앙 정렬 */
        height: 500px; /* 배너의 높이 설정 */
        width: 100vw; /* 페이지의 전체 너비를 사용 */
        margin-left: calc(-50vw + 50%); /* 페이지 중앙 정렬 후 왼쪽으로 이동 */
        display: flex;
        align-items: flex-end; /* 텍스트를 배너 하단에 배치 */
        justify-content: center;
        color: white;
        position: relative;
        z-index: 1;
        font-family: 'Nanum Gothic', sans-serif; /* Nanum Gothic 폰트 적용 */
    }

    /* 텍스트 스타일 */
    .full-width-banner h1 {
        font-size: 3em;
        margin: 0;
        padding: 20px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 텍스트에 그림자 추가 */
    }

    /* 불필요한 텍스트 숨기기 */
    .stText, .stMarkdown p {
        display: none; /* 모든 텍스트 요소를 숨깁니다 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the full-width banner
st.markdown(
    """
    <div class="full-width-banner">
        <h1>Welcome to My Streamlit App</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Sample content
st.write("This is the content of the app below the banner.")
st.write("You can add more Streamlit components here.")