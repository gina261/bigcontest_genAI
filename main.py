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



# CSS for changing the color of the Streamlit header
st.markdown(
    """
    <style>
    /* 상단 바의 배경색 변경 */
    ._streamlitAppContainer_nim44_1 {
        background-color: #4CAF50 !important; /* 원하는 색상으로 변경하세요 */
        border-bottom: 1px solid #333333;
        visibility: visible;
    }

    /* 내부 컨테이너 스타일 조정 */
    ._stateContainer_nim44_26 {
        padding-top: 10px; /* 필요 시 여백 조정 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sample content
st.title("Hello, Ybigta!")
st.write("Customized Streamlit App")
st.write("This app has a customized top bar.")