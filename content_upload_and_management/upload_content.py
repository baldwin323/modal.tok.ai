```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['UPLOAD_FOLDER'] = './uploads'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Content(db.Model):
    content_id = db.Column(db.String(100), primary_key=True)
    creator_id = db.Column(db.String(100), nullable=False)
    content_type = db.Column(db.String(100), nullable=False)
    content_file = db.Column(db.String(200), nullable=False)

    def __init__(self, content_id, creator_id, content_type, content_file):
        self.content_id = content_id
        self.creator_id = creator_id
        self.content_type = content_type
        self.content_file = content_file

class ContentSchema(ma.Schema):
    class Meta:
        fields = ('content_id', 'creator_id', 'content_type', 'content_file')

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)

@app.route('/upload_content', methods=['POST'])
def upload_content():
    creator_id = request.form['creator_id']
    content_type = request.form['content_type']
    content_file = request.files['content_file']

    filename = secure_filename(content_file.filename)
    content_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    new_content = Content(content_id, creator_id, content_type, filename)
    db.session.add(new_content)
    db.session.commit()

    return content_schema.jsonify(new_content)

if __name__ == '__main__':
    app.run(debug=True)
```