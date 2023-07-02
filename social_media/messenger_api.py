import requests
from credentials import MESSENGER_ACCESS_TOKEN

class MessengerAPI:
    def __init__(self):
        self.access_token = MESSENGER_ACCESS_TOKEN
        self.api_url = 'https://graph.facebook.com/v2.6/me/messages'

    def send_message(self, recipient_id, message_text):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'messaging_type': 'RESPONSE',
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'text': message_text
            }
        }
        params = {
            'access_token': self.access_token
        }
        response = requests.post(self.api_url, headers=headers, params=params, json=data)
        return response.json()

    def receive_message(self, data):
        for event in data['entry'][0]['messaging']:
            if 'message' in event:
                return {
                    'sender_id': event['sender']['id'],
                    'message_text': event['message']['text']
                }
        return None

messenger_api = MessengerAPI()