```python
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from user_registration_and_authentication.password_management import verify_password
from models import User, UserSchema

app = Flask(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
user_schema = UserSchema()

@app.route('/login', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        return jsonify({'message': 'User not found!'}), 404

    if verify_password(data['password'], user.password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
```