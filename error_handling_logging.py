```python
import logging

# Shared dependencies
api_keys = {}
error_log = []

def handleError(e):
    error_message = str(e)
    error_log.append(error_message)
    logging.error(error_message)

def logApiKeys():
    for key in api_keys:
        logging.info(f"API Key for {key}: {api_keys[key]}")

def logErrorMessages():
    for error in error_log:
        logging.error(error)

def setupLogging():
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    setupLogging()
    try:
        logApiKeys()
    except Exception as e:
        handleError(e)
    try:
        logErrorMessages()
    except Exception as e:
        handleError(e)
```