```python
import datetime
from subscription_management.subscription_plans import SubscriptionPlan
from subscription_management.billing_cycles import BillingCycle

class RevenueTracking:
    def __init__(self):
        self.revenue_data = []

    def track_subscription_revenue(self, user_id, subscription_plan):
        subscription = SubscriptionPlan(user_id, subscription_plan)
        billing_cycle = BillingCycle(subscription)
        revenue = billing_cycle.calculate_revenue()
        self.revenue_data.append({
            'user_id': user_id,
            'subscription_plan': subscription_plan,
            'revenue': revenue,
            'date': datetime.datetime.now()
        })

    def track_sales_commission(self, user_id, sales_amount, commission_rate):
        commission = sales_amount * commission_rate
        self.revenue_data.append({
            'user_id': user_id,
            'sales_amount': sales_amount,
            'commission_rate': commission_rate,
            'commission': commission,
            'date': datetime.datetime.now()
        })

    def get_revenue_report(self):
        return self.revenue_data
```