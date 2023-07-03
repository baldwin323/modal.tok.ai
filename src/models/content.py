```python
class Content:
    def __init__(self, content_id, creator_id, privacy_settings, content_data):
        self.content_id = content_id
        self.creator_id = creator_id
        self.privacy_settings = privacy_settings
        self.content_data = content_data

    def set_privacy(self, privacy_settings):
        self.privacy_settings = privacy_settings

    def get_privacy(self):
        return self.privacy_settings

    def get_content_data(self):
        return self.content_data

    def set_content_data(self, content_data):
        self.content_data = content_data
```