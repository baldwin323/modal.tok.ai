```python
from cryptography.fernet import Fernet

# Shared dependency: Encryption Key
encryption_key = Fernet.generate_key()

def encrypt_data(user_data):
    """
    Encrypts user data using the shared encryption key.
    """
    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(user_data)
    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Decrypts user data using the shared encryption key.
    """
    cipher_suite = Fernet(encryption_key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data
```