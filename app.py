# =========================
# FACE ATTENDANCE FINAL
# =========================

import streamlit as st
import face_recognition
from PIL import Image
import numpy as np

st.set_page_config(page_title="AI Student System", layout="wide")

# ================= CSS =================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#020024,#6d28d9);
    color:white;
}

.big-title{
    text-align:center;
    font-size:70px;
    font-weight:bold;
    color:white;
    text-shadow:0px 0px 20px #00ffcc;
}

.success-box{
    background:#16a34a;
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:35px;
    font-weight:bold;
    color:white;
    box-shadow:0px 0px 20px #00ff99;
}

.fail-box{
    background:#dc2626;
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:35px;
    font-weight:bold;
    color:white;
    box-shadow:0px 0px 20px red;
}

.metric-card{
    background:linear-gradient(135deg,#16a34a,#22c55e);
    padding:35px;
    border-radius:25px;
    text-align:center;
    box-shadow:0px 0px 25px rgba(0,255,100,0.6);
}

.metric-title{
    font-size:28px;
    font-weight:bold;
    color:white;
}

.metric-value{
    font-size:60px;
    font-weight:bold;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================

if "login" not in st.session_state:
    st.session_state.login = False

if st.session_state.login == False:

    st.markdown("<div class='big-title'>🔐 AI Student System Login</div>", unsafe_allow_html=True)

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("🚀 Login"):

        if username == "admin" and password == "admin123":
            st.session_state.login = True
            st.rerun()

        else:
            st.error("Wrong Username or Password")

# ================= MAIN APP =================

else:

    st.markdown("<div class='big-title'>🎓 AI Student System</div>", unsafe_allow_html=True)

    st.write("")

    # ===== DASHBOARD =====

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-title">👨‍🎓 Total Students</div>
        <div class="metric-value">5</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-title">🏆 Topper</div>
        <div class="metric-value">Priya</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-title">⚠ Weak Students</div>
        <div class="metric-value">2</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-title">📉 Poor Attendance</div>
        <div class="metric-value">2</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ================= FACE RECOGNITION =================

    st.header("📸 AI Face Attendance System")

    st.info("Only Shivam Face Attendance Allowed")

    # ===== ORIGINAL IMAGE =====

    known_image = face_recognition.load_image_file("shivam.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    # ===== CAMERA =====

    uploaded_image = st.camera_input("Take Student Photo")

    if uploaded_image is not None:

        image = Image.open(uploaded_image)
        image_np = np.array(image)

        face_locations = face_recognition.face_locations(image_np)

        if len(face_locations) == 0:

            st.markdown("""
            <div class='fail-box'>
            ❌ FACE NOT DETECTED
            </div>
            """, unsafe_allow_html=True)

        else:

            uploaded_encoding = face_recognition.face_encodings(image_np)[0]

            results = face_recognition.compare_faces(
                [known_encoding],
                uploaded_encoding
            )

            if results[0]:

                st.markdown("""
                <div class='success-box'>
                ✅ FACE VERIFIED SUCCESSFULLY
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div class='success-box'>
                🎯 ATTENDANCE MARKED SUCCESSFULLY
                </div>
                """, unsafe_allow_html=True)

            else:

                st.markdown("""
                <div class='fail-box'>
                ❌ UNKNOWN FACE DETECTED
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div class='fail-box'>
                🚫 ATTENDANCE DENIED
                </div>
                """, unsafe_allow_html=True)
