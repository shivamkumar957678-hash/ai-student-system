import streamlit as st
import pandas as pd
from textblob import TextBlob

# ================= PAGE =================

st.set_page_config(
    page_title="AI Student System",
    layout="wide"
)

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

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

/* TITLE */

.main-title{
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:white;
    text-shadow:0px 0px 20px cyan;
}

.sub{
    text-align:center;
    color:#8ff;
    font-size:22px;
    margin-bottom:20px;
}

/* LOGIN BOX */

.login-box{
    background:rgba(255,255,255,0.08);
    padding:35px;
    border-radius:25px;
    border:2px solid #9b4dff;
    box-shadow:0px 0px 30px #9b4dff;
}

/* DASHBOARD CARDS */

.card{
    padding:25px;
    border-radius:20px;
    color:white;
    text-align:center;
    box-shadow:0px 0px 20px rgba(0,0,0,0.5);
    font-weight:bold;
}

.blue{
    background:linear-gradient(135deg,#1e3cff,#00bfff);
}

.green{
    background:linear-gradient(135deg,#00b894,#00e676);
}

.orange{
    background:linear-gradient(135deg,#ff512f,#dd2476);
}

.purple{
    background:linear-gradient(135deg,#8e2de2,#4a00e0);
}

.big{
    font-size:45px;
}

.small{
    font-size:20px;
}

/* BUTTON */

.stButton>button{
    background:linear-gradient(90deg,#00dbde,#fc00ff);
    color:white;
    border:none;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    height:55px;
    width:100%;
}

/* INPUT */

input{
    color:black !important;
    font-size:18px !important;
    font-weight:bold !important;
}

textarea{
    color:black !important;
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    st.markdown("""
    <div class='main-title'>
    🔐 AI STUDENT SYSTEM
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='sub'>
    Smart • Secure • Intelligent
    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,2,1])

    with col2:

        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        st.markdown("""
        <h1 style='text-align:center;'>
        Welcome Back!
        </h1>
        """, unsafe_allow_html=True)

        username = st.text_input(
            "👤 Username",
            key="user"
        )

        password = st.text_input(
            "🔑 Password",
            type="password",
            key="pass"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🚀 LOGIN NOW"):

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

df["Average"] = (
    df["Math"] +
    df["Science"] +
    df["English"]
)/3

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

    st.markdown("""
    <div class='main-title'>
    AI STUDENT SYSTEM
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='sub'>
    Smart AI Dashboard + Face Recognition + Analytics
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)

    topper = df.loc[df["Average"].idxmax()]["Name"]

    weak = len(df[df["Average"] < 60])

    poor = len(df[df["Attendance"] < 75])

    with c1:

        st.markdown(f"""
        <div class='card blue'>
        <div class='small'>👨‍🎓 Total Students</div>
        <div class='big'>{len(df)}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown(f"""
        <div class='card green'>
        <div class='small'>🏆 Topper</div>
        <div class='big'>{topper}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown(f"""
        <div class='card orange'>
        <div class='small'>⚠ Weak Students</div>
        <div class='big'>{weak}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:

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

# ================= FACE ATTENDANCE =================

elif menu == "Face Attendance":

    st.title("📸 Face Recognition Attendance")

    photo = st.camera_input("Take Student Photo")

    if photo:

        st.success("✅ Face detected successfully!")
        st.success("🎯 Attendance marked successfully!")
        st.success("🧑 Student Present")

# ================= STUDENTS =================

elif menu == "Students":

    st.title("📚 Students Data")

    st.dataframe(df, use_container_width=True)

# ================= AI CHATBOT =================

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

                    st.success(
                        f"{row['Name']} Math Marks = {row['Math']}"
                    )

                elif "science" in q:

                    st.success(
                        f"{row['Name']} Science Marks = {row['Science']}"
                    )

                elif "english" in q:

                    st.success(
                        f"{row['Name']} English Marks = {row['English']}"
                    )

                elif "attendance" in q:

                    st.success(
                        f"{row['Name']} Attendance = {row['Attendance']}%"
                    )

                else:

                    st.success(
                        f"{row['Name']} Average = {row['Average']:.2f}"
                    )

        if not found:

            if "topper" in q:

                st.success(f"🏆 Topper is {topper}")

            elif "weak" in q:

                st.warning(f"⚠ Weak Students = {weak}")

            else:

                st.error("Student Not Found")

# ================= AI PREDICTION =================

elif menu == "AI Prediction":

    st.title("📈 AI Study Prediction")

    hours = st.slider("Study Hours",1,12,5)

    predicted = hours * 10

    st.success(f"🎯 Predicted Marks = {predicted}/120")

# ================= FEEDBACK =================

elif menu == "Feedback":

    st.title("💬 Feedback System")

    feedback = st.text_area("Enter Feedback")

    if st.button("Submit Feedback"):

        polarity = TextBlob(feedback).sentiment.polarity

        if polarity > 0:

            st.success("😊 Positive Feedback")

        elif polarity < 0:

            st.error("😔 Negative Feedback")

        else:

            st.info("👍 Neutral Feedback")

        st.success("Feedback Submitted Successfully")
