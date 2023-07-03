```python
import requests
from model_talk_ai.config import SOCIAL_MEDIA_API_KEYS

class SocialMediaIntegration:
    def __init__(self):
        self.api_keys = SOCIAL_MEDIA_API_KEYS

    def login(self, platform):
        api_key = self.api_keys[platform]
        # Implement login logic here

    def send_message(self, platform, user_id, message):
        api_key = self.api_keys[platform]
        # Implement message sending logic here

    def receive_message(self, platform, user_id):
        api_key = self.api_keys[platform]
        # Implement message receiving logic here

    def handle_interaction(self, platform, user_id, message):
        self.login(platform)
        self.send_message(platform, user_id, message)
        response = self.receive_message(platform, user_id)
        return response

def integrate_social_media(platform, user_id, message):
    smi = SocialMediaIntegration()
    response = smi.handle_interaction(platform, user_id, message)
    return response
```