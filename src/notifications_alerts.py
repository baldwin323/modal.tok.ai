```python
import json
from src.shared_dependencies import user_id, content_id, newSubscriber, newContent

class Notification:
    def __init__(self, user_id, content_id):
        self.user_id = user_id
        self.content_id = content_id

    def send_notification(self, message_name, additional_info=None):
        notification = {
            'user_id': self.user_id,
            'content_id': self.content_id,
            'message_name': message_name,
            'additional_info': additional_info
        }
        # Here, you would typically send the notification to a service that handles them.
        # For the purpose of this example, we'll just print it.
        print(json.dumps(notification))

def sendNotification(user_id, content_id, message_name, additional_info=None):
    notification = Notification(user_id, content_id)
    notification.send_notification(message_name, additional_info)

def customizeNotification(user_id, content_id, settings):
    # This function would typically interact with a database or another service to customize notifications.
    # For the purpose of this example, we'll just print the settings.
    print(f'Customizing notifications for user {user_id} and content {content_id} with settings {settings}')

# Example usage:
sendNotification(user_id, content_id, newSubscriber, {'subscriber_id': '123'})
customizeNotification(user_id, content_id, {'email': False, 'push': True})
```