```python
import json
from support_help_center import SupportRequestDataSchema

class HandleSupportRequests:
    def __init__(self):
        self.supportRequestList = []
        self.supportRequestDataSchema = SupportRequestDataSchema()

    def load_support_requests(self):
        with open('support_requests.json', 'r') as file:
            self.supportRequestList = json.load(file)

    def save_support_requests(self):
        with open('support_requests.json', 'w') as file:
            json.dump(self.supportRequestList, file)

    def handle_support_request(self, supportRequest):
        if self.supportRequestDataSchema.validate(supportRequest):
            self.supportRequestList.append(supportRequest)
            self.save_support_requests()
            return 'supportRequest handled successfully'
        else:
            return 'Invalid supportRequest data'

    def get_support_requests(self):
        self.load_support_requests()
        return self.supportRequestList

if __name__ == "__main__":
    handler = HandleSupportRequests()
    print(handler.get_support_requests())
```