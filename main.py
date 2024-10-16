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



# 상단 네비게이션 바
st.markdown(
    """
    <style>
    /* 기본 바디 스타일 */
    body {
        margin: 0;
        font-family: 'Karla', sans-serif;
    }
    
    /* 고정된 네비게이션 바 스타일 */
    .navbar {
        position: fixed;
        top: 0;
        width: 100%;
        background-color: #333;
        color: white;
        padding: 10px;
        text-align: center;
        z-index: 1000; /* 컨텐츠 위로 네비게이션 바를 고정합니다 */
    }

    .navbar a {
        color: white;
        text-decoration: none;
        padding: 14px 20px;
        display: inline-block;
    }

    .navbar a:hover {
        background-color: #555;
    }

    /* 메뉴바 아래 컨텐츠가 네비게이션 바 아래로 내려오게 하기 위한 마진 */
    .content {
        margin-top: 60px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the navbar
st.markdown(
    """
    <div class="navbar">
        <a href="#section1">Home</a>
        <a href="#section2">About</a>
        <a href="#section3">Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Content sections
st.markdown('<div class="content">', unsafe_allow_html=True)
st.header("Section 1: Home")
st.write("Welcome to the home section.")

st.header("Section 2: About")
st.write("This is the about section.")

st.header("Section 3: Contact")
st.write("Feel free to contact us.")
st.markdown('</div>', unsafe_allow_html=True)