```python
from src.models.user import User
from src.models.subscriber import Subscriber
from src.config import SUPPORTED_PLATFORMS

class MultiPlatformAccessController:
    def __init__(self):
        self.supported_platforms = SUPPORTED_PLATFORMS

    def check_platform_availability(self, platform):
        if platform in self.supported_platforms:
            return True
        return False

    def get_user_platform(self, user_id):
        user = User.get(user_id)
        return user.platform

    def switch_platform(self, user_id, new_platform):
        if self.check_platform_availability(new_platform):
            user = User.get(user_id)
            user.platform = new_platform
            user.save()
            return True
        return False

    def get_subscriber_platform(self, subscriber_id):
        subscriber = Subscriber.get(subscriber_id)
        return subscriber.platform

    def switch_subscriber_platform(self, subscriber_id, new_platform):
        if self.check_platform_availability(new_platform):
            subscriber = Subscriber.get(subscriber_id)
            subscriber.platform = new_platform
            subscriber.save()
            return True
        return False
```