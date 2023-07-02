```python
import stripe
from user_auth_system.account_management import User
from payment_gateway_integration.financial_transactions import TransactionSchema

stripe.api_key = "your_stripe_api_key"

def process_content_purchase(user_id, content_id, card_details):
    user = User.get(user_id)
    if not user:
        return {"error": "User not found"}

    content_price = get_content_price(content_id)
    if not content_price:
        return {"error": "Content not found or not available for purchase"}

    try:
        charge = stripe.Charge.create(
            amount=content_price,
            currency="usd",
            source=card_details,  # obtained with Stripe.js
            description=f"Content purchase by {user.username}"
        )
        if charge.paid:
            transaction = TransactionSchema(
                user_id=user_id,
                product_id=content_id,
                amount=content_price
            )
            transaction.save()
            return {"success": "Content purchased successfully"}
        else:
            return {"error": "Payment failed"}

    except stripe.error.CardError as e:
        return {"error": str(e)}

def get_content_price(content_id):
    # This function should be implemented based on your content pricing model
    pass
```