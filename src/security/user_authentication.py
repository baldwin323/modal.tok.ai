```python
import hashlib
from src.security.data_encryption import encryptData
from src.security.privacy_compliance import checkCompliance

class UserAuthentication:
    def __init__(self, user_data_schema):
        self.user_data_schema = user_data_schema
        self.encryption_key = "your_encryption_key_here"

    def loginUser(self, username, password):
        user = self.user_data_schema.get(username)
        if user and self.checkPassword(user, password):
            return {"message": "loginSuccess", "user": user}
        else:
            return {"message": "loginFailure"}

    def logoutUser(self, username):
        user = self.user_data_schema.get(username)
        if user:
            return {"message": "userLogout", "user": user}
        else:
            return {"message": "logoutFailure"}

    def checkPassword(self, user, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return user['password'] == encryptData(hashed_password, self.encryption_key)

    def authenticateUser(self, username, password):
        user = self.user_data_schema.get(username)
        if user and self.checkPassword(user, password) and checkCompliance(user):
            return True
        else:
            return False
```