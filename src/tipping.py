```python
import payment_gateways as pg
from user_data import User
from creator_data import Creator

def send_tip(user_id, creator_id, amount):
    user = User.get(user_id)
    creator = Creator.get(creator_id)

    if user.balance < amount:
        return {"status": "error", "message": "Insufficient balance"}

    transaction = pg.process_payment(user, creator, amount)

    if transaction["status"] == "success":
        user.balance -= amount
        creator.balance += amount
        User.update(user)
        Creator.update(creator)
        return {"status": "success", "message": "Tip sent successfully"}

    return {"status": "error", "message": "Transaction failed"}

def get_tips_for_creator(creator_id):
    creator = Creator.get(creator_id)
    return creator.tips_received
```