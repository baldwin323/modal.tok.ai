```python
import os
from content_data_schema import Content

def uploadContent(user_id, content_type, content_file):
    try:
        # Check if the content file exists
        if not os.path.exists(content_file):
            raise FileNotFoundError("Content file does not exist")

        # Create a new content instance
        new_content = Content(user_id, content_type, content_file)

        # Save the content instance to the database
        new_content.save()

        # Send a notification about the new content
        sendNotification(user_id, 'content-update', {'content_id': new_content.id})

        print("Content uploaded successfully")
    except Exception as e:
        handleContentError(e)

def handleContentError(error):
    print(f"An error occurred: {error}")
```