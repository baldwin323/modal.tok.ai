```python
import datetime
from payment_gateway_integration.transaction_handler import processTransaction
from subscription_management.subscription_plans import manageSubscription

class SalesCommission:
    def __init__(self, user_id, transaction_id, commission_rate):
        self.user_id = user_id
        self.transaction_id = transaction_id
        self.commission_rate = commission_rate
        self.transaction_amount = processTransaction(self.transaction_id).amount
        self.commission_amount = self.calculate_commission()

    def calculate_commission(self):
        return self.transaction_amount * self.commission_rate

    def record_commission(self):
        commission_data = {
            'user_id': self.user_id,
            'transaction_id': self.transaction_id,
            'commission_rate': self.commission_rate,
            'commission_amount': self.commission_amount,
            'date': datetime.datetime.now()
        }
        return commission_data

def handleSalesCommission(user_id, transaction_id, commission_rate):
    sales_commission = SalesCommission(user_id, transaction_id, commission_rate)
    commission_data = sales_commission.record_commission()
    return commission_data
```