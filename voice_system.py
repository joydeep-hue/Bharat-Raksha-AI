from gtts import gTTS
import os
import json
import time # Added this because your test_voice function uses it

class VoiceGuardian:
    def __init__(self):
        self.languages = {
            'hi': 'hi',  # Hindi
            'ta': 'ta',  # Tamil
            'te': 'te',  # Telugu
            'bn': 'bn',  # Bengali
            'mr': 'mr',  # Marathi
            'gu': 'gu',  # Gujarati
        }
    
    def speak(self, text, lang='hi'):
        """Convert text to speech"""
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            filename = "warning.mp3"
            tts.save(filename)
            
            # --- FIX FOR TERMUX ---
            # Instead of playsound, we use mpv
            os.system(f"mpv --no-video {filename}")
            
            # Clean up
            if os.path.exists(filename):
                os.remove(filename)
            
        except Exception as e:
            print(f"Voice error: {e}")
    
    def scam_warning(self, scam_type, lang='hi'):
        """Predefined scam warnings"""
        warnings = {
            'hi': {
                'upi': "चेतावनी! यह यूपीआई धोखाधड़ी हो सकती है। कृपया भुगतान न करें।",
                'job': "सावधान! यह नौकरी का घोटाला लगता है। आगे बढ़ने से पहले सत्यापित करें।",
                'lottery': "यह लॉटरी घोटाला है। कोई पैसा न भेजें।",
                'bank': "बैंक कभी भी ओटीपी नहीं मांगता। यह धोखाधड़ी है।"
            },
            'ta': {
                'upi': "எச்சரிக்கை! இது யூபிஐ மோசடியாக இருக்கலாம். தயவுசெய்து பணம் செலுத்த வேண்டாம்.",
                'job': "எச்சரிக்கை! இது வேலை மோசடியாக தோன்றுகிறது. தொடருவதற்கு முன் சரிபார்க்கவும்."
            },
            'te': {
                'upi': "హెచ్చరిక! ఇది యూపిఐ మోసం కావచ్చు. దయచేసి చెల్లించవద్దు.",
                'job': "జాగ్రత్త! ఇది జాబ్ స్కామ్ అనిపించడం లేదు. కొనసాగించడానికి ముందు ధ్రువీకరించండి."
            }
        }
        
        if lang in warnings and scam_type in warnings[lang]:
            self.speak(warnings[lang][scam_type], lang)
        else:
            self.speak("Warning! Possible scam detected.", 'en')
    
    def test_voice(self):
        """Test all languages"""
        print("Testing voice system...")
        self.speak("भारत रक्षा एआई सक्रिय है। आप सुरक्षित हैं।", 'hi')
        time.sleep(1)
        self.speak("பாரத் ரக்ஷா AI செயல்பாட்டில் உள்ளது. நீங்கள் பாதுகாப்பாக இருக்கிறீர்கள்.", 'ta')

# To run it:
if __name__ == "__main__":
    guardian = VoiceGuardian()
    guardian.test_voice()

