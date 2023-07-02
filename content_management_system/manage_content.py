```python
from user_data_schema import User
from content_data_schema import Content

def manageContent(user_id, content_id, action):
    user = User.objects.get(id=user_id)
    content = Content.objects.get(id=content_id)

    if action == 'delete':
        if user == content.creator:
            content.delete()
        else:
            raise PermissionError("User does not have permission to delete this content.")
    elif action == 'update':
        if user == content.creator:
            # Update content logic here
            pass
        else:
            raise PermissionError("User does not have permission to update this content.")
    elif action == 'view':
        # View content logic here
        pass
    else:
        raise ValueError("Invalid action.")

    return True
```