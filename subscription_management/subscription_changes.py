```python
import datetime
from user_data_schema import User
from subscription_data_schema import Subscription
from transaction_handler import processTransaction

def manageSubscription(user_id, new_subscription_type):
    user = User.query.get(user_id)
    old_subscription = Subscription.query.filter_by(user_id=user_id).first()

    if old_subscription.subscription_type != new_subscription_type:
        old_subscription.end_date = datetime.datetime.now()
        new_subscription = Subscription(user_id=user_id, subscription_type=new_subscription_type, start_date=datetime.datetime.now())
        
        if new_subscription_type == 'premium':
            processTransaction(user_id, 10)
        elif new_subscription_type == 'standard':
            processTransaction(user_id, 5)
        
        Subscription.add(new_subscription)
        User.update(user)

def cancelSubscription(user_id):
    user = User.query.get(user_id)
    subscription = Subscription.query.filter_by(user_id=user_id).first()
    
    if subscription:
        subscription.end_date = datetime.datetime.now()
        User.update(user)

def upgradeSubscription(user_id):
    manageSubscription(user_id, 'premium')

def downgradeSubscription(user_id):
    manageSubscription(user_id, 'standard')
```