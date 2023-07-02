```python
import stripe
from user_data import UserData
from creator_data import CreatorData

stripe.api_key = "your_stripe_api_key"

def process_payment(user_id, creator_id, amount):
    user = UserData.get_user(user_id)
    creator = CreatorData.get_creator(creator_id)

    if user and creator:
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                source=user.payment_info,
                description=f"Payment from {user.username} to {creator.username}"
            )
            if charge.paid:
                return True
            else:
                return False
        except stripe.error.CardError as e:
            print(f"Card error: {e}")
            return False
    else:
        print("User or creator not found.")
        return False
```