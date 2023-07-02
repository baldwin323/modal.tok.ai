```python
import requests
from UserAuthenticationSystem import UserDataSchema

class APIIntegrationModule:
    def __init__(self, user_data: UserDataSchema):
        self.user_data = user_data

    def get_social_media_data(self, platform: str):
        api_key = self.user_data.api_credentials[platform]
        headers = {'Authorization': f'Bearer {api_key}'}

        if platform == 'OnlyFans':
            url = 'https://onlyfans.com/api/user'
        else:
            raise ValueError('Unsupported platform')

        response = requests.get(url, headers=headers)
        return response.json()

    def post_social_media_data(self, platform: str, data: dict):
        api_key = self.user_data.api_credentials[platform]
        headers = {'Authorization': f'Bearer {api_key}'}

        if platform == 'OnlyFans':
            url = 'https://onlyfans.com/api/post'
        else:
            raise ValueError('Unsupported platform')

        response = requests.post(url, headers=headers, data=data)
        return response.json()
```