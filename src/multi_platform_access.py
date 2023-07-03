```python
from src.models.user import User
from src.config import SUPPORTED_PLATFORMS

class MultiPlatformAccess:
    def __init__(self):
        self.supported_platforms = SUPPORTED_PLATFORMS

    def check_platform_availability(self, platform):
        if platform in self.supported_platforms:
            return True
        return False

    def access_platform(self, user_id, platform):
        user = User.get(user_id)
        if not user:
            return "User not found"
        if not self.check_platform_availability(platform):
            return "Platform not supported"
        # Logic to access the platform goes here
        return "Access granted"

    def get_supported_platforms(self):
        return self.supported_platforms
```