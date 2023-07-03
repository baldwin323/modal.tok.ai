```python
import stripe
from model_talk_ai.config import PAYMENT_SYSTEM_CONFIG

stripe.api_key = PAYMENT_SYSTEM_CONFIG['stripe_api_key']

class PaymentSystem:
    def __init__(self, user):
        self.user = user

    def create_customer(self):
        customer = stripe.Customer.create(
            email=self.user.email,
            name=self.user.name
        )
        return customer.id

    def create_subscription(self, customer_id, plan_id):
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {"plan": plan_id},
            ],
        )
        return subscription.id

    def handle_payment(self, amount, currency='usd'):
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            customer=self.user.stripe_customer_id,
        )
        return charge.id

    def update_payment_info(self, customer_id, source):
        stripe.Customer.modify(
            customer_id,
            source=source
        )

    def cancel_subscription(self, subscription_id):
        stripe.Subscription.delete(subscription_id)
```
