```python
import requests
from credentials import ONLYFANS_AFFILIATE_API_KEY

class OnlyFansAffiliateAPI:
    def __init__(self):
        self.base_url = "https://onlyfans.com/api2/"
        self.headers = {
            "Authorization": f"Bearer {ONLYFANS_AFFILIATE_API_KEY}"
        }

    def get_affiliate_data(self, user_id):
        response = requests.get(f"{self.base_url}affiliates/{user_id}", headers=self.headers)
        return response.json()

    def create_affiliate_link(self, user_id, product_id):
        data = {
            "user_id": user_id,
            "product_id": product_id
        }
        response = requests.post(f"{self.base_url}affiliates/create_link", headers=self.headers, data=data)
        return response.json()

onlyfans_affiliate_api = OnlyFansAffiliateAPI()
```