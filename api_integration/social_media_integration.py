```python
import requests
from user_auth_system.account_management import User
from profile_management.api_credentials import get_api_credentials

class SocialMediaIntegration:
    def __init__(self, user: User):
        self.user = user
        self.api_credentials = get_api_credentials(user)

    def get_social_media_data(self, platform: str):
        if platform.lower() == 'twitter':
            return self.get_twitter_data()
        elif platform.lower() == 'instagram':
            return self.get_instagram_data()
        elif platform.lower() == 'onlyfans':
            return self.get_onlyfans_data()
        else:
            raise ValueError(f"Unsupported platform: {platform}")

    def get_twitter_data(self):
        twitter_api_key, twitter_api_secret = self.api_credentials['twitter']
        # Add code here to fetch data from Twitter API using the credentials

    def get_instagram_data(self):
        instagram_api_key, instagram_api_secret = self.api_credentials['instagram']
        # Add code here to fetch data from Instagram API using the credentials

    def get_onlyfans_data(self):
        onlyfans_api_key, onlyfans_api_secret = self.api_credentials['onlyfans']
        # Add code here to fetch data from OnlyFans API using the credentials
```