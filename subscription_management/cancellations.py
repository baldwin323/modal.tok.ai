```python
from datetime import datetime
from user_data_schema import User
from subscription_data_schema import Subscription

def cancel_subscription(user_id):
    user = User.query.get(user_id)
    if user and user.subscription:
        user.subscription.status = 'Cancelled'
        user.subscription.cancelled_at = datetime.now()
        db.session.commit()
        return {"message": "Subscription cancelled successfully."}, 200
    else:
        return {"message": "User or subscription not found."}, 404

def handle_cancellation_request(request):
    user_id = request.get('user_id')
    if user_id:
        return cancel_subscription(user_id)
    else:
        return {"message": "Invalid request. User ID is required."}, 400
```