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

# 글꼴 설정
# Custom CSS style for changing the font
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@400;700&display=swap" rel="stylesheet">
    <style>
    .custom-title {
        font-family: 'Karla', sans-serif;
        font-size: 48px;
        color: #294f7e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="custom-title">Hello, Ybigta!</h1>', unsafe_allow_html=True)



# CSS for adding a background image to the top section
st.markdown(
    """
    <style>
    .top-banner {
        background-image: url('https://img.siksinhot.com/seeon/1551856689061267.jpg'); /* 배경으로 사용할 이미지 URL */
        background-size: cover; /* 이미지 크기를 전체 영역에 맞춤 */
        background-position: center; /* 이미지 중앙 정렬 */
        height: 300px; /* 배너의 높이 설정 */
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
    }

    /* 텍스트 스타일 */
    .top-banner h1 {
        font-size: 3em;
        font-family: 'Karla', sans-serif;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the top banner
st.markdown(
    """
    <div class="top-banner">
        <h1>Welcome to My Streamlit App</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Sample content
st.write("This is the content of the app below the banner.")
st.write("You can add more Streamlit components here.")