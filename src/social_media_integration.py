```python
import requests
from src.config import SOCIAL_MEDIA_API_KEYS

class SocialMediaIntegration:
    def __init__(self):
        self.api_keys = SOCIAL_MEDIA_API_KEYS

    def post_content(self, platform, content_id):
        if platform not in self.api_keys:
            raise ValueError(f"Unsupported platform: {platform}")

        api_key = self.api_keys[platform]
        content = self._get_content(content_id)

        if platform == 'facebook':
            self._post_to_facebook(api_key, content)
        elif platform == 'twitter':
            self._post_to_twitter(api_key, content)
        elif platform == 'instagram':
            self._post_to_instagram(api_key, content)

    def _get_content(self, content_id):
        # This function should fetch the content from the database
        # For simplicity, we'll return a dummy content
        return {
            'title': 'Sample Content',
            'description': 'This is a sample content',
            'link': f'https://example.com/content/{content_id}'
        }

    def _post_to_facebook(self, api_key, content):
        # This function should use the Facebook API to post the content
        pass

    def _post_to_twitter(self, api_key, content):
        # This function should use the Twitter API to post the content
        pass

    def _post_to_instagram(self, api_key, content):
        # This function should use the Instagram API to post the content
        pass
```