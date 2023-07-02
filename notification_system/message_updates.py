```python
import json
from datetime import datetime
from shared_dependencies import User_Data_Schema, Message_Names, sendNotification

class MessageUpdates:

    def __init__(self):
        self.user_data = User_Data_Schema()
        self.message_names = Message_Names()

    def new_message_notification(self, user_id, message):
        user = self.user_data.get_user(user_id)
        if user:
            notification_content = {
                "title": self.message_names.new_message,
                "message": message,
                "timestamp": datetime.now().isoformat()
            }
            sendNotification(user, notification_content)
        else:
            print(f"No user found with id {user_id}")

    def update_message_notification(self, user_id, message):
        user = self.user_data.get_user(user_id)
        if user:
            notification_content = {
                "title": self.message_names.update_message,
                "message": message,
                "timestamp": datetime.now().isoformat()
            }
            sendNotification(user, notification_content)
        else:
            print(f"No user found with id {user_id}")

if __name__ == "__main__":
    message_updates = MessageUpdates()
    message_updates.new_message_notification(1, "This is a new message")
    message_updates.update_message_notification(1, "This is an updated message")
```