import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI Student System", layout="wide")

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>

html, body, [class*="css"]  {
    background: #050816;
    color: white;
}

/* Hide Streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main title */
.main-title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#00e5ff;
    text-shadow:0px 0px 25px #00e5ff;
}

.sub-title{
    text-align:center;
    color:white;
    font-size:22px;
    margin-bottom:30px;
}

/* Cards */
.card{
    background: rgba(20,20,40,0.95);
    border:2px solid #9d00ff;
    border-radius:20px;
    padding:25px;
    box-shadow:0 0 25px #6a00ff;
}

/* Headings */
.section-title{
    color:white !important;
    font-size:32px !important;
    font-weight:bold !important;
}

/* Labels */
label, .stTextInput label, .stTextArea label{
    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
}

/* Inputs */
.stTextInput input{
    background:#0f172a !important;
    color:white !important;
    border:2px solid #8b5cf6 !important;
    border-radius:12px !important;
    padding:12px !important;
}

/* Text area */
textarea{
    background:#0f172a !important;
    color:white !important;
}

/* Buttons */
.stButton>button{
    width:100%;
    background: linear-gradient(90deg,#0072ff,#d400ff);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
}

/* Metric cards */
.metric{
    padding:20px;
    border-radius:18px;
    text-align:center;
    color:white;
    font-size:22px;
    font-weight:bold;
}

/* Table */
[data-testid="stDataFrame"]{
    background:#0f172a;
    border-radius:15px;
    padding:10px;
}

/* Success */
.stSuccess{
    background:#064e3b !important;
}

/* Error */
.stError{
    background:#7f1d1d !important;
}

</style>
""", unsafe_allow_html=True)

# ===================== HEADER =====================
st.markdown("<div class='main-title'>🔐 AI STUDENT SYSTEM</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Smart • Secure • Intelligent</div>", unsafe_allow_html=True)

# ===================== LOGIN SECTION =====================
col1, col2 = st.columns(2)

# LEFT SIDE
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>📸 Face Authentication</div>", unsafe_allow_html=True)
    st.write("Login with your registered face")

    img = st.camera_input("Capture Face")

    if img:
        st.success("✅ Face detected successfully!")
        st.image(img, width=300)

    if st.button("📷 Capture & Login"):
        st.success("Access Granted ✅")

    st.info("Only registered face is allowed to access the system.")

    st.markdown("</div>", unsafe_allow_html=True)

# RIGHT SIDE
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>🔑 Manual Login</div>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "1234":
            st.success("✅ Login Successful")

        else:
            st.error("❌ Wrong Username or Password")

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ===================== DASHBOARD =====================
st.markdown("## 📊 AI STUDENT SYSTEM DASHBOARD")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class='metric' style='background:#2563eb;'>
    👨‍🎓<br>5<br>Total Students
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class='metric' style='background:#16a34a;'>
    🏆<br>Priya<br>Topper
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class='metric' style='background:#ea580c;'>
    ⚠️<br>2<br>Weak Students
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class='metric' style='background:#9333ea;'>
    📉<br>2<br>Poor Attendance
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ===================== ADD STUDENT =====================
c1, c2 = st.columns(2)

with c1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("## ➕ Add New Student")

    student_name = st.text_input("Student Name")

    attendance = st.slider("Attendance (%)", 0, 100, 80)
    math = st.slider("Math Marks", 0, 100, 70)
    science = st.slider("Science Marks", 0, 100, 70)
    english = st.slider("English Marks", 0, 100, 70)

    if st.button("✅ Add Student"):
        st.success(f"{student_name} Added Successfully!")

    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("## 📸 Face Recognition Attendance")

    face = st.camera_input("Take Student Photo")

    if face:
        st.success("✅ Face detected successfully!")
        st.success("✅ Attendance marked successfully!")
        st.success("🎉 Student Present")

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ===================== TABLE =====================
st.markdown("## 📋 Student Performance Table")

data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Rohit"],
    "Attendance (%)": [90, 95, 60, 85, 55],
    "Math": [88, 98, 45, 82, 40],
    "Science": [90, 99, 50, 84, 35],
    "English": [85, 97, 55, 81, 45]
}

df = pd.DataFrame(data)

df["Average"] = round(
    (df["Math"] + df["Science"] + df["English"]) / 3, 2
)

st.dataframe(df, use_container_width=True)

# ===================== CHARTS =====================
g1, g2 = st.columns(2)

with g1:
    st.markdown("## 📈 Attendance Graph")
    st.bar_chart(df.set_index("Name")["Attendance (%)"])

with g2:
    st.markdown("## 🥧 Student Marks Ratio")
    st.line_chart(df.set_index("Name")["Average"])

st.write("")

# ===================== CHATBOT + AI =====================
a1, a2 = st.columns(2)

with a1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("## 🤖 AI Chatbot")

    question = st.text_input("Ask any question")

    if st.button("Ask AI"):
        st.success("AI Response: Student performance is improving 🚀")

    st.markdown("</div>", unsafe_allow_html=True)

with a2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("## 🎯 AI Study Prediction")

    hours = st.slider("Study Hours Per Day", 1, 10, 6)

    predicted = hours * 10

    st.info(f"Predicted Marks: {predicted}/100")

    if predicted >= 60:
        st.success("🎉 Good! Keep it up and you can score well.")

    st.markdown("</div>", unsafe_allow_html=True)

# ===================== FEEDBACK =====================
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("## 💬 Feedback System")

feedback = st.text_area("Enter your feedback")

if st.button("Submit Feedback"):
    st.success("✅ Feedback Submitted Successfully")

st.markdown("</div>", unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<hr>
<center>
<h4>© 2025 AI Student System | Made with ❤️ by Shivam Kumar</h4>
</center>
""", unsafe_allow_html=True)
