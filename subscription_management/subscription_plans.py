```python
class SubscriptionPlan:
    def __init__(self, plan_id, name, price, duration):
        self.plan_id = plan_id
        self.name = name
        self.price = price
        self.duration = duration

class SubscriptionPlans:
    def __init__(self):
        self.plans = []

    def add_plan(self, plan_id, name, price, duration):
        new_plan = SubscriptionPlan(plan_id, name, price, duration)
        self.plans.append(new_plan)

    def remove_plan(self, plan_id):
        for plan in self.plans:
            if plan.plan_id == plan_id:
                self.plans.remove(plan)
                break

    def get_plan(self, plan_id):
        for plan in self.plans:
            if plan.plan_id == plan_id:
                return plan
        return None

    def get_all_plans(self):
        return self.plans
```