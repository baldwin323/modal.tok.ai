```python
from models.user import User
from models.subscriber import Subscriber
from controllers.support_help_center_controller import SupportHelpCenterController

class SupportHelpCenter:
    def __init__(self):
        self.controller = SupportHelpCenterController()

    def get_faq(self):
        return self.controller.get_faq()

    def get_knowledge_base(self):
        return self.controller.get_knowledge_base()

    def create_ticket(self, user_id, issue):
        user = User.get(user_id)
        if not user:
            return "User not found"
        return self.controller.create_ticket(user, issue)

    def contact_support(self, user_id, message):
        user = User.get(user_id)
        if not user:
            return "User not found"
        return self.controller.contact_support(user, message)

    def report_issue(self, user_id, issue):
        user = User.get(user_id)
        if not user:
            return "User not found"
        return self.controller.report_issue(user, issue)
```