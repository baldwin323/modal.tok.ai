```python
import pandas as pd
from admin_panel.analytics_data_schema import AnalyticsDataSchema

class AccessAnalytics:
    def __init__(self):
        self.analytics_data_schema = AnalyticsDataSchema()
        self.analytics_display = 'analyticsDisplay'

    def get_analytics_data(self):
        # Fetch data from the database
        data = self.analytics_data_schema.fetch_data()

        # Convert data to pandas DataFrame for easier manipulation
        df = pd.DataFrame(data)

        return df

    def display_analytics(self):
        df = self.get_analytics_data()

        # Display the analytics data on the admin panel
        # This is a placeholder function, replace with actual display function
        display_function(self.analytics_display, df)

    def update_analytics(self, message_name='analyticsUpdate'):
        # Update the analytics data based on the received message
        # This is a placeholder function, replace with actual update function
        update_function(message_name, self.get_analytics_data())

if __name__ == "__main__":
    access_analytics = AccessAnalytics()
    access_analytics.display_analytics()
    access_analytics.update_analytics()
```