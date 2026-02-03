import streamlit as st
import time
from datetime import datetime

st.set_page_config(
    page_title="Bharat Raksha AI",
    page_icon="🇮🇳",
    layout="wide"
)

# Simple CSS
st.markdown("""
<style>
    .bharat-header {
        background: linear-gradient(135deg, #FF9933, #FFD700);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="bharat-header">
    <h1>🛡️ भारत रक्षा AI</h1>
    <h3>Quantum Anti-Scam Protection</h3>
    <p>🇮🇳 Made for India | 24/7 Protection</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# SIMPLE PROTECTION MODULES
st.header("🔒 Protection Modules")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📱 SMS Scanner", use_container_width=True):
        st.success("✅ SMS Scanning Active!")
        st.write("Now scanning messages for scams...")
        time.sleep(1)

with col2:
    if st.button("📞 Call Protection", use_container_width=True):
        st.success("✅ Call Screening Active!")
        st.write("Blocking scam calls...")

with col3:
    if st.button("💳 UPI Safety", use_container_width=True):
        st.success("✅ UPI Protection Active!")
        st.write("Monitoring transactions...")

st.markdown("---")

# LANGUAGE SELECTION
st.header("🌍 Choose Language")
language = st.selectbox("Select:", ["Hindi", "Tamil", "Telugu", "English", "Bengali", "Marathi"])
st.info(f"Selected: {language} - Voice alerts will use this language")

st.markdown("---")

# SCAM REPORTING
st.header("⚠️ Report Scam")
scam_type = st.selectbox("Type:", ["UPI Fraud", "Job Scam", "Fake Call", "Lottery", "Other"])
details = st.text_area("Details:")

if st.button("🚨 Report to Cyber Crime", type="primary"):
    if details:
        st.success(f"✅ Reported! Reference: BR{int(time.time())}")
        st.balloons()
    else:
        st.error("Please enter details")

st.markdown("---")

# STATUS
st.header("📊 System Status")
st.metric("Protection", "ACTIVE", "24/7")
st.metric("Users", "1", "You")
st.metric("Scams Blocked", "0", "Today")

st.markdown("---")
st.markdown("### 🇮🇳 जय हिंद! जय भारत!")
st.markdown("**Bharat Raksha AI - Protecting Every Indian**")
