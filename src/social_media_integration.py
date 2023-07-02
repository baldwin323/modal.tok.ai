```python
import os
from social_media_api import SocialMediaAPI

class SocialMediaIntegration:
    def __init__(self, user_id, content_id):
        self.user_id = user_id
        self.content_id = content_id
        self.api = SocialMediaAPI()

    def integrateSocialMedia(self, platform):
        """
        Integrate with specified social media platform
        """
        self.api.connect(platform, self.user_id)

    def postPromotion(self, message, platform):
        """
        Post and promote content across specified platform
        """
        self.api.post(self.content_id, message, platform)

if __name__ == "__main__":
    user_id = os.getenv('USER_ID')
    content_id = os.getenv('CONTENT_ID')
    smi = SocialMediaIntegration(user_id, content_id)

    # Integrate with a social media platform
    smi.integrateSocialMedia('facebook')

    # Post and promote content on the platform
    smi.postPromotion('Check out my new content!', 'facebook')
```