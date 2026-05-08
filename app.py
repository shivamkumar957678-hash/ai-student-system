import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# =========================
# GRAPH SECTION
# =========================

st.markdown("## 📊 Student Analytics Dashboard")

students = ["Rahul", "Priya", "Aman", "Sneha", "Rohit"]
marks = [88, 98, 50, 82, 40]
attendance = [90, 95, 60, 85, 55]

df = pd.DataFrame({
    "Students": students,
    "Marks": marks,
    "Attendance": attendance
})

col1, col2 = st.columns(2)

# ================= PIE CHART =================
with col1:
    st.markdown("### 🎯 Student Marks Ratio")

    fig1, ax1 = plt.subplots(figsize=(5,5))

    colors = ["#00E5FF", "#00FF85", "#FF9800", "#FF00E5", "#FF1744"]

    ax1.pie(
        marks,
        labels=students,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90
    )

    ax1.axis('equal')
    st.pyplot(fig1)

# ================= BAR GRAPH =================
with col2:
    st.markdown("### 📈 Attendance Graph")

    fig2, ax2 = plt.subplots(figsize=(6,5))

    bars = ax2.bar(
        students,
        attendance,
        color=["#00E5FF","#00FF85","#FF9800","#FF00E5","#FF1744"]
    )

    ax2.set_ylim(0,100)
    ax2.set_ylabel("Attendance %")
    ax2.set_xlabel("Students")

    st.pyplot(fig2)

# ================= TABLE =================
st.markdown("### 📋 Student Performance Table")

st.dataframe(df, use_container_width=True)
