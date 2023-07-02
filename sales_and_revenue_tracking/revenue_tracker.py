```python
import datetime
from payment_gateway_integration.transaction_handler import TransactionData
from subscription_management.subscription_plans import SubscriptionData

class RevenueTracker:
    def __init__(self):
        self.revenue_data = []

    def track_revenue(self, transaction_data: TransactionData, subscription_data: SubscriptionData):
        revenue_item = {
            'transaction_id': transaction_data.transaction_id,
            'user_id': transaction_data.user_id,
            'amount': transaction_data.amount,
            'date': datetime.datetime.now(),
            'subscription_id': subscription_data.subscription_id if subscription_data else None
        }
        self.revenue_data.append(revenue_item)

    def get_total_revenue(self):
        return sum(item['amount'] for item in self.revenue_data)

    def get_revenue_by_user(self, user_id):
        return sum(item['amount'] for item in self.revenue_data if item['user_id'] == user_id)

    def get_revenue_by_subscription(self, subscription_id):
        return sum(item['amount'] for item in self.revenue_data if item['subscription_id'] == subscription_id)
```