```python
import os
from fbchat import Client
from fbchat.models import *

class MessengerIntegration(Client):
    def __init__(self, email, password):
        super().__init__(email, password)

    def send_message(self, user_id, message):
        self.send(Message(text=message), thread_id=user_id, thread_type=ThreadType.USER)

    def receive_message(self):
        if len(self.fetchThreadMessages(thread_id=self.uid, limit=1)) > 0:
            return self.fetchThreadMessages(thread_id=self.uid, limit=1)[0].text
        else:
            return None

if __name__ == "__main__":
    email = os.getenv('MESSENGER_EMAIL')
    password = os.getenv('MESSENGER_PASSWORD')
    messenger = MessengerIntegration(email, password)
```
