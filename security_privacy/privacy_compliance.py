```python
import json
from user_data_schema import UserData
from admin_data_schema import AdminData

class PrivacyCompliance:
    def __init__(self):
        self.privacy_settings = json.load(open('privacySettings.json'))

    def ensure_privacy_compliance(self, user_data: UserData, admin_data: AdminData):
        if not self.privacy_settings['compliance']:
            raise Exception('Privacy compliance settings are not enabled')

        if user_data.age < 13:
            raise Exception('User is under the age limit for data collection')

        if admin_data.role != 'admin':
            raise Exception('Only admins can ensure privacy compliance')

        user_data.is_compliant = True
        return user_data

    def update_privacy_settings(self, new_settings):
        self.privacy_settings = new_settings
        with open('privacySettings.json', 'w') as f:
            json.dump(self.privacy_settings, f)

        return self.privacy_settings

if __name__ == "__main__":
    privacy_compliance = PrivacyCompliance()
    user_data = UserData('John Doe', 25, 'user')
    admin_data = AdminData('Admin', 'admin')

    try:
        privacy_compliance.ensure_privacy_compliance(user_data, admin_data)
        print('User data is compliant')
    except Exception as e:
        print(str(e))

    new_settings = {'compliance': True}
    privacy_compliance.update_privacy_settings(new_settings)
    print('Privacy settings updated')
```