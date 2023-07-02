```python
import requests
from error_handling import handle_error

# API keys for different social media platforms and OpenAI
api_keys = {
    "OnlyFans": "YOUR_ONLYFANS_API_KEY",
    "Twitter": "YOUR_TWITTER_API_KEY",
    "Instagram": "YOUR_INSTAGRAM_API_KEY",
    "OpenAI": "YOUR_OPENAI_API_KEY"
}

def authenticate(platform):
    try:
        if platform in api_keys:
            response = requests.get(
                f"https://{platform}.com/oauth2/token",
                headers={"Authorization": f"Bearer {api_keys[platform]}"}
            )
            response.raise_for_status()
            return response.json()["access_token"]
        else:
            raise ValueError(f"Unsupported platform: {platform}")
    except Exception as e:
        handle_error(e, "AuthenticationFailed")
```