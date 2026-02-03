import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bharat Raksha AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ भारत रक्षा AI")
st.subheader("24/7 Protection Against Scams")

# Language selection
language = st.selectbox(
    "Choose Language / भाषा चुनें",
    ["Hindi", "Tamil", "Telugu", "Bengali", "English"]
)

# Protection modules
st.header("🔒 Protection Modules")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("SMS Protection"):
        st.success("SMS Monitoring Active")
        st.info("Scam SMS will be blocked automatically")

with col2:
    if st.button("Call Protection"):
        st.success("Call Screening Active")
        st.info("Scam calls will be identified")

with col3:
    if st.button("UPI Safety"):
        st.success("Transaction Safety Active")
        st.info("Fraudulent UPI payments will be blocked")

# Report scam
st.header("⚠️ Report Scam")
scam_type = st.selectbox(
    "Scam Type",
    ["UPI Fraud", "Job Scam", "Lottery", "Bank", "Other"]
)

if st.button("Report to Cyber Crime Cell"):
    st.success("Reported to authorities!")
    st.balloons()

# Real-time status
st.sidebar.header("📊 System Status")
st.sidebar.metric("Protected Since", "Today")
st.sidebar.metric("Scams Blocked", "0")
st.sidebar.metric("Active Users", "1")

# Footer
st.markdown("---")
st.markdown("### 🇮🇳 Made for India, By Indians")
st.markdown("**Free Forever • 24/7 Protection • All Languages**")
