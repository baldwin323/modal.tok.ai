```python
import json
from datetime import datetime
from UserAuthenticationSystem import UserDataSchema
from APIIntegrationModule import get_platform_api

class MessagingSystem:
    def __init__(self):
        self.message_schema = {
            "message_id": "",
            "sender_id": "",
            "receiver_id": "",
            "platform": "",
            "message_content": "",
            "timestamp": ""
        }

    def sendMessage(self, sender_id, receiver_id, platform, message_content):
        message = self.message_schema.copy()
        message["message_id"] = self.generate_message_id()
        message["sender_id"] = sender_id
        message["receiver_id"] = receiver_id
        message["platform"] = platform
        message["message_content"] = message_content
        message["timestamp"] = str(datetime.now())

        platform_api = get_platform_api(platform)
        platform_api.send_message(message)

        return 'messageSent', message

    def receiveMessage(self, platform):
        platform_api = get_platform_api(platform)
        new_messages = platform_api.get_new_messages()

        for message in new_messages:
            message["message_id"] = self.generate_message_id()
            message["timestamp"] = str(datetime.now())

        return 'messageReceived', new_messages

    def generate_message_id(self):
        return str(datetime.now().timestamp()).replace(".", "")

if __name__ == "__main__":
    ms = MessagingSystem()
    print(ms.sendMessage("user1", "user2", "OnlyFans", "Hello, World!"))
    print(ms.receiveMessage("OnlyFans"))
```