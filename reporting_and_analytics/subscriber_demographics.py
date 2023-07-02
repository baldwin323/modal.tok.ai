```python
import pandas as pd
from user_data_schema import UserData
from subscription_data_schema import SubscriptionData

class SubscriberDemographics:
    def __init__(self):
        self.user_data = UserData()
        self.subscription_data = SubscriptionData()

    def get_subscriber_demographics(self):
        # Merge user and subscription data on user_id
        merged_data = pd.merge(self.user_data.get_user_data(), self.subscription_data.get_subscription_data(), on='user_id')

        # Group by subscription type and get count
        demographics = merged_data.groupby('subscription_type').count()

        return demographics

    def generate_report(self):
        demographics = self.get_subscriber_demographics()

        # Generate report
        report = demographics.to_csv('subscriber_demographics_report.csv')

        return report

if __name__ == "__main__":
    subscriber_demographics = SubscriberDemographics()
    subscriber_demographics.generate_report()
```