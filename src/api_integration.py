```python
import requests
from src import config
from src import models

class APIIntegration:
    def __init__(self):
        self.api_keys = config.API_KEYS

    def fetch_social_media_data(self, platform, user_id):
        if platform == 'Twitter':
            url = f"https://api.twitter.com/2/users/{user_id}"
            headers = {"Authorization": f"Bearer {self.api_keys['Twitter']}"}
        elif platform == 'Instagram':
            url = f"https://graph.instagram.com/{user_id}"
            headers = {"Authorization": f"Bearer {self.api_keys['Instagram']}"}
        else:
            raise ValueError("Unsupported platform")

        response = requests.get(url, headers=headers)
        return response.json()

    def process_payment(self, payment_gateway, payment_data):
        if payment_gateway == 'Stripe':
            url = "https://api.stripe.com/v1/charges"
            headers = {"Authorization": f"Bearer {self.api_keys['Stripe']}"}
        elif payment_gateway == 'PayPal':
            url = "https://api.paypal.com/v1/payments/payment"
            headers = {"Authorization": f"Bearer {self.api_keys['PayPal']}"}
        else:
            raise ValueError("Unsupported payment gateway")

        response = requests.post(url, headers=headers, data=payment_data)
        return response.json()

    def fetch_analytics_data(self):
        url = "https://www.googleapis.com/analytics/v3/data/ga"
        headers = {"Authorization": f"Bearer {self.api_keys['GoogleAnalytics']}"}

        response = requests.get(url, headers=headers)
        return response.json()
```