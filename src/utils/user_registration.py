```python
from src.models import User
from src.database import db_session
from werkzeug.security import generate_password_hash

def register_user(username, password, email):
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, email=email)
    db_session.add(new_user)
    db_session.commit()
```