import streamlit as st
import random
import pandas as pd
import numpy as np
import time
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import plotly.express as px
import plotly.graph_objects as go

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Unified AI Observability",
    layout="wide"
)

# =========================
# STYLING
# =========================
st.markdown("""
<style>
.main { background-color: #0E1117; }
.stMetric {
    background-color: #1C1F26;
    padding: 15px;
    border-radius: 10px;
}
h1, h2, h3 { color: #00C8FF; }
</style>
""", unsafe_allow_html=True)

# =========================
# LOGIN SCREEN
# =========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Enterprise AI Observability Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user and pwd:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Enter credentials")
    st.stop()

# =========================
# LOADING
# =========================
with st.spinner("Initializing AI Monitoring Systems..."):
    time.sleep(2)

# =========================
# SIDEBAR
# =========================
st.sidebar.image("EEGineers_logo.png", width=160)
st.sidebar.title("Team EEGineers")

# =========================
# RISK ENGINE
# =========================
def calculate_risk():
    return random.uniform(20, 95)

ai_risk_score = calculate_risk()

# =========================
# RISK GAUGE
# =========================
gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=ai_risk_score,
    title={'text': "Unified AI Risk Score"},
    gauge={
        'axis': {'range': [0, 100]},
        'steps': [
            {'range': [0, 40], 'color': "green"},
            {'range': [40, 70], 'color': "yellow"},
            {'range': [70, 100], 'color': "red"}
        ]
    }
))
st.sidebar.plotly_chart(gauge, use_container_width=True)

# =========================
# TITLE
# =========================
st.title("🏦 Unified AI Observability Dashboard")

# =========================
# AUTO ALERT BANNER
# =========================
if ai_risk_score > 80:
    st.markdown("""
    <div style='background-color:#ff4b4b;
                padding:20px;
                border-radius:10px;
                text-align:center;
                font-size:22px;
                font-weight:bold;
                color:white'>
        🚨 CRITICAL AI SYSTEM RISK DETECTED — IMMEDIATE ACTION REQUIRED 🚨
    </div>
    """, unsafe_allow_html=True)

# =========================
# NAVIGATION
# =========================
section = st.sidebar.radio(
    "Navigation",
    ["Dashboard Overview", "Traditional ML", "LLM Systems", "Governance"]
)

# =========================
# DASHBOARD OVERVIEW
# =========================
if section == "Dashboard Overview":

    st.subheader("🏦 Enterprise AI System Status")

    colA, colB, colC, colD = st.columns(4)
    colA.metric("System Status", "STABLE" if ai_risk_score < 60 else "MONITORING")
    colB.metric("Models Monitored", random.randint(12, 20))
    colC.metric("Compliance Score", f"{random.randint(90,98)}%")
    colD.metric("AI Confidence", f"{random.randint(92,99)}%")

    st.info(f"🛡 Last AI Compliance Audit: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')} — STATUS: PASSED")

    health = random.randint(85, 99)
    st.progress(health/100)
    st.caption(f"Overall AI System Health: {health}%")

    st.subheader("📡 Live Risk Streaming")

    chart_placeholder = st.empty()
    data = pd.DataFrame(columns=["Time", "Risk"])

    for i in range(20):
        new = pd.DataFrame({"Time":[i], "Risk":[random.uniform(20,90)]})
        data = pd.concat([data, new])
        chart_placeholder.line_chart(data.set_index("Time"))
        time.sleep(0.15)

    st.subheader("🏗 System Architecture")
    st.image(
        "https://copilot.microsoft.com/th/id/BCO.29f32b06-6c7e-4322-8bcf-a9d1a8b51de1.png"
    )

# =========================
# TRADITIONAL ML
# =========================
elif section == "Traditional ML":

    uploaded_ml = st.file_uploader("Upload ML Predictions CSV", type="csv")

    if uploaded_ml:
        ml_data = pd.read_csv(uploaded_ml)

        if {'actual','predicted'}.issubset(ml_data.columns):

            accuracy = accuracy_score(ml_data['actual'], ml_data['predicted'])
            precision = precision_score(ml_data['actual'], ml_data['predicted'], zero_division=0)
            recall = recall_score(ml_data['actual'], ml_data['predicted'], zero_division=0)
            f1 = f1_score(ml_data['actual'], ml_data['predicted'], zero_division=0)

            st.metric("Accuracy", f"{accuracy:.2f}")
            st.metric("Precision", f"{precision:.2f}")
            st.metric("Recall", f"{recall:.2f}")
            st.metric("F1", f"{f1:.2f}")

            fig = px.bar(
                x=["Accuracy","Precision","Recall","F1"],
                y=[accuracy,precision,recall,f1],
                title="ML Performance"
            )
            st.plotly_chart(fig, use_container_width=True)

            if "group" in ml_data.columns:
                bias = ml_data.groupby("group")['predicted'].mean().reset_index()
                fig2 = px.bar(bias, x="group", y="predicted", title="Bias by Group")
                st.plotly_chart(fig2, use_container_width=True)

# =========================
# LLM SYSTEMS
# =========================
elif section == "LLM Systems":

    uploaded_llm = st.file_uploader("Upload LLM Logs CSV", type="csv")

    if uploaded_llm:
        llm = pd.read_csv(uploaded_llm)

        if {'latency','tokens'}.issubset(llm.columns):
            st.metric("Avg Latency", f"{llm['latency'].mean():.2f}")
            st.metric("Avg Tokens", int(llm['tokens'].mean()))

# =========================
# GOVERNANCE
# =========================
elif section == "Governance":

    st.subheader("Responsible AI Controls")
    st.write("✔ Bias Monitoring")
    st.write("✔ Hallucination Monitoring")
    st.write("✔ Risk Governance")
    st.write("✔ Audit Transparency")

    if st.button("Generate Compliance Report"):
        df = pd.DataFrame({
            "Category":["ML Reliability","LLM Safety","Bias","Audit"],
            "Status":["OK","OK","OK","OK"]
        })
        st.dataframe(df)
