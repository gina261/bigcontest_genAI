import os
import numpy as np
import pandas as pd

from transformers import AutoTokenizer, AutoModel
import torch
from tqdm import tqdm
# import faiss

import streamlit as st

# Gemini 설정
import google.generativeai as genai

st.set_page_config(page_title="🍊🍊🍊")

st.title("Hello Ybigta👋")
st.subheader("Ybigta Team DA's Bigcontest")