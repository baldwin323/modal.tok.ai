```python
import googleanalytics as ga
from src import config

def initialize_analytics():
    account = ga.authenticate(identity=config.GOOGLE_ANALYTICS_ID)
    profile = account.default_profile
    return profile

def get_page_views(profile, start_date, end_date):
    return profile.core.query.range(start_date, end_date).metrics('ga:pageviews').get()

def get_unique_visitors(profile, start_date, end_date):
    return profile.core.query.range(start_date, end_date).metrics('ga:users').get()

def get_bounce_rate(profile, start_date, end_date):
    return profile.core.query.range(start_date, end_date).metrics('ga:bounceRate').get()
```