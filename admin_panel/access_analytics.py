```python
import pandas as pd
from reporting_analytics.revenue_report import RevenueDataSchema
from reporting_analytics.engagement_report import EngagementDataSchema
from reporting_analytics.subscriber_demographics import SubscriberDataSchema

class AccessAnalytics:
    def __init__(self):
        self.revenue_data = RevenueDataSchema()
        self.engagement_data = EngagementDataSchema()
        self.subscriber_data = SubscriberDataSchema()

    def accessAnalytics(self, user_id):
        user_revenue_data = self.revenue_data.get_data(user_id)
        user_engagement_data = self.engagement_data.get_data(user_id)
        user_subscriber_data = self.subscriber_data.get_data(user_id)

        analytics_data = pd.concat([user_revenue_data, user_engagement_data, user_subscriber_data], axis=1)
        return analytics_data
```