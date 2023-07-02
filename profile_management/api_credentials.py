```python
from user_auth_system.account_management import User

class APICredentials:
    def __init__(self, user: User):
        self.user = user
        self.api_key = None
        self.api_secret = None
        self.access_token = None

    def set_api_credentials(self, api_key: str, api_secret: str, access_token: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.save_credentials()

    def save_credentials(self):
        # Save the API credentials to the user's profile
        self.user.api_credentials = {
            'api_key': self.api_key,
            'api_secret': self.api_secret,
            'access_token': self.access_token
        }

    def get_api_credentials(self):
        # Retrieve the API credentials from the user's profile
        return self.user.api_credentials
```