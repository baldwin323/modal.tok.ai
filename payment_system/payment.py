```python
import stripe

class PaymentSystem:
    def __init__(self, stripe_api_key):
        stripe.api_key = stripe_api_key

    def create_customer(self, email, payment_method):
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method,
            invoice_settings={
                'default_payment_method': payment_method,
            },
        )
        return customer

    def create_subscription(self, customer_id, price_id):
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {
                    'price': price_id,
                },
            ],
            expand=['latest_invoice.payment_intent'],
        )
        return subscription

    def calculate_commission(self, amount, commission_rate):
        commission = amount * commission_rate
        return commission

    def payout(self, amount, destination_account):
        payout = stripe.Payout.create(
            amount=amount,
            currency="usd",
            destination=destination_account,
        )
        return payout
```