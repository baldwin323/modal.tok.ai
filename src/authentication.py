```python
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from src.models import User
from src.database import db_session

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def register_user(username, password):
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db_session.add(new_user)
    db_session.commit()

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None
```