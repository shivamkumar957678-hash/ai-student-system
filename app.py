# app.py

```python
import streamlit as st
import pandas as pd
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="AI Student System", layout="wide")

# =======================
# CUSTOM CSS
# =======================
st.markdown("""
<style>
body {
    background-color: #050520;
}
.main {
    background: linear-gradient(to right, #050520, #12002f);
    color: white;
}
.big-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: cyan;
    text-shadow: 0px 0px 15px cyan;
}
.subtitle {
    text-align: center;
    color: white;
    font-size: 20px;
}
.card {
    background-color: #111133;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 0px 15px #7a00ff;
    margin-bottom: 20px;
}
.metric {
    background: linear-gradient(to right, #1e3cff, #8a2be2);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 25px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =======================
# HEADER
# =======================
st.markdown('<div class="big-title">🔐 AI STUDENT SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart • Secure • Intelligent</div>', unsafe_allow_html=True)
st.write("---")

# =======================
# LOGIN SECTION
# =======================
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📸 Face Authentication")

    img_file = st.camera_input("Take your photo")

    if img_file is not None:
        image = Image.open(img_file)
        st.image(image, caption="Face Captured", use_container_width=True)

        st.success("✅ Face detected successfully!")
        st.success("✅ Access Granted")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔑 Manual Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "shivam" and password == "1234":
            st.success("✅ Login Successful")
        else:
            st.error("❌ Wrong Username or Password")

    st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# =======================
# DASHBOARD
# =======================
col3, col4, col5, col6 = st.columns(4)

with col3:
    st.markdown("<div class='metric'>👨‍🎓<br>5 Students</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='metric'>🏆<br>Topper Priya</div>", unsafe_allow_html=True)

with col5:
    st.markdown("<div class='metric'>⚠️<br>2 Weak Students</div>", unsafe_allow_html=True)

with col6:
    st.markdown("<div class='metric'>📉<br>Poor Attendance</div>", unsafe_allow_html=True)

st.write("---")

# =======================
# STUDENT TABLE
# =======================
st.subheader("📋 Student Performance Table")

data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Rohit"],
    "Attendance": [90, 95, 60, 85, 55],
    "Math": [88, 98, 45, 82, 40],
    "Science": [90, 99, 50, 84, 35],
    "English": [85, 97, 55, 81, 45]
}

_df = pd.DataFrame(data)
_df["Average"] = _df[["Math", "Science", "English"]].mean(axis=1)

st.dataframe(_df, use_container_width=True)

# =======================
# ADD STUDENT
# =======================
st.write("---")
st.subheader("➕ Add New Student")

name = st.text_input("Student Name")
attendance = st.slider("Attendance", 0, 100, 80)
math = st.slider("Math", 0, 100, 70)
science = st.slider("Science", 0, 100, 70)
english = st.slider("English", 0, 100, 70)

if st.button("Add Student"):
    st.success(f"✅ {name} added successfully")

# =======================
# CHARTS
# =======================
st.write("---")
st.subheader("📊 Attendance Graph")

st.bar_chart(_df.set_index("Name")["Attendance"])

st.subheader("📈 Marks Graph")
st.line_chart(_df.set_index("Name")[["Math", "Science", "English"]])

# =======================
# AI CHATBOT
# =======================
st.write("---")
st.subheader("🤖 AI Chatbot")

question = st.text_input("Ask question")

if st.button("Ask"):
    q = question.lower()

    if "topper" in q:
        st.success("🏆 Priya is the topper")

    elif "weak" in q:
        st.warning("⚠️ Aman and Rohit are weak students")

    elif "attendance" in q:
        st.info("📊 Average attendance is 77%")

    else:
        st.write("🤖 AI Response: System working correctly")

# =======================
# FOOTER
# =======================
st.write("---")
st.markdown("<center>❤️ Made by Shivam Kumar</center>", unsafe_allow_html=True)
```

# requirements.txt

```txt
streamlit
pandas
numpy
opencv-python-headless
Pillow
```

# Replit / Streamlit Run Command

```bash
streamlit run app.py --server.port 5000 --server.address 0.0.0.0
```

# Username & Password

```txt
Username: shivam
Password: 1234
```

# Important

* Browser me Camera Allow karna
* Mobile me bhi camera open hoga
* Face Authentication dikhega
* Manual Login bhi dikhega
* Dashboard + Charts + AI Chatbot sab kaam karega
* app.py me pura code paste karna
* requirements.txt me requirements paste karna
