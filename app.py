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
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020024,#090979,#3d0075);
    color:white;
}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

/* TITLE */
.main-title{
    text-align:center;
    font-size:60px;
    font-weight:900;
    color:#00F5FF;
    text-shadow:0px 0px 25px #00F5FF;
}

.sub-title{
    text-align:center;
    font-size:24px;
    color:#00ffff;
    margin-bottom:25px;
}

/* DARK BOX */
.dark-box{
    background:#050816;
    padding:20px;
    border-radius:20px;
    border:2px solid #b026ff;
    box-shadow:0px 0px 20px #b026ff;
    margin-bottom:20px;
}

/* INPUT */
.stTextInput input{
    background:#0b1120 !important;
    color:white !important;
    border:2px solid #b026ff !important;
    border-radius:12px !important;
    padding:12px !important;
}

/* TEXT AREA */
.stTextArea textarea{
    background:#0b1120 !important;
    color:white !important;
    border:2px solid #b026ff !important;
    border-radius:12px !important;
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
    font-size:18px;
    font-weight:bold;
    box-shadow:0px 0px 20px #d400ff;
}

/* METRIC */
[data-testid="metric-container"]{
    background:#050816;
    border:2px solid #b026ff;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 0px 20px #b026ff;
}

[data-testid="metric-container"] label{
    color:#00ffff !important;
    font-size:18px !important;
}

[data-testid="metric-container"] div{
    color:white !important;
}

/* TABLE */
[data-testid="stDataFrame"]{
    background:#050816;
    border:2px solid #b026ff;
    border-radius:20px;
    padding:10px;
    box-shadow:0px 0px 20px #b026ff;
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
st.markdown(
    '<div class="main-title">🔐 AI STUDENT SYSTEM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Smart • Secure • Intelligent</div>',
    unsafe_allow_html=True
)

# =========================
# DATA
# =========================
df = pd.DataFrame({
    "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
    "Attendance":[90,95,60,85,55],
    "Math":[88,98,45,82,40],
    "Science":[90,99,50,84,35],
    "English":[85,97,55,81,45]
})

df["Average"] = round(
    (df["Math"] + df["Science"] + df["English"]) / 3,2
)

# =========================
# MAIN LAYOUT
# =========================
left,right = st.columns([1,2])

# =========================
# LEFT SIDE
# =========================
with left:

    # FACE AUTH
    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("📸 Face Authentication")

    st.write("Login with your registered face")

    camera = st.camera_input("Capture Face")

    if st.button("📷 Capture & Login"):
        st.success("✅ Face detected successfully!")
        st.success("🎉 Access Granted")

    st.markdown('</div>', unsafe_allow_html=True)

    # LOGIN
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

    # ADD STUDENT
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

    # FACE ATTENDANCE
    st.markdown('<div class="dark-box">', unsafe_allow_html=True)

    st.subheader("📸 Face Recognition Attendance")

    face = st.camera_input("Take Student Photo")

    if st.button("🎯 Mark Attendance"):
        st.success("✅ Attendance Marked")
        st.success("🎉 Student Present")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# RIGHT SIDE
# =========================
with right:

    st.markdown("## 📊 AI STUDENT SYSTEM DASHBOARD")

    # METRICS
    m1,m2,m3,m4 = st.columns(4)

    with m1:
        st.metric("👨‍🎓 Total Students","5")

    with m2:
        st.metric("🏆 Topper","Priya")

    with m3:
        st.metric("⚠ Weak Students","2")

    with m4:
        st.metric("📉 Poor Attendance","2")

    # TABLE
    st.markdown("## 📋 Student Performance Table")

    st.dataframe(df,use_container_width=True)

    # CHARTS
    c1,c2 = st.columns(2)

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
        font_color="white",
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
        title_font_color="#ff00ff"
    )

    with c1:
        st.plotly_chart(fig_bar,use_container_width=True)

    with c2:
        st.plotly_chart(fig_pie,use_container_width=True)

    # BOTTOM
    b1,b2,b3 = st.columns(3)

    # AI CHATBOT
    with b1:

        st.markdown('<div class="dark-box">', unsafe_allow_html=True)

        st.subheader("🤖 AI Chatbot")

        question = st.text_input("Ask any question")

        if st.button("Ask AI"):

            if question:
                st.success("AI Response: Student performance is improving 🚀")

        st.markdown('</div>', unsafe_allow_html=True)

    # AI PREDICTION
    with b2:

        st.markdown('<div class="dark-box">', unsafe_allow_html=True)

        st.subheader("🧠 AI Study Prediction")

        study_hours = st.slider("Study Hours",1,10,6)

        predicted_marks = study_hours * 10

        st.metric("Predicted Marks",f"{predicted_marks}/100")

        if predicted_marks >= 60:
            st.success("🎉 Good! Keep it up and you can score well.")
        else:
            st.warning("⚠ Need More Practice")

        st.markdown('</div>', unsafe_allow_html=True)

    # FEEDBACK
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
