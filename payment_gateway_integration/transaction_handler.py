```python
import datetime
from payment_gateway_integration.payment_gateway import PaymentGateway
from shared_dependencies import TransactionDataSchema, handlePaymentError

class TransactionHandler:
    def __init__(self):
        self.payment_gateway = PaymentGateway()

    def process_transaction(self, user_id, amount, transaction_type):
        transaction_data = TransactionDataSchema(user_id, amount, transaction_type, datetime.datetime.now())
        try:
            transaction_status = self.payment_gateway.process_payment(transaction_data)
            if transaction_status:
                return "Transaction Successful"
            else:
                return "Transaction Failed"
        except Exception as e:
            handlePaymentError(e)

    def refund_transaction(self, transaction_id):
        try:
            refund_status = self.payment_gateway.refund_payment(transaction_id)
            if refund_status:
                return "Refund Successful"
            else:
                return "Refund Failed"
        except Exception as e:
            handlePaymentError(e)
```