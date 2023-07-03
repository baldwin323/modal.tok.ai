```python
from src.models.user import User
from src.models.content import Content

class PrivacySecurityController:
    def __init__(self):
        pass

    def set_content_privacy(self, user_id, content_id, is_private):
        user = User.get(user_id)
        content = Content.get(content_id)
        if user.is_creator_of(content):
            content.set_privacy(is_private)
        else:
            raise Exception("User does not have permission to change this content's privacy settings")

    def restrict_content_access(self, user_id, content_id, restricted_subscriber_ids):
        user = User.get(user_id)
        content = Content.get(content_id)
        if user.is_creator_of(content):
            content.restrict_access(restricted_subscriber_ids)
        else:
            raise Exception("User does not have permission to restrict access to this content")

    def report_abusive_behavior(self, reporter_id, reported_user_id, report_details):
        reporter = User.get(reporter_id)
        reported_user = User.get(reported_user_id)
        reporter.report_abuse(reported_user, report_details)
```
