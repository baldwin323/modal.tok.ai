```python
import datetime
from transaction_handler import processTransaction
from user_data_schema import User
from transaction_data_schema import Transaction

class PaymentGateway:
    def __init__(self):
        self.users = []
        self.transactions = []

    def add_user(self, user_id, subscription_status):
        user = User(user_id, subscription_status)
        self.users.append(user)

    def process_payment(self, user_id, amount, transaction_type):
        transaction_id = len(self.transactions) + 1
        transaction_time = datetime.datetime.now()
        transaction = Transaction(transaction_id, user_id, amount, transaction_type, transaction_time)
        self.transactions.append(transaction)

        # Process the transaction
        processTransaction(transaction)

    def get_transaction_history(self, user_id):
        user_transactions = [transaction for transaction in self.transactions if transaction.user_id == user_id]
        return user_transactions

    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
```