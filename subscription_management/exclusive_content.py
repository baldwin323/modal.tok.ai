```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Subscription(db.Model):
    subscription_id = db.Column(db.String(100), primary_key=True)
    creator_id = db.Column(db.String(100), nullable=False)
    exclusive_content = db.Column(db.String(500), nullable=False)

    def __init__(self, subscription_id, creator_id, exclusive_content):
        self.subscription_id = subscription_id
        self.creator_id = creator_id
        self.exclusive_content = exclusive_content

class SubscriptionSchema(ma.Schema):
    subscription_id = fields.String(required=True)
    creator_id = fields.String(required=True)
    exclusive_content = fields.String(required=True)

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

@app.route('/offer_exclusive_content', methods=['POST'])
def offer_exclusive_content():
    subscription_id = request.json['subscription_id']
    creator_id = request.json['creator_id']
    exclusive_content = request.json['exclusive_content']

    new_subscription = Subscription(subscription_id, creator_id, exclusive_content)

    db.session.add(new_subscription)
    db.session.commit()

    return subscription_schema.jsonify(new_subscription)

if __name__ == '__main__':
    app.run(debug=True)
```