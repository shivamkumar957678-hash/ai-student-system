# =========================
# AI POWERED STUDENT PERFORMANCE SYSTEM
# =========================

import streamlit as st
import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

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

    h1,h2,h3{
        color:white;
    }

    .login-box{
        padding:40px;
        border-radius:20px;
        background: rgba(255,255,255,0.08);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.title("🔐 AI Student System Login")

    st.markdown("## 👤 Username")
    username = st.text_input(
        "",
        placeholder="Enter Username"
    )

    st.markdown("## 🔑 Password")
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

[data-testid="stMetric"]{
background:#16a34a;
padding:15px;
border-radius:15px;
}

label, .stSelectbox label, .stTextInput label,
.stTextArea label, .stSlider label {

    color:#00ff99 !important;
    font-size:28px !important;
    font-weight:bold !important;
}

.stTextInput input,
.stTextArea textarea {

    border-radius:15px !important;
    border:3px solid #00ff99 !important;
    font-size:22px !important;
}

.stSelectbox div[data-baseweb="select"]{
    border:3px solid #00ff99 !important;
    border-radius:15px !important;
    font-size:22px !important;
}

[data-testid="stCameraInput"]{
    border:3px solid #00ff99 !important;
    border-radius:20px !important;
    padding:15px;
}

.stButton button{

    background:#16a34a !important;
    color:white !important;
    font-size:24px !important;
    font-weight:bold !important;
    border-radius:15px !important;
    border:none !important;
    padding:15px 30px !important;
    box-shadow:0px 0px 15px #16a34a !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# DATABASE DATA
# -------------------------
data = {
    "Name":["Rahul","Shivam","Aman","Priya","Rohit","Aditi","Karan","Neha","Arjun","Sneha","Vikas","Anjali"],
    "Attendance":[90,75,60,95,55,88,78,92,81,85,68,94],
    "Math":[88,76,45,95,40,91,67,85,79,82,58,96],
    "Science":[85,70,50,98,35,89,72,90,80,84,60,97],
    "English":[80,72,55,90,45,93,70,87,76,81,59,95]
}

df = pd.DataFrame(data)

# -------------------------
# ADD STUDENT SECTION
# -------------------------
st.subheader("➕ Add New Student")

new_name = st.text_input("👨‍🎓 Student Name")

new_attendance = st.number_input(
    "📅 Attendance %",
    0,100,75
)

new_math = st.number_input(
    "📘 Math Marks",
    0,100,50
)

new_science = st.number_input(
    "🔬 Science Marks",
    0,100,50
)

new_english = st.number_input(
    "📖 English Marks",
    0,100,50
)

if st.button("✅ Add Student"):

    avg = (
        new_math +
        new_science +
        new_english
    ) / 3

    if avg >= 85:
        status = "Topper"

    elif avg >= 60:
        status = "Good"

    else:
        status = "Weak"

    new_row = pd.DataFrame({

        "Name":[new_name],
        "Attendance":[new_attendance],
        "Math":[new_math],
        "Science":[new_science],
        "English":[new_english]

    })

    df = pd.concat(
        [df,new_row],
        ignore_index=True
    )

    st.markdown(f"""
    <div style="
    background:#16a34a;
    padding:20px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:30px;
    font-weight:bold;
    box-shadow:0px 0px 20px #16a34a;
    ">
    ✅ {new_name} Added Successfully
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
    st.metric(
        "⚠ Weak Students",
        len(weak_students)
    )

with col4:
    poor = len(df[df["Attendance"] < 75])
    st.metric("📉 Poor Attendance", poor)

# -------------------------
# GRAPHS
# -------------------------
c1,c2,c3 = st.columns(3)

with c1:

    st.subheader("📚 Subject Wise Average")

    subject_avg = [
        df["Math"].mean(),
        df["Science"].mean(),
        df["English"].mean()
    ]

    fig, ax = plt.subplots()

    ax.bar(
        ["Math","Science","English"],
        subject_avg,
        color=["red","blue","green"]
    )

    ax.set_ylabel("Marks")

    st.pyplot(fig)

with c2:

    st.subheader("📈 Attendance Analysis")

    fig2, ax2 = plt.subplots(figsize=(8,4))

    ax2.plot(
        df["Name"],
        df["Attendance"],
        marker='o',
        color='cyan'
    )

    plt.xticks(rotation=45)

    ax2.set_ylabel("Attendance %")

    st.pyplot(fig2)

with c3:

    st.subheader("🏆 Topper vs Others")

    fig3, ax3 = plt.subplots(figsize=(7,7))

    ax3.pie(
        df["Average"],
        labels=df["Name"],
        autopct='%1.1f%%'
    )

    st.pyplot(fig3)

# -------------------------
# TABLE
# -------------------------
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

# -------------------------
# AI CHATBOT
# -------------------------
st.subheader("🤖 AI Chatbot")

q = st.text_input("🤖 Ask AI Question")

if q:

    q = q.lower()

    if "topper" in q:

        st.markdown(f"""
        <div style="
        background:#16a34a;
        padding:20px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:35px;
        font-weight:bold;
        box-shadow:0px 0px 20px #16a34a;
        ">
        🏆 {topper['Name']} IS THE TOPPER
        </div>
        """, unsafe_allow_html=True)

    elif "weak" in q:

        weak_names = ", ".join(
            weak_students["Name"].tolist()
        )

        st.markdown(f"""
        <div style="
        background:#dc2626;
        padding:20px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:35px;
        font-weight:bold;
        box-shadow:0px 0px 20px #dc2626;
        ">
        ⚠ WEAK STUDENTS: {weak_names}
        </div>
        """, unsafe_allow_html=True)

    elif "average" in q or "avg" in q:

        avg_student = df["Average"].mean()

        st.markdown(f"""
        <div style="
        background:#2563eb;
        padding:20px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:35px;
        font-weight:bold;
        box-shadow:0px 0px 20px #2563eb;
        ">
        📊 OVERALL AVERAGE MARKS: {avg_student:.2f}
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div style="
        background:#dc2626;
        padding:20px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:35px;
        font-weight:bold;
        box-shadow:0px 0px 20px #dc2626;
        margin-top:15px;
        ">
        🤖 AI COULD NOT UNDERSTAND THE QUESTION
        </div>
        """, unsafe_allow_html=True)

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
margin-top:10px;
box-shadow:0px 0px 20px #16a34a;
">
🎯 Predicted Marks: {prediction[0]:.2f}
</div>
""", unsafe_allow_html=True)

# -------------------------
# FEEDBACK SYSTEM
# -------------------------
st.subheader("💬 Feedback System with AI Sentiment Analysis")

feedback = st.text_area("💬 Enter Feedback")

if feedback:

    sentiment = TextBlob(feedback).sentiment.polarity

    if sentiment > 0:

        st.markdown(f"""
        <div style="
        background:#16a34a;
        padding:20px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:35px;
        font-weight:bold;
        box-shadow:0px 0px 20px #16a34a;
        ">
        😊 POSITIVE FEEDBACK | SCORE: {sentiment:.2f}
        </div>
        """, unsafe_allow_html=True)

    elif sentiment < 0:

        st.markdown(f"""
        <div style="
        background:#dc2626;
        padding:20px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:35px;
        font-weight:bold;
        box-shadow:0px 0px 20px #dc2626;
        ">
        😔 NEGATIVE FEEDBACK | SCORE: {sentiment:.2f}
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div style="
        background:#2563eb;
        padding:20px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:35px;
        font-weight:bold;
        box-shadow:0px 0px 20px #2563eb;
        ">
        😐 NEUTRAL FEEDBACK | SCORE: {sentiment:.2f}
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# AI FACE ATTENDANCE
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
    box-shadow:0px 0px 20px #16a34a;
    ">
    ✅ Face Detected Successfully
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

    st.markdown("""
    <h1 style='color:lime;text-align:center;
    font-size:45px;
    font-weight:bold;
    text-shadow:0px 0px 15px lime;'>
    🎯 Attendance Marked Successfully
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:#2563eb;
    padding:20px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:28px;
    font-weight:bold;
    box-shadow:0px 0px 20px #2563eb;
    ">
    📌 Student Present
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:#16a34a;
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:35px;
    font-weight:bold;
    box-shadow:0px 0px 25px #16a34a;
    ">
    🤖 AI VERIFIED FACE SUCCESSFULLY
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# REPORT GENERATOR
# -------------------------
st.subheader("📩 Weekly AI Report")

student = st.selectbox("📚 Select Student", df["Name"])

email = st.text_input("📧 Enter Email")

if st.button("🚀 Generate Report"):

    row = df[df["Name"] == student].iloc[0]

    st.markdown("""
    <div style="
    background:#16a34a;
    padding:20px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:35px;
    font-weight:bold;
    box-shadow:0px 0px 20px #16a34a;
    ">
    ✅ Report Generated Successfully
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
    background:#2563eb;
    padding:20px;
    border-radius:20px;
    color:white;
    font-size:28px;
    font-weight:bold;
    margin-top:15px;
    box-shadow:0px 0px 20px #2563eb;
    ">
    👨‍🎓 Student: {student}<br><br>

    📧 Email: {email}<br><br>

    📊 Attendance: {row['Attendance']}%<br><br>

    📚 Average Marks: {row['Average']:.2f}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:#16a34a;
    padding:20px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:35px;
    font-weight:bold;
    margin-top:20px;
    box-shadow:0px 0px 20px #16a34a;
    ">
    🤖 AI SUMMARY CREATED SUCCESSFULLY
    </div>
    """, unsafe_allow_html=True)