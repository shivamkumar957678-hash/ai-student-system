import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.set_page_config(page_title="AI Student System", layout="wide")

# ================= CSS =================
st.markdown("""
<style>

html, body, [class*="css"] {
    background: linear-gradient(135deg,#020024,#090979,#6a00ff);
    color: white;
}

/* Main Title */
.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#00e5ff;
    text-shadow:0px 0px 20px #00e5ff;
}

.sub-title{
    text-align:center;
    font-size:22px;
    color:white;
    margin-bottom:30px;
}

/* Cards */
.card{
    background: rgba(255,255,255,0.06);
    padding:20px;
    border-radius:20px;
    border:2px solid #ff00ff;
    box-shadow:0 0 20px #8a2be2;
}

/* Inputs */
.stTextInput label{
    color:white !important;
    font-size:18px !important;
    font-weight:bold;
}

.stTextInput input{
    background:white !important;
    color:black !important;
    border-radius:10px;
    padding:10px;
}

/* Buttons */
.stButton>button{
    width:100%;
    background: linear-gradient(90deg,#00c6ff,#8e2de2);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
}

/* Dashboard cards */
.dashboard-card{
    padding:20px;
    border-radius:18px;
    color:white;
    text-align:center;
    font-size:24px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("<div class='main-title'>🔐 AI STUDENT SYSTEM</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Smart • Secure • Intelligent</div>", unsafe_allow_html=True)

# ================= LOGIN =================
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("## 📸 Face Authentication")
    st.write("Login with your registered face")

    picture = st.camera_input("Capture Face")

    if picture:
        st.success("✅ Face matched successfully!")
        st.image(picture, width=300)

    if st.button("📷 Capture & Login"):
        st.success("Access Granted ✅")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("## 🔑 Manual Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("Login Successful ✅")
        else:
            st.error("Wrong Username or Password ❌")

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ================= DASHBOARD =================
st.markdown("## 📊 AI STUDENT SYSTEM DASHBOARD")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='dashboard-card' style='background:#0066ff;'>
    👨‍🎓<br>5<br>Total Students
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='dashboard-card' style='background:#00aa55;'>
    🏆<br>Priya<br>Topper
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='dashboard-card' style='background:#ff6600;'>
    ⚠️<br>2<br>Weak Students
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='dashboard-card' style='background:#9900cc;'>
    📉<br>2<br>Poor Attendance
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ================= STUDENT TABLE =================
data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Rohit"],
    "Attendance": [90, 95, 60, 85, 55],
    "Math": [88, 98, 45, 82, 40],
    "Science": [90, 99, 50, 84, 35],
    "English": [85, 97, 55, 81, 45]
}

df = pd.DataFrame(data)

df["Average"] = round(
    (df["Math"] + df["Science"] + df["English"]) / 3, 2
)

st.markdown("## 📋 Student Performance Table")
st.dataframe(df, use_container_width=True)

# ================= CHART =================
st.markdown("## 📈 Attendance Graph")
st.bar_chart(df.set_index("Name")["Attendance"])

# ================= CHATBOT =================
st.markdown("## 🤖 AI Chatbot")

question = st.text_input("Ask any question about students")

if st.button("Ask"):
    st.success("AI Response: Student performance is improving steadily 🚀")

# ================= PREDICTION =================
st.markdown("## 🎯 AI Study Prediction")

hours = st.slider("Study Hours Per Day", 1, 10, 5)

predicted = hours * 10

st.info(f"Predicted Marks: {predicted}/100")

# ================= FEEDBACK =================
st.markdown("## 💬 Feedback System")

feedback = st.text_area("Enter your feedback")

if st.button("Submit Feedback"):
    st.success("Feedback Submitted Successfully ✅")

# ================= FOOTER =================
st.markdown("""
<hr>
<center>
<h4>© 2025 AI Student System | Made with ❤️ by Shivam Kumar</h4>
</center>
""", unsafe_allow_html=True)
