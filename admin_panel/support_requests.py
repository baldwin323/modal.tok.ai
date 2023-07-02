```python
import datetime
from user_data_schema import User
from error_handling_functions import handleAdminError

class SupportRequest:
    def __init__(self, request_id, user_id, request_text, status="Open"):
        self.request_id = request_id
        self.user_id = user_id
        self.request_text = request_text
        self.status = status
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return f"Request ID: {self.request_id}, User ID: {self.user_id}, Status: {self.status}, Created At: {self.created_at}"

class SupportRequestHandler:
    def __init__(self):
        self.requests = []

    def create_request(self, user_id, request_text):
        try:
            if User.exists(user_id):
                request_id = len(self.requests) + 1
                new_request = SupportRequest(request_id, user_id, request_text)
                self.requests.append(new_request)
                print(f"Support request created: {new_request}")
            else:
                raise ValueError("User does not exist.")
        except Exception as e:
            handleAdminError(e)

    def close_request(self, request_id):
        try:
            request = next((r for r in self.requests if r.request_id == request_id), None)
            if request:
                request.status = "Closed"
                print(f"Support request closed: {request}")
            else:
                raise ValueError("Request does not exist.")
        except Exception as e:
            handleAdminError(e)

    def view_all_requests(self):
        for request in self.requests:
            print(request)
```
