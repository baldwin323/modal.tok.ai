```python
import datetime
from subscription_management.subscription_plans import SubscriptionPlan
from shared_dependencies import User, Subscription, sendNotification

def check_renewals():
    users = User.get_all_users()
    for user in users:
        subscription = Subscription.get_by_user_id(user.id)
        if subscription:
            if subscription.expiry_date <= datetime.datetime.now():
                send_renewal_notification(user, subscription)

def send_renewal_notification(user, subscription):
    message = f"Dear {user.name}, your subscription plan {subscription.plan.name} is about to expire. Please renew your subscription."
    sendNotification(user.id, 'subscription-update', message)

if __name__ == "__main__":
    check_renewals()
```