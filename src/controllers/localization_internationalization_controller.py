```python
from src.models.user import User
from src.models.content import Content
from src.config import SUPPORTED_LANGUAGES, PAYMENT_GATEWAY_CONFIG

class LocalizationInternationalizationController:
    def __init__(self):
        self.supported_languages = SUPPORTED_LANGUAGES
        self.payment_gateway_config = PAYMENT_GATEWAY_CONFIG

    def localize_content(self, content_id, language):
        if language not in self.supported_languages:
            raise ValueError(f"Unsupported language: {language}")

        content = Content.get_by_id(content_id)
        content.language = language
        content.save()

    def internationalize_app(self, user_id, language):
        if language not in self.supported_languages:
            raise ValueError(f"Unsupported language: {language}")

        user = User.get_by_id(user_id)
        user.language = language
        user.save()

    def integrate_payment_gateway(self, user_id, region):
        user = User.get_by_id(user_id)
        user.payment_gateway = self.payment_gateway_config[region]
        user.save()
```