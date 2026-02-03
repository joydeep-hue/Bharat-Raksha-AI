# metrics.py - Track real impact
import json
from datetime import datetime

class BharatMetrics:
    def __init__(self):
        self.metrics_file = "bharat_metrics.json"
        self.init_metrics()
    
    def init_metrics(self):
        base_metrics = {
            "total_scams_blocked": 0,
            "money_saved_rupees": 0,
            "users_protected": 1,
            "sms_scanned": 0,
            "voice_alerts": 0,
            "start_date": str(datetime.now()),
            "daily_stats": {}
        }
        
        try:
            with open(self.metrics_file, "r") as f:
                existing = json.load(f)
                # Update with existing data
                base_metrics.update(existing)
        except:
            pass
        
        with open(self.metrics_file, "w") as f:
            json.dump(base_metrics, f, indent=4)
    
    def add_scam_blocked(self, amount_saved=0):
        metrics = self.get_metrics()
        metrics["total_scams_blocked"] += 1
        metrics["money_saved_rupees"] += amount_saved
        self.save_metrics(metrics)
    
    def get_metrics(self):
        with open(self.metrics_file, "r") as f:
            return json.load(f)
    
    def save_metrics(self, metrics):
        with open(self.metrics_file, "w") as f:
            json.dump(metrics, f, indent=4)

# Usage in dashboard.py
# from metrics import BharatMetrics
# metrics = BharatMetrics()
# metrics.add_scam_blocked(5000)  # When scam is blocked
