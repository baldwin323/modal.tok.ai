```python
import pandas as pd
from src.models.subscriber import Subscriber
from src.models.content import Content

class AnalyticsInsights:
    def __init__(self):
        self.subscriber_data = pd.DataFrame(columns=['subscriber_id', 'subscription_date', 'engagement', 'revenue'])
        self.content_data = pd.DataFrame(columns=['content_id', 'views', 'likes', 'comments'])

    def track_subscriber_growth(self, subscriber: Subscriber):
        new_subscriber_data = {'subscriber_id': subscriber.subscriber_id, 'subscription_date': subscriber.subscription_date, 'engagement': subscriber.engagement, 'revenue': subscriber.revenue}
        self.subscriber_data = self.subscriber_data.append(new_subscriber_data, ignore_index=True)

    def track_content_engagement(self, content: Content):
        new_content_data = {'content_id': content.content_id, 'views': content.views, 'likes': content.likes, 'comments': content.comments}
        self.content_data = self.content_data.append(new_content_data, ignore_index=True)

    def get_subscriber_insights(self):
        subscriber_insights = self.subscriber_data.describe()
        return subscriber_insights

    def get_content_insights(self):
        content_insights = self.content_data.describe()
        return content_insights
```