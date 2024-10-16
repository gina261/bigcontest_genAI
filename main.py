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
    /* 상단의 기본 Streamlit 바를 숨깁니다 */
    .css-18e3th9, .css-1d391kg {
        visibility: hidden;
    }

    /* 상단 바의 배경색을 원하는 색으로 변경합니다 (visible 상태일 때 사용) */
    .css-18e3th9 {
        background-color: #4CAF50 !important; /* 원하는 색상으로 변경하세요 */
        visibility: visible; /* 이 줄을 주석 해제 시 색 변경만 적용됩니다 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sample content
st.title("Hello, Ybigta!")
st.write("Customized Streamlit App")
st.write("This app has a customized top bar.")