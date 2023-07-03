```python
from flask import Flask, request
from src.controllers.privacy_security_controller import PrivacySecurityController
from src.controllers.analytics_insights_controller import AnalyticsInsightsController
from src.controllers.social_media_controller import SocialMediaController
from src.controllers.notifications_alerts_controller import NotificationsAlertsController
from src.controllers.support_help_center_controller import SupportHelpCenterController
from src.controllers.multi_platform_access_controller import MultiPlatformAccessController
from src.controllers.localization_internationalization_controller import LocalizationInternationalizationController

app = Flask(__name__)

@app.route('/privacy-security', methods=['POST'])
def privacy_security():
    return PrivacySecurityController().handle_request(request)

@app.route('/analytics-insights', methods=['GET'])
def analytics_insights():
    return AnalyticsInsightsController().handle_request(request)

@app.route('/social-media', methods=['POST'])
def social_media():
    return SocialMediaController().handle_request(request)

@app.route('/notifications-alerts', methods=['POST'])
def notifications_alerts():
    return NotificationsAlertsController().handle_request(request)

@app.route('/support-help-center', methods=['GET', 'POST'])
def support_help_center():
    return SupportHelpCenterController().handle_request(request)

@app.route('/multi-platform-access', methods=['GET'])
def multi_platform_access():
    return MultiPlatformAccessController().handle_request(request)

@app.route('/localization-internationalization', methods=['GET', 'POST'])
def localization_internationalization():
    return LocalizationInternationalizationController().handle_request(request)

if __name__ == '__main__':
    app.run(debug=True)
```