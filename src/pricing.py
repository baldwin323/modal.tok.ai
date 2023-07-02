```python
import json

# Importing User, Content and Creator Data Schemas
from user_data import UserData
from content_data import ContentData
from creator_data import CreatorData

class Pricing:

    def __init__(self):
        self.user_data = UserData()
        self.content_data = ContentData()
        self.creator_data = CreatorData()

    def set_price(self, content_id, price):
        """
        Set the price for a specific piece of content.
        """
        content = self.content_data.get_content(content_id)
        if content:
            content['price'] = price
            self.content_data.update_content(content)
            return True
        return False

    def get_price(self, content_id):
        """
        Get the price for a specific piece of content.
        """
        content = self.content_data.get_content(content_id)
        if content:
            return content['price']
        return None

    def unlock_content(self, user_id, content_id):
        """
        Unlock a specific piece of content for a user after payment.
        """
        user = self.user_data.get_user(user_id)
        content = self.content_data.get_content(content_id)
        if user and content:
            if user['subscription_status'] == 'active' and user['payment_information']['balance'] >= content['price']:
                user['payment_information']['balance'] -= content['price']
                self.user_data.update_user(user)
                return True
        return False
```