```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskcrud'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/register', methods=['POST'])
def register_user():
    email = request.json['email']
    password = request.json['password']

    new_user = User(email, password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

if __name__ == '__main__':
    app.run(debug=True)
```