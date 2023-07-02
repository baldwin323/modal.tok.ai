```python
import json
from content_management_system.content_data_schema import ContentDataSchema
from user_account_management import UserAccountManagement

class FlaggedContentReview:
    def __init__(self):
        self.content_data_schema = ContentDataSchema()
        self.user_account_management = UserAccountManagement()

    def get_flagged_content(self):
        flagged_content = self.content_data_schema.get_flagged_content()
        return flagged_content

    def review_content(self, content_id):
        content = self.content_data_schema.get_content_by_id(content_id)
        if not content:
            return "Content not found"
        return json.dumps(content, indent=4)

    def approve_content(self, content_id):
        self.content_data_schema.update_content_status(content_id, "Approved")
        self.user_account_management.send_notification(content_id, "Your content has been approved")

    def reject_content(self, content_id, reason):
        self.content_data_schema.update_content_status(content_id, "Rejected")
        self.user_account_management.send_notification(content_id, f"Your content has been rejected due to: {reason}")

    def handle_flagged_content(self):
        flagged_content = self.get_flagged_content()
        for content in flagged_content:
            print(f"Reviewing content: {content['content_id']}")
            print(self.review_content(content['content_id']))
            action = input("Approve or Reject? (A/R): ")
            if action.lower() == 'a':
                self.approve_content(content['content_id'])
            elif action.lower() == 'r':
                reason = input("Enter reason for rejection: ")
                self.reject_content(content['content_id'], reason)
            else:
                print("Invalid action. Skipping this content.")
```
