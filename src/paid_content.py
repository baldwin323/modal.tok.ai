```python
from src.user_data import UserData
from src.content_data import ContentData
from src.payment_gateways import PaymentGateway

class PaidContent:
    def __init__(self):
        self.user_data = UserData()
        self.content_data = ContentData()
        self.payment_gateway = PaymentGateway()

    def unlock_content(self, user_id, content_id):
        user = self.user_data.get_user(user_id)
        content = self.content_data.get_content(content_id)

        if user.subscription_status:
            return "Content is already available for this user."

        if self.payment_gateway.process_payment(user.payment_information, content.price):
            user.unlocked_content.append(content_id)
            return "Content unlocked successfully."

        return "Payment failed. Please try again."

    def set_price(self, content_id, price):
        content = self.content_data.get_content(content_id)
        content.price = price
        return "Price set successfully."
```