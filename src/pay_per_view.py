```python
from src.pricing import setPrice
from src.payment_gateways import processPayment
from src.user_data import UserData
from src.content_data import ContentData

class PayPerView:
    def __init__(self):
        self.user_data = UserData()
        self.content_data = ContentData()

    def unlockContent(self, user_id, content_id):
        user = self.user_data.get_user(user_id)
        content = self.content_data.get_content(content_id)

        if user.subscription_status:
            print("You are already subscribed.")
            return

        if content.price > user.payment_info.balance:
            print("Insufficient balance.")
            return

        processPayment(user.payment_info, content.price)
        user.unlocked_content.append(content_id)
        print("Content unlocked successfully.")

    def offerContent(self, content_id, price):
        content = self.content_data.get_content(content_id)
        setPrice(content, price)
        print("Content offered for pay-per-view successfully.")
```