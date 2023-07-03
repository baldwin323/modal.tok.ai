```python
import requests
from instagram_private_api import Client, ClientCompatPatch

class InstagramIntegration:
    def __init__(self, username, password):
        self.api = Client(username, password)

    def post_photo(self, photo_path, caption):
        with open(photo_path, 'rb') as photo_file:
            self.api.post_photo(photo_file.read(), caption=caption)

    def send_direct_message(self, user_id, message):
        self.api.direct_message(user_id, message)

    def get_user_info(self, username):
        return self.api.username_info(username)

    def get_recent_posts(self, user_id):
        return self.api.user_feed(user_id, count=10)

    def comment_on_post(self, media_id, comment_text):
        self.api.post_comment(media_id, comment_text)

    def like_post(self, media_id):
        self.api.post_like(media_id)

    def get_followers(self, user_id):
        return self.api.user_followers(user_id)

    def follow_user(self, user_id):
        self.api.friendships_create(user_id)

    def unfollow_user(self, user_id):
        self.api.friendships_destroy(user_id)
```