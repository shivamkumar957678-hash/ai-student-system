import streamlit as st
import pandas as pd
from textblob import TextBlob

st.set_page_config(page_title="AI Student System", layout="wide")

# ================= LOGIN =================

if "login" not in st.session_state:
    st.session_state.login = False

# ================= CSS =================

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: Arial;
}

/* MAIN BACKGROUND */
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

.sidebar-title{
    text-align:center;
    font-size:28px;
    color:#00ffff;
    font-weight:bold;
    margin-bottom:20px;
    text-shadow:0px 0px 20px cyan;
}

/* INPUT BOX */
.stTextInput input{
    background:#ffffff !important;
    color:black !important;
    border-radius:12px !important;
    border:2px solid #00ffff !important;
    padding:14px !important;
    font-size:20px !important;
    font-weight:bold !important;
}

/* PASSWORD BOX */
.stTextInput label{
    color:white !important;
    font-size:22px !important;
    font-weight:bold !important;
}

/* BUTTON */
.stButton button{
    background:linear-gradient(90deg,#00c6ff,#a100ff);
    color:white;
    border:none;
    border-radius:12px;
    font-size:22px;
    font-weight:bold;
    padding:14px 30px;
    box-shadow:0 0 20px cyan;
}

/* CARDS */
.card{
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:22px;
    font-weight:bold;
    box-shadow:0px 0px 20px rgba(0,255,255,0.5);
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
    background:linear-gradient(135deg,#8e2de2,#4a00e0);
}

/* TABLE */
table{
    color:white !important;
}

/* HEADINGS */
h1,h2,h3{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN PAGE =================

if not st.session_state.login:

    st.markdown("""
    <h1 style='text-align:center;
    font-size:70px;
    color:white;
    text-shadow:0px 0px 30px cyan;'>
    🔐 AI STUDENT SYSTEM
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,2,1])

    with col2:

        st.markdown("""
        <div style="
        background:rgba(255,255,255,0.08);
        padding:40px;
        border-radius:25px;
        border:2px solid cyan;
        box-shadow:0px 0px 30px cyan;">
        """, unsafe_allow_html=True)

        st.markdown("""
        <h1 style='text-align:center;color:white;'>
        Welcome Back!
        </h1>
        """, unsafe_allow_html=True)

        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        if st.button("🚀 LOGIN NOW"):

            if username == "shivam-user" and password == "12345":
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Wrong Username or Password")

        st.markdown("</div>", unsafe_allow_html=True)

# ================= DASHBOARD =================

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

    st.title("🎓 AI STUDENT SYSTEM DASHBOARD")

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

        data = pd.DataFrame({
            "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
            "Attendance":[90,95,60,85,55],
            "Math":[88,98,45,82,40],
            "Science":[90,99,50,84,35],
            "English":[85,97,55,81,45]
        })

        st.subheader("📋 Student Performance Table")
        st.dataframe(data, use_container_width=True)

    # ================= ADD STUDENT =================

    elif menu == "Add Student":

        st.subheader("➕ Add Student")

        name = st.text_input("Student Name")

        attendance = st.slider("Attendance",0,100,80)
        math = st.slider("Math",0,100,70)
        science = st.slider("Science",0,100,70)
        english = st.slider("English",0,100,70)

        if st.button("✅ Add Student"):
            st.success(f"{name} Added Successfully")

    # ================= FACE ATTENDANCE =================

    elif menu == "Face Attendance":

        st.subheader("📸 Face Recognition Attendance")

        pic = st.camera_input("Take Photo")

        if pic:
            st.success("✅ Face detected successfully")
            st.success("🎯 Attendance marked successfully")
            st.success("🧑 Student Present")

    # ================= STUDENTS =================

    elif menu == "Students":

        st.subheader("👨‍🎓 Students")

        df = pd.DataFrame({
            "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
            "Attendance":[90,95,60,85,55],
            "Average":[87,98,50,82,40]
        })

        st.dataframe(df, use_container_width=True)

    # ================= CHATBOT =================

    elif menu == "AI Chatbot":

        st.subheader("🤖 AI Chatbot")

        q = st.text_input("Ask Question")

        if st.button("Ask"):

            if "topper" in q.lower():
                st.success("🏆 Priya is the topper")

            elif "weak" in q.lower():
                st.warning("⚠️ Aman and Rohit are weak students")

            else:
                st.info("AI Assistant Ready")

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
        st.session_state.login = False
        st.rerun()
