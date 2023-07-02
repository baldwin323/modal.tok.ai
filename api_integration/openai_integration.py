```python
import openai
from user_auth_system.account_management import User
from profile_management.api_credentials import get_api_credentials

class OpenAIIntegration:
    def __init__(self, user: User):
        self.user = user
        self.api_key, self.api_secret = get_api_credentials(user)

    def setup_openai(self):
        openai.api_key = self.api_key

    def clone_personality(self, text: str):
        self.setup_openai()
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text,
            temperature=0.5,
            max_tokens=100
        )
        return response.choices[0].text.strip()

    def generate_response(self, message: str):
        cloned_text = self.clone_personality(message)
        return cloned_text
```