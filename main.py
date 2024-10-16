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

st.set_page_config(page_title="🍊🍊🍊")

st.title("Hello Ybigta👋")
st.subheader("Ybigta Team DA's Bigcontest")

# Custom CSS style for changing the font
st.markdown(
    """
    <style>
    .custom-title {
        font-family: 'Courier New', monospace;
        font-size: 48px;
        color: #2E86C1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Using HTML directly to apply the custom style to the title
st.markdown('<h1 class="custom-title">Hello, Streamlit!</h1>', unsafe_allow_html=True)