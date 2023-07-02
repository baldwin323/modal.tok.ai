```python
import datetime
from subscription_management.subscription_plans import SubscriptionPlan
from user_data_schema import User

class SalesCommission:
    def __init__(self, user: User, subscription_plan: SubscriptionPlan):
        self.user = user
        self.subscription_plan = subscription_plan
        self.commission_rate = 0.1  # 10% commission rate

    def calculate_commission(self):
        return self.subscription_plan.price * self.commission_rate

    def record_commission(self):
        commission = self.calculate_commission()
        timestamp = datetime.datetime.now()
        record = {
            'user_id': self.user.user_id,
            'subscription_plan': self.subscription_plan.plan_id,
            'commission': commission,
            'timestamp': timestamp
        }
        return record

    def update_user_revenue(self):
        self.user.revenue += self.calculate_commission()

    def process_commission(self):
        self.record_commission()
        self.update_user_revenue()
```