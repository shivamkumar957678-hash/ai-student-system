import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Student System",
    layout="wide"
)

# =========================
# FULL DARK CSS
# =========================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020024,#090979,#3d0075);
    color:white;
}

/* REMOVE WHITE */
.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

/* TITLE */
.main-title{
    text-align:center;
    font-size:65px;
    font-weight:900;
    color:#00F5FF;
    text-shadow:0px 0px 25px #00F5FF;
}

.sub-title{
    text-align:center;
    font-size:25px;
    color:#00FFFF;
    margin-bottom:30px;
}

/* BOX */
.dark-box{
    background:#030712;
    padding:20px;
    border-radius:20px;
    border:2px solid #b026ff;
    box-shadow:0px 0px 25px #b026ff;
    margin-bottom:20px;
}

/* INPUT */
.stTextInput input{
    background:#050816 !important;
    color:white !important;
    border:2px solid #b026ff !important;
    border-radius:12px !important;
    padding:12px !important;
}

/* LABEL */
label{
    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
}

/* BUTTON */
.stButton button{
    width:100%;
    background:linear-gradient(90deg,#007bff,#d400ff);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:20px;
    font-weight:bold;
    box-shadow:0px 0px 20px #d400ff;
}

/* METRICS */
[data-testid="metric-container"]{
    background:#050816;
    border:2px solid #b026ff;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 0px 20px #b026ff;
}

/* TABLE */
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

/* CHART */
.js-plotly-plot{
    background:#050816 !important;
    border-radius:20px;
    border:2px solid #b026ff;
    box-shadow:0px 0px 25px #b026ff;
    padding:10px;
}

h1,h2,h3{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown(
    '<div class="main-title">🔐 AI STUDENT SYSTEM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Smart • Secure • Intelligent</div>',
    unsafe_allow_html=True
)

# =========================
# LOGIN SECTION
# =========================
col1, col2 = st.columns(2)

# FACE LOGIN
with col1:

    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("📷 Face Authentication")

    st.write("Login with your registered face")

    img = st.camera_input("Capture Face")

    if st.button("📸 Capture & Login"):
        st.success("✅ Face detected successfully!")
        st.success("🎉 Access Granted")

    st.markdown('</div>', unsafe_allow_html=True)

# MANUAL LOGIN
with col2:

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
# DASHBOARD TITLE
# =========================
st.markdown("## 📊 AI STUDENT SYSTEM DASHBOARD")

# =========================
# METRICS
# =========================
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
# TABLE
# =========================
st.markdown("## 📋 Student Performance Table")

st.dataframe(df,use_container_width=True)

# =========================
# CHARTS
# =========================
c1,c2 = st.columns(2)

# BAR GRAPH
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
    font_color="white",
    title_font_size=28,
    title_font_color="#00F5FF"
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
    font_color="white",
    title_font_size=28,
    title_font_color="#ff00ff"
)

with c1:
    st.plotly_chart(fig_bar,use_container_width=True)

with c2:
    st.plotly_chart(fig_pie,use_container_width=True)

# =========================
# ADD STUDENT
# =========================
st.markdown("## ➕ Add New Student")

a1,a2,a3 = st.columns(3)

with a1:
    student_name = st.text_input("Student Name")

with a2:
    attendance = st.slider("Attendance",0,100,80)

with a3:
    marks = st.slider("Average Marks",0,100,70)

if st.button("✅ Add Student"):
    st.success(f"{student_name} Added Successfully")

# =========================
# FEEDBACK
# =========================
st.markdown("## 💬 Feedback System")

feedback = st.text_area("Enter your feedback")

if st.button("Submit Feedback"):
    st.success("✅ Feedback Submitted")

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
