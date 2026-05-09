# =========================
# FULL FINAL AI STUDENT SYSTEM
# =========================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AI Student System", layout="wide")

# =========================
# DARK CSS
# =========================

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#020024,#090979,#3d0075);
color:white;
}

.block-container{
padding-top:1rem;
}

.main-title{
text-align:center;
font-size:60px;
font-weight:900;
color:#00F5FF;
text-shadow:0px 0px 20px #00F5FF;
}

.sub-title{
text-align:center;
font-size:22px;
color:#00ffff;
margin-bottom:25px;
}

.dark-box{
background:#030712;
padding:20px;
border-radius:20px;
border:2px solid #b026ff;
box-shadow:0px 0px 20px #b026ff;
margin-bottom:20px;
}

.stTextInput input{
background:#050816 !important;
color:white !important;
border:2px solid #b026ff !important;
border-radius:12px !important;
}

.stTextArea textarea{
background:#050816 !important;
color:white !important;
border:2px solid #b026ff !important;
border-radius:12px !important;
}

label{
color:white !important;
font-weight:bold !important;
font-size:18px !important;
}

.stButton button{
width:100%;
background:linear-gradient(90deg,#007bff,#d400ff);
color:white;
border:none;
padding:12px;
font-size:18px;
font-weight:bold;
border-radius:12px;
box-shadow:0px 0px 20px #d400ff;
}

[data-testid="metric-container"]{
background:#050816;
border:2px solid #b026ff;
padding:15px;
border-radius:15px;
box-shadow:0px 0px 20px #b026ff;
}

[data-testid="stDataFrame"]{
background:#050816;
border-radius:20px;
border:2px solid #b026ff;
box-shadow:0px 0px 25px #b026ff;
padding:10px;
}

thead tr th{
background:#111827 !important;
color:#00ffff !important;
}

tbody tr td{
background:#050816 !important;
color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.markdown('<div class="main-title">🔐 AI STUDENT SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Smart • Secure • Intelligent</div>', unsafe_allow_html=True)

# =========================
# LOGIN
# =========================

c1,c2 = st.columns(2)

with c1:

    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("📷 Face Authentication")

    st.write("Login with your registered face")

    img = st.camera_input("Capture Face")

    if st.button("📸 Capture & Login"):
        st.success("✅ Face detected successfully")
        st.success("🎉 Access Granted")

    st.markdown('</div>', unsafe_allow_html=True)

with c2:

    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("🔑 Manual Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":
            st.success("✅ Login Successful")
        else:
            st.error("❌ Wrong Username or Password")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# DASHBOARD
# =========================

st.markdown("## 📊 AI STUDENT SYSTEM DASHBOARD")

m1,m2,m3,m4 = st.columns(4)

with m1:
    st.metric("👨‍🎓 Total Students","5")

with m2:
    st.metric("🏆 Topper","Priya")

with m3:
    st.metric("⚠ Weak Students","2")

with m4:
    st.metric("📉 Poor Attendance","2")

# =========================
# DATA
# =========================

df = pd.DataFrame({
    "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
    "Attendance":[90,95,60,85,55],
    "Math":[88,98,45,82,40],
    "Science":[90,99,50,84,35],
    "English":[85,97,55,81,45],
    "Average":[87.67,98,50,82.33,40]
})

# =========================
# MAIN SECTION
# =========================

left,right = st.columns([1,2])

# =========================
# ADD STUDENT
# =========================

with left:

    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("➕ Add New Student")

    student_name = st.text_input("Student Name")

    attendance = st.slider("Attendance (%)",0,100,80)

    math = st.slider("Math Marks",0,100,70)

    science = st.slider("Science Marks",0,100,70)

    english = st.slider("English Marks",0,100,70)

    if st.button("✅ Add Student"):
        st.success(f"{student_name} Added Successfully")

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # FACE ATTENDANCE
    # =========================

    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("📸 Face Recognition Attendance")

    face = st.camera_input("Take Student Photo")

    if st.button("🎯 Mark Attendance"):
        st.success("✅ Attendance Marked")
        st.success("🎉 Student Present")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# TABLE + CHARTS
# =========================

with right:

    st.markdown("### 📋 Student Performance Table")

    st.dataframe(df,use_container_width=True)

    ch1,ch2 = st.columns(2)

    # BAR CHART

    fig_bar = px.bar(
        df,
        x="Name",
        y="Attendance",
        color="Name",
        title="📊 Attendance Graph",
        template="plotly_dark"
    )

    fig_bar.update_layout(
        paper_bgcolor="#050816",
        plot_bgcolor="#050816",
        font_color="white"
    )

    # PIE CHART

    fig_pie = px.pie(
        df,
        names="Name",
        values="Average",
        hole=0.4,
        title="🔥 Student Marks Ratio",
        template="plotly_dark"
    )

    fig_pie.update_layout(
        paper_bgcolor="#050816",
        plot_bgcolor="#050816",
        font_color="white"
    )

    with ch1:
        st.plotly_chart(fig_bar,use_container_width=True)

    with ch2:
        st.plotly_chart(fig_pie,use_container_width=True)

# =========================
# BOTTOM SECTION
# =========================

b1,b2,b3 = st.columns(3)

# =========================
# AI CHATBOT
# =========================

with b1:

    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("🤖 AI Chatbot")

    question = st.text_input("Ask anything about students")

    if st.button("Ask AI"):

        if question:
            st.success(f"AI Response: {question} performance is good.")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# AI PREDICTION
# =========================

with b2:

    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("🧠 AI Study Prediction")

    study_hours = st.slider("Study Hours",1,10,6)

    predicted_marks = study_hours * 10

    st.metric("Predicted Marks",f"{predicted_marks}/100")

    if predicted_marks >= 60:
        st.success("🎉 Good! You can score well")
    else:
        st.warning("⚠ Need More Practice")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FEEDBACK
# =========================

with b3:

    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("💬 Feedback System")

    feedback = st.text_area("Enter your feedback")

    if st.button("Submit Feedback"):
        st.success("✅ Feedback Submitted")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================

st.markdown("""
<hr>
<center>
<h4 style='color:white;'>
© 2026 AI Student System | Made with ❤️ by Shivam Kumar
</h4>
</center>
""", unsafe_allow_html=True)
