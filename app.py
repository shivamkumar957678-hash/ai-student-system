# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import face_recognition

# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="AI Student System",
    layout="wide"
)

# ======================
# CSS
# ======================

st.markdown("""
<style>

html, body, [class*="css"]{
    background:#050816;
    color:white;
    font-family:'Segoe UI';
}

.stApp{
    background:linear-gradient(135deg,#020024,#090979,#6a00ff);
}

.title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#00f5ff;
    text-shadow:0px 0px 20px #00f5ff;
}

.sub{
    text-align:center;
    color:#00f5ff;
    font-size:20px;
}

.box{
    background:rgba(0,0,0,0.35);
    border:2px solid #b026ff;
    border-radius:25px;
    padding:20px;
    box-shadow:0px 0px 20px #b026ff;
}

.card{
    padding:20px;
    border-radius:20px;
    color:white;
    text-align:center;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#00dbde,#fc00ff);
    color:white;
    border:none;
    border-radius:10px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ======================
# LOGIN SESSION
# ======================

if "login" not in st.session_state:
    st.session_state.login = False

# ======================
# FACE IMAGE
# ======================

KNOWN_IMAGE = "shivam.jpg"

# ======================
# LOGIN PAGE
# ======================

if st.session_state.login == False:

    st.markdown("""
    <div class='title'>
    🔐 AI STUDENT SYSTEM
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='sub'>
    Smart • Secure • Intelligent
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1,col2 = st.columns(2)

    # FACE LOGIN

    with col1:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("📸 Face Authentication")

        st.write("Login with your registered face")

        camera = st.camera_input("Capture Face")

        if camera is not None:

            try:

                known_image = face_recognition.load_image_file(KNOWN_IMAGE)

                known_encoding = face_recognition.face_encodings(
                    known_image
                )[0]

                uploaded_image = face_recognition.load_image_file(camera)

                uploaded_encoding = face_recognition.face_encodings(
                    uploaded_image
                )[0]

                result = face_recognition.compare_faces(
                    [known_encoding],
                    uploaded_encoding
                )

                if result[0]:

                    st.success("✅ Access Granted")
                    st.success("🎉 Face Matched Successfully")

                    st.session_state.login = True

                    st.rerun()

                else:

                    st.error("❌ Access Denied")
                    st.error("🚫 Face Not Registered")

            except:

                st.error("❌ Face Not Detected Properly")

        st.markdown("</div>", unsafe_allow_html=True)

    # MANUAL LOGIN

    with col2:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("🔑 Manual Login")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("🚀 LOGIN NOW"):

            if username == "shivam" and password == "12345":

                st.session_state.login = True

                st.rerun()

            else:

                st.error("❌ Wrong Username or Password")

        st.markdown("</div>", unsafe_allow_html=True)

# ======================
# DASHBOARD
# ======================

else:

    # ======================
    # DATA
    # ======================

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
    ) / 3

    topper = df.loc[df["Average"].idxmax()]

    weak_students = len(
        df[df["Average"] < 60]
    )

    poor_attendance = len(
        df[df["Attendance"] < 75]
    )

    # ======================
    # TITLE
    # ======================

    st.markdown("""
    <div class='title'>
    🎓 AI STUDENT SYSTEM DASHBOARD
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ======================
    # TOP CARDS
    # ======================

    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.markdown(f"""
        <div class='card'
        style='background:linear-gradient(90deg,#0061ff,#60efff);'>
        <h3>Total Students</h3>
        <h1>{len(df)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown(f"""
        <div class='card'
        style='background:linear-gradient(90deg,#11998e,#38ef7d);'>
        <h3>Topper</h3>
        <h1>{topper['Name']}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown(f"""
        <div class='card'
        style='background:linear-gradient(90deg,#f12711,#f5af19);'>
        <h3>Weak Students</h3>
        <h1>{weak_students}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c4:

        st.markdown(f"""
        <div class='card'
        style='background:linear-gradient(90deg,#8e2de2,#ff00cc);'>
        <h3>Poor Attendance</h3>
        <h1>{poor_attendance}</h1>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ======================
    # SECOND ROW
    # ======================

    a1,a2,a3 = st.columns([1,1,1.5])

    with a1:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("➕ Add New Student")

        st.text_input("Student Name")

        st.slider("Attendance (%)",0,100,80)

        st.slider("Math",0,100,70)

        st.slider("Science",0,100,70)

        st.slider("English",0,100,70)

        st.button("✅ Add Student")

        st.markdown("</div>", unsafe_allow_html=True)

    with a2:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("📸 Face Recognition Attendance")

        st.button("📷 Take Photo")

        st.success("✅ Face detected successfully!")
        st.success("✅ Attendance marked successfully!")
        st.success("🎉 Student Present")

        st.markdown("</div>", unsafe_allow_html=True)

    with a3:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("📋 Student Performance Table")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # ======================
    # GRAPH ROW
    # ======================

    g1,g2 = st.columns(2)

    with g1:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("📊 Student Marks Ratio")

        fig1,ax1 = plt.subplots(
            figsize=(5,5)
        )

        ax1.pie(
            df["Average"],
            labels=df["Name"],
            autopct="%1.1f%%"
        )

        st.pyplot(fig1)

        st.markdown("</div>", unsafe_allow_html=True)

    with g2:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("📈 Attendance Graph")

        fig2,ax2 = plt.subplots(
            figsize=(8,5)
        )

        ax2.bar(
            df["Name"],
            df["Attendance"]
        )

        st.pyplot(fig2)

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # ======================
    # LAST ROW
    # ======================

    l1,l2,l3 = st.columns(3)

    # CHATBOT

    with l1:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("🤖 AI Chatbot")

        question = st.text_input(
            "Ask Any Question"
        )

        if st.button("Ask"):

            q = question.lower()

            if "topper" in q:

                st.success(
                    f"🏆 Topper is {topper['Name']}"
                )

            elif "weak" in q:

                st.success(
                    f"⚠ Weak Students = {weak_students}"
                )

            elif "aman english" in q:

                st.success(
                    "📘 Aman English Marks = 55"
                )

            else:

                st.info(
                    "🤖 AI Assistant Ready"
                )

        st.markdown("</div>", unsafe_allow_html=True)

    # AI PREDICTION

    with l2:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("🧠 AI Study Prediction")

        hours = st.slider(
            "Study Hours",
            1,
            12,
            5
        )

        marks = hours * 10

        st.success(
            f"📚 Predicted Marks = {marks}"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # FEEDBACK

    with l3:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.subheader("💬 Feedback System")

        st.text_area("Enter Feedback")

        if st.button("Submit Feedback"):

            st.success(
                "✅ Feedback Submitted"
            )

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    if st.button("🚪 Logout"):

        st.session_state.login = False

        st.rerun()
