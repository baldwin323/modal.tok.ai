```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from user_registration_and_authentication.authenticate import authenticate_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskcreator'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.String(100), unique=True)
    personal_info = db.Column(db.String(200))
    bio = db.Column(db.String(500))
    profile_picture = db.Column(db.String(200))
    cover_image = db.Column(db.String(200))

    def __init__(self, creator_id, personal_info, bio, profile_picture, cover_image):
        self.creator_id = creator_id
        self.personal_info = personal_info
        self.bio = bio
        self.profile_picture = profile_picture
        self.cover_image = cover_image

class ProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'creator_id', 'personal_info', 'bio', 'profile_picture', 'cover_image')

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)

@app.route('/create_profile', methods=['POST'])
def create_profile():
    auth_token = request.headers.get('Authorization')
    if authenticate_user(auth_token):
        creator_id = request.json['creator_id']
        personal_info = request.json['personal_info']
        bio = request.json['bio']
        profile_picture = request.json['profile_picture']
        cover_image = request.json['cover_image']

        new_profile = Profile(creator_id, personal_info, bio, profile_picture, cover_image)

        db.session.add(new_profile)
        db.session.commit()

        return profile_schema.jsonify(new_profile)
    else:
        return jsonify({'message': 'Invalid token'})

if __name__ == '__main__':
    app.run(debug=True)
```