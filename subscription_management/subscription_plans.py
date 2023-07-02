```python
from datetime import datetime
from user_data_schema import User
from subscription_data_schema import Subscription

class SubscriptionPlan:
    def __init__(self, plan_id, name, price, duration):
        self.plan_id = plan_id
        self.name = name
        self.price = price
        self.duration = duration  # duration in days

    def get_details(self):
        return {
            "plan_id": self.plan_id,
            "name": self.name,
            "price": self.price,
            "duration": self.duration
        }

class SubscriptionManager:
    def __init__(self):
        self.subscription_plans = {}

    def add_plan(self, plan_id, name, price, duration):
        if plan_id in self.subscription_plans:
            raise Exception("Plan ID already exists.")
        self.subscription_plans[plan_id] = SubscriptionPlan(plan_id, name, price, duration)

    def remove_plan(self, plan_id):
        if plan_id not in self.subscription_plans:
            raise Exception("Plan ID does not exist.")
        del self.subscription_plans[plan_id]

    def get_plan(self, plan_id):
        if plan_id not in self.subscription_plans:
            raise Exception("Plan ID does not exist.")
        return self.subscription_plans[plan_id].get_details()

    def subscribe_user(self, user_id, plan_id):
        user = User.get_user(user_id)
        plan = self.get_plan(plan_id)
        subscription = Subscription(user_id, plan_id, datetime.now(), plan["duration"])
        user.add_subscription(subscription)

    def cancel_subscription(self, user_id, plan_id):
        user = User.get_user(user_id)
        user.remove_subscription(plan_id)
```