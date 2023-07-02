```python
import pandas as pd
from sales_revenue_tracking.revenue_tracking import RevenueDataSchema

class RevenueReport:
    def __init__(self):
        self.revenue_data = RevenueDataSchema()

    def generate_report(self, user_id):
        user_revenue_data = self.revenue_data.get_user_revenue(user_id)
        report = pd.DataFrame(user_revenue_data)
        return report

    def get_total_revenue(self):
        total_revenue = self.revenue_data.get_total_revenue()
        return total_revenue

    def get_average_revenue_per_user(self):
        total_revenue = self.get_total_revenue()
        total_users = self.revenue_data.get_total_users()
        average_revenue_per_user = total_revenue / total_users
        return average_revenue_per_user

    def get_revenue_growth(self, period):
        current_period_revenue = self.revenue_data.get_revenue_for_period(period)
        previous_period_revenue = self.revenue_data.get_revenue_for_period(period - 1)
        revenue_growth = (current_period_revenue - previous_period_revenue) / previous_period_revenue
        return revenue_growth
```