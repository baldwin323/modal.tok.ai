```python
import os
from content_data_schema import ContentData

class ContentManager:
    def __init__(self):
        self.content_data = ContentData()

    def upload_content(self, user_id, content_type, content_file):
        content_id = self.generate_content_id()
        new_content = {
            'content_id': content_id,
            'user_id': user_id,
            'content_type': content_type,
            'content_file': content_file
        }
        self.content_data.add_content(new_content)
        return content_id

    def delete_content(self, user_id, content_id):
        content = self.content_data.get_content(content_id)
        if content and content['user_id'] == user_id:
            self.content_data.delete_content(content_id)
            return True
        return False

    def update_content(self, user_id, content_id, content_file):
        content = self.content_data.get_content(content_id)
        if content and content['user_id'] == user_id:
            content['content_file'] = content_file
            self.content_data.update_content(content)
            return True
        return False

    def generate_content_id(self):
        return os.urandom(16).hex()

    def handleContentError(self, error):
        print(f"An error occurred: {error}")
        # Add more specific error handling logic here
```
