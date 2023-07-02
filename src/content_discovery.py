```python
import json

# User Data Schema
user_data = {
    "user_id": "",
    "username": "",
    "subscription_status": "",
    "payment_info": ""
}

# Content Data Schema
content_data = {
    "content_id": "",
    "creator_id": "",
    "content_type": "",
    "price": "",
    "popularity_metrics": ""
}

def discoverContent(user_interests, category, popularity):
    # Load content data
    with open('content_data.json') as json_file:
        data = json.load(json_file)

    # Filter content based on user interests, category, and popularity
    filtered_content = [content for content in data if content['content_type'] in user_interests and content['category'] == category and content['popularity_metrics'] >= popularity]

    return filtered_content

def searchContent(search_query):
    # Load content data
    with open('content_data.json') as json_file:
        data = json.load(json_file)

    # Search for content based on search query
    searched_content = [content for content in data if search_query in content['content_type'] or search_query in content['creator_id']]

    return searched_content
```