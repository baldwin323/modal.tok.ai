```python
import hashlib
from user_model import User

def signup(username, password, email):
    # Check if user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return {"error": "User already exists"}

    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Create a new user
    new_user = User(username=username, password=hashed_password, email=email)

    # Save the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return {"message": "User created successfully"}

def validate_signup_form(username, password, email):
    # Basic form validation
    if not username or not password or not email:
        return {"error": "All fields are required"}

    # Check if email is valid
    if "@" not in email or "." not in email:
        return {"error": "Invalid email address"}

    # Check if password is secure
    if len(password) < 8:
        return {"error": "Password must be at least 8 characters long"}

    return signup(username, password, email)
```