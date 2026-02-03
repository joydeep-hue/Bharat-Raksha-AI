import time
import os
import re
from datetime import datetime

print("📱 SMS Guardian Starting...")

# Scam keywords in multiple languages
SCAM_PATTERNS = {
    'hindi': ['जीत', 'लॉटरी', 'ओटीपी', 'बैंक', 'पुरस्कार', 'तुरंत'],
    'tamil': ['வெற்றி', 'லாட்டரி', 'OTP', 'வங்கி', 'பரிசு', 'அவசர'],
    'english': ['win', 'lottery', 'urgent', 'payment', 'click', 'free']
}

class SMSGuardian:
    def __init__(self):
        self.alerts_file = "scam_alerts.txt"
        
    def check_message(self, message):
        """Check if message is scam"""
        message_lower = message.lower()
        
        for lang, keywords in SCAM_PATTERNS.items():
            for keyword in keywords:
                if keyword.lower() in message_lower:
                    return True, keyword, lang
        
        return False, None, None
    
    def save_alert(self, message, keyword, language):
        """Save scam alert"""
        alert_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        alert_text = f"""
        ⚠️ SCAM ALERT ⚠️
        Time: {alert_time}
        Language: {language}
        Keyword: {keyword}
        Message: {message[:100]}...
        -------------------------
        """
        
        with open(self.alerts_file, "a") as f:
            f.write(alert_text)
        
        print(f"[!] Scam detected: {keyword} ({language})")
        return alert_text
    
    def simulate_sms(self):
        """Simulate receiving SMS (for testing)"""
        test_messages = [
            "You won 50 lakhs lottery! Click link to claim.",
            "आपने 10 लाख जीते हैं! तुरंत क्लिक करें।",
            "Your bank account needs verification. Send OTP.",
            "வங்கி கணக்கு சரிபார்ப்பு தேவை. OTP அனுப்பவும்."
        ]
        
        for msg in test_messages:
            print(f"\nChecking: {msg}")
            is_scam, keyword, lang = self.check_message(msg)
            
            if is_scam:
                self.save_alert(msg, keyword, lang)
                self.voice_alert(lang)
            else:
                print("✅ Safe message")
            
            time.sleep(2)
    
    def voice_alert(self, language):
        """Voice alert in detected language"""
        alerts = {
            'hindi': "चेतावनी! संभावित धोखाधड़ी संदेश मिला।",
            'tamil': "எச்சரிக்கை! சந்தேகத்திற்குரிய செய்தி கிடைத்தது.",
            'english': "Warning! Possible scam message detected."
        }
        
        alert_text = alerts.get(language, alerts['english'])
        
        # Create voice alert
        from gtts import gTTS
        tts = gTTS(text=alert_text, lang=language[:2], slow=False)
        tts.save("alert.mp3")
        os.system("play-audio alert.mp3")

# Run SMS guardian
if __name__ == "__main__":
    guard = SMSGuardian()
    print("\n" + "="*50)
    print("Testing SMS scam detection...")
    print("="*50 + "\n")
    
    guard.simulate_sms()
    
    print("\n" + "="*50)
    print("✅ Test complete! Check scam_alerts.txt")
    print("="*50)
