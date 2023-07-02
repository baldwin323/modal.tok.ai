```python
import stripe
from UserAuthenticationSystem import UserDataSchema
from TransactionDataSchema import TransactionData

stripe.api_key = "your_stripe_api_key"

def processPayment(user_id, amount, currency="usd"):
    user = UserDataSchema.get_user(user_id)
    if not user:
        return {"status": "error", "message": "User not found"}

    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            source=user['stripe_token'],
            description=f"Charge for {user['username']}"
        )
        transaction = TransactionData(user_id, charge.id, amount, currency)
        transaction.save()
        return {"status": "success", "message": "Payment processed", "transaction_id": charge.id}
    except stripe.error.CardError as e:
        return {"status": "error", "message": str(e)}

def refundPayment(user_id, transaction_id):
    user = UserDataSchema.get_user(user_id)
    if not user:
        return {"status": "error", "message": "User not found"}

    transaction = TransactionData.get_transaction(transaction_id)
    if not transaction or transaction['user_id'] != user_id:
        return {"status": "error", "message": "Transaction not found"}

    try:
        refund = stripe.Refund.create(
            charge=transaction['transaction_id']
        )
        transaction.update_status('refunded')
        return {"status": "success", "message": "Refund processed", "refund_id": refund.id}
    except stripe.error.InvalidRequestError as e:
        return {"status": "error", "message": str(e)}
```