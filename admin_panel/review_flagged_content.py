```python
import json
from admin_panel.manage_user_accounts import UserDataSchema

class ContentDataSchema:
    def __init__(self, content_id, user_id, content, flag_status):
        self.content_id = content_id
        self.user_id = user_id
        self.content = content
        self.flag_status = flag_status

def reviewFlaggedContent():
    flagged_content_list = []
    try:
        with open('flagged_content.json', 'r') as file:
            flagged_content_list = json.load(file)
    except FileNotFoundError:
        print("No flagged content found.")

    for content in flagged_content_list:
        content_data = ContentDataSchema(**content)
        if content_data.flag_status:
            print(f"Content ID: {content_data.content_id}, User ID: {content_data.user_id}, Content: {content_data.content}")

def updateFlagStatus(content_id, status):
    flagged_content_list = []
    try:
        with open('flagged_content.json', 'r') as file:
            flagged_content_list = json.load(file)
    except FileNotFoundError:
        print("No flagged content found.")

    for content in flagged_content_list:
        if content['content_id'] == content_id:
            content['flag_status'] = status
            with open('flagged_content.json', 'w') as file:
                json.dump(flagged_content_list, file)
            print(f"Content ID: {content_id} flag status updated to: {status}")
            break
    else:
        print("Content ID not found.")
```