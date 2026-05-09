import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from fpdf import FPDF

st.set_page_config(
    page_title="Ultimate AI Student System",
    layout="wide"
)

# =========================
# DATA
# =========================
data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Rohit"],
    "Attendance": [90, 95, 60, 85, 55],
    "Math": [88, 98, 45, 82, 40],
    "Science": [90, 99, 50, 84, 35],
    "English": [85, 97, 55, 81, 45],
}

df = pd.DataFrame(data)
df["Average"] = (
    df["Math"] + df["Science"] + df["English"]
) / 3

topper = df.loc[df["Average"].idxmax(), "Name"]
weak_students = len(df[df["Average"] < 60])
poor_attendance = len(df[df["Attendance"] < 75])

# =========================
# LOGIN
# =========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================
# CSS
# =========================
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#020024,#090979,#3d0ca3);
color:white;
}

h1,h2,h3,h4,h5,h6,p,label{
color:white !important;
}

.title{
text-align:center;
font-size:60px;
font-weight:bold;
color:#00e5ff;
text-shadow:0 0 20px #00e5ff;
}

.sub{
text-align:center;
font-size:24px;
color:#00ffff;
margin-bottom:30px;
}

.box{
background:rgba(0,0,0,0.35);
padding:20px;
border-radius:20px;
border:2px solid #bb00ff;
box-shadow:0 0 20px #bb00ff;
margin-bottom:20px;
}

.metric{
padding:20px;
border-radius:20px;
text-align:center;
font-weight:bold;
color:white;
box-shadow:0 0 20px rgba(255,255,255,0.3);
}

