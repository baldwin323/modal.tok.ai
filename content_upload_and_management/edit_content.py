```python
from flask import request, jsonify
from flask_restful import Resource
from models import db, Content, ContentSchema

content_schema = ContentSchema()

class EditContent(Resource):
    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = content_schema.load(json_data)
        if errors:
            return errors, 422
        content_id = data['content_id']
        content = Content.query.filter_by(id=content_id).first()
        if not content:
            return {'message': 'Content does not exist'}, 400
        content.title = data['title']
        content.description = data['description']
        content.category = data['category']
        content.file_path = data['file_path']
        db.session.commit()

        result = content_schema.dump(content).data

        return {"status": 'success', 'data': result}, 201
```