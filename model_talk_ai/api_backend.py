```python
import requests
from model_talk_ai.config import ONLYFANS_AFFILIATE_API_KEY

class APIBackend:
    def __init__(self):
        self.api_key = ONLYFANS_AFFILIATE_API_KEY

    def handle_api(self, user_id, referral_link):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'user_id': user_id,
            'referral_link': referral_link
        }
        response = requests.post('https://onlyfans.com/api/affiliate', headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None
```
