```python
import pandas as pd
from user_data_schema import UserData
from content_data_schema import ContentData

def generateReport(user_id):
    # Fetch user data
    user_data = UserData.objects.get(user_id=user_id)
    
    # Fetch content data
    content_data = ContentData.objects.filter(user_id=user_id)
    
    # Calculate engagement metrics
    total_views = sum([content.views for content in content_data])
    total_likes = sum([content.likes for content in content_data])
    total_comments = sum([content.comments for content in content_data])
    
    # Create a DataFrame for the report
    report_data = {
        'User ID': user_id,
        'Username': user_data.username,
        'Total Views': total_views,
        'Total Likes': total_likes,
        'Total Comments': total_comments
    }
    report_df = pd.DataFrame(report_data, index=[0])
    
    # Save the report as a CSV file
    report_df.to_csv(f'{user_id}_engagement_report.csv', index=False)

    return f'Engagement report for {user_data.username} has been generated.'
```