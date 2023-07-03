```python
from src.models.user import User
from src.models.subscriber import Subscriber
from src.models.content import Content

class SupportHelpCenterController:
    def __init__(self):
        self.users = []
        self.subscribers = []
        self.contents = []

    def provideSupport(self, user_id):
        user = self._find_user(user_id)
        if user:
            return f"Providing support to {user.name}"
        else:
            return "User not found"

    def reportIssue(self, user_id, issue):
        user = self._find_user(user_id)
        if user:
            return f"Issue reported by {user.name}: {issue}"
        else:
            return "User not found"

    def contactSupport(self, user_id):
        user = self._find_user(user_id)
        if user:
            return f"{user.name} contacted support"
        else:
            return "User not found"

    def _find_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None
```