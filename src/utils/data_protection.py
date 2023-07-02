```python
import os
from cryptography.fernet import Fernet

# Load the secret key from environment variables
SECRET_KEY = os.getenv('SECRET_KEY')

def protect_data(data):
    """
    This function encrypts the provided data using Fernet symmetric encryption.
    """
    cipher_suite = Fernet(SECRET_KEY)
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text

def unprotect_data(cipher_text):
    """
    This function decrypts the provided cipher text using Fernet symmetric encryption.
    """
    cipher_suite = Fernet(SECRET_KEY)
    data = cipher_suite.decrypt(cipher_text).decode()
    return data
```