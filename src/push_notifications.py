```python
import json
from messaging_system import MessagingSystem

class PushNotifications:
    def __init__(self, user_data_schema):
        self.user_data_schema = user_data_schema
        self.messaging_system = MessagingSystem(user_data_schema)

    def send_notification(self, user_id, message_name):
        user = self.user_data_schema.get(user_id)
        if not user:
            return "User not found"

        message = self.messaging_system.get_message(message_name)
        if not message:
            return "Message not found"

        notification = {
            "userId": user_id,
            "message": message
        }

        return json.dumps(notification)

    def new_message_notification(self, user_id, creator_id):
        message_name = "newMessage"
        message = f"You have a new message from {creator_id}"
        self.messaging_system.create_message(message_name, message)
        return self.send_notification(user_id, message_name)

    def new_interaction_notification(self, user_id, content_id):
        message_name = "newInteraction"
        message = f"You have a new interaction on your content {content_id}"
        self.messaging_system.create_message(message_name, message)
        return self.send_notification(user_id, message_name)
```