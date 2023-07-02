```python
from shared_dependencies import UserDataSchema, SubscriptionDataSchema

class UserAccount:
    def __init__(self, user_data: UserDataSchema, subscription_data: SubscriptionDataSchema):
        self.user_data = user_data
        self.subscription_data = subscription_data

    def manageUserAccount(self, user_id: str, action: str, **kwargs):
        if action == 'create':
            self._createUserAccount(user_id, **kwargs)
        elif action == 'update':
            self._updateUserAccount(user_id, **kwargs)
        elif action == 'delete':
            self._deleteUserAccount(user_id)
        else:
            raise ValueError(f"Invalid action: {action}")

    def _createUserAccount(self, user_id: str, **kwargs):
        # Code to create a new user account
        pass

    def _updateUserAccount(self, user_id: str, **kwargs):
        # Code to update an existing user account
        pass

    def _deleteUserAccount(self, user_id: str):
        # Code to delete a user account
        pass
```