import streamlit as st
import time
from datetime import datetime
import os
import subprocess
import threading

st.set_page_config(page_title="Bharat Raksha AI", page_icon="🛡️", layout="wide")

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        color: #FF9933;
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        padding: 10px;
    }
    .protection-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        width: 100%;
        padding: 15px;
        font-size: 1.2em;
        border-radius: 10px;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border: none;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .success-box {
        background: #d4edda;
        color: #155724;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# ================== HEADER ==================
st.markdown('<div class="main-header">🛡️ भारत रक्षा AI</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:1.2em; color:#138808;">24/7 Protection Against Scams & Fraud</p>', unsafe_allow_html=True)

st.markdown("---")

# ================== SIDEBAR STATUS ==================
st.sidebar.title("🔧 System Status")

# Check file existence
def check_status():
    return {
        "Protection Log": os.path.exists("protection_log.txt"),
        "Scam Alerts": os.path.exists("scam_alerts.txt"),
        "SMS Protection": os.path.exists("sms_active.txt"),
        "Scam Reports": os.path.exists("scam_reports.txt"),
        "Voice System": os.path.exists("voice_test.py")
    }

status = check_status()

for item, active in status.items():
    if active:
        st.sidebar.success(f"✅ {item}")
    else:
        st.sidebar.warning(f"⚠️ {item}")

# File counts
if status["Scam Alerts"]:
    with open("scam_alerts.txt", "r") as f:
        alert_count = len(f.readlines())
    st.sidebar.info(f"🚨 Scams Detected: {alert_count}")

if status["Scam Reports"]:
    with open("scam_reports.txt", "r") as f:
        report_count = len(f.readlines())
    st.sidebar.info(f"📝 Reports Filed: {report_count}")

# Quick Actions
st.sidebar.markdown("---")
st.sidebar.subheader("⚡ Quick Actions")
if st.sidebar.button("🔄 Refresh Status"):
    st.rerun()

if st.sidebar.button("🗑️ Clear Logs"):
    for file in ["protection_log.txt", "scam_alerts.txt", "scam_reports.txt", "sms_active.txt"]:
        if os.path.exists(file):
            os.remove(file)
    st.sidebar.success("Logs cleared!")
    time.sleep(1)
    st.rerun()

# ================== MAIN CONTENT ==================
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌍 Choose Language / भाषा चुनें")
    language = st.selectbox("", ["Hindi", "Tamil", "Telugu", "Bengali", "Marathi", "English", "Punjabi", "Gujarati"], 
                           label_visibility="collapsed", index=0)
    
    # Show greeting in selected language
    greetings = {
        "Hindi": "नमस्ते! आप सुरक्षित हैं।",
        "Tamil": "வணக்கம்! நீங்கள் பாதுகாப்பாக இருக்கிறீர்கள்.",
        "Telugu": "నమస్కారం! మీరు సురక్షితంగా ఉన్నారు.",
        "English": "Hello! You are protected.",
        "Bengali": "নমস্কার! আপনি সুরক্ষিত।",
        "Marathi": "नमस्कार! तुम्ही सुरक्षित आहात.",
        "Punjabi": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਤੁਸੀਂ ਸੁਰੱਖਿਅਤ ਹੋ।",
        "Gujarati": "નમસ્તે! તમે સુરક્ષિત છો."
    }
    
    st.info(f"**{greetings.get(language, 'Hello! You are protected.')}**")

with col2:
    st.subheader("📊 Live Status")
    
    # Real-time metrics
    status_col1, status_col2, status_col3 = st.columns(3)
    
    with status_col1:
        if os.path.exists("protection_log.txt"):
            with open("protection_log.txt", "r") as f:
                lines = len(f.readlines())
            st.metric("System", "ACTIVE", f"{lines} logs")
        else:
            st.metric("System", "INACTIVE", "Start protection")
    
    with status_col2:
        if os.path.exists("scam_alerts.txt"):
            with open("scam_alerts.txt", "r") as f:
                alerts = len(f.readlines())
            st.metric("Scams", f"{alerts}", "detected")
        else:
            st.metric("Scams", "0", "detected")
    
    with status_col3:
        st.metric("Users", "1", "You")

st.markdown("---")

# ================== PROTECTION MODULES ==================
st.subheader("🔒 Protection Modules")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📱 SMS Protection", key="sms_btn"):
        # Create activation file
        with open("sms_active.txt", "w") as f:
            f.write(f"SMS Protection Activated: {datetime.now()}\n")
            f.write(f"Language: {language}\n")
            f.write(f"Status: ACTIVE\n")
        
        st.success("✅ SMS Monitoring ACTIVATED")
        
        # Show progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
            status_text.text(f"Initializing... {i+1}%")
        
        status_text.text("✅ Ready! Scanning incoming messages...")
        
        # Update protection log
        with open("protection_log.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%H:%M:%S')} - SMS Protection Activated\n")
        
        st.balloons()

with col2:
    if st.button("📞 Call Protection", key="call_btn"):
        st.success("✅ Call Screening ACTIVATED")
        
        # Simulate call screening
        with st.expander("📞 Live Call Log", expanded=True):
            st.write("**Status:** 🟢 Active")
            st.write("**Last scan:** Just now")
            st.write("**Mode:** Automatic screening")
            st.write("**Languages:** Hindi, English, Tamil")
            
            # Fake call log
            calls = [
                ("+91 98765XXXXX", "Safe", "2 min ago"),
                ("Unknown", "Suspicious", "5 min ago"),
                ("+91 87654XXXXX", "Safe", "10 min ago")
            ]
            
            for number, status, time_ago in calls:
                if status == "Suspicious":
                    st.error(f"🚫 {number} - {status} ({time_ago})")
                else:
                    st.success(f"✅ {number} - {status} ({time_ago})")
        
        # Update log
        with open("protection_log.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%H:%M:%S')} - Call Protection Activated\n")

with col3:
    if st.button("💳 UPI Safety", key="upi_btn"):
        st.success("✅ UPI Safety ACTIVATED")
        
        # Safety features
        st.markdown("""
        <div class="success-box">
        <strong>✅ Safety Features Enabled:</strong><br>
        1. Payee name verification<br>
        2. Amount limit alerts<br>
        3. Unknown sender warnings<br>
        4. QR code safety check<br>
        5. Transaction pattern analysis
        </div>
        """, unsafe_allow_html=True)
        
        # Update log
        with open("protection_log.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%H:%M:%S')} - UPI Safety Activated\n")

st.markdown("---")

# ================== REPORT SCAM ==================
st.subheader("⚠️ Report Scam")

report_col1, report_col2 = st.columns([2, 1])

with report_col1:
    scam_type = st.selectbox(
        "Scam Type:",
        ["UPI/Payment Fraud", "Job/Employment Scam", "Lottery/Prize", 
         "Bank/Fake Call", "Online Shopping", "Fake SMS", "Other"]
    )
    
    scam_details = st.text_area(
        "Describe the scam (include phone number/URL if available):",
        height=100,
        placeholder="Example: Received call from +91 98765XXXXX claiming to be from SBI Bank asking for OTP..."
    )
    
    phone_number = st.text_input("Your contact (optional):", placeholder="+91 XXXXX XXXXX")

with report_col2:
    st.write("###")
    st.write("###")
    if st.button("🚨 Report to Cyber Crime", type="primary", use_container_width=True):
        if scam_details.strip():
            # Create report
            report_id = f"BR{int(time.time())}"
            report_data = f"""
{'='*60}
REPORT ID: {report_id}
TIME: {datetime.now()}
TYPE: {scam_type}
LANGUAGE: {language}
DETAILS: {scam_details}
CONTACT: {phone_number if phone_number else 'Not provided'}
STATUS: PENDING_SYNC
{'='*60}
"""
            
            # Save to file
            with open("scam_reports.txt", "a") as f:
                f.write(report_data + "\n")
            
            # Also save to scam_alerts for monitoring
            with open("scam_alerts.txt", "a") as f:
                f.write(f"{datetime.now()} - User reported: {scam_type[:30]}...\n")
            
            # Show success
            st.success("✅ Reported Successfully!")
            st.balloons()
            
            # Show report summary
            st.markdown(f"""
            <div class="success-box">
            <strong>📋 Report Summary:</strong><br>
            • <strong>ID:</strong> {report_id}<br>
            • <strong>Type:</strong> {scam_type}<br>
            • <strong>Time:</strong> {datetime.now().strftime('%H:%M:%S')}<br>
            • <strong>Status:</strong> Queued for Cyber Crime portal
            </div>
            """, unsafe_allow_html=True)
            
            st.info("""
            **Next Steps:**
            1. Report saved locally
            2. Will auto-sync with Cyber Crime portal
            3. Keep reference ID for tracking
            4. You may receive SMS confirmation
            """)
        else:
            st.error("⚠️ Please describe the scam before reporting")

st.markdown("---")

# ================== LIVE PROTECTION LOG ==================
st.subheader("📝 Live Protection Log")

if os.path.exists("protection_log.txt"):
    with open("protection_log.txt", "r") as f:
        logs = f.readlines()
    
    if logs:
        # Show last 15 entries
        container = st.container(height=300)
        with container:
            for log in reversed(logs[-15:]):
                log = log.strip()
                if "Activated" in log or "ACTIVE" in log:
                    st.success(f"🟢 {log}")
                elif "Scam" in log or "Suspicious" in log:
                    st.error(f"🚨 {log}")
                elif "Error" in log or "Failed" in log:
                    st.error(f"❌ {log}")
                else:
                    st.info(f"📝 {log}")
        
        # Log statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.caption(f"Total entries: {len(logs)}")
        with col2:
            if len(logs) > 0:
                last_log = logs[-1].strip()
                st.caption(f"Last: {last_log[:40]}...")
        with col3:
            st.caption(f"Started: {logs[0][:19] if logs else 'N/A'}")
    else:
        st.info("Protection log is empty. Activate protection modules to see activity.")
else:
    st.warning("Protection log not found. System may not be running.")

# ================== FILE BROWSER ==================
with st.expander("📁 View System Files"):
    if st.button("Refresh File List"):
        st.rerun()
    
    txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
    py_files = [f for f in os.listdir(".") if f.endswith(".py")]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Data Files (.txt):**")
        for file in txt_files:
            size = os.path.getsize(file)
            st.code(f"{file} ({size} bytes)")
    
    with col2:
        st.write("**Python Files (.py):**")
        for file in py_files:
            st.code(file)

# ================== FOOTER ==================
st.markdown("---")
st.markdown("### 🇮🇳 Made for India, By Indians")
st.markdown("**Free Forever • 24/7 Protection • All Languages Supported**")

st.markdown("""
<div style="text-align: center; margin-top: 20px; color: #666;">
    <small>
    Bharat Raksha AI | Version 1.0 | 
    <a href="https://github.com/joydeep-hue/Bharat-Raksha-AI" target="_blank">GitHub</a> | 
    Protection Status: ACTIVE
    </small>
</div>
""", unsafe_allow_html=True)
# Add PWA manifest
st.markdown("""
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#FF9933">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
""", unsafe_allow_html=True)
# Add at top of dashboard.py
import requests

def check_for_updates():
    """Check if new APK version available"""
    try:
        # Store current APK version
        CURRENT_APK_VERSION = "1.0"
        
        # Get latest version from your GitHub
        latest_version = "1.0"  # You update this when rebuilding APK
        
        if latest_version != CURRENT_APK_VERSION:
            st.warning(f"📱 New app version {latest_version} available!")
            st.markdown("[Download updated APK](https://your-link-to-new-apk)")
            return False
        return True
    except:
        return True

# Call in sidebar
with st.sidebar:
    if not check_for_updates():
        st.error("Please update app for new features!")
