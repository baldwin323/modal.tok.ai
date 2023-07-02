```python
import json
from content_management_system.content_manager import ContentDataSchema
from notification_system.notification_sender import sendNotification

def handle_content_update(content_id):
    # Fetch the updated content details
    content_data = ContentDataSchema.objects.get(content_id=content_id)

    # Prepare the notification message
    message = {
        'type': 'content-update',
        'content_id': content_data.content_id,
        'user_id': content_data.user_id,
        'content_type': content_data.content_type,
        'message': f'New {content_data.content_type} has been uploaded.'
    }

    # Send the notification
    sendNotification(json.dumps(message))

def handle_content_error(error):
    print(f"Error occurred: {error}")
    # Add error handling code here
```