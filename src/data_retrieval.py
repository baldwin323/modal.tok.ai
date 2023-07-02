```python
import requests
from src.authentication import authenticate
from src.error_handling import handle_error

def retrieve_data(api_keys, platform):
    try:
        if platform == 'OnlyFans':
            url = 'https://onlyfans.com/api/'
        elif platform == 'Twitter':
            url = 'https://api.twitter.com/1.1/'
        elif platform == 'Instagram':
            url = 'https://graph.instagram.com/'

        headers = authenticate(api_keys, platform)
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            handle_error(response)

    except Exception as e:
        handle_error(e)

def retrieve_follower_count(user_data):
    try:
        follower_count = user_data['follower_count']
        return follower_count
    except KeyError as e:
        handle_error(e)

def retrieve_engagement_metrics(user_data):
    try:
        engagement_metrics = user_data['engagement_metrics']
        return engagement_metrics
    except KeyError as e:
        handle_error(e)

def retrieve_content_uploads(user_data):
    try:
        content_uploads = user_data['content_uploads']
        return content_uploads
    except KeyError as e:
        handle_error(e)
```