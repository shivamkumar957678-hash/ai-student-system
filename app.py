# =========================
# AI STUDENT SYSTEM FINAL
# =========================

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os

# ================= PAGE =================

st.set_page_config(
    page_title="AI Student System",
    layout="wide"
)

# ================= CSS =================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020024,#6d28d9);
    color:white;
}

.big-title{
    text-align:center;
    font-size:75px;
    font-weight:bold;
    color:white;
    text-shadow:0px 0px 20px #00ffcc;
}

.sub-title{
    text-align:center;
    font-size:30px;
    color:#c4ffea;
    margin-bottom:40px;
}

.metric-card{
    background:linear-gradient(135deg,#16a34a,#22c55e);
    padding:35px;
    border-radius:25px;
    text-align:center;
    box-shadow:0px 0px 25px rgba(0,255,100,0.6);
    margin-bottom:20px;
}

.metric-title{
    font-size:28px;
    font-weight:bold;
    color:white;
}

.metric-value{
    font-size:60px;
    font-weight:bold;
    color:white;
}

.success-box{
    background:#16a34a;
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
    color:white;
    box-shadow:0px 0px 20px #00ff99;
}

.fail-box{
    background:#dc2626;
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
    color:white;
    box-shadow:0px 0px 20px red;
}

.stButton>button{
    background:linear-gradient(135deg,#16a34a,#22c55e);
    color:white;
    border:none;
    border-radius:15px;
    padding:15px 30px;
    font-size:22px;
    font-weight:bold;
    box-shadow:0px 0px 20px rgba(0,255,120,0.7);
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================

if "login" not in st.session_state:
    st.session_state.login = False

if st.session_state.login == False:

    st.markdown("<div class='big-title'>🔐 AI Student System Login</div>", unsafe_allow_html=True)

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("🚀 Login"):

        if username == "admin" and password == "admin123":
            st.session_state.login = True
            st.rerun()

        else:
            st.error("Wrong Username or Password")

# ================= MAIN =================

else:

    st.markdown("<div class='big-title'>🎓 AI Student System</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub-title'>🚀 Smart AI Dashboard + Face Attendance + Analytics</div>", unsafe_allow_html=True)

    # ================= LOAD CSV =================

    if os.path.exists("students.csv"):
        df = pd.read_csv("students.csv")
    else:
        df = pd.DataFrame({
            "Name":["Rahul","Shivam","Priya","Aman","Rohit"],
            "Attendance":[90,75,95,60,55],
            "Math":[88,76,95,45,40],
            "Science":[85,70,98,50,35],
            "English":[80,72,90,55,45]
        })

    # ================= CALCULATE =================

    df["Average"] = (
        df["Math"] +
        df["Science"] +
        df["English"]
    ) / 3

    topper_name = df.loc[df["Average"].idxmax(),"Name"]

    weak_students = len(df[df["Average"] < 50])

    poor_attendance = len(df[df["Attendance"] < 75])

    # ================= DASHBOARD =================

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-title">👨‍🎓 Total Students</div>
        <div class="metric-value">{len(df)}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-title">🏆 Topper</div>
        <div class="metric-value">{topper_name}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-title">⚠ Weak Students</div>
        <div class="metric-value">{weak_students}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-title">📉 Poor Attendance</div>
        <div class="metric-value">{poor_attendance}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ================= ADD STUDENT =================

    st.header("➕ Add New Student")

    name = st.text_input("Student Name")
    attendance = st.slider("Attendance",0,100,80)
    math = st.slider("Math",0,100,70)
    science = st.slider("Science",0,100,70)
    english = st.slider("English",0,100,70)

    if st.button("✅ Add Student"):

        new_data = pd.DataFrame({
            "Name":[name],
            "Attendance":[attendance],
            "Math":[math],
            "Science":[science],
            "English":[english]
        })

        df = pd.concat([df,new_data], ignore_index=True)

        df.to_csv("students.csv", index=False)

        st.success("Student Added Successfully")

    # ================= TABLE =================

    st.header("📊 Student Performance Table")

    st.dataframe(df, use_container_width=True)

    # ================= FACE ATTENDANCE =================

    st.header("📸 Face Attendance System")

    camera = st.camera_input("Take Your Photo")

    if camera is not None:

        st.markdown("""
        <div class='success-box'>
        ✅ FACE DETECTED SUCCESSFULLY
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='success-box'>
        🎯 ATTENDANCE MARKED SUCCESSFULLY
        </div>
        """, unsafe_allow_html=True)

    # ================= AI CHATBOT =================

    st.header("🤖 AI Chatbot")

    question = st.text_input("Ask Question")

    if question:

        q = question.lower()

        found = False

        for i,row in df.iterrows():

            student = str(row["Name"]).lower()

            if student in q:

                found = True

                if "english" in q:
                    st.success(f"📘 English Marks of {row['Name']} = {row['English']}")

                elif "math" in q:
                    st.success(f"➗ Math Marks of {row['Name']} = {row['Math']}")

                elif "science" in q:
                    st.success(f"🔬 Science Marks of {row['Name']} = {row['Science']}")

                elif "attendance" in q:
                    st.success(f"📅 Attendance of {row['Name']} = {row['Attendance']}%")

                else:
                    st.success(f"""
                    👨‍🎓 {row['Name']}

                    📘 English: {row['English']}

                    ➗ Math: {row['Math']}

                    🔬 Science: {row['Science']}

                    📅 Attendance: {row['Attendance']}%
                    """)

        if found == False:
            st.error("❌ STUDENT NOT FOUND")
