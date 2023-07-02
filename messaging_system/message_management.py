```python
import datetime
from user_auth_system.account_management import User
from messaging_system.chat_interface import DOMElements

class Message:
    def __init__(self, message_id, sender_id, receiver_id, message_content):
        self.message_id = message_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message_content = message_content
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return self.message_content

def sendMessage(sender: User, receiver: User, message_content: str):
    message_id = generateMessageID()
    message = Message(message_id, sender.user_id, receiver.user_id, message_content)
    DOMElements.message_input.value = ""
    return message

def receiveMessage(message: Message):
    DOMElements.message_input.value = message.message_content
    return message

def generateMessageID():
    return uuid.uuid4().hex
```