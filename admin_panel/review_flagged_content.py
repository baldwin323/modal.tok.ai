```python
from content_management_system.content_data_schema import ContentDataSchema

class ReviewFlaggedContent:
    def __init__(self):
        self.content_data_schema = ContentDataSchema()

    def get_flagged_content(self):
        flagged_content = self.content_data_schema.get_flagged_content()
        return flagged_content

    def review_content(self, content_id):
        content = self.content_data_schema.get_content_by_id(content_id)
        if content['flagged']:
            print(f"Reviewing content: {content['content_id']}")
            # Add review process here
            # After review, update the content status
            self.content_data_schema.update_content_status(content_id, 'reviewed')
            print(f"Content: {content['content_id']} has been reviewed.")
        else:
            print("Content is not flagged.")

    def remove_content(self, content_id):
        self.content_data_schema.remove_content(content_id)
        print(f"Content: {content_id} has been removed.")
```