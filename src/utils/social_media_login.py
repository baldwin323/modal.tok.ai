```python
import requests
from src.config import SOCIAL_MEDIA_API_KEYS

def social_login(provider, access_token):
    if provider == 'twitter':
        return twitter_login(access_token)
    elif provider == 'instagram':
        return instagram_login(access_token)
    elif provider == 'onlyfans':
        return onlyfans_login(access_token)
    else:
        raise ValueError('Invalid social media provider')

def twitter_login(access_token):
    url = "https://api.twitter.com/1.1/account/verify_credentials.json"
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers)
    return response.json()

def instagram_login(access_token):
    url = "https://graph.instagram.com/me?fields=id,username&access_token=" + access_token
    response = requests.get(url)
    return response.json()

def onlyfans_login(access_token):
    url = "https://onlyfans.com/api2/user/current"
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers)
    return response.json()
```