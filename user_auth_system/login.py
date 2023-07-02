```python
import hashlib
from user_model import User
from session_data import Session

def login(username, password):
    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Fetch the user from the database
    user = User.get(username=username)

    # Check if the user exists and the password is correct
    if user and user.password == hashed_password:
        # Create a new session for the user
        session = Session.create(user_id=user.id)

        # Return the session data
        return session
    else:
        # If the login failed, return None
        return None
```