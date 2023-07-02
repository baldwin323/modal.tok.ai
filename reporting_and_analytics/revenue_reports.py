```python
import pandas as pd
from sales_and_revenue_tracking.revenue_tracker import RevenueTracker
from subscription_management.subscription_plans import SubscriptionPlans

class RevenueReports:
    def __init__(self):
        self.revenue_tracker = RevenueTracker()
        self.subscription_plans = SubscriptionPlans()

    def generate_revenue_report(self, user_id):
        user_revenue_data = self.revenue_tracker.get_user_revenue(user_id)
        user_subscription_data = self.subscription_plans.get_user_subscription(user_id)

        revenue_report = pd.DataFrame({
            'Subscription Revenue': user_revenue_data['subscription_revenue'],
            'Merchandise Sales Revenue': user_revenue_data['merchandise_sales_revenue'],
            'Content Purchase Revenue': user_revenue_data['content_purchase_revenue'],
            'Total Revenue': user_revenue_data['total_revenue'],
            'Subscription Plan': user_subscription_data['subscription_plan'],
            'Subscription Status': user_subscription_data['subscription_status']
        }, index=[0])

        return revenue_report

    def generate_total_revenue_report(self):
        total_revenue_data = self.revenue_tracker.get_total_revenue()
        total_subscription_data = self.subscription_plans.get_total_subscriptions()

        total_revenue_report = pd.DataFrame({
            'Total Subscription Revenue': total_revenue_data['total_subscription_revenue'],
            'Total Merchandise Sales Revenue': total_revenue_data['total_merchandise_sales_revenue'],
            'Total Content Purchase Revenue': total_revenue_data['total_content_purchase_revenue'],
            'Total Revenue': total_revenue_data['total_revenue'],
            'Total Subscriptions': total_subscription_data['total_subscriptions']
        }, index=[0])

        return total_revenue_report
```