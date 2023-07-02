```python
import json
from src.security.user_authentication import User

class PrivacyCompliance:
    def __init__(self):
        self.privacy_regulations = self.load_privacy_regulations()

    def load_privacy_regulations(self):
        with open('privacy_regulations.json', 'r') as file:
            return json.load(file)

    def check_compliance(self, user: User):
        for regulation in self.privacy_regulations:
            if not self.check_regulation_compliance(user, regulation):
                return False
        return True

    def check_regulation_compliance(self, user: User, regulation):
        if regulation['type'] == 'age':
            return user.age >= regulation['value']
        elif regulation['type'] == 'country':
            return user.country == regulation['value']
        else:
            return True
```