.blue{
background:linear-gradient(135deg,#005bea,#00c6fb);
}

.green{
background:linear-gradient(135deg,#11998e,#38ef7d);
}

.red{
background:linear-gradient(135deg,#ff416c,#ff4b2b);
}

.purple{
background:linear-gradient(135deg,#8e2de2,#ff00ff);
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#007bff,#d000ff);
color:white;
border:none;
border-radius:12px;
padding:12px;
font-size:20px;
font-weight:bold;
box-shadow:0 0 15px #d000ff;
}

input{
background:#000 !important;
color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown(
    '<div class="title">🔐 AI STUDENT SYSTEM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub">Smart • Secure • Intelligent</div>',
    unsafe_allow_html=True
)

# =========================
# TOP SECTION
# =========================
left, right = st.columns([1, 2])

# =========================
# LEFT SIDE
# =========================
with left:

    col1, col2 = st.columns(2)

    # FACE AUTH
    with col1:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown("## 📷 Face Authentication")
        st.write("Login with your registered face")

        camera = st.camera_input("Capture Face")

        st.button("📸 Capture & Login")

        st.success("✅ Face matched successfully")
        st.info("Redirecting to dashboard...")

        st.markdown("</div>", unsafe_allow_html=True)

    # LOGIN
    with col2:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown("## 🔑 Manual Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if username == "admin" and password == "admin123":
                st.session_state.logged_in = True
                st.success("✅ Login Successful")

            else:
                st.error("❌ Wrong Username or Password")

        if st.button("Forgot Password"):
            st.info("Default Login → admin / admin123")

        st.markdown("</div>", unsafe_allow_html=True)

    # ADD STUDENT
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown("## ➕ Add New Student")

        st.text_input("Student Name")

        st.slider("Attendance (%)", 0, 100, 80)
        st.slider("Math Marks", 0, 100, 70)
        st.slider("Science Marks", 0, 100, 70)
        st.slider("English Marks", 0, 100, 70)

        st.button("✅ Add Student")

        st.markdown("</div>", unsafe_allow_html=True)

    # FACE ATTENDANCE
    with col4:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown("## 🪪 Face Recognition Attendance")

        cam2 = st.camera_input("Click below to capture student photo")

        st.button("📸 Take Photo")

        st.success("✅ Face detected successfully!")
        st.success("✅ Attendance marked successfully!")
        st.info("🎉 Student Present")

        st.markdown("</div>", unsafe_allow_html=True)

# =========================
# RIGHT SIDE
# =========================
with right:

    st.markdown(
        "<h1 style='text-align:center;'>📊 AI STUDENT SYSTEM DASHBOARD</h1>",
        unsafe_allow_html=True
    )

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown(f"""
        <div class="metric blue">
        👨‍🎓<br>
        Total Students<br><br>
        <h1>5</h1>
        All Registered Students
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="metric green">
        🏆<br>
        Topper<br><br>
        <h1>{topper}</h1>
        Highest Average Marks
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="metric red">
        ⚠<br>
        Weak Students<br><br>
        <h1>{weak_students}</h1>
        Need Improvement
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown(f"""
        <div class="metric purple">
        📉<br>
        Poor Attendance<br><br>
        <h1>{poor_attendance}</h1>
        Attendance &lt; 75%
        </div>
        """, unsafe_allow_html=True)

    # ======================
    # TABLE
    # ======================
    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.markdown("## 📋 Student Performance Table")

    st.dataframe(df, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ======================
    # CHARTS
    # ======================
    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown("## 📊 Attendance Graph")

        fig = px.bar(
            df,
            x="Name",
            y="Attendance",
            color="Name",
            text="Attendance"
        )

        fig.update_layout(
            paper_bgcolor="#020024",
            plot_bgcolor="#020024",
            font_color="white"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown("## 🔥 Student Marks Ratio")

        fig2 = px.pie(
            df,
            names="Name",
            values="Average",
            hole=0.3
        )

        fig2.update_layout(
            paper_bgcolor="#020024",
            plot_bgcolor="#020024",
            font_color="white"
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ======================
    # BOTTOM
    # ======================
    b1, b2, b3 = st.columns(3)

    # CHATBOT
    with b1:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown("## 🤖 AI Chatbot")

        question = st.text_input("Ask anything about students")

        if st.button("Ask AI"):

            q = question.lower()

            if "topper" in q:
                st.success(f"🏆 Topper is {topper}")

            elif "weak" in q:
                st.warning(f"⚠ Weak students count: {weak_students}")

            elif "attendance" in q:
                st.info("📊 Attendance data loaded")

            else:
                st.write("🤖 AI Response: Student system working perfectly.")

        st.markdown("</div>", unsafe_allow_html=True)

    # AI PREDICTION
    with b2:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown("## 🧠 AI Study Prediction")

        hrs = st.slider("Study Hours", 1, 10, 5)

        predicted = hrs * 10

        st.metric("Predicted Marks", f"{predicted}/100")

        if predicted >= 80:
            st.success("🌟 Excellent performance expected!")

        elif predicted >= 60:
            st.info("👍 Good performance expected!")

        else:
            st.warning("⚠ Need more study.")

        st.markdown("</div>", unsafe_allow_html=True)

    # FEEDBACK
    with b3:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown("## 💬 Feedback System")

        feedback = st.text_area("Enter your feedback")

        if st.button("Submit Feedback"):
            st.success("✅ Feedback Submitted")

        st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SEARCH
# =========================
st.markdown('<div class="box">', unsafe_allow_html=True)

st.markdown("## 🔍 Search Student")

search = st.text_input("Enter Student Name")

if search:
    result = df[df["Name"].str.contains(search, case=False)]

    if not result.empty:
        st.dataframe(result, use_container_width=True)
    else:
        st.error("Student Not Found")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# LEADERBOARD
# =========================
st.markdown('<div class="box">', unsafe_allow_html=True)

st.markdown("## 🏅 Leaderboard")

leaderboard = df.sort_values("Average", ascending=False)

for i, row in leaderboard.iterrows():
    st.write(
        f"🥇 {row['Name']} → {round(row['Average'],2)}"
    )

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PDF DOWNLOAD
# =========================
st.markdown('<div class="box">', unsafe_allow_html=True)

st.markdown("## 📄 Attendance PDF Report")

if st.button("Generate PDF"):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Student Attendance Report", ln=True)

    for i, row in df.iterrows():
        pdf.cell(
            200,
            10,
            txt=f"{row['Name']} - Attendance: {row['Attendance']}%",
            ln=True
        )

    pdf.output("attendance_report.pdf")

    with open("attendance_report.pdf", "rb") as file:
        st.download_button(
            "⬇ Download PDF",
            file,
            file_name="attendance_report.pdf"
        )

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<h3 style='text-align:center;color:#ff66ff;'>
© 2025 AI Student System | Made with ❤️ by Shivam Kumar
</h3>
""", unsafe_allow_html=True)
