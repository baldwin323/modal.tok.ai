```python
import json
import os

def load_json(file_path):
    """
    Load JSON data from a file
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(file_path, data):
    """
    Save JSON data to a file
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def check_file_exists(file_path):
    """
    Check if a file exists
    """
    return os.path.isfile(file_path)

def create_directory(directory_path):
    """
    Create a directory if it doesn't exist
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def get_env_variable(var_name):
    """
    Get the value of an environment variable
    """
    return os.getenv(var_name)
```