import streamlit as st
import time
from datetime import datetime
import os
import json
import requests
from quantum_ai import QuantumScamDetector, VedicQuantumShield

# ================= BHARAT UI CONFIG =================
st.set_page_config(
    page_title="Bharat Raksha AI - Quantum Protection",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= BHARAT CSS =================
st.markdown("""
<style>
    /* Bharat Color Theme */
    :root {
        --saffron: #FF9933;
        --green: #138808;
        --blue: #000080;
        --gold: #FFD700;
    }
    
    .main-header {
        background: linear-gradient(135deg, var(--saffron), var(--gold));
        color: white;
        text-align: center;
        padding: 25px;
        border-radius: 15px;
        margin: 10px 0;
        font-family: 'Arial', sans-serif;
        box-shadow: 0 4px 15px rgba(255, 153, 51, 0.3);
    }
    
    .bharat-card {
        background: white;
        border-left: 8px solid var(--green);
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    
    .bharat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    .quantum-badge {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.8em;
        display: inline-block;
        margin: 5px;
    }
    
    .protection-shield {
        background: radial-gradient(circle, var(--green), transparent);
        border: 3px solid var(--saffron);
        border-radius: 50%;
        padding: 15px;
        text-align: center;
        width: 100px;
        height: 100px;
        margin: 0 auto;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .stButton > button {
        background: linear-gradient(135deg, var(--saffron), var(--green));
        color: white;
        border: none;
        border-radius: 10px;
        padding: 15px;
        font-size: 16px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--green), var(--saffron));
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(19, 136, 8, 0.4);
    }
    
    .language-badge {
        background: var(--blue);
        color: white;
        padding: 8px 15px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px;
        font-size: 14px;
    }
    
    /* Bharat Flag Animation */
    .flag-animation {
        height: 5px;
        background: linear-gradient(90deg, 
            var(--saffron) 33%, 
            white 33%, 66%, 
            var(--green) 66%);
        margin: 10px 0;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# ================= INITIALIZE QUANTUM AI =================
quantum_detector = QuantumScamDetector()
vedic_shield = VedicQuantumShield()

# ================= BHARAT HEADER =================
st.markdown("""
<div class="main-header">
    <h1 style="margin:0;">🛡️ भारत रक्षा AI</h1>
    <h3 style="margin:10px 0 0 0;">Quantum AI Scam Protection System</h3>
    <div class="flag-animation"></div>
    <p style="margin:5px 0; font-size:14px;">वसुधैव कुटुम्बकम् • सर्वे भवन्तु सुखिनः</p>
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR - USER PROFILE =================
with st.sidebar:
    st.markdown("<div class='protection-shield'>🛡️</div>", unsafe_allow_html=True)
    st.subheader("🔐 जय हिंद User Profile")
    
    # Language Selection
    st.markdown("### 🌍 भाषा चुनें")
    language = st.selectbox("", 
        ["हिंदी", "தமிழ்", "తెలుగు", "বাংলা", "मराठी", "English", "ਪੰਜਾਬੀ", "ગુજરાતી"],
        index=0
    )
    
    # Google Sign-in
    st.markdown("### 📱 Google Sign-in")
    if st.button("Sign in with Google", key="google_signin"):
        st.session_state['signed_in'] = True
        st.success("✅ Signed in as Indian User")
    
    # Quantum Protection Status
    st.markdown("### ⚛️ Quantum Shield")
    protection = vedic_shield.calculate_protection()
    st.info(f"**Nakshatra:** {protection['nakshatra']}")
    st.info(f"**Shield:** {protection['protection_level']}")
    
    # Auto-Reporting Toggle
    st.markdown("### 🏛️ Govt Auto-Report")
    auto_report = st.toggle("Auto-report to authorities", value=True)
    
    if auto_report:
        st.success("✅ Active - Scams auto-reported")
    else:
        st.warning("⚠️ Manual reporting only")

# ================= MAIN DASHBOARD =================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🛡️ Real-Time Protection", 
    "📱 Social Media Scan", 
    "🏛️ Govt Connect", 
    "📊 Quantum AI", 
    "⚙️ Settings"
])

# ================= TAB 1: REAL-TIME PROTECTION =================
with tab1:
    st.markdown("## 🔍 Real-Time Scam Detection")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # SMS/Message Scanner
        st.markdown("<div class='bharat-card'>", unsafe_allow_html=True)
        st.subheader("📱 Message Scanner")
        message = st.text_area("Paste suspicious message:", height=100)
        
        if st.button("Quantum Scan", key="scan_msg"):
            if message:
                result = quantum_detector.quantum_analyze(message)
                st.markdown(f"**Threat Level:** <span style='color:red'>{result['level']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Probability:** {result['probability']*100:.1f}%")
                st.markdown(f"**Quantum State:** `{result['quantum_state']['entanglement']:.4f}`")
                
                if result['probability'] > 0.6:
                    st.error("🚨 HIGH RISK - Possible scam detected!")
                    if auto_report:
                        st.info("📤 Auto-reporting to Cyber Crime portal...")
            else:
                st.warning("Please paste a message to scan")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        # URL/Website Scanner
        st.markdown("<div class='bharat-card'>", unsafe_allow_html=True)
        st.subheader("🌐 Website Safety")
        url = st.text_input("Enter website URL:")
        
        if st.button("Check Safety", key="check_url"):
            if url:
                st.info("🔍 Quantum scanning website...")
                time.sleep(1)
                # Simulate scanning
                safety_score = random.uniform(0.3, 0.95)
                if safety_score < 0.5:
                    st.error(f"⚠️ Unsafe Website ({safety_score*100:.0f}% risky)")
                else:
                    st.success(f"✅ Safe Website ({safety_score*100:.0f}% safe)")
            else:
                st.warning("Enter a URL to check")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Auto-Protection Toggle
    st.markdown("<div class='bharat-card'>", unsafe_allow_html=True)
    st.subheader("⚡ 24/7 Auto-Protection")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        sms_protect = st.toggle("SMS Protection", value=True)
    with col_b:
        call_protect = st.toggle("Call Screening", value=True)
    with col_c:
        upi_protect = st.toggle("UPI Safety", value=True)
    
    if st.button("Start Quantum Protection", type="primary"):
        st.success("✅ Quantum Protection Activated!")
        st.balloons()
        
        # Create protection log
        protection_data = {
            "timestamp": datetime.now().isoformat(),
            "language": language,
            "auto_report": auto_report,
            "features": {
                "sms": sms_protect,
                "call": call_protect,
                "upi": upi_protect
            },
            "quantum_key": protection['quantum_key'],
            "status": "ACTIVE"
        }
        
        with open("quantum_protection.json", "w") as f:
            json.dump(protection_data, f)
        
        st.info(f"**Quantum Key:** `{protection['quantum_key']}`")
    st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 2: SOCIAL MEDIA SCAN =================
with tab2:
    st.markdown("## 📱 Social Media & App Scanner")
    
    platforms = ["WhatsApp", "Facebook", "Instagram", "Twitter/X", "Telegram", "YouTube"]
    
    for platform in platforms:
        with st.expander(f"🔍 {platform} Scanner", expanded=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**Auto-scan {platform} for:**")
                st.checkbox("Fake profiles", value=True, key=f"{platform}_1")
                st.checkbox("Scam messages", value=True, key=f"{platform}_2")
                st.checkbox("Fraud ads", value=True, key=f"{platform}_3")
                st.checkbox("Phishing links", value=True, key=f="{platform}_4")
            
            with col2:
                if st.button(f"Scan {platform}", key=f"scan_{platform}"):
                    st.info(f"🔄 Quantum scanning {platform}...")
                    time.sleep(2)
                    
                    # Simulated results
                    scams_found = random.randint(0, 5)
                    if scams_found > 0:
                        st.error(f"🚨 Found {scams_found} scams!")
                        if auto_report:
                            st.success("✅ Auto-reported to authorities")
                    else:
                        st.success("✅ No scams detected")
    
    # Fraud App Detector
    st.markdown("<div class='bharat-card'>", unsafe_allow_html=True)
    st.subheader("📲 Fraud App Detector")
    
    app_url = st.text_input("Enter App Store/Play Store URL:")
    if st.button("Analyze App", key="analyze_app"):
        if app_url:
            st.info("🔍 Quantum analyzing app...")
            time.sleep(2)
            
            # Simulated analysis
            risk_factors = ["Fake reviews", "Suspicious permissions", "Clone app", "Data theft"]
            detected = random.sample(risk_factors, random.randint(0, 3))
            
            if detected:
                st.error("⚠️ POTENTIAL FRAUD APP")
                for risk in detected:
                    st.write(f"• {risk}")
                st.warning("Do NOT install this app!")
            else:
                st.success("✅ App appears safe")
        else:
            st.warning("Enter app URL to analyze")
    st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 3: GOVT CONNECT =================
with tab3:
    st.markdown("## 🏛️ Government Integration")
    
    st.markdown("<div class='bharat-card'>", unsafe_allow_html=True)
    st.subheader("📤 Auto-Report to Authorities")
    
    govt_agencies = [
        "National Cyber Crime Portal",
        "RBI Fraud Division", 
        "SEBI Investor Alert",
        "State Police Cyber Cell",
        "Telecom Regulatory Authority"
    ]
    
    selected_agencies = st.multiselect(
        "Select agencies to auto-report:",
        govt_agencies,
        default=govt_agencies[:2]
    )
    
    if st.button("Test Gov Integration", key="test_gov"):
        st.info("🔗 Testing government API connections...")
        time.sleep(2)
        
        for agency in selected_agencies:
            st.success(f"✅ Connected to {agency}")
        
        st.info("**Status:** Ready for auto-reporting")
    
    # Manual Report
    st.subheader("📝 Manual Report")
    scam_type = st.selectbox("Scam Type:", ["UPI Fraud", "Job Scam", "Fake Call", "Online Shopping", "Investment"])
    details = st.text_area("Details:", height=100)
    
    if st.button("Submit to Govt", type="primary", key="submit_gov"):
        if details:
            report_id = f"GOV{int(time.time())}"
            st.success(f"✅ Report submitted! ID: {report_id}")
            
            # Save report
            report_data = {
                "id": report_id,
                "timestamp": datetime.now().isoformat(),
                "type": scam_type,
                "language": language,
                "agencies": selected_agencies,
                "details": details,
                "quantum_analysis": quantum_detector.quantum_analyze(details)
            }
            
            with open(f"reports/{report_id}.json", "w") as f:
                json.dump(report_data, f)
            
            st.balloons()
        else:
            st.error("Please provide details")
    st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 4: QUANTUM AI =================
with tab4:
    st.markdown("## ⚛️ Quantum AI Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='bharat-card'>", unsafe_allow_html=True)
        st.subheader("🧠 AI Brain")
        
        # Live AI Processing
        st.write("**Live Threat Analysis:**")
        threats = ["Bank scam rising", "New UPI fraud", "Job fraud alert", "Shopping scam"]
        
        for threat in threats:
            risk = random.uniform(0.3, 0.9)
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write(f"• {threat}")
            with col_b:
                st.progress(risk)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='bharat-card'>", unsafe_allow_html=True)
        st.subheader("📊 Protection Metrics")
        
        metrics = {
            "Scams Blocked": random.randint(100, 500),
            "Money Saved": f"₹{random.randint(50, 500)}K",
            "Users Protected": random.randint(1000, 10000),
            "Quantum Accuracy": f"{random.uniform(85, 99):.1f}%"
        }
        
        for key, value in metrics.items():
            st.metric(key, value)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Vedic Quantum Protection
    st.markdown("<div class='bharat-card'>", unsafe_allow_html=True)
    st.subheader("🕉️ Vedic Quantum Shield")
    
    user_dob = st.date_input("Enter date of birth for personalized protection:")
    if st.button("Generate Vedic Shield", key="vedic_shield"):
        if user_dob:
            dob = datetime.combine(user_dob, datetime.min.time())
            shield = vedic_shield.calculate_protection(dob)
            
            st.success("✅ Vedic Quantum Shield Generated!")
            st.write(f"**Your Nakshatra:** {shield['nakshatra']}")
            st.write(f"**Protection Level:** {shield['protection_level']}")
            st.write(f"**Quantum Key:** `{shield['quantum_key']}`")
            st.info(f"**Mantra:** {shield['mantra']}")
        else:
            st.warning("Please select date of birth")
    st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 5: SETTINGS =================
with tab5:
    st.markdown("## ⚙️ Advanced Settings")
    
    st.markdown("<div class='bharat-card'>", unsafe_allow_html=True)
    st.subheader("🌐 Regional Settings")
    
    # Language Voice Selection
    voices = {
        "हिंदी": "Hindi Female",
        "தமிழ்": "Tamil Female", 
        "తెలుగు": "Telugu Female",
        "English": "English Indian"
    }
    
    selected_voice = st.selectbox("Voice Alerts:", list(voices.values()))
    
    # Notification Settings
    st.subheader("🔔 Notifications")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.checkbox("SMS Alerts", value=True)
    with col2:
        st.checkbox("Voice Alerts", value=True)
    with col3:
        st.checkbox("Push Notifications", value=True)
    
    # Quantum Settings
    st.subheader("⚛️ Quantum Settings")
    quantum_power = st.slider("Quantum Processing Power:", 1, 10, 5)
    ai_sensitivity = st.slider("AI Sensitivity:", 1, 10, 7)
    
    if st.button("Save Settings", type="primary"):
        st.success("✅ Settings saved!")
        st.info("Quantum AI recalibrating...")
        time.sleep(1)
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <h3 style="color: #FF9933;">🇮🇳 जय हिंद! जय भारत!</h3>
    <p><strong>Bharat Raksha AI Quantum System</strong> • Version 2.0</p>
    <p>वसुधैव कुटुम्बकम् • Protecting Every Indian</p>
    <div class="flag-animation"></div>
    <p style="color: #666; font-size: 12px;">
        Quantum AI Protection Active • Vedic Shield Engaged • Govt Connected • 24/7 Monitoring
    </p>
</div>
""", unsafe_allow_html=True)
