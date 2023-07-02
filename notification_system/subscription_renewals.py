```python
import datetime
from subscription_management.subscription_plans import SubscriptionDataSchema
from notification_system.notification_data import NotificationDataSchema

def send_renewal_notification(user_id, subscription_plan):
    # Fetch user and subscription data
    user_data = UserDataSchema.objects.get(user_id=user_id)
    subscription_data = SubscriptionDataSchema.objects.get(subscription_plan=subscription_plan)

    # Check if subscription is due for renewal
    if subscription_data.expiry_date <= datetime.datetime.now():
        # Create a new notification
        notification = NotificationDataSchema(
            user_id=user_id,
            message_name='SubscriptionRenewal',
            message_content=f'Your subscription plan {subscription_plan} is due for renewal.',
            timestamp=datetime.datetime.now()
        )
        notification.save()

        # Send the notification to the user
        user_data.notifications.add(notification)
        user_data.save()

        return True

    return False
```