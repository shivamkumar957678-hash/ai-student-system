import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF

# ================= PAGE =================
st.set_page_config(page_title="Ultimate AI Student System", layout="wide")

# ================= CSS =================
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#020024,#090979,#3d0075);
color:white;
}

h1,h2,h3,h4,h5,h6,p,label{
color:white !important;
}

.main-title{
text-align:center;
font-size:60px;
font-weight:bold;
color:#00e5ff;
text-shadow:0 0 20px #00e5ff;
}

.sub-title{
text-align:center;
font-size:24px;
color:#00ffff;
margin-bottom:25px;
}

.box{
background:rgba(0,0,0,0.45);
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
box-shadow:0 0 20px rgba(255,255,255,0.2);
}

.blue{
background:linear-gradient(135deg,#0052D4,#4364F7);
}

.green{
background:linear-gradient(135deg,#11998e,#38ef7d);
}

.orange{
background:linear-gradient(135deg,#ff512f,#dd2476);
}

.purple{
background:linear-gradient(135deg,#8E2DE2,#DA22FF);
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#0072ff,#d400ff);
color:white;
border:none;
border-radius:12px;
padding:12px;
font-size:18px;
font-weight:bold;
}

.stTextInput input{
background:#020b2d !important;
color:white !important;
border:2px solid #bb00ff !important;
border-radius:10px !important;
}

.stTextArea textarea{
background:#020b2d !important;
color:white !important;
border:2px solid #bb00ff !important;
border-radius:10px !important;
}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("<div class='main-title'>🔐 ULTIMATE AI STUDENT SYSTEM</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Smart • Secure • Intelligent</div>", unsafe_allow_html=True)

# ================= DATA =================
df = pd.DataFrame({
    "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
    "Attendance":[90,95,60,85,55],
    "Math":[88,98,45,82,40],
    "Science":[90,99,50,84,35],
    "English":[85,97,55,81,45]
})

df["Average"] = round(
(df["Math"]+df["Science"]+df["English"])/3,2
)

# ================= LOGIN =================
left,right = st.columns([1,2])

with left:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("📷 Face Authentication")

    st.camera_input("Capture Face")

    st.button("📸 Capture & Login")

    st.success("✅ Camera Ready")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("🔑 Manual Login")

    users = {
        "admin":"admin123",
        "rahul":"rahul123",
        "priya":"priya123"
    }

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username in users and users[username] == password:
            st.success(f"✅ Welcome {username}")
        else:
            st.error("❌ Wrong Username or Password")

    with st.expander("🔒 Forgot Password"):

        uname = st.text_input("Enter Username")

        if st.button("Recover Password"):

            if uname in users:
                st.success(f"Password: {users[uname]}")
            else:
                st.error("User not found")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("📁 Upload Excel / CSV")

    uploaded = st.file_uploader(
        "Upload Student File",
        type=["csv","xlsx"]
    )

    if uploaded:
        st.success("✅ File Uploaded Successfully")

    st.markdown("</div>", unsafe_allow_html=True)

with right:

    st.markdown("## 📊 AI STUDENT SYSTEM DASHBOARD")

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class='metric blue'>
        <h4>👨‍🎓 Total Students</h4>
        <h1>5</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='metric green'>
        <h4>🏆 Topper</h4>
        <h1>Priya</h1>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='metric orange'>
        <h4>⚠ Weak Students</h4>
        <h1>2</h1>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class='metric purple'>
        <h4>📉 Poor Attendance</h4>
        <h1>2</h1>
        </div>
        """, unsafe_allow_html=True)

    # SEARCH
    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("🔍 Search Student")

    search = st.text_input("Enter Student Name")

    if search:

        result = df[
            df["Name"].str.lower() == search.lower()
        ]

        if not result.empty:
            st.dataframe(result)
        else:
            st.warning("Student not found")

    st.markdown("</div>", unsafe_allow_html=True)

    # TABLE
    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("📋 Student Performance Table")

    st.dataframe(df, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # CHARTS
    g1,g2 = st.columns(2)

    with g1:

        fig = px.bar(
            df,
            x="Name",
            y="Attendance",
            color="Name",
            template="plotly_dark"
        )

        fig.update_layout(
            paper_bgcolor="#000814",
            plot_bgcolor="#000814"
        )

        st.plotly_chart(fig, use_container_width=True)

    with g2:

        pie = px.pie(
            df,
            names="Name",
            values="Average",
            hole=0.4,
            template="plotly_dark"
        )

        pie.update_layout(
            paper_bgcolor="#000814",
            plot_bgcolor="#000814"
        )

        st.plotly_chart(pie, use_container_width=True)

# ================= AI FEATURES =================

b1,b2,b3 = st.columns(3)

with b1:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("🤖 AI Chatbot")

    q = st.text_input("Ask AI")

    if st.button("Ask AI"):
        st.success(f"AI Response: {q} performance is improving 🚀")

    st.markdown("</div>", unsafe_allow_html=True)

with b2:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("🧠 AI Performance Analysis")

    student = st.selectbox(
        "Select Student",
        df["Name"]
    )

    student_data = df[df["Name"] == student].iloc[0]

    avg = student_data["Average"]

    if avg >= 85:
        st.success("🌟 Excellent Performance")

    elif avg >= 60:
        st.warning("📘 Needs Practice")

    else:
        st.error("⚠ Math Weak")

    st.markdown("</div>", unsafe_allow_html=True)

with b3:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("🎤 Voice Assistant")

    voice = st.text_input(
        "Example: Show Rahul marks"
    )

    if st.button("Run Voice Command"):

        cmd = voice.lower()

        found = False

        for i,row in df.iterrows():

            if row["Name"].lower() in cmd:

                st.success(f"{row['Name']} Marks")

                st.write(f"Math: {row['Math']}")
                st.write(f"Science: {row['Science']}")
                st.write(f"English: {row['English']}")
                st.write(f"Attendance: {row['Attendance']}%")

                found = True

        if not found:
            st.error("Student not found")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= ADMIN DASHBOARD =================

st.markdown("<div class='box'>", unsafe_allow_html=True)

st.subheader("🛠 Admin Dashboard")

a1,a2,a3,a4 = st.columns(4)

with a1:
    st.metric("🏫 Total Classes", "12")

with a2:
    st.metric("💰 Fees Pending", "3")

with a3:
    st.metric(
        "📊 Avg Attendance",
        f"{round(df['Attendance'].mean(),2)}%"
    )

with a4:
    st.metric("📅 Monthly Analytics", "Good")

st.markdown("</div>", unsafe_allow_html=True)

# ================= PDF REPORTS =================

p1,p2 = st.columns(2)

# ATTENDANCE PDF
with p1:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("📄 Attendance PDF Report")

    if st.button("Generate Attendance PDF"):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", "B", 18)

        pdf.cell(
            200,
            10,
            txt="Attendance Report",
            ln=True
        )

        pdf.ln(10)

        pdf.set_font("Arial", size=12)

        for i,row in df.iterrows():

            pdf.cell(
                200,
                10,
                txt=f"{row['Name']} - Attendance: {row['Attendance']}%",
                ln=True
            )

        pdf.output("attendance_report.pdf")

        with open("attendance_report.pdf", "rb") as file:

            st.download_button(
                "⬇ Download Attendance PDF",
                file,
                file_name="attendance_report.pdf"
            )

    st.markdown("</div>", unsafe_allow_html=True)

# SUBJECT PDF
with p2:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("📘 Subject Wise Marks PDF")

    selected_student = st.selectbox(
        "Select Student",
        df["Name"]
    )

    if st.button("Generate Subject PDF"):

        student_data = df[
            df["Name"] == selected_student
        ].iloc[0]

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", "B", 18)

        pdf.cell(
            200,
            10,
            txt="Student Subject Report",
            ln=True
        )

        pdf.ln(10)

        pdf.set_font("Arial", size=14)

        pdf.cell(
            200,
            10,
            txt=f"Student Name: {student_data['Name']}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"Attendance: {student_data['Attendance']}%",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"Math: {student_data['Math']}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"Science: {student_data['Science']}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"English: {student_data['English']}",
            ln=True
        )

        pdf.output("subject_report.pdf")

        with open("subject_report.pdf", "rb") as file:

            st.download_button(
                "⬇ Download Subject PDF",
                file,
                file_name="subject_report.pdf"
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================

st.markdown("""
<center>
<h4 style='color:white;'>
© 2026 Ultimate AI Student System | Made with ❤️ by Shivam Kumar
</h4>
</center>
""", unsafe_allow_html=True)
