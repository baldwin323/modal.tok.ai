```python
from werkzeug.security import generate_password_hash, check_password_hash
from user_registration_and_authentication.register import UserSchema

def manage_password(user_id, old_password, new_password):
    user = UserSchema.query.get(user_id)
    if user and check_password_hash(user.password, old_password):
        user.password = generate_password_hash(new_password)
        db.session.commit()
        return True
    return False
```