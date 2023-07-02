```python
from user_auth_system.account_management import User, SessionData

class PersonalInfo:
    def __init__(self, user: User, session_data: SessionData):
        self.user = user
        self.session_data = session_data

    def update_personal_info(self, name: str, email: str, phone: str):
        if self.session_data.user_id == self.user.user_id:
            self.user.name = name
            self.user.email = email
            self.user.phone = phone
            return True
        else:
            return False

    def get_personal_info(self):
        if self.session_data.user_id == self.user.user_id:
            return {
                "name": self.user.name,
                "email": self.user.email,
                "phone": self.user.phone
            }
        else:
            return None
```