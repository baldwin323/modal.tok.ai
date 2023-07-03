```python
import kik
from kik.api import KikApi
from kik.messages import messages_from_json, TextMessage

class KikIntegration:
    def __init__(self, api_key, bot_name):
        self.kik_api = KikApi(bot_name, api_key)
        self.bot_name = bot_name

    def send_message(self, chat_id, message):
        text_message = TextMessage(
            to=chat_id,
            chat_id=chat_id,
            body=message
        )
        self.kik_api.send_messages([text_message])

    def receive_message(self, messages):
        for message in messages_from_json(messages):
            if isinstance(message, TextMessage):
                self.send_message(message.from_user, "Received your message!")

    def configure_kik(self, webhook):
        self.kik_api.update_configuration(webhook)

    def run(self, request):
        if not self.kik_api.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
            return 'Invalid signature', 403
        messages = messages_from_json(request.json['messages'])
        self.receive_message(messages)
        return 'OK', 200
```
This code creates a class for Kik integration. It initializes with the bot name and API key, and has methods for sending and receiving messages, configuring the webhook, and running the bot. The `run` method also verifies the signature of incoming requests for security.