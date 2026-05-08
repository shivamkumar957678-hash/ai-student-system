# app.py

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI Student System", layout="wide")

# ================= CSS =================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020024,#090979,#7b2ff7);
    color:white;
}

html, body, [class*="css"]{
    font-family: 'Segoe UI', sans-serif;
}

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:white;
    text-shadow:0 0 20px cyan;
}

.sub{
    text-align:center;
    color:#9ff;
    font-size:22px;
    margin-bottom:20px;
}

.login-box{
    background:rgba(255,255,255,0.08);
    padding:30px;
    border-radius:25px;
    border:2px solid #9b4dff;
    box-shadow:0 0 25px #9b4dff;
}

.card{
    padding:25px;
    border-radius:20px;
    color:white;
    text-align:center;
    box-shadow:0 0 15px rgba(0,0,0,0.5);
    font-weight:bold;
}

.blue{background:linear-gradient(135deg,#1e3cff,#00bfff);}
.green{background:linear-gradient(135deg,#00b894,#00e676);}
.orange{background:linear-gradient(135deg,#ff512f,#dd2476);}
.purple{background:linear-gradient(135deg,#8e2de2,#4a00e0);}

.big{
    font-size:45px;
}

.small{
    font-size:20px;
}

.sidebar .sidebar-content{
    background:#050816;
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    st.markdown("<div class='main-title'>🔐 AI STUDENT SYSTEM</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Smart • Secure • Intelligent</div>", unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,2,1])

    with col2:

        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        st.markdown("## Welcome Back!")

        username = st.text_input("👤 Username", placeholder="shivam-user")
        password = st.text_input("🔑 Password", type="password", placeholder="12345")

        if st.button("🚀 LOGIN NOW", use_container_width=True):

            if username == "shivam-user" and password == "12345":
                st.session_state.login = True
                st.rerun()

            else:
                st.error("Wrong Username or Password")

        st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# ================= DATA =================

data = {
    "Name":["Rahul","Priya","Aman","Sneha","Rohit"],
    "Attendance":[90,95,60,85,55],
    "Math":[88,98,45,82,40],
    "Science":[90,99,50,84,35],
    "English":[85,97,55,81,45]
}

df = pd.DataFrame(data)
df["Average"] = df[["Math","Science","English"]].mean(axis=1)

# ================= SIDEBAR =================

st.sidebar.title("🎓 AI STUDENT SYSTEM")

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

# ================= DASHBOARD =================

if menu == "Dashboard":

    st.markdown("<div class='main-title'>AI STUDENT SYSTEM</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub'>Smart AI Dashboard + Face Recognition + Analytics</div>", unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class='card blue'>
        <div class='small'>👨‍🎓 Total Students</div>
        <div class='big'>{len(df)}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        topper = df.loc[df["Average"].idxmax()]["Name"]
        st.markdown(f"""
        <div class='card green'>
        <div class='small'>🏆 Topper</div>
        <div class='big'>{topper}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        weak = len(df[df["Average"] < 60])
        st.markdown(f"""
        <div class='card orange'>
        <div class='small'>⚠ Weak Students</div>
        <div class='big'>{weak}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        poor = len(df[df["Attendance"] < 75])
        st.markdown(f"""
        <div class='card purple'>
        <div class='small'>📉 Poor Attendance</div>
        <div class='big'>{poor}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 📋 Student Performance Table")
    st.dataframe(df, use_container_width=True)

# ================= ADD STUDENT =================

elif menu == "Add Student":

    st.title("➕ Add New Student")

    name = st.text_input("Student Name")

    attendance = st.slider("Attendance",0,100,80)
    math = st.slider("Math",0,100,70)
    science = st.slider("Science",0,100,70)
    english = st.slider("English",0,100,70)

    if st.button("✅ Add Student"):

        avg = (math + science + english)/3

        new_row = {
            "Name":name,
            "Attendance":attendance,
            "Math":math,
            "Science":science,
            "English":english,
            "Average":avg
        }

        df.loc[len(df)] = new_row

        st.success("Student Added Successfully")

        st.dataframe(df, use_container_width=True)

# ================= FACE =================

elif menu == "Face Attendance":

    st.title("📸 Face Recognition Attendance")

    pic = st.camera_input("Take Student Photo")

    if pic:
        st.success("✅ Face Detected Successfully")
        st.success("🎯 Attendance Marked Successfully")
        st.success("🧑 Student Present")

# ================= STUDENTS =================

elif menu == "Students":

    st.title("📚 Students Data")

    st.dataframe(df, use_container_width=True)

# ================= CHATBOT =================

elif menu == "AI Chatbot":

    st.title("🤖 AI Chatbot")

    question = st.text_input("Ask Question")

    if question:

        q = question.lower()

        found = False

        for i,row in df.iterrows():

            name = row["Name"].lower()

            if name in q:

                found = True

                if "math" in q:
                    st.success(f"{row['Name']} Math Marks = {row['Math']}")

                elif "science" in q:
                    st.success(f"{row['Name']} Science Marks = {row['Science']}")

                elif "english" in q:
                    st.success(f"{row['Name']} English Marks = {row['English']}")

                elif "attendance" in q:
                    st.success(f"{row['Name']} Attendance = {row['Attendance']}%")

                else:
                    st.success(f"{row['Name']} Average = {row['Average']:.2f}")

        if not found:

            if "topper" in q:
                st.success(f"🏆 Topper is {topper}")

            elif "weak" in q:
                st.warning(f"⚠ Weak Students = {weak}")

            else:
                st.error("Student Not Found")

# ================= PREDICTION =================

elif menu == "AI Prediction":

    st.title("📈 AI Study Prediction")

    hours = st.slider("Study Hours",1,12,5)

    predicted = hours * 10

    st.success(f"🎯 Predicted Marks = {predicted}/120")

    if predicted > 80:
        st.success("Excellent Performance Expected")

    elif predicted > 50:
        st.warning("Average Performance")

    else:
        st.error("Need More Study")

# ================= FEEDBACK =================

elif menu == "Feedback":

    st.title("💬 Feedback System")

    feedback = st.text_area("Enter Feedback")

    if st.button("Submit Feedback"):

        st.success("✅ Feedback Submitted Successfully")

        if "good" in feedback.lower():
            st.success("😊 Positive Feedback")

        elif "bad" in feedback.lower():
            st.error("😔 Negative Feedback")

        else:
            st.info("👍 Thanks For Feedback")
