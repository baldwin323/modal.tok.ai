```python
from cryptography.fernet import Fernet
from user_data_schema import UserData

class DataEncryption:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_user_data(self, user_data: UserData):
        encrypted_data = self.cipher_suite.encrypt(user_data)
        return encrypted_data

    def decrypt_user_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data

data_encryption = DataEncryption()

def implementDataEncryption(user_data: UserData):
    encrypted_data = data_encryption.encrypt_user_data(user_data)
    return encrypted_data

def decryptUserData(encrypted_data):
    decrypted_data = data_encryption.decrypt_user_data(encrypted_data)
    return decrypted_data
```