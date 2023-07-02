```python
import json

class CreatorProfile:
    def __init__(self, user_data_schema):
        self.user_data_schema = user_data_schema

    def get_profile(self, username):
        try:
            with open(self.user_data_schema, 'r') as file:
                data = json.load(file)
                if username in data:
                    return data[username]
                else:
                    return "User not found"
        except FileNotFoundError:
            return "User data file not found"

    def update_profile(self, username, new_data):
        try:
            with open(self.user_data_schema, 'r') as file:
                data = json.load(file)
                if username in data:
                    data[username].update(new_data)
                    with open(self.user_data_schema, 'w') as file:
                        json.dump(data, file)
                    return "Profile updated successfully"
                else:
                    return "User not found"
        except FileNotFoundError:
            return "User data file not found"

    def delete_profile(self, username):
        try:
            with open(self.user_data_schema, 'r') as file:
                data = json.load(file)
                if username in data:
                    del data[username]
                    with open(self.user_data_schema, 'w') as file:
                        json.dump(data, file)
                    return "Profile deleted successfully"
                else:
                    return "User not found"
        except FileNotFoundError:
            return "User data file not found"
```