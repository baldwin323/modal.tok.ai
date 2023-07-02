```python
from src.security.user_authentication import authenticateUser
from src.security.data_encryption import encryptData, decryptData
from src.mobile_interface.user_interface import User, Feature

def accessFeature(user, feature_id):
    # Check if user is authenticated
    if not authenticateUser(user):
        return {"message": "loginFailure"}

    # Decrypt user data
    user_data = decryptData(user.data)

    # Check if user has access to the feature
    if feature_id not in user_data['features']:
        return {"message": "featureAccessDenied"}

    # Access the feature
    feature = Feature(feature_id)
    feature_data = feature.access()

    # Encrypt the feature data before sending it to the user
    encrypted_feature_data = encryptData(feature_data)

    return {
        "message": "featureAccessed",
        "data": encrypted_feature_data
    }
```