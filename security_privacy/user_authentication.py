```python
import hashlib
from admin_panel.manage_user_accounts import UserDataSchema

class UserAuthentication:
    def __init__(self):
        self.users = UserDataSchema.load_users()

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, username: str, password: str) -> bool:
        user = self.users.get(username)
        if user:
            return user['password'] == self.hash_password(password)
        return False

    def secureUserAuthentication(self, username: str, password: str) -> bool:
        if self.verify_password(username, password):
            print(f"User {username} authenticated successfully.")
            return True
        else:
            print(f"Authentication failed for user {username}.")
            return False
```