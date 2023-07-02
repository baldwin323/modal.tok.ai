```python
import bcrypt
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    profile_details = db.Column(db.JSON)
    api_credentials = db.Column(db.JSON)
    transaction_data = db.Column(db.JSON)

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

def signup(username, password, profile_details, api_credentials):
    user = User(username=username)
    user.set_password(password)
    user.profile_details = profile_details
    user.api_credentials = api_credentials
    db.session.add(user)
    db.session.commit()
    return {'message': 'signupSuccess'}

def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return {'message': 'loginSuccess'}
    else:
        return {'message': 'loginFailure'}

def update_profile(username, profile_details, api_credentials):
    user = User.query.filter_by(username=username).first()
    if user:
        user.profile_details = profile_details
        user.api_credentials = api_credentials
        db.session.commit()
        return {'message': 'profileUpdate'}
    else:
        return {'message': 'userNotFound'}

def process_payment(username, transaction_data):
    user = User.query.filter_by(username=username).first()
    if user:
        user.transaction_data = transaction_data
        db.session.commit()
        return {'message': 'paymentProcessed'}
    else:
        return {'message': 'userNotFound'}
```