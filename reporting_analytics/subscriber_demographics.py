```python
import pandas as pd
from user_data_schema import UserData
from subscription_data_schema import SubscriptionData

def generate_subscriber_demographics():
    # Load user and subscription data
    user_data = pd.read_csv(UserData)
    subscription_data = pd.read_csv(SubscriptionData)

    # Merge the two dataframes on 'user_id'
    merged_data = pd.merge(user_data, subscription_data, on='user_id')

    # Group by subscription plan and count the number of users for each plan
    subscription_demographics = merged_data.groupby('subscription_plan')['user_id'].count()

    return subscription_demographics

if __name__ == "__main__":
    subscriber_demographics = generate_subscriber_demographics()
    print(subscriber_demographics)
```