```python
from support_help_center import SupportRequestDataSchema

class SupportRequest:
    def __init__(self, support_request_data: SupportRequestDataSchema):
        self.support_request_data = support_request_data

    def handleSupportRequest(self):
        request_id = self.support_request_data.request_id
        user_id = self.support_request_data.user_id
        request_content = self.support_request_data.request_content

        # Handle the support request here
        # This is a placeholder for the actual code to handle the support request
        print(f"Handling support request {request_id} from user {user_id}")

class AdminPanel:
    def __init__(self):
        self.support_requests = []

    def addSupportRequest(self, support_request_data: SupportRequestDataSchema):
        new_request = SupportRequest(support_request_data)
        self.support_requests.append(new_request)

    def handleAllSupportRequests(self):
        for request in self.support_requests:
            request.handleSupportRequest()

# Example usage:
# admin_panel = AdminPanel()
# admin_panel.addSupportRequest(support_request_data)
# admin_panel.handleAllSupportRequests()
```