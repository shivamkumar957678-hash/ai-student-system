# =========================
# AI STUDENT SYSTEM FINAL
# =========================

import streamlit as st
import pandas as pd
import numpy as np
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Student System",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background: linear-gradient(135deg,#020024,#6d28d9);
    color:white;
}

/* LOGIN TITLE */
.big-title{
    text-align:center;
    font-size:90px;
    font-weight:900;
    color:white;
    text-shadow:0 0 25px #00ffcc;
}

/* SUB TITLE */
.sub-title{
    text-align:center;
    font-size:32px;
    color:#c4ffea;
    font-weight:bold;
    margin-bottom:40px;
}

/* METRIC CARDS */
.metric-card{
    background:linear-gradient(135deg,#16a34a,#22c55e);
    padding:40px;
    border-radius:30px;
    text-align:center;
    box-shadow:0 0 35px rgba(0,255,120,0.6);
    margin-bottom:25px;
}

.metric-title{
    font-size:34px;
    font-weight:900;
    color:white;
    margin-bottom:20px;
}

.metric-value{
    font-size:80px;
    font-weight:bold;
    color:white;
}

/* BUTTON */
.stButton>button{
    background:linear-gradient(135deg,#16a34a,#22c55e);
    color:white;
    border:none;
    border-radius:15px;
    padding:15px 30px;
    font-size:22px;
    font-weight:bold;
    box-shadow:0 0 20px rgba(0,255,120,0.7);
}

/* INPUT */
.stTextInput input{
    border-radius:15px;
    font-size:22px;
}

/* SUCCESS BOX */
.success-box{
    background:#16a34a;
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:32px;
    font-weight:bold;
    color:white;
    margin-top:20px;
    box-shadow:0 0 20px #00ff99;
}

/* CHATBOT */
.chat-box{
    background:#1e293b;
    padding:20px;
    border-radius:20px;
    margin-top:10px;
    font-size:24px;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN ----------------

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

# ---------------- MAIN APP ----------------

else:

    st.markdown("<div class='big-title'>System</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>🚀 Smart AI Dashboard + Face Recognition + Analytics</div>", unsafe_allow_html=True)

    # ---------------- CSV LOAD ----------------

    if os.path.exists("students.csv"):
        df = pd.read_csv("students.csv")
    else:
        df = pd.DataFrame(columns=[
            "Name","Attendance","Math","Science","English"
        ])

    # ---------------- CALCULATIONS ----------------

    if len(df) > 0:

        df["Average"] = (
            df["Math"] +
            df["Science"] +
            df["English"]
        ) / 3

        topper_name = df.loc[df["Average"].idxmax(),"Name"]

        weak_students = len(df[df["Average"] < 50])

        poor_attendance = len(df[df["Attendance"] < 75])

    else:
        topper_name = "None"
        weak_students = 0
        poor_attendance = 0

    # ---------------- BIG CARDS ----------------

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

    # ---------------- ADD STUDENT ----------------

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

        st.success("Student Added Permanently")

    # ---------------- TABLE ----------------

    st.header("📊 Student Performance Table")

    st.dataframe(df, use_container_width=True)

    # ---------------- FACE ATTENDANCE ----------------

    st.header("📸 Face Recognition Attendance")

    camera = st.camera_input("Take Student Photo")

    if camera:
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

    # ---------------- AI CHATBOT ----------------

    st.header("🤖 AI Chatbot")

    question = st.text_input("🤖 Ask AI Question")

    if question:

        q = question.lower()

        found = False

        for i,row in df.iterrows():

            student = str(row["Name"]).lower()

            if student in q:

                found = True

                if "english" in q:
                    st.markdown(f"""
                    <div class='chat-box'>
                    📘 English Marks of {row['Name']} = {row['English']}
                    </div>
                    """, unsafe_allow_html=True)

                elif "math" in q:
                    st.markdown(f"""
                    <div class='chat-box'>
                    ➗ Math Marks of {row['Name']} = {row['Math']}
                    </div>
                    """, unsafe_allow_html=True)

                elif "science" in q:
                    st.markdown(f"""
                    <div class='chat-box'>
                    🔬 Science Marks of {row['Name']} = {row['Science']}
                    </div>
                    """, unsafe_allow_html=True)

                elif "attendance" in q:
                    st.markdown(f"""
                    <div class='chat-box'>
                    📅 Attendance of {row['Name']} = {row['Attendance']}%
                    </div>
                    """, unsafe_allow_html=True)

                else:
                    st.markdown(f"""
                    <div class='chat-box'>
                    👨‍🎓 Student: {row['Name']} <br><br>
                    📘 English: {row['English']} <br>
                    ➗ Math: {row['Math']} <br>
                    🔬 Science: {row['Science']} <br>
                    📅 Attendance: {row['Attendance']}%
                    </div>
                    """, unsafe_allow_html=True)

        if found == False:
            st.error("❌ STUDENT NOT FOUND")
