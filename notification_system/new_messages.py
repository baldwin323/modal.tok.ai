```python
import json
from shared_dependencies import NotificationDataSchema, UserDataSchema

def send_new_message_notification(user_id, message):
    user_data = UserDataSchema.get_user_data(user_id)
    notification_data = NotificationDataSchema.create_notification_data('NewMessage', message)
    
    if user_data['notification_preference'] == 'email':
        send_email_notification(user_data['email'], notification_data)
    elif user_data['notification_preference'] == 'app':
        send_app_notification(user_data['device_id'], notification_data)

def send_email_notification(email, notification_data):
    # This function will send an email notification. The implementation of this function depends on the email service used.
    pass

def send_app_notification(device_id, notification_data):
    # This function will send an app notification. The implementation of this function depends on the push notification service used.
    pass
```