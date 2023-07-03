```python
from flask import Blueprint, render_template
from src.controllers.social_media_controller import SocialMediaController

social_media_blueprint = Blueprint('social_media', __name__, template_folder='templates')

@social_media_blueprint.route('/social-media-integration', methods=['GET', 'POST'])
def social_media_integration():
    social_media_controller = SocialMediaController()
    if request.method == 'POST':
        platform = request.form.get('platform')
        content_id = request.form.get('content_id')
        social_media_controller.integrateSocialMedia(platform, content_id)
        social_media_controller.postContent(platform, content_id)
        return redirect(url_for('social_media.social_media_integration'))
    else:
        return render_template('social_media_integration.html')

@social_media_blueprint.route('/cross-platform-posting', methods=['GET', 'POST'])
def cross_platform_posting():
    social_media_controller = SocialMediaController()
    if request.method == 'POST':
        platforms = request.form.getlist('platforms')
        content_id = request.form.get('content_id')
        for platform in platforms:
            social_media_controller.postContent(platform, content_id)
        return redirect(url_for('social_media.cross_platform_posting'))
    else:
        return render_template('cross_platform_posting.html')
```