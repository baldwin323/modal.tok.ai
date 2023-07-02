```python
import kik
from credentials import YOUR_KIK_USERNAME, YOUR_KIK_API_KEY

class KikAPI:
    def __init__(self):
        self.kik_api = kik.KikApi(YOUR_KIK_USERNAME, YOUR_KIK_API_KEY)

    def send_message(self, username, message):
        to_send = kik.messages.TextMessage(
            to=username,
            chat_id=self.kik_api.random_guid(),
            body=message
        )
        self.kik_api.send_messages([to_send])

    def receive_message(self):
        messages = self.kik_api.get_messages()
        for message in messages:
            if isinstance(message, kik.messages.TextMessage):
                return message.body

    def login(self):
        self.kik_api.start()

    def logout(self):
        self.kik_api.stop()
```