```python
import stripe
from src import config

stripe.api_key = config.STRIPE_API_KEY

def process_payment(amount, currency, source, description):
    try:
        stripe.Charge.create(
            amount=amount,
            currency=currency,
            source=source,
            description=description,
        )
        return True
    except stripe.error.StripeError as e:
        print(e)
        return False
```