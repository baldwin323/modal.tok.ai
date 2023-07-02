```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskmysql'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, nullable=False)
    content_type = db.Column(db.String(70), nullable=False)
    content_data = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, creator_id, content_type, content_data):
        self.creator_id = creator_id
        self.content_type = content_type
        self.content_data = content_data

class ContentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'creator_id', 'content_type', 'content_data')

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)

@app.route('/content', methods=['PUT'])
def update_content():
    id = request.json['id']
    content_type = request.json['content_type']
    content_data = request.json['content_data']

    content = Content.query.get(id)
    content.content_type = content_type
    content.content_data = content_data

    db.session.commit()
    return content_schema.jsonify(content)

@app.route('/content', methods=['DELETE'])
def delete_content():
    id = request.json['id']
    content = Content.query.get(id)
    db.session.delete(content)
    db.session.commit()

    return content_schema.jsonify(content)

if __name__ == "__main__":
    app.run(debug=True)
```