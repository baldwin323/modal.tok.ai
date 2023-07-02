```python
from shared_dependencies import NotificationDataSchema, User_Data_Schema
from datetime import datetime

class OtherEventsNotification:
    def __init__(self, user_data: User_Data_Schema, notification_data: NotificationDataSchema):
        self.user_data = user_data
        self.notification_data = notification_data

    def send_notification(self, event_type: str, event_details: str):
        notification_time = datetime.now()
        notification_message = f"Dear {self.user_data.user_id}, a new event of type {event_type} has occurred. Details: {event_details}. Time: {notification_time}"
        self.notification_data.notifications.append({
            'user_id': self.user_data.user_id,
            'message': notification_message,
            'time': notification_time
        })
        return notification_message

# Example usage:
# user_data = User_Data_Schema(user_id='123', subscription_plan='Premium')
# notification_data = NotificationDataSchema(notifications=[])
# other_event_notification = OtherEventsNotification(user_data, notification_data)
# print(other_event_notification.send_notification('System Update', 'We have updated our terms and conditions.'))
```