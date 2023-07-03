```python
from src.models.user import User
from src.models.subscriber import Subscriber
from src.models.content import Content
from src.utils import sendNotification, customizeAlerts

class NotificationsAlertsController:
    def __init__(self):
        self.users = User.get_all_users()
        self.subscribers = Subscriber.get_all_subscribers()
        self.contents = Content.get_all_contents()

    def notify_new_subscriber(self, subscriber_id):
        subscriber = next((s for s in self.subscribers if s.id == subscriber_id), None)
        if subscriber:
            for user in self.users:
                if user.id == subscriber.user_id:
                    sendNotification(user.id, 'new-subscriber', f'New subscriber: {subscriber.name}')
                    break

    def notify_new_message(self, user_id, message):
        user = next((u for u in self.users if u.id == user_id), None)
        if user:
            sendNotification(user.id, 'new-message', message)

    def notify_content_update(self, content_id):
        content = next((c for c in self.contents if c.id == content_id), None)
        if content:
            for subscriber in self.subscribers:
                if subscriber.user_id == content.user_id:
                    sendNotification(subscriber.id, 'content-update', f'Content updated: {content.title}')
                    break

    def customize_user_alerts(self, user_id, settings):
        user = next((u for u in self.users if u.id == user_id), None)
        if user:
            customizeAlerts(user.id, settings)
```
