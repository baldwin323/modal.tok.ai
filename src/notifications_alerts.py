```python
from src.models.user import User
from src.models.subscriber import Subscriber
from src.models.content import Content

class NotificationsAlerts:
    def __init__(self):
        self.subscribers = []
        self.messages = []
        self.content_updates = []

    def add_subscriber(self, subscriber_id):
        subscriber = Subscriber.get_by_id(subscriber_id)
        if subscriber:
            self.subscribers.append(subscriber)
            self.send_notification('new-subscriber', subscriber)

    def add_message(self, user_id, message):
        user = User.get_by_id(user_id)
        if user:
            self.messages.append(message)
            self.send_notification('new-message', user)

    def add_content_update(self, content_id):
        content = Content.get_by_id(content_id)
        if content:
            self.content_updates.append(content)
            self.send_notification('content-update', content)

    def send_notification(self, message_name, user):
        # This is a placeholder function. In a real-world application, this would send a notification to the user.
        print(f'Sending {message_name} notification to {user.name}')

    def customize_alerts(self, user_id, settings):
        user = User.get_by_id(user_id)
        if user:
            user.notification_settings = settings
            print(f'Notification settings updated for {user.name}')
```