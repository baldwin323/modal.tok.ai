```python
# Importing required modules
import json

# Shared Dependencies
knowledgeBaseList = 'knowledgeBaseList'
knowledgeBaseUpdate = 'knowledgeBaseUpdate'
updateKnowledgeBase = 'updateKnowledgeBase'

class KnowledgeBase:
    def __init__(self):
        self.knowledge_base = []

    def load_knowledge_base(self):
        try:
            with open('knowledge_base.json', 'r') as file:
                self.knowledge_base = json.load(file)
        except FileNotFoundError:
            self.knowledge_base = []

    def save_knowledge_base(self):
        with open('knowledge_base.json', 'w') as file:
            json.dump(self.knowledge_base, file)

    def update_knowledge_base(self, update):
        self.knowledge_base.append(update)
        self.save_knowledge_base()

    def get_knowledge_base(self):
        return self.knowledge_base

# Creating an instance of KnowledgeBase
knowledge_base = KnowledgeBase()

# Loading the existing knowledge base
knowledge_base.load_knowledge_base()

# Function to handle knowledge base updates
def handle_knowledge_base_update(update):
    knowledge_base.update_knowledge_base(update)

# Function to get the knowledge base
def get_knowledge_base():
    return knowledge_base.get_knowledge_base()
```