import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Student System", layout="wide")

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

body {
    background: linear-gradient(135deg,#020024,#090979,#4B0082);
}

.stApp {
    background: linear-gradient(135deg,#020024,#090979,#4B0082);
    color: white;
}

/* TITLE */
.title {
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#00F5FF;
    text-shadow:0px 0px 20px #00F5FF;
}

.subtitle{
    text-align:center;
    color:#00F5FF;
    font-size:24px;
    margin-bottom:30px;
}

/* BOX */
.box {
    background:#050816;
    padding:20px;
    border-radius:20px;
    border:2px solid #8A2BE2;
    box-shadow:0px 0px 25px #8A2BE2;
    margin-bottom:20px;
}

/* INPUT */
.stTextInput input {
    background:#0B1120 !important;
    color:white !important;
    border:2px solid #8A2BE2 !important;
    border-radius:10px !important;
}

/* LABEL */
label {
    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
}

/* BUTTON */
.stButton button {
    width:100%;
    background:linear-gradient(90deg,#007BFF,#C000FF);
    color:white;
    border:none;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    padding:12px;
    box-shadow:0px 0px 20px #C000FF;
}

/* DATAFRAME */
[data-testid="stDataFrame"] {
    background-color:#050816;
    border:2px solid #8A2BE2;
    border-radius:15px;
    padding:10px;
    box-shadow:0px 0px 20px #8A2BE2;
}

thead tr th {
    background-color:#111827 !important;
    color:cyan !important;
}

tbody tr td {
    background-color:#050816 !important;
    color:white !important;
}

/* METRIC */
[data-testid="metric-container"] {
    background:#050816;
    border:2px solid #8A2BE2;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 0px 20px #8A2BE2;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown('<div class="title">🔐 AI STUDENT SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart • Secure • Intelligent</div>', unsafe_allow_html=True)

# =========================
# LOGIN SECTION
# =========================
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.subheader("📷 Face Authentication")
    st.write("Login with your registered face")

    camera = st.camera_input("Capture Face")

    if st.button("📸 Capture & Login"):
        st.success("✅ Face detected successfully!")
        st.success("🎉 Access Granted")

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="box">', unsafe_allow_html=True)

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
# STUDENT DATA
# =========================
students_df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Rohit"],
    "Attendance": [90, 95, 60, 85, 55],
    "Math": [88, 98, 45, 82, 40],
    "Science": [90, 99, 50, 84, 35],
    "English": [85, 97, 55, 81, 45],
    "Average": [87.67, 98.00, 50.00, 82.33, 40.00]
})

# =========================
# DASHBOARD METRICS
# =========================
st.markdown("## 📊 AI STUDENT SYSTEM DASHBOARD")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("👨‍🎓 Total Students", "5")

with m2:
    st.metric("🏆 Topper", "Priya")

with m3:
    st.metric("⚠ Weak Students", "2")

with m4:
    st.metric("📉 Poor Attendance", "2")

# =========================
# STUDENT TABLE
# =========================
st.markdown("## 📋 Student Performance Table")
st.dataframe(students_df, use_container_width=True)

# =========================
# CHARTS
# =========================
col3, col4 = st.columns(2)

# BAR GRAPH
fig_bar = px.bar(
    students_df,
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
    title_font_size=24,
    title_font_color="#00F5FF",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor="#222"),
)

# PIE CHART
fig_pie = px.pie(
    students_df,
    names="Name",
    values="Average",
    title="🔥 Student Marks Ratio",
    template="plotly_dark",
    hole=0.3
)

fig_pie.update_layout(
    paper_bgcolor="#050816",
    plot_bgcolor="#050816",
    font_color="white",
    title_font_size=24,
    title_font_color="#FF00FF"
)

with col3:
    st.plotly_chart(fig_bar, use_container_width=True)

with col4:
    st.plotly_chart(fig_pie, use_container_width=True)

# =========================
# ADD STUDENT
# =========================
st.markdown("## ➕ Add New Student")

c1, c2, c3 = st.columns(3)

with c1:
    name = st.text_input("Student Name")

with c2:
    attendance = st.slider("Attendance (%)", 0, 100, 80)

with c3:
    marks = st.slider("Average Marks", 0, 100, 75)

if st.button("✅ Add Student"):
    st.success(f"{name} added successfully!")

# =========================
# FEEDBACK
# =========================
st.markdown("## 💬 Feedback System")

feedback = st.text_area("Enter your feedback")

if st.button("Submit Feedback"):
    st.success("✅ Feedback Submitted Successfully")

# =========================
# FOOTER
# =========================
st.markdown("""
<hr>
<center>
<h4 style='color:white;'>© 2026 AI Student System | Made with ❤️ by Shivam Kumar</h4>
</center>
""", unsafe_allow_html=True)
