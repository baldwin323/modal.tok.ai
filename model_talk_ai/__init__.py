```python
from .config import load_config
from .chatbot import Chatbot
from .personality_cloning import clone_personality
from .social_media_integration import integrate_social_media
from .natural_language_processing import process_language
from .api_backend import handle_api
from .payment_system import handle_payment
from .ui import render_ui

def init_app():
    # Load configuration
    config = load_config()

    # Initialize chatbot
    chatbot = Chatbot(clone_personality, integrate_social_media, process_language, handle_api, handle_payment)

    # Render UI
    render_ui(chatbot)

    return chatbot
```