```python
import logging

def handle_error(error):
    """
    Function to handle errors gracefully.
    """
    error_message = str(error)
    log_error(error_message)
    print(f"An error occurred: {error_message}")
    return None

def log_error(error_message):
    """
    Function to log errors for future debugging.
    """
    logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
    logging.error(error_message)
```