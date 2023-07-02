```python
import datetime
from user_auth_system.account_management import User
from payment_gateway_integration.financial_transactions import processTransaction

class Subscription:
    def __init__(self, user_id, product_id, amount, card_number, expiry_date, cvv, card_holder_name):
        self.user_id = user_id
        self.product_id = product_id
        self.amount = amount
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.card_holder_name = card_holder_name
        self.subscription_date = datetime.datetime.now()

    def renew_subscription(self):
        user = User.get_user_by_id(self.user_id)
        if user:
            transaction_status = processTransaction(self.user_id, self.product_id, self.amount, self.card_number, self.expiry_date, self.cvv, self.card_holder_name)
            if transaction_status == "Success":
                self.subscription_date = datetime.datetime.now()
                return "Subscription renewed successfully"
            else:
                return "Failed to renew subscription"
        else:
            return "User not found"

    def cancel_subscription(self):
        self.subscription_date = None
        return "Subscription cancelled successfully"
```