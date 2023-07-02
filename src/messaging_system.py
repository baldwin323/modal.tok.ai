```python
import json
from user_data_schema import User
from creator_data_schema import Creator

class MessagingSystem:
    def __init__(self):
        self.messages = []

    def send_message(self, sender: User, receiver: Creator, message: str):
        new_message = {
            "sender_id": sender.user_id,
            "receiver_id": receiver.creator_id,
            "message": message,
            "message_name": "newMessage"
        }
        self.messages.append(new_message)
        return json.dumps(new_message)

    def get_messages(self, user_id: str):
        user_messages = [message for message in self.messages if message['sender_id'] == user_id or message['receiver_id'] == user_id]
        return json.dumps(user_messages)

    def delete_message(self, message_id: int):
        self.messages = [message for message in self.messages if message['message_id'] != message_id]
        return json.dumps(self.messages)
```