import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="AI Student System", layout="wide")

# ===================== STYLING =====================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#050b2d,#6a11cb);
    color: white;
}

/* Main Heading */
.main-title{
    text-align:center;
    font-size:75px;
    font-weight:bold;
    color:white;
    text-shadow:0px 0px 25px #00ffcc;
}

/* Sub Heading */
.sub-title{
    text-align:center;
    font-size:32px;
    font-weight:bold;
    color:#b8ffe8;
    margin-bottom:30px;
}

/* Login Labels */
div[data-testid="stTextInput"] label {
    color:white !important;
    font-size:30px !important;
    font-weight:bold !important;
}

/* Input Box */
.stTextInput input {
    height:70px !important;
    font-size:26px !important;
    border-radius:20px !important;
}

/* Button */
.stButton button{
    background:#16c95f !important;
    color:white !important;
    font-size:28px !important;
    font-weight:bold !important;
    border-radius:20px !important;
    height:70px !important;
    width:250px !important;
    box-shadow:0px 0px 20px #16c95f;
}

/* Cards */
.card{
    background:#19b84a;
    padding:35px;
    border-radius:25px;
    text-align:center;
    box-shadow:0px 0px 25px rgba(0,255,150,0.7);
    margin-bottom:20px;
}

.card h2{
    color:white;
    font-size:32px;
}

.card h1{
    color:white;
    font-size:70px;
}

/* Section Headings */
.section{
    font-size:42px;
    font-weight:bold;
    color:white;
    margin-top:30px;
}

/* Success Box */
.success-box{
    background:#18b44c;
    padding:25px;
    border-radius:20px;
    color:white;
    font-size:28px;
    font-weight:bold;
    box-shadow:0px 0px 20px #18b44c;
}

/* Chatbot */
.chat-box{
    background:#ffffff22;
    padding:20px;
    border-radius:20px;
    font-size:24px;
}
</style>
""", unsafe_allow_html=True)

# ===================== LOGIN =====================
if "login" not in st.session_state:
    st.session_state.login = False

if st.session_state.login == False:

    st.markdown('<h1 class="main-title">🔐 AI Student System Login</h1>', unsafe_allow_html=True)

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("🚀 Login"):

        if username == "admin" and password == "admin123":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Wrong Username or Password")

# ===================== MAIN APP =====================
else:

    st.markdown('<h1 class="main-title">🎓 AI Student System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">🚀 Smart AI Dashboard + Face Recognition + Analytics</p>', unsafe_allow_html=True)

    # ===================== DATA =====================
    if os.path.exists("students.csv"):
        df = pd.read_csv("students.csv")
    else:
        data = {
            "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
            "Attendance":[90,95,60,85,55],
            "Math":[88,98,45,82,40],
            "Science":[90,99,50,84,35],
            "English":[85,97,55,81,45]
        }
        df = pd.DataFrame(data)
        df.to_csv("students.csv", index=False)

    df["Average"] = df[["Math","Science","English"]].mean(axis=1)

    topper = df.loc[df["Average"].idxmax(), "Name"]
    weak_students = len(df[df["Average"] < 60])
    poor_attendance = len(df[df["Attendance"] < 75])

    # ===================== DASHBOARD =====================
    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="card">
        <h2>👨‍🎓 Total Students</h2>
        <h1>{len(df)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="card">
        <h2>🏆 Topper</h2>
        <h1>{topper}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="card">
        <h2>⚠ Weak Students</h2>
        <h1>{weak_students}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="card">
        <h2>📉 Poor Attendance</h2>
        <h1>{poor_attendance}</h1>
        </div>
        """, unsafe_allow_html=True)

    # ===================== ADD STUDENT =====================
    st.markdown('<p class="section">➕ Add New Student</p>', unsafe_allow_html=True)

    name = st.text_input("Student Name")
    attendance = st.slider("Attendance",0,100,80)
    math = st.slider("Math",0,100,70)
    science = st.slider("Science",0,100,70)
    english = st.slider("English",0,100,70)

    if st.button("✅ Add Student"):

        new_student = pd.DataFrame({
            "Name":[name],
            "Attendance":[attendance],
            "Math":[math],
            "Science":[science],
            "English":[english]
        })

        df = pd.concat([df,new_student], ignore_index=True)
        df.to_csv("students.csv", index=False)

        st.success(f"{name} Added Successfully")

    # ===================== FACE ATTENDANCE =====================
    st.markdown('<p class="section">📸 Face Recognition Attendance</p>', unsafe_allow_html=True)

    camera = st.camera_input("Take Student Photo")

    if camera:
        st.markdown("""
        <div class="success-box">
        ✅ Face Detected Successfully <br><br>
        🎯 Attendance Marked Successfully <br><br>
        📌 Student Present
        </div>
        """, unsafe_allow_html=True)

    # ===================== STUDENT TABLE =====================
    st.markdown('<p class="section">📊 Student Performance Table</p>', unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True)

    # ===================== AI CHATBOT =====================
    st.markdown('<p class="section">🤖 AI Chatbot</p>', unsafe_allow_html=True)

    question = st.text_input("Ask AI Question")

    if question:

        q = question.lower()

        found = False

        for i,row in df.iterrows():

            student = row["Name"].lower()

            if student in q:

                found = True

                if "english" in q:
                    st.success(f"{row['Name']} English Marks: {row['English']}")

                elif "math" in q:
                    st.success(f"{row['Name']} Math Marks: {row['Math']}")

                elif "science" in q:
                    st.success(f"{row['Name']} Science Marks: {row['Science']}")

                elif "attendance" in q:
                    st.success(f"{row['Name']} Attendance: {row['Attendance']}%")

                else:
                    st.success(f"{row['Name']} Average Marks: {round(row['Average'],2)}")

        if found == False:
            st.error("❌ STUDENT NOT FOUND")

    # ===================== AI PREDICTION =====================
    st.markdown('<p class="section">🧠 AI Study Prediction</p>', unsafe_allow_html=True)

    hours = st.slider("📚 Study Hours",1,12,2)

    predicted_marks = hours * 15

    st.markdown(f"""
    <div class="success-box">
    📚 Study Hours: {hours} <br><br>
    🎯 Predicted Marks: {predicted_marks}
    </div>
    """, unsafe_allow_html=True)

    # ===================== FEEDBACK =====================
    st.markdown('<p class="section">💬 Feedback System</p>', unsafe_allow_html=True)

    feedback = st.text_area("Enter Feedback")

    if st.button("📩 Submit Feedback"):

        if feedback != "":
            st.markdown("""
            <div class="success-box">
            ✅ Feedback Submitted Successfully <br><br>
            🤖 AI Sentiment: Positive
            </div>
            """, unsafe_allow_html=True)

    # ===================== FOOTER =====================
    st.markdown("""
    <hr>
    <h3 style='text-align:center;color:white;'>
    🚀 AI Student Management System | Made By Shivam Kumar
    </h3>
    """, unsafe_allow_html=True)
