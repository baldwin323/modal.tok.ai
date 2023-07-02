import requests
from credentials import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_USER_ID
from chatbot.nltk_processing import process_message

class InstagramAPI:
    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id

    def get_user_info(self):
        url = f"https://graph.instagram.com/{self.user_id}?fields=id,username&access_token={self.access_token}"
        response = requests.get(url)
        return response.json()

    def send_message(self, recipient_id, message):
        url = f"https://graph.instagram.com/{recipient_id}/messages?access_token={self.access_token}"
        payload = {
            "message": {
                "text": message
            }
        }
        response = requests.post(url, json=payload)
        return response.json()

    def receive_message(self, message):
        processed_message = process_message(message)
        return processed_message

instagram_api = InstagramAPI(INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_USER_ID)