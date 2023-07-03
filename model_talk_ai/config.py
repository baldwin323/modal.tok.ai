```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Exported Variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SOCIAL_MEDIA_API_KEYS = {
    'kik': os.getenv('KIK_API_KEY'),
    'telegram': os.getenv('TELEGRAM_API_KEY'),
    'instagram': os.getenv('INSTAGRAM_API_KEY'),
    'messenger': os.getenv('MESSENGER_API_KEY')
}
ONLYFANS_AFFILIATE_API_KEY = os.getenv('ONLYFANS_AFFILIATE_API_KEY')

# Payment System Config
PAYMENT_SYSTEM_CONFIG = {
    'subscription_charge': os.getenv('SUBSCRIPTION_CHARGE'),
    'sales_percentage': os.getenv('SALES_PERCENTAGE')
}
```