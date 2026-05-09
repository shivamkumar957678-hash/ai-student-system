import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import os

# ================= PAGE =================
st.set_page_config(page_title="Ultimate AI Student System", layout="wide")

# ================= THEME =================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

if st.session_state.theme == "dark":
    bg = "linear-gradient(135deg,#000814,#140152,#3a0ca3)"
    card = "#050816"
    text = "white"
else:
    bg = "linear-gradient(135deg,#f1f5ff,#dbeafe,#e0e7ff)"
    card = "white"
    text = "black"

# ================= CSS =================
st.markdown(f"""
<style>
.stApp{{
background:{bg};
color:{text};
}}

.main-title{{
text-align:center;
font-size:60px;
font-weight:bold;
color:#00e5ff;
text-shadow:0 0 20px #00e5ff;
}}

.sub-title{{
text-align:center;
font-size:24px;
margin-bottom:25px;
}}

.neon-box{{
background:{card};
padding:20px;
border-radius:20px;
border:2px solid #bb00ff;
box-shadow:0 0 20px #bb00ff;
margin-bottom:20px;
}}

.metric-card{{
padding:20px;
""", unsafe_allow_html=True)
