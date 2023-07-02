```python
import json
from content_management_system import ContentDataSchema
from notification_system import NotificationDataSchema

def send_content_update_notification(user_id, content_id):
    # Fetch the content details
    content_data = ContentDataSchema.objects.get(id=content_id)
    
    # Prepare the notification data
    notification_data = NotificationDataSchema()
    notification_data.user_id = user_id
    notification_data.content_id = content_id
    notification_data.message_name = 'ContentUpdateNotification'
    notification_data.message = f"New update in {content_data.title}"
    
    # Save the notification data
    notification_data.save()

    # Send the notification
    send_notification(user_id, notification_data)

def send_notification(user_id, notification_data):
    # Convert the notification data to JSON
    notification_json = json.dumps(notification_data, default=str)

    # Send the notification (the actual implementation depends on the notification system)
    # For example, it could be an email, a push notification, etc.
    # Here we just print it for simplicity
    print(f"Sending notification to user {user_id}: {notification_json}")
```