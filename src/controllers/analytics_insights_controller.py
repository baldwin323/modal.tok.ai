```python
from src.models.user import User
from src.models.subscriber import Subscriber
from src.models.content import Content
from src.analytics_insights import AnalyticsInsights

class AnalyticsInsightsController:
    def __init__(self):
        self.analytics_insights = AnalyticsInsights()

    def track_subscriber_growth(self, user_id):
        user = User.get(user_id)
        return self.analytics_insights.track_subscriber_growth(user)

    def track_engagement(self, content_id):
        content = Content.get(content_id)
        return self.analytics_insights.track_engagement(content)

    def track_revenue(self, user_id):
        user = User.get(user_id)
        return self.analytics_insights.track_revenue(user)

    def get_subscriber_demographics(self, user_id):
        user = User.get(user_id)
        return self.analytics_insights.get_subscriber_demographics(user)

    def get_subscriber_preferences(self, subscriber_id):
        subscriber = Subscriber.get(subscriber_id)
        return self.analytics_insights.get_subscriber_preferences(subscriber)
```