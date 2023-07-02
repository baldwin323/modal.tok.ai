```python
from flask import request, jsonify
from src import models, authentication, authorization, api_integration

def register_user():
    data = request.get_json()
    user = models.User(data)
    if authentication.registerUser(user):
        return jsonify({"message": "userRegistered"}), 201
    else:
        return jsonify({"message": "registrationFailed"}), 400

def login_user():
    data = request.get_json()
    user = models.User(data)
    if authentication.loginUser(user):
        return jsonify({"message": "userLoggedIn"}), 200
    else:
        return jsonify({"message": "loginFailed"}), 401

def fetch_data():
    if authorization.verifyUser(request.headers.get('Authorization')):
        data = api_integration.fetchData()
        if data:
            return jsonify({"message": "dataFetched", "data": data}), 200
        else:
            return jsonify({"message": "fetchFailed"}), 400
    else:
        return jsonify({"message": "unauthorized"}), 403

def process_payment():
    data = request.get_json()
    if authorization.verifyUser(request.headers.get('Authorization')):
        if api_integration.processPayment(data):
            return jsonify({"message": "paymentSuccessful"}), 200
        else:
            return jsonify({"message": "paymentFailed"}), 400
    else:
        return jsonify({"message": "unauthorized"}), 403
```