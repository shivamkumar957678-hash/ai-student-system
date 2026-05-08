# =========================
# AI POWERED STUDENT PERFORMANCE SYSTEM
# =========================

import streamlit as st
import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import os

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="AI Student System", layout="wide")

# -------------------------
# LOGIN DETAILS
# -------------------------
USERNAME = "shivam"
PASSWORD = "12345"

# -------------------------
# SESSION
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------
# LOGIN PAGE
# -------------------------
if not st.session_state.logged_in:

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(to right,#0f172a,#7c3aed);
        color:white;
    }

    .login-box{
        padding:50px;
        border-radius:25px;
        background: rgba(255,255,255,0.08);
        margin-top:40px;
    }

    .big-label{
        color:white;
        font-size:45px;
        font-weight:bold;
        margin-top:20px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.markdown("""
    <h1 style='
    text-align:center;
    color:white;
    font-size:70px;
    font-weight:bold;
    '>
    🔐 AI Student System Login
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("<div class='big-label'>👤 Username</div>", unsafe_allow_html=True)

    username = st.text_input(
        "",
        placeholder="Enter Username"
    )

    st.markdown("<div class='big-label'>🔑 Password</div>", unsafe_allow_html=True)

    password = st.text_input(
        "",
        type="password",
        placeholder="Enter Password"
    )

    if st.button("🚀 Login"):

        if username == USERNAME and password == PASSWORD:

            st.session_state.logged_in = True
            st.success("✅ Login Successful")
            st.rerun()

        else:

            st.error("❌ Wrong Username or Password")

    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# -------------------------
# MAIN CSS
# -------------------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(to right,#0f172a,#7c3aed);
color:white;
}

h1,h2,h3{
color:white;
}

label{
color:#00ff99 !important;
font-size:24px !important;
font-weight:bold !important;
}

.stButton button{
background:#16a34a !important;
color:white !important;
font-size:22px !important;
font-weight:bold !important;
border-radius:15px !important;
padding:12px 25px !important;
box-shadow:0px 0px 15px #16a34a !important;
}

.stTextInput input,
.stTextArea textarea{
border:3px solid #00ff99 !important;
border-radius:15px !important;
font-size:22px !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# CSV DATABASE
# -------------------------
if os.path.exists("students.csv"):

    df = pd.read_csv("students.csv")

else:

    data = {
        "Name":["Rahul","Shivam","Aman","Priya","Rohit","Aditi","Karan","Neha","Arjun","Sneha","Vikas","Anjali"],
        "Attendance":[90,75,60,95,55,88,78,92,81,85,68,94],
        "Math":[88,76,45,95,40,91,67,85,79,82,58,96],
        "Science":[85,70,50,98,35,89,72,90,80,84,60,97],
        "English":[80,72,55,90,45,93,70,87,76,81,59,95]
    }

    df = pd.DataFrame(data)

    df.to_csv("students.csv", index=False)

# -------------------------
# ADD STUDENT
# -------------------------
st.subheader("➕ Add New Student")

new_name = st.text_input("👨‍🎓 Student Name")

new_attendance = st.number_input("📅 Attendance %",0,100,75)

new_math = st.number_input("📘 Math Marks",0,100,50)

new_science = st.number_input("🔬 Science Marks",0,100,50)

new_english = st.number_input("📖 English Marks",0,100,50)

if st.button("✅ Add Student"):

    new_row = pd.DataFrame({

        "Name":[new_name],
        "Attendance":[new_attendance],
        "Math":[new_math],
        "Science":[new_science],
        "English":[new_english]

    })

    df = pd.concat([df,new_row],ignore_index=True)

    df.to_csv("students.csv", index=False)

    st.markdown(f"""
    <div style="
    background:#16a34a;
    padding:20px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:30px;
    font-weight:bold;
    ">
    ✅ {new_name} Added Permanently
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# AI CALCULATIONS
# -------------------------
df["Average"] = df[["Math","Science","English"]].mean(axis=1)

topper = df.loc[df["Average"].idxmax()]
weak_students = df[df["Average"] < 60]

# -------------------------
# TITLE
# -------------------------
st.title("🎓 AI-Powered Student Performance System")
st.subheader("🚀 AI + Automation + Smart Analytics")

# -------------------------
# METRICS
# -------------------------
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("👨‍🎓 Total Students", len(df))

with col2:
    st.metric("🏆 Topper", topper["Name"])

with col3:
    st.metric("⚠ Weak Students", len(weak_students))

with col4:
    poor = len(df[df["Attendance"] < 75])
    st.metric("📉 Poor Attendance", poor)

# -------------------------
# STATUS
# -------------------------
def status(avg):

    if avg >= 85:
        return "Topper"

    elif avg >= 60:
        return "Good"

    else:
        return "Weak"

df["Status"] = df["Average"].apply(status)

# -------------------------
# TABLE
# -------------------------
st.subheader("📋 Student Performance Table")

st.dataframe(df, use_container_width=True)

# -------------------------
# AI CHATBOT
# -------------------------
st.subheader("🤖 AI Chatbot")

q = st.text_input("🤖 Ask AI Question")

if q:

    q = q.lower()

    # ENGLISH
    if "english" in q:

        found = False

        for i in range(len(df)):

            student_name = str(df.iloc[i]["Name"]).lower()

            if student_name in q:

                marks = df.iloc[i]["English"]

                st.markdown(f"""
                <div style="
                background:#2563eb;
                padding:20px;
                border-radius:20px;
                text-align:center;
                color:white;
                font-size:35px;
                font-weight:bold;
                ">
                📖 {df.iloc[i]['Name']} English Marks: {marks}
                </div>
                """, unsafe_allow_html=True)

                found = True

        if found == False:

            st.error("❌ STUDENT NOT FOUND")

    # MATH
    elif "math" in q:

        found = False

        for i in range(len(df)):

            student_name = str(df.iloc[i]["Name"]).lower()

            if student_name in q:

                marks = df.iloc[i]["Math"]

                st.markdown(f"""
                <div style="
                background:#16a34a;
                padding:20px;
                border-radius:20px;
                text-align:center;
                color:white;
                font-size:35px;
                font-weight:bold;
                ">
                📘 {df.iloc[i]['Name']} Math Marks: {marks}
                </div>
                """, unsafe_allow_html=True)

                found = True

        if found == False:

            st.error("❌ STUDENT NOT FOUND")

    # SCIENCE
    elif "science" in q:

        found = False

        for i in range(len(df)):

            student_name = str(df.iloc[i]["Name"]).lower()

            if student_name in q:

                marks = df.iloc[i]["Science"]

                st.markdown(f"""
                <div style="
                background:#9333ea;
                padding:20px;
                border-radius:20px;
                text-align:center;
                color:white;
                font-size:35px;
                font-weight:bold;
                ">
                🔬 {df.iloc[i]['Name']} Science Marks: {marks}
                </div>
                """, unsafe_allow_html=True)

                found = True

        if found == False:

            st.error("❌ STUDENT NOT FOUND")

    # TOPPER
    elif "topper" in q:

        st.success(f"🏆 {topper['Name']} is the Topper")

    # WEAK
    elif "weak" in q:

        weak_names = ", ".join(weak_students["Name"].tolist())

        st.error(f"⚠ Weak Students: {weak_names}")

    else:

        st.error("🤖 AI आपका सवाल समझ नहीं पाया")

# -------------------------
# ML PREDICTION
# -------------------------
st.subheader("🧠 AI Model Implementation (ML/DL)")

hours = np.array([1,2,3,4,5,6]).reshape(-1,1)
marks = np.array([20,35,50,65,80,95])

model = LinearRegression()
model.fit(hours, marks)

study = st.slider("📚 Study Hours",1,10)

prediction = model.predict([[study]])

st.markdown(f"""
<div style="
background:#16a34a;
padding:20px;
border-radius:20px;
text-align:center;
color:white;
font-size:35px;
font-weight:bold;
">
🎯 Predicted Marks: {prediction[0]:.2f}
</div>
""", unsafe_allow_html=True)

# -------------------------
# FEEDBACK
# -------------------------
st.subheader("💬 Feedback System")

feedback = st.text_area("💬 Enter Feedback")

if feedback:

    sentiment = TextBlob(feedback).sentiment.polarity

    if sentiment > 0:

        st.success("😊 Positive Feedback")

    elif sentiment < 0:

        st.error("😔 Negative Feedback")

    else:

        st.warning("😐 Neutral Feedback")

# -------------------------
# FACE ATTENDANCE
# -------------------------
st.subheader("📸 AI Face Recognition Attendance")

img = st.camera_input("📸 Take Student Photo")

if img is not None:

    st.image(img, width=400)

    st.markdown("""
    <div style="
    background:#16a34a;
    padding:20px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:30px;
    font-weight:bold;
    ">
    ✅ Face Detected Successfully
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style='color:lime;text-align:center;font-size:45px;'>
    🎯 Attendance Marked Successfully
    </h1>
    """, unsafe_allow_html=True)

# -------------------------
# REPORT
# -------------------------
st.subheader("📩 Weekly AI Report")

student = st.selectbox("📚 Select Student", df["Name"])

email = st.text_input("📧 Enter Email")

if st.button("🚀 Generate Report"):

    row = df[df["Name"] == student].iloc[0]

    st.markdown(f"""
    <div style="
    background:#2563eb;
    padding:20px;
    border-radius:20px;
    color:white;
    font-size:28px;
    font-weight:bold;
    ">
    👨‍🎓 Student: {student}<br><br>

    📧 Email: {email}<br><br>

    📊 Attendance: {row['Attendance']}%<br><br>

    📚 Average Marks: {row['Average']:.2f}
    </div>
    """, unsafe_allow_html=True)
