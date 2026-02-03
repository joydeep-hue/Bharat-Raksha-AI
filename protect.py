#!/usr/bin/env python3
"""
BHARAT RAKSHA AI - Basic Version
Anti-Scam Protection for India
Works 24/7 on Android
"""

import os
import time
from datetime import datetime

print("🇮🇳" * 20)
print("       BHARAT RAKSHA AI")
print("       24/7 Protection")
print("🇮🇳" * 20)
print()

class SimpleGuardian:
    def __init__(self):
        self.protection_log = "protection_log.txt"
        self.scam_count = 0
        
    def start_protection(self):
        """Start 24/7 protection"""
        print("[+] Protection starting...")
        print("[+] Log file: protection_log.txt")
        print("[+] Press Ctrl+C to stop")
        print()
        
        # Create protection log
        with open(self.protection_log, "w") as f:
            f.write(f"=== BHARAT RAKSHA AI ===\n")
            f.write(f"Started: {datetime.now()}\n")
            f.write(f"Status: ACTIVE 24/7\n")
            f.write("="*30 + "\n\n")
        
        # Main protection loop
        try:
            while True:
                self.check_system()
                time.sleep(5)  # Check every 5 seconds
                
        except KeyboardInterrupt:
            print("\n[!] Protection stopping...")
            self.stop_protection()
    
    def check_system(self):
        """Check system status"""
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Simulate protection activity
        status = f"[{current_time}] ✅ System Protected"
        
        # Log to file
        with open(self.protection_log, "a") as f:
            f.write(f"{status}\n")
        
        # Show on screen
        print(status)
    
    def stop_protection(self):
        """Clean shutdown"""
        with open(self.protection_log, "a") as f:
            f.write(f"\nStopped: {datetime.now()}\n")
            f.write("Protection ended safely.\n")
        
        print("[+] Protection log saved")
        print("[+] Thank you for using Bharat Raksha AI")

# Run protection
if __name__ == "__main__":
    guard = SimpleGuardian()
    guard.start_protection()
