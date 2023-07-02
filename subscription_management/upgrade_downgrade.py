```python
from user_data_schema import User
from subscription_data_schema import Subscription

def upgrade_plan(user_id, new_plan):
    user = User.objects.get(id=user_id)
    subscription = Subscription.objects.get(user=user)
    
    # Check if the new plan is higher than the current one
    if subscription.plan < new_plan:
        subscription.plan = new_plan
        subscription.save()
        return {"status": "success", "message": "Plan upgraded successfully"}
    else:
        return {"status": "error", "message": "New plan must be higher than the current one"}

def downgrade_plan(user_id, new_plan):
    user = User.objects.get(id=user_id)
    subscription = Subscription.objects.get(user=user)
    
    # Check if the new plan is lower than the current one
    if subscription.plan > new_plan:
        subscription.plan = new_plan
        subscription.save()
        return {"status": "success", "message": "Plan downgraded successfully"}
    else:
        return {"status": "error", "message": "New plan must be lower than the current one"}
```