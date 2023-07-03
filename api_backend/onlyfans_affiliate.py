```python
import requests

class OnlyFansAffiliateAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.onlyfans.com/affiliate"

    def track_referral(self, referral_id):
        url = f"{self.base_url}/track/{referral_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def credit_promotion(self, promotion_id, amount):
        url = f"{self.base_url}/credit/{promotion_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"amount": amount}
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None
```