```python
from user_auth_system.account_management import User

def update_social_media_handles(user_id, twitter_handle=None, instagram_handle=None, onlyfans_handle=None):
    user = User.query.get(user_id)
    if not user:
        raise Exception("User not found")

    if twitter_handle:
        user.twitter_handle = twitter_handle
    if instagram_handle:
        user.instagram_handle = instagram_handle
    if onlyfans_handle:
        user.onlyfans_handle = onlyfans_handle

    user.save()

def get_social_media_handles(user_id):
    user = User.query.get(user_id)
    if not user:
        raise Exception("User not found")

    return {
        "twitter_handle": user.twitter_handle,
        "instagram_handle": user.instagram_handle,
        "onlyfans_handle": user.onlyfans_handle
    }
```