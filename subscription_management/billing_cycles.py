```python
import datetime
from dateutil.relativedelta import relativedelta
from subscription_management.subscription_plans import SubscriptionPlan
from shared_dependencies.transaction_data_schema import Transaction

class BillingCycle:
    def __init__(self, user_id, subscription_plan):
        self.user_id = user_id
        self.subscription_plan = SubscriptionPlan(subscription_plan)
        self.start_date = datetime.datetime.now()
        self.end_date = self.calculate_end_date()

    def calculate_end_date(self):
        if self.subscription_plan.plan_type == 'monthly':
            return self.start_date + relativedelta(months=1)
        elif self.subscription_plan.plan_type == 'yearly':
            return self.start_date + relativedelta(years=1)
        else:
            raise ValueError("Invalid subscription plan type")

    def renew_subscription(self):
        self.start_date = self.end_date
        self.end_date = self.calculate_end_date()
        transaction = Transaction(self.user_id, self.subscription_plan.price)
        transaction.processTransaction()

    def cancel_subscription(self):
        self.end_date = datetime.datetime.now()

    def upgrade_subscription(self, new_plan):
        self.subscription_plan = SubscriptionPlan(new_plan)
        self.end_date = self.calculate_end_date()
        transaction = Transaction(self.user_id, self.subscription_plan.price)
        transaction.processTransaction()

    def downgrade_subscription(self, new_plan):
        self.subscription_plan = SubscriptionPlan(new_plan)
        self.end_date = self.calculate_end_date()
        transaction = Transaction(self.user_id, self.subscription_plan.price)
        transaction.processTransaction()
```