```python
import pandas as pd
from datetime import datetime
from user_data_schema import UserData
from content_data_schema import ContentData
from subscription_data_schema import SubscriptionData

class EngagementMetrics:
    def __init__(self):
        self.user_data = UserData()
        self.content_data = ContentData()
        self.subscription_data = SubscriptionData()

    def calculate_engagement(self, user_id):
        user_content = self.content_data.get_user_content(user_id)
        user_subscriptions = self.subscription_data.get_user_subscriptions(user_id)
        
        engagement_score = len(user_content) * 0.5 + len(user_subscriptions) * 0.5
        return engagement_score

    def get_engagement_report(self):
        users = self.user_data.get_all_users()
        engagement_report = pd.DataFrame(columns=['user_id', 'engagement_score', 'last_active'])

        for user in users:
            engagement_score = self.calculate_engagement(user['user_id'])
            last_active = self.user_data.get_last_active(user['user_id'])
            engagement_report = engagement_report.append({'user_id': user['user_id'], 'engagement_score': engagement_score, 'last_active': last_active}, ignore_index=True)

        return engagement_report

    def get_most_engaged_users(self, top_n=10):
        engagement_report = self.get_engagement_report()
        most_engaged_users = engagement_report.sort_values(by='engagement_score', ascending=False).head(top_n)
        return most_engaged_users

    def get_least_engaged_users(self, top_n=10):
        engagement_report = self.get_engagement_report()
        least_engaged_users = engagement_report.sort_values(by='engagement_score', ascending=True).head(top_n)
        return least_engaged_users
```