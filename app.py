import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

st.set_page_config(page_title="AI Student System", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#020024,#090979,#6a00ff);
    color:white;
}
h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}
.block-container{
    padding-top:1rem;
}
.card{
    background:#08142b;
    padding:20px;
    border-radius:15px;
    border:1px solid #222;
    box-shadow:0 0 15px rgba(0,255,255,0.2);
}
.metric{
    text-align:center;
    padding:20px;
    border-radius:15px;
    color:white;
    font-weight:bold;
}
.blue{background:linear-gradient(45deg,#005bea,#00c6fb);}
.green{background:linear-gradient(45deg,#11998e,#38ef7d);}
.orange{background:linear-gradient(45deg,#ff512f,#dd2476);}
.purple{background:linear-gradient(45deg,#8e2de2,#4a00e0);}
button[kind="primary"]{
    background:linear-gradient(45deg,#00dbde,#fc00ff)!important;
    border:none!important;
    color:white!important;
    border-radius:10px!important;
}
</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    st.markdown("<h1 style='text-align:center;'>🔐 AI STUDENT SYSTEM</h1>", unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        image = Image.open("shivam.jpg")
        st.image(image, width=250)

        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        if st.button("🚀 LOGIN NOW"):

            if username == "shivam" and password == "12345":
                st.success("✅ Login Successful")
                st.session_state.login = True
                st.rerun()
            else:
                st.error("❌ Wrong Username or Password")

        st.markdown("</div>", unsafe_allow_html=True)

# ================= DASHBOARD =================
else:

    st.markdown("<h1 style='text-align:center;'>🎓 AI STUDENT SYSTEM DASHBOARD</h1>", unsafe_allow_html=True)

    # TOP CARDS
    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown("<div class='metric blue'>👨‍🎓<br>Total Students<br><h1>5</h1></div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='metric green'>🏆<br>Topper<br><h1>Priya</h1></div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='metric orange'>⚠️<br>Weak Students<br><h1>2</h1></div>", unsafe_allow_html=True)

    with c4:
        st.markdown("<div class='metric purple'>📉<br>Poor Attendance<br><h1>2</h1></div>", unsafe_allow_html=True)

    st.write("")

    # DATA
    names = ["Rahul","Priya","Aman","Sneha","Rohit"]
    attendance = [90,95,60,85,55]
    average = [88,98,50,82,40]

    # SECOND ROW
    col1,col2,col3 = st.columns([1,1,2])

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("➕ Add Student")

        st.text_input("Student Name")
        st.slider("Attendance",0,100,80)
        st.slider("Math",0,100,70)
        st.slider("Science",0,100,70)
        st.slider("English",0,100,70)

        st.button("✅ Add Student")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📸 Face Attendance")

        st.success("✅ Face detected successfully")
        st.success("✅ Attendance marked")
        st.info("🎉 Student Present")

        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📋 Student Performance Table")

        df = pd.DataFrame({
            "Name":names,
            "Attendance":attendance,
            "Average":average
        })

        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # GRAPHS
    g1,g2 = st.columns(2)

    with g1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📊 Student Marks Ratio")

        fig1, ax1 = plt.subplots()
        ax1.pie(average, labels=names, autopct='%1.1f%%')
        st.pyplot(fig1)

        st.markdown("</div>", unsafe_allow_html=True)

    with g2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📈 Attendance Graph")

        fig2, ax2 = plt.subplots()
        ax2.bar(names, attendance)
        st.pyplot(fig2)

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # BOTTOM
    b1,b2,b3 = st.columns(3)

    with b1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🤖 AI Chatbot")

        q = st.text_input("Ask Any Question")

        if st.button("Ask"):
            st.success("🤖 AI Assistant Ready")
            st.write("Answer:", q)

        st.markdown("</div>", unsafe_allow_html=True)

    with b2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🧠 AI Study Prediction")

        hours = st.slider("Study Hours",1,12,5)

        marks = hours * 10

        st.success(f"📚 Predicted Marks = {marks}")

        st.markdown("</div>", unsafe_allow_html=True)

    with b3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("💬 Feedback System")

        st.text_area("Enter Feedback")

        st.button("Submit Feedback")

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("<h4 style='text-align:center;'>© 2025 AI Student System | Made with ❤️ by Shivam Kumar</h4>", unsafe_allow_html=True)

    if st.button("🚪 Logout"):
        st.session_state.login = False
        st.rerun()
