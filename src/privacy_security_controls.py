```python
from src.models.user import User
from src.models.content import Content
from src.controllers.privacy_security_controller import PrivacySecurityController

class PrivacySecurityControls:
    def __init__(self):
        self.controller = PrivacySecurityController()

    def set_content_privacy(self, user_id, content_id, is_private):
        user = User.get(user_id)
        content = Content.get(content_id)
        if user and content:
            self.controller.set_content_privacy(user, content, is_private)

    def restrict_content_access(self, user_id, content_id, restricted_subscriber_ids):
        user = User.get(user_id)
        content = Content.get(content_id)
        if user and content:
            self.controller.restrict_content_access(user, content, restricted_subscriber_ids)

    def report_abusive_behavior(self, reporter_id, reported_user_id, report_details):
        reporter = User.get(reporter_id)
        reported_user = User.get(reported_user_id)
        if reporter and reported_user:
            self.controller.report_abusive_behavior(reporter, reported_user, report_details)
```