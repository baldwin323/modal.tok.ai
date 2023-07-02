```python
import requests
from error_handling_logging import handleError

# API keys for third-party services
api_keys = {
    "OnlyFans": "YOUR_ONLYFANS_API_KEY",
    "Twitter": "YOUR_TWITTER_API_KEY",
    "Instagram": "YOUR_INSTAGRAM_API_KEY",
    "PayPal": "YOUR_PAYPAL_API_KEY",
    "Stripe": "YOUR_STRIPE_API_KEY",
    "GoogleAnalytics": "YOUR_GOOGLE_ANALYTICS_API_KEY"
}

def make_api_request(service_name, endpoint, method="GET", data=None):
    try:
        headers = {"Authorization": f"Bearer {api_keys[service_name]}"}
        if method == "GET":
            response = requests.get(endpoint, headers=headers)
        elif method == "POST":
            response = requests.post(endpoint, headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        handleError(e, service_name, endpoint)
        return None

# Example usage:
# response = make_api_request("Twitter", "https://api.twitter.com/1.1/statuses/user_timeline.json")
# print(response)
```