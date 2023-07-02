```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskmysql'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.String(100))
    personal_info = db.Column(db.String(200))
    bio = db.Column(db.String(500))
    profile_picture = db.Column(db.String(200))
    cover_image = db.Column(db.String(200))
    branding_style = db.Column(db.String(200))

    def __init__(self, creator_id, personal_info, bio, profile_picture, cover_image, branding_style):
        self.creator_id = creator_id
        self.personal_info = personal_info
        self.bio = bio
        self.profile_picture = profile_picture
        self.cover_image = cover_image
        self.branding_style = branding_style

class ProfileSchema(ma.Schema):
    class Meta:
        fields = ('creator_id', 'personal_info', 'bio', 'profile_picture', 'cover_image', 'branding_style')

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)

@app.route('/customize_profile', methods=['PUT'])
def customize_profile():
    creator_id = request.json['creator_id']
    personal_info = request.json['personal_info']
    bio = request.json['bio']
    profile_picture = request.json['profile_picture']
    cover_image = request.json['cover_image']
    branding_style = request.json['branding_style']

    profile = Profile.query.get(creator_id)
    profile.personal_info = personal_info
    profile.bio = bio
    profile.profile_picture = profile_picture
    profile.cover_image = cover_image
    profile.branding_style = branding_style

    db.session.commit()

    return profile_schema.jsonify(profile)

if __name__ == "__main__":
    app.run(debug=True)
```