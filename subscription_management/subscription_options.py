```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/subscription_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, nullable=False)
    tier = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(20), nullable=False)

    def __init__(self, creator_id, tier, price, duration):
        self.creator_id = creator_id
        self.tier = tier
        self.price = price
        self.duration = duration

class SubscriptionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'creator_id', 'tier', 'price', 'duration')

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

@app.route('/subscription', methods=['POST'])
def add_subscription():
    creator_id = request.json['creator_id']
    tier = request.json['tier']
    price = request.json['price']
    duration = request.json['duration']

    new_subscription = Subscription(creator_id, tier, price, duration)

    db.session.add(new_subscription)
    db.session.commit()

    return subscription_schema.jsonify(new_subscription)

@app.route('/subscription', methods=['GET'])
def get_subscriptions():
    all_subscriptions = Subscription.query.all()
    result = subscriptions_schema.dump(all_subscriptions)
    return jsonify(result)

@app.route('/subscription/<id>', methods=['GET'])
def get_subscription(id):
    subscription = Subscription.query.get(id)
    return subscription_schema.jsonify(subscription)

@app.route('/subscription/<id>', methods=['PUT'])
def update_subscription(id):
    subscription = Subscription.query.get(id)

    creator_id = request.json['creator_id']
    tier = request.json['tier']
    price = request.json['price']
    duration = request.json['duration']

    subscription.creator_id = creator_id
    subscription.tier = tier
    subscription.price = price
    subscription.duration = duration

    db.session.commit()

    return subscription_schema.jsonify(subscription)

@app.route('/subscription/<id>', methods=['DELETE'])
def delete_subscription(id):
    subscription = Subscription.query.get(id)
    db.session.delete(subscription)
    db.session.commit()

    return subscription_schema.jsonify(subscription)

if __name__ == '__main__':
    app.run(debug=True)
```