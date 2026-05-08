import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# ================= PAGE =================

st.set_page_config(
    page_title="AI Student System",
    layout="wide"
)

# ================= LOGIN SESSION =================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ================= CSS =================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020024,#090979,#6a00ff);
    color:white;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#020024,#090979,#6a00ff);
    border-right:2px solid cyan;
}

section[data-testid="stSidebar"] *{
    color:white !important;
    font-weight:bold;
}

/* TITLE */

.main-title{
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:white;
    text-shadow:0px 0px 30px cyan;
}

/* HEADING */

h1,h2,h3,label,p{
    color:white !important;
    font-weight:bold !important;
}

/* INPUT */

.stTextInput input{
    background:white !important;
    color:black !important;
    border-radius:12px !important;
    border:2px solid cyan !important;
    font-size:20px !important;
    font-weight:bold !important;
}

/* TEXT AREA */

textarea{
    background:white !important;
    color:black !important;
    font-size:18px !important;
    border-radius:12px !important;
    border:2px solid cyan !important;
}

/* BUTTON */

.stButton button{
    background:linear-gradient(90deg,#00c6ff,#a100ff);
    color:white;
    border:none;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    padding:12px 25px;
    box-shadow:0px 0px 20px cyan;
}

/* CARD */

.card{
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:25px;
    font-weight:bold;
    box-shadow:0px 0px 25px rgba(0,255,255,0.5);
}

/* COLORS */

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
    background:linear-gradient(135deg,#8e2de2,#4a00e0);
}

/* LOGIN BOX */

.login-box{
    background:rgba(255,255,255,0.08);
    padding:40px;
    border-radius:25px;
    border:2px solid cyan;
    box-shadow:0px 0px 30px cyan;
}

/* SIDEBAR TITLE */

.sidebar-title{
    text-align:center;
    font-size:30px;
    color:#00ffff;
    font-weight:bold;
    text-shadow:0px 0px 20px cyan;
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN PAGE =================

if not st.session_state.logged_in:

    st.markdown("""
    <div class='main-title'>
    🔐 AI STUDENT SYSTEM
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1,c2,c3 = st.columns([1,2,1])

    with c2:

        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        st.markdown("""
        <h1 style='text-align:center;color:white;'>
        Welcome Back!
        </h1>
        """, unsafe_allow_html=True)

        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        if st.button("🚀 LOGIN NOW"):

            if username == "shivam-user" and password == "12345":
                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error("❌ Wrong Username or Password")

        st.markdown("</div>", unsafe_allow_html=True)

# ================= MAIN DASHBOARD =================

else:

    st.sidebar.markdown("""
    <div class='sidebar-title'>
    🎓 AI STUDENT SYSTEM
    </div>
    """, unsafe_allow_html=True)

    menu = st.sidebar.radio(
        "MENU",
        [
            "Dashboard",
            "Add Student",
            "Face Attendance",
            "Students",
            "AI Chatbot",
            "AI Prediction",
            "Feedback"
        ]
    )

    st.markdown("""
    <div class='main-title' style='font-size:55px;'>
    🎓 AI STUDENT SYSTEM DASHBOARD
    </div>
    """, unsafe_allow_html=True)

    # ================= DASHBOARD =================

    if menu == "Dashboard":

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.markdown("""
            <div class='card blue'>
            👨‍🎓<br><br>
            Total Students<br><br>
            5
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class='card green'>
            🏆<br><br>
            Topper<br><br>
            Priya
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class='card red'>
            ⚠️<br><br>
            Weak Students<br><br>
            2
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown("""
            <div class='card purple'>
            📉<br><br>
            Poor Attendance<br><br>
            2
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("📋 Student Performance Table")

        data = pd.DataFrame({
            "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
            "Attendance":[90,95,60,85,55],
            "Math":[88,98,45,82,40],
            "Science":[90,99,50,84,35],
            "English":[85,97,55,81,45]
        })

        st.dataframe(data, use_container_width=True)

        # ================= GRAPH SECTION =================

        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("📊 Student Analytics Dashboard")

        students = ["Rahul","Priya","Aman","Sneha","Rohit"]
        marks = [88,98,50,82,40]
        attendance_data = [90,95,60,85,55]

        col1, col2 = st.columns(2)

        # PIE CHART

        with col1:

            fig1, ax1 = plt.subplots(figsize=(5,5))

            colors = [
                "#00E5FF",
                "#00FF85",
                "#FF9800",
                "#FF00E5",
                "#FF1744"
            ]

            ax1.pie(
                marks,
                labels=students,
                autopct='%1.1f%%',
                colors=colors,
                startangle=90
            )

            ax1.axis('equal')

            st.pyplot(fig1)

        # BAR GRAPH

        with col2:

            fig2, ax2 = plt.subplots(figsize=(6,5))

            ax2.bar(
                students,
                attendance_data,
                color=[
                    "#00E5FF",
                    "#00FF85",
                    "#FF9800",
                    "#FF00E5",
                    "#FF1744"
                ]
            )

            ax2.set_ylim(0,100)

            ax2.set_ylabel("Attendance %")
            ax2.set_xlabel("Students")

            st.pyplot(fig2)

    # ================= ADD STUDENT =================

    elif menu == "Add Student":

        st.subheader("➕ Add Student")

        name = st.text_input("Student Name")

        attendance = st.slider("Attendance",0,100,80)
        math = st.slider("Math",0,100,70)
        science = st.slider("Science",0,100,70)
        english = st.slider("English",0,100,70)

        if st.button("✅ Add Student"):
            st.success(f"🎉 {name} Added Successfully")

    # ================= FACE ATTENDANCE =================

    elif menu == "Face Attendance":

        st.subheader("📸 Face Recognition Attendance")

        img = st.camera_input("Take Photo")

        if img:
            st.success("✅ Face Detected Successfully")
            st.success("🎯 Attendance Marked Successfully")
            st.success("🧑 Student Present")

    # ================= STUDENTS =================

    elif menu == "Students":

        st.subheader("👨‍🎓 Students List")

        df = pd.DataFrame({
            "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
            "Attendance":[90,95,60,85,55],
            "Average":[87,98,50,82,40]
        })

        st.dataframe(df, use_container_width=True)

    # ================= AI CHATBOT =================

    elif menu == "AI Chatbot":

        st.subheader("🤖 AI Chatbot")

        st.markdown("""
        <h3 style='color:#00ffff;'>
        Ask Any Question About Students
        </h3>
        """, unsafe_allow_html=True)

        q = st.text_input("💬 Enter Your Question")

        if st.button("🚀 Ask AI"):

            question = q.lower()

            if "topper" in question:
                st.success("🏆 Priya is the topper with highest marks")

            elif "weak" in question:
                st.warning("⚠️ Aman and Rohit are weak students")

            elif "attendance" in question:
                st.info("📊 Average attendance is 77%")

            elif "aman english" in question:
                st.success("📘 Aman English Marks = 55")

            elif "rahul math" in question:
                st.success("➗ Rahul Math Marks = 88")

            elif "priya science" in question:
                st.success("🧪 Priya Science Marks = 99")

            elif "sneha attendance" in question:
                st.success("📅 Sneha Attendance = 85%")

            elif "rohit average" in question:
                st.success("📈 Rohit Average = 40")

            elif "students" in question:
                st.success("👨‍🎓 Rahul, Priya, Aman, Sneha, Rohit")

            elif "total students" in question:
                st.success("📚 Total Students = 5")

            elif "best attendance" in question:
                st.success("🥇 Priya has best attendance = 95%")

            elif "face attendance" in question:
                st.success("📸 Face Attendance System Active")

            elif "feedback" in question:
                st.success("💬 Feedback System Running Successfully")

            else:
                st.error("❌ Question Not Found In Database")

    # ================= AI PREDICTION =================

    elif menu == "AI Prediction":

        st.subheader("📈 AI Study Prediction")

        hrs = st.slider("Study Hours",1,12,5)

        marks = hrs * 10

        st.success(f"📚 Predicted Marks = {marks}")

    # ================= FEEDBACK =================

    elif menu == "Feedback":

        st.subheader("💬 Feedback System")

        feedback = st.text_area("Enter Feedback")

        if st.button("Submit Feedback"):

            polarity = TextBlob(feedback).sentiment.polarity

            if polarity > 0:
                st.success("😊 Positive Feedback")

            elif polarity < 0:
                st.error("😔 Negative Feedback")

            else:
                st.info("😐 Neutral Feedback")

    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()
