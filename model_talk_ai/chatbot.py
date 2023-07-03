```python
import json
from .personality_cloning import clone_personality
from .social_media_integration import integrate_social_media
from .natural_language_processing import process_language
from .api_backend import handle_api
from .payment_system import handle_payment

USER_MESSAGE = "user_message"
BOT_MESSAGE = "bot_message"

class ChatBot:
    def __init__(self, user_schema, message_schema):
        self.user_schema = user_schema
        self.message_schema = message_schema
        self.current_user = None
        self.current_message = None

    def receive_message(self, message_json):
        message_data = json.loads(message_json)
        self.current_message = self.message_schema.load(message_data)
        self.current_user = self.user_schema.load(self.current_message['user'])

    def process_message(self):
        if self.current_message['type'] == USER_MESSAGE:
            processed_message = process_language(self.current_message['content'])
            response = clone_personality(processed_message, self.current_user)
            self.send_message(response, BOT_MESSAGE)

    def send_message(self, message_content, message_type):
        message_data = self.message_schema.dump({
            'user': self.current_user,
            'content': message_content,
            'type': message_type
        })
        integrate_social_media(json.dumps(message_data))

    def handle_payment_request(self, payment_json):
        payment_data = json.loads(payment_json)
        payment = handle_payment(payment_data, self.current_user)
        self.send_message(payment, BOT_MESSAGE)

    def handle_api_request(self, api_json):
        api_data = json.loads(api_json)
        api_response = handle_api(api_data, self.current_user)
        self.send_message(api_response, BOT_MESSAGE)
```