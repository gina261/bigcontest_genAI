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
    /* Streamlit 기본 상단 바의 배경색과 테두리 색 변경 */
    .css-18e3th9 {
        background-color: #333333; /* 원하는 배경색으로 변경 */
        border-bottom: 1px solid #444444; /* 테두리 색상 */
    }
    
    /* Streamlit 메뉴 버튼(햄버거 메뉴)와 메뉴 아이콘 색 변경 */
    .css-1q8dd3e, .css-1v3fvcr {
        color: white; /* 텍스트 및 아이콘 색을 흰색으로 설정 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sample content
st.title("Customized Streamlit App")
st.write("This app has a customized top bar.")