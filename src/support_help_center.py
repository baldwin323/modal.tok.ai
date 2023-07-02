```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Support(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100))
    issue = db.Column(db.String(200))
    status = db.Column(db.String(50))

    def __init__(self, user_id, issue, status):
        self.user_id = user_id
        self.issue = issue
        self.status = status

class SupportSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'issue', 'status')

support_schema = SupportSchema()
supports_schema = SupportSchema(many=True)

@app.route('/support', methods=['POST'])
def getSupport():
    user_id = request.json['user_id']
    issue = request.json['issue']
    status = "Open"
    new_support = Support(user_id, issue, status)
    db.session.add(new_support)
    db.session.commit()
    return support_schema.jsonify(new_support)

@app.route('/support', methods=['GET'])
def getIssues():
    all_issues = Support.query.all()
    result = supports_schema.dump(all_issues)
    return jsonify(result)

@app.route('/support/<id>', methods=['PUT'])
def reportIssue(id):
    issue = Support.query.get(id)
    status = request.json['status']
    issue.status = status
    db.session.commit()
    return support_schema.jsonify(issue)

if __name__ == "__main__":
    app.run(debug=True)
```