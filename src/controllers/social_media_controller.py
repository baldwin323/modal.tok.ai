```python
from src.models.user import User
from src.models.content import Content
from src.utils import SOCIAL_MEDIA_API_KEYS

class SocialMediaController:
    def __init__(self):
        self.user = User()
        self.content = Content()

    def integrateSocialMedia(self, user_id, platform):
        if platform not in SOCIAL_MEDIA_API_KEYS:
            raise ValueError(f"Unsupported platform: {platform}")
        api_key = SOCIAL_MEDIA_API_KEYS[platform]
        # Integration logic goes here

    def postContent(self, user_id, content_id, platform):
        user = self.user.get(user_id)
        content = self.content.get(content_id)
        if platform not in SOCIAL_MEDIA_API_KEYS:
            raise ValueError(f"Unsupported platform: {platform}")
        api_key = SOCIAL_MEDIA_API_KEYS[platform]
        # Posting logic goes here
```