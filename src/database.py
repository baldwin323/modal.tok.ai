```python
import pymongo
from pymongo import MongoClient
from src import config

class Database:
    def __init__(self):
        self.client = MongoClient(config.DATABASE_CONNECTION_STRING)
        self.db = self.client[config.DATABASE_NAME]

    def insert(self, collection, data):
        return self.db[collection].insert_one(data)

    def find(self, collection, query):
        return self.db[collection].find(query)

    def update(self, collection, query, new_values):
        return self.db[collection].update_one(query, new_values)

    def delete(self, collection, query):
        return self.db[collection].delete_one(query)
```