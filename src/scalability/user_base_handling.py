```python
import pymongo
from src.security.user_authentication import authenticateUser
from src.security.data_encryption import encryptData, decryptData

# MongoDB client setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
collection = db["users"]

# User Data Schema
user_data_schema = {
    "username": "",
    "password": "",
    "email": "",
    "created_at": "",
    "last_login": ""
}

def handle_new_user(user_data):
    # Validate user data against schema
    for key in user_data_schema.keys():
        if key not in user_data:
            return {"status": "failure", "message": "Invalid user data"}

    # Encrypt sensitive data
    user_data["password"] = encryptData(user_data["password"])

    # Insert new user into the database
    collection.insert_one(user_data)

    return {"status": "success", "message": "User created successfully"}

def handle_user_login(user_data):
    # Fetch user from the database
    user = collection.find_one({"username": user_data["username"]})

    # If user doesn't exist
    if not user:
        return {"status": "failure", "message": "User not found"}

    # Check password
    if decryptData(user["password"]) != user_data["password"]:
        return {"status": "failure", "message": "Incorrect password"}

    # Update last login time
    collection.update_one({"username": user_data["username"]}, {"$set": {"last_login": user_data["last_login"]}})

    return {"status": "success", "message": "Login successful"}

def handle_user_logout(user_data):
    # Fetch user from the database
    user = collection.find_one({"username": user_data["username"]})

    # If user doesn't exist
    if not user:
        return {"status": "failure", "message": "User not found"}

    # Update last login time
    collection.update_one({"username": user_data["username"]}, {"$set": {"last_login": user_data["last_login"]}})

    return {"status": "success", "message": "Logout successful"}

def get_user_count():
    return collection.count_documents({})
```