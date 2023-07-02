```python
import datetime
from subscription_data_schema import Subscription

def BillingCycleUpdate(user_id, new_billing_date):
    # Fetch the user's subscription data
    user_subscription = Subscription.objects.get(user_id=user_id)

    # Update the billing cycle
    user_subscription.billing_cycle = new_billing_date
    user_subscription.save()

    # Send a notification to the user about the billing cycle update
    sendNotification(user_id, 'BillingCycleUpdate')

def calculate_next_billing_date(user_id):
    # Fetch the user's subscription data
    user_subscription = Subscription.objects.get(user_id=user_id)

    # Calculate the next billing date based on the subscription plan
    if user_subscription.subscription_plan == 'monthly':
        next_billing_date = user_subscription.billing_cycle + datetime.timedelta(days=30)
    elif user_subscription.subscription_plan == 'quarterly':
        next_billing_date = user_subscription.billing_cycle + datetime.timedelta(days=90)
    elif user_subscription.subscription_plan == 'yearly':
        next_billing_date = user_subscription.billing_cycle + datetime.timedelta(days=365)

    # Update the billing cycle
    BillingCycleUpdate(user_id, next_billing_date)

def check_billing_due(user_id):
    # Fetch the user's subscription data
    user_subscription = Subscription.objects.get(user_id=user_id)

    # Check if the billing date is due
    if user_subscription.billing_cycle <= datetime.datetime.now():
        # If due, calculate the next billing date
        calculate_next_billing_date(user_id)
```