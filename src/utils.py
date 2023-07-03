```python
import json
from src.models.user import User
from src.models.subscriber import Subscriber
from src.models.content import Content

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def convert_to_user(data):
    return User(data['user_id'], data['username'], data['email'], data['password'])

def convert_to_subscriber(data):
    return Subscriber(data['subscriber_id'], data['username'], data['email'])

def convert_to_content(data):
    return Content(data['content_id'], data['title'], data['description'], data['creator_id'], data['is_private'])

def validate_platform(platform):
    return platform in SUPPORTED_PLATFORMS

def validate_language(language):
    return language in SUPPORTED_LANGUAGES
```