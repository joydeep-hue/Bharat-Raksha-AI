import android
import time
import re

class SMSGuardian:
    def __init__(self):
        self.droid = android.Android()
        self.scam_keywords = [
            r'win.*lottery',
            r'urgent.*payment',
            r'click.*link',
            r'send.*OTP',
            r'bank.*account',
            r'free.*money',
            r'claim.*prize',
            r'password.*reset'
        ]
        
    def request_permissions(self):
        """Request SMS read permission"""
        print("🔐 Requesting SMS permission...")
        self.droid.requestPermissions([
            'android.permission.READ_SMS',
            'android.permission.RECEIVE_SMS'
        ])
        return True
    
    def read_sms(self):
        """Read latest SMS"""
        try:
            # Get last 10 SMS
            result = self.droid.smsGetMessages(False, 'inbox')
            
            if result.error is None:
                messages = result.result
                
                for msg in messages:
                    body = msg['body'].lower()
                    sender = msg['address']
                    
                    # Check for scams
                    scam_found = self.detect_scam(body)
                    
                    if scam_found:
                        self.alert_user(sender, scam_found)
                        
            return True
                    
        except Exception as e:
            print(f"SMS Error: {e}")
            return False
    
    def detect_scam(self, message):
        """Detect scam patterns"""
        for pattern in self.scam_keywords:
            if re.search(pattern, message, re.IGNORECASE):
                return pattern
        return None
    
    def alert_user(self, sender, scam_type):
        """Alert user about scam"""
        alert_msg = f"⚠️ Scam SMS detected from {sender}"
        alert_msg += f"\nType: {scam_type}"
        alert_msg += "\nDon't reply or click links!"
        
        print(alert_msg)
        
        # Save to log
        with open("scam_alerts.txt", "a") as f:
            f.write(f"{time.ctime()}: {alert_msg}\n")
        
        return True
    
    def start_monitoring(self):
        """Start SMS monitoring"""
        print("📱 Starting SMS Guardian...")
        
        if self.request_permissions():
            print("✅ Permissions granted")
            
            while True:
                self.read_sms()
                time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    guardian = SMSGuardian()
    guardian.start_monitoring()
