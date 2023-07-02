```python
import json
from user_data_schema import UserData
from admin_data_schema import AdminData

class ManageUserAccounts:
    def __init__(self):
        self.user_list = []
        self.admin_data = AdminData()

    def load_users(self):
        with open('user_data.json', 'r') as file:
            data = json.load(file)
            for user in data['users']:
                self.user_list.append(UserData(user))

    def update_user(self, user_id, update_data):
        for user in self.user_list:
            if user.id == user_id:
                user.update_data(update_data)
                self.admin_data.log('userUpdate', user_id)
                break

    def delete_user(self, user_id):
        for user in self.user_list:
            if user.id == user_id:
                self.user_list.remove(user)
                self.admin_data.log('userUpdate', user_id)
                break

    def add_user(self, user_data):
        new_user = UserData(user_data)
        self.user_list.append(new_user)
        self.admin_data.log('userUpdate', new_user.id)

if __name__ == "__main__":
    manager = ManageUserAccounts()
    manager.load_users()
    manager.update_user(1, {'name': 'New Name'})
    manager.delete_user(2)
    manager.add_user({'id': 3, 'name': 'New User', 'email': 'newuser@example.com'})
```