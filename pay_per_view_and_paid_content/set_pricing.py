```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskmysql'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Pricing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, unique=True)
    price = db.Column(db.Float)

    def __init__(self, content_id, price):
        self.content_id = content_id
        self.price = price

class PricingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'content_id', 'price')

pricing_schema = PricingSchema()
pricings_schema = PricingSchema(many=True)

@app.route('/set_pricing', methods=['POST'])
def set_pricing():
    content_id = request.json['content_id']
    price = request.json['price']

    new_pricing = Pricing(content_id, price)

    db.session.add(new_pricing)
    db.session.commit()

    return pricing_schema.jsonify(new_pricing)

if __name__ == '__main__':
    app.run(debug=True)
```