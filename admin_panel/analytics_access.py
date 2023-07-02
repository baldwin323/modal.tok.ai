```python
import pandas as pd
from reporting_and_analytics.revenue_reports import RevenueReport
from reporting_and_analytics.engagement_metrics import EngagementMetrics
from reporting_and_analytics.subscriber_demographics import SubscriberDemographics

class AnalyticsAccess:
    def __init__(self, user_role):
        self.user_role = user_role

    def check_access(self):
        if self.user_role != 'admin':
            raise Exception('Access Denied. Only admin can access analytics.')

    def get_revenue_report(self):
        self.check_access()
        revenue_report = RevenueReport()
        return revenue_report.generate_report()

    def get_engagement_metrics(self):
        self.check_access()
        engagement_metrics = EngagementMetrics()
        return engagement_metrics.generate_report()

    def get_subscriber_demographics(self):
        self.check_access()
        subscriber_demographics = SubscriberDemographics()
        return subscriber_demographics.generate_report()

    def get_all_reports(self):
        self.check_access()
        revenue_report = self.get_revenue_report()
        engagement_metrics = self.get_engagement_metrics()
        subscriber_demographics = self.get_subscriber_demographics()

        all_reports = pd.concat([revenue_report, engagement_metrics, subscriber_demographics], axis=1)
        return all_reports
```