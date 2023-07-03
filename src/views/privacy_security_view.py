```python
from flask import Blueprint, render_template, request
from src.controllers.privacy_security_controller import PrivacySecurityController

privacy_security_view = Blueprint('privacy_security_view', __name__)

@privacy_security_view.route('/privacy-settings', methods=['GET', 'POST'])
def privacy_settings():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        private_content = request.form.get('private_content')
        restricted_access = request.form.get('restricted_access')
        PrivacySecurityController.setPrivacy(user_id, private_content, restricted_access)
    return render_template('privacy_settings.html')

@privacy_security_view.route('/security-controls', methods=['GET', 'POST'])
def security_controls():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        report_abuse = request.form.get('report_abuse')
        PrivacySecurityController.setSecurity(user_id, report_abuse)
    return render_template('security_controls.html')
```