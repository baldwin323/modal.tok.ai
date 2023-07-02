```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Subscription(db.Model):
    subscription_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, nullable=False)
    tier = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(50), nullable=False)

class SubscriptionSchema(Schema):
    subscription_id = fields.Int()
    creator_id = fields.Int()
    tier = fields.Str()
    price = fields.Float()
    duration = fields.Str()

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

@app.route('/subscription', methods=['POST'])
def setup_subscription():
    creator_id = request.json['creator_id']
    tier = request.json['tier']
    price = request.json['price']
    duration = request.json['duration']

    new_subscription = Subscription(creator_id=creator_id, tier=tier, price=price, duration=duration)

    db.session.add(new_subscription)
    db.session.commit()

    return subscription_schema.jsonify(new_subscription)

if __name__ == '__main__':
    app.run(debug=True)
```