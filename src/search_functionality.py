```python
import json

# Importing User, Content and Creator Data Schemas
from user_data import UserData
from content_data import ContentData
from creator_data import CreatorData

class SearchFunctionality:
    def __init__(self):
        self.user_data = UserData()
        self.content_data = ContentData()
        self.creator_data = CreatorData()

    def search_content(self, search_query):
        results = []
        for content in self.content_data.contents:
            if search_query.lower() in content['content_name'].lower():
                results.append(content)
        return results

    def search_creators(self, search_query):
        results = []
        for creator in self.creator_data.creators:
            if search_query.lower() in creator['username'].lower():
                results.append(creator)
        return results

    def search(self, search_query, search_type='content'):
        if search_type == 'content':
            return self.search_content(search_query)
        elif search_type == 'creator':
            return self.search_creators(search_query)
        else:
            return "Invalid search type. Please choose 'content' or 'creator'."

if __name__ == "__main__":
    search_functionality = SearchFunctionality()
    print(json.dumps(search_functionality.search('search_query', 'content'), indent=4))
    print(json.dumps(search_functionality.search('search_query', 'creator'), indent=4))
```