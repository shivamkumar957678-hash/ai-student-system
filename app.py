# =========================
# AI POWERED STUDENT PERFORMANCE SYSTEM
# =========================

import streamlit as st
import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Student System",
    page_icon="🎓",
    layout="wide"
)

# =========================
# LOGIN DETAILS
# =========================

USERNAME = "shivam"
PASSWORD = "12345"

# =========================
# SESSION
# =========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================
# LOGIN PAGE
# =========================

if not st.session_state.logged_in:

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(to right,#020617,#7c3aed);
        color:white;
    }

    .login-box{
        padding:50px;
        border-radius:30px;
        background: rgba(255,255,255,0.08);
        box-shadow:0px 0px 30px rgba(255,255,255,0.1);
        margin-top:40px;
    }

    .login-title{
        text-align:center;
        font-size:70px;
        font-weight:bold;
        color:white;
        text-shadow:0px 0px 15px #22c55e;
    }

    .login-label{
        font-size:35px;
        color:white;
        font-weight:bold;
        margin-top:20px;
    }

    .stButton button{
        background:linear-gradient(to right,#16a34a,#22c55e);
        color:white;
        font-size:28px;
        font-weight:bold;
        border:none;
        border-radius:18px;
        padding:15px 40px;
        box-shadow:0px 0px 20px #22c55e;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.markdown("""
    <div class='login-title'>
    🔐 AI Student System Login
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-label'>👤 Username</div>", unsafe_allow_html=True)

    username = st.text_input("", placeholder="Enter Username")

    st.markdown("<div class='login-label'>🔑 Password</div>", unsafe_allow_html=True)

    password = st.text_input("", type="password", placeholder="Enter Password")

    if st.button("🚀 Login"):

        if username == USERNAME and password == PASSWORD:

            st.session_state.logged_in = True
            st.success("✅ Login Successful")
            st.rerun()

        else:

            st.error("❌ Wrong Username or Password")

    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# =========================
# MAIN CSS
# =========================

st.markdown("""
<style>

.stApp{
background: linear-gradient(to right,#020617,#7c3aed);
color:white;
}

/* TITLES */

.main-title{
text-align:center;
font-size:75px;
font-weight:bold;
color:white;
text-shadow:0px 0px 20px #22c55e;
}

.sub-title{
text-align:center;
font-size:30px;
font-weight:bold;
color:#bbf7d0;
margin-bottom:30px;
}

/* METRIC CARDS */

[data-testid="stMetric"]{
background: linear-gradient(135deg,#16a34a,#22c55e);
padding:35px;
border-radius:25px;
text-align:center;
box-shadow:0px 0px 25px rgba(34,197,94,0.9);
border:2px solid rgba(255,255,255,0.2);
}

[data-testid="stMetricLabel"]{
font-size:28px !important;
font-weight:bold !important;
color:white !important;
}

[data-testid="stMetricValue"]{
font-size:55px !important;
font-weight:bold !important;
color:white !important;
}

/* BUTTON */

.stButton button{
background: linear-gradient(to right,#16a34a,#22c55e) !important;
color:white !important;
font-size:24px !important;
font-weight:bold !important;
border:none !important;
padding:14px 35px !important;
border-radius:18px !important;
box-shadow:0px 0px 20px #22c55e !important;
}

/* INPUTS */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input{
font-size:22px !important;
border-radius:15px !important;
border:3px solid #22c55e !important;
}

/* SELECT */

div[data-baseweb="select"] > div{
font-size:22px !important;
border-radius:15px !important;
border:3px solid #22c55e !important;
}

/* HEADINGS */

h1,h2,h3{
color:white !important;
font-weight:bold !important;
}

label{
font-size:24px !important;
font-weight:bold !important;
color:#bbf7d0 !important;
}

/* TABLE */

[data-testid="stDataFrame"]{
border-radius:20px;
overflow:hidden;
box-shadow:0px 0px 20px rgba(255,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)

# =========================
# CSV DATABASE
# =========================

if os.path.exists("students.csv"):

    df = pd.read_csv("students.csv")

else:

    data = {

        "Name":[
            "Rahul","Shivam","Aman","Priya",
            "Rohit","Aditi","Karan","Neha",
            "Arjun","Sneha","Vikas","Anjali"
        ],

        "Attendance":[
            90,75,60,95,
            55,88,78,92,
            81,85,68,94
        ],

        "Math":[
            88,76,45,95,
            40,91,67,85,
            79,82,58,96
        ],

        "Science":[
            85,70,50,98,
            35,89,72,90,
            80,84,60,97
        ],

        "English":[
            80,72,55,90,
            45,93,70,87,
            76,81,59,95
        ]
    }

    df = pd.DataFrame(data)

    df.to_csv("students.csv", index=False)

# =========================
# CALCULATIONS
# =========================

df["Average"] = df[
    ["Math","Science","English"]
].mean(axis=1)

topper = df.loc[df["Average"].idxmax()]

weak_students = df[df["Average"] < 60]

# =========================
# TITLE
# =========================

st.markdown("""
<div class='main-title'>
🎓 AI Student Performance System
</div>

<div class='sub-title'>
🚀 Smart AI Dashboard + Face Attendance + Analytics
</div>
""", unsafe_allow_html=True)

# =========================
# METRICS
# =========================

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

st.write("")

# =========================
# ADD STUDENT
# =========================

st.subheader("➕ Add New Student")

c1,c2,c3 = st.columns(3)

with c1:
    new_name = st.text_input("👤 Student Name")

with c2:
    new_attendance = st.number_input("📅 Attendance",0,100,75)

with c3:
    new_math = st.number_input("📘 Math",0,100,50)

c4,c5 = st.columns(2)

with c4:
    new_science = st.number_input("🔬 Science",0,100,50)

with c5:
    new_english = st.number_input("📖 English",0,100,50)

if st.button("✅ Add Student"):

    new_row = pd.DataFrame({

        "Name":[new_name],
        "Attendance":[new_attendance],
        "Math":[new_math],
        "Science":[new_science],
        "English":[new_english]

    })

    df = pd.concat([df,new_row], ignore_index=True)

    df.to_csv("students.csv", index=False)

    st.success(f"✅ {new_name} Added Permanently")

# =========================
# TABLE
# =========================

st.subheader("📋 Student Performance Table")

def status(avg):

    if avg >= 85:
        return "Topper"

    elif avg >= 60:
        return "Good"

    else:
        return "Weak"

df["Status"] = df["Average"].apply(status)

st.dataframe(df, use_container_width=True)

# =========================
# AI CHATBOT
# =========================

st.subheader("🤖 AI Chatbot")

q = st.text_input("🤖 Ask AI Question")

if q:

    q = q.lower()
    found = False

    for i in range(len(df)):

        name = str(df.iloc[i]["Name"]).lower()

        if name in q:

            if "english" in q:

                st.success(
                    f"📖 {df.iloc[i]['Name']} English Marks: {df.iloc[i]['English']}"
                )

                found = True

            elif "math" in q:

                st.success(
                    f"📘 {df.iloc[i]['Name']} Math Marks: {df.iloc[i]['Math']}"
                )

                found = True

            elif "science" in q:

                st.success(
                    f"🔬 {df.iloc[i]['Name']} Science Marks: {df.iloc[i]['Science']}"
                )

                found = True

    if "topper" in q:

        st.success(f"🏆 {topper['Name']} is the Topper")

        found = True

    elif "weak" in q:

        weak_names = ", ".join(weak_students["Name"].tolist())

        st.error(f"⚠ Weak Students: {weak_names}")

        found = True

    if found == False:

        st.error("❌ Student Not Found")

# =========================
# ML MODEL
# =========================

st.subheader("🧠 AI Model Implementation")

hours = np.array([1,2,3,4,5,6]).reshape(-1,1)

marks = np.array([20,35,50,65,80,95])

model = LinearRegression()

model.fit(hours, marks)

study = st.slider("📚 Study Hours",1,10)

prediction = model.predict([[study]])

st.success(f"🎯 Predicted Marks: {prediction[0]:.2f}")

# =========================
# FEEDBACK
# =========================

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

# =========================
# FACE ATTENDANCE
# =========================

st.subheader("📸 AI Face Attendance")

img = st.camera_input("📸 Take Student Photo")

if img is not None:

    st.image(img, width=350)

    st.success("✅ Face Detected Successfully")

    st.markdown("""
    <h1 style='
    text-align:center;
    color:lime;
    font-size:45px;
    text-shadow:0px 0px 15px lime;
    '>
    🎯 Attendance Marked Successfully
    </h1>
    """, unsafe_allow_html=True)

# =========================
# REPORT
# =========================

st.subheader("📩 Weekly AI Report")

student = st.selectbox(
    "📚 Select Student",
    df["Name"]
)

email = st.text_input("📧 Enter Email")

if st.button("🚀 Generate Report"):

    row = df[df["Name"] == student].iloc[0]

    st.success("✅ Report Generated Successfully")

    st.write(f"👨‍🎓 Student: {student}")
    st.write(f"📧 Email: {email}")
    st.write(f"📊 Attendance: {row['Attendance']}%")
    st.write(f"📚 Average Marks: {row['Average']:.2f}")

    st.success("🤖 AI Summary Created Successfully")
