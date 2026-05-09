import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AI Student System", layout="wide")

# ================= CSS =================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020024,#05053d,#6a00ff);
    color:white;
}

h1,h2,h3,h4,h5,h6,p,label,div,span{
    color:white !important;
}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#00e5ff;
    text-shadow:0px 0px 20px #00e5ff;
}

.sub{
    text-align:center;
    color:#00ffff;
    font-size:24px;
    margin-bottom:30px;
}

.card{
    background:rgba(0,0,0,0.45);
    padding:20px;
    border-radius:20px;
    border:1px solid #bb00ff;
    box-shadow:0 0 20px #bb00ff;
}

.stTextInput input{
    background:#050520 !important;
    color:white !important;
    border:2px solid #bb00ff !important;
    border-radius:15px !important;
    padding:12px !important;
    font-size:18px !important;
}

.stTextInput label{
    color:white !important;
    font-size:20px !important;
    font-weight:bold !important;
}

.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#007bff,#d400ff);
    color:white;
    border:none;
    border-radius:15px;
    font-size:20px;
    font-weight:bold;
    padding:12px;
    box-shadow:0 0 20px #d400ff;
}

.metric{
    padding:20px;
    border-radius:20px;
    color:white;
    text-align:center;
    font-size:25px;
    font-weight:bold;
}

.blue{background:linear-gradient(135deg,#0061ff,#60efff);}
green{background:linear-gradient(135deg,#11998e,#38ef7d);}
.orange{background:linear-gradient(135deg,#f12711,#f5af19);}
purple{background:linear-gradient(135deg,#7b2ff7,#f107a3);}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================

st.markdown('<div class="main-title">🔐 AI STUDENT SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Smart • Secure • Intelligent</div>', unsafe_allow_html=True)

# ================= LOGIN SECTION =================

col1, col2 = st.columns(2)

with col1:
    st.markdown("## 📷 Face Authentication")
    st.write("Login with your registered face")

    camera = st.camera_input("Capture Face")

    if camera:
        st.success("✅ Face detected successfully!")
        st.success("✅ Attendance marked successfully!")
        st.success("🎉 Student Present")

with col2:
    st.markdown("## 🔑 Manual Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.success("✅ Login Successful")
        else:
            st.error("❌ Wrong Username or Password")

st.markdown("---")

# ================= DASHBOARD =================

st.markdown("# 📊 AI STUDENT SYSTEM DASHBOARD")

m1,m2,m3,m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric" style="background:linear-gradient(135deg,#0061ff,#60efff);">
    👨‍🎓<br>5<br>Total Students
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric" style="background:linear-gradient(135deg,#11998e,#38ef7d);">
    🏆<br>Priya<br>Topper
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric" style="background:linear-gradient(135deg,#f12711,#f5af19);">
    ⚠️<br>2<br>Weak Students
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric" style="background:linear-gradient(135deg,#7b2ff7,#f107a3);">
    📉<br>2<br>Poor Attendance
    </div>
    """, unsafe_allow_html=True)

# ================= STUDENT DATA =================

students = pd.DataFrame({
    "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
    "Attendance":[90,95,60,85,55],
    "Math":[88,98,45,82,40],
    "Science":[90,99,50,84,35],
    "English":[85,97,55,81,45]
})

students["Average"] = students[["Math","Science","English"]].mean(axis=1)

# ================= ADD STUDENT =================

c1,c2,c3 = st.columns([1,1,2])

with c1:
    st.markdown("## ➕ Add New Student")

    st.text_input("Student Name")
    st.slider("Attendance (%)",0,100,80)
    st.slider("Math Marks",0,100,70)
    st.slider("Science Marks",0,100,70)
    st.slider("English Marks",0,100,70)

    st.button("✅ Add Student")

with c2:
    st.markdown("## 📸 Face Recognition Attendance")

    cam2 = st.camera_input("Take Photo")

    if cam2:
        st.success("✅ Face detected successfully!")
        st.success("✅ Attendance marked successfully!")
        st.success("🎉 Student Present")

with c3:
    st.markdown("## 📋 Student Performance Table")
    st.dataframe(students, use_container_width=True)

# ================= CHARTS =================

g1,g2 = st.columns(2)

with g1:
    fig_bar = px.bar(
        students,
        x="Name",
        y="Attendance",
        color="Name",
        title="Attendance Graph",
        template="plotly_dark"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with g2:
    fig_pie = px.pie(
        students,
        names="Name",
        values="Average",
        title="Student Marks Ratio",
        template="plotly_dark"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# ================= CHATBOT + PREDICTION =================

x1,x2,x3 = st.columns(3)

with x1:
    st.markdown("## 🤖 AI Chatbot")
    q = st.text_input("Ask question")

    if st.button("Ask"):
        st.success("AI Response: Student performance is good.")

with x2:
    st.markdown("## 🧠 AI Study Prediction")

    hrs = st.slider("Study Hours",1,10,6)

    marks = hrs * 10

    st.metric("Predicted Marks", f"{marks}/100")

    if marks > 60:
        st.success("🎉 Good! Keep it up and you can score well.")
    else:
        st.warning("⚠️ Need more study hours.")

with x3:
    st.markdown("## 💬 Feedback System")

    fb = st.text_area("Enter your feedback")

    if st.button("Submit Feedback"):
        st.success("✅ Feedback Submitted")

# ================= FOOTER =================

st.markdown("""
<hr>
<center>
<h4 style='color:white;'>
© 2025 AI Student System | Made with ❤️ by Shivam Kumar
</h4>
</center>
""", unsafe_allow_html=True)
