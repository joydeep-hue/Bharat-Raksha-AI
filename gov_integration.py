# Auto-report to government
import requests

class GovReporter:
    GOV_APIS = {
        'cybercrime': 'https://cybercrime.gov.in/api/report',
        'rbi': 'https://m.rbi.org.in/api/fraud',
        'trai': 'https://www.trai.gov.in/api/spam'
    }
    
    def auto_report(self, scam_data):
        """Auto-report to all agencies"""
        for name, api in self.GOV_APIS.items():
            try:
                response = requests.post(api, json=scam_data)
                print(f"Reported to {name}: {response.status_code}")
            except:
                print(f"Failed to report to {name}")
