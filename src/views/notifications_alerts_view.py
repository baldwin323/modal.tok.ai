```python
from flask import Blueprint, render_template, request
from src.controllers.notifications_alerts_controller import NotificationsAlertsController

notifications_alerts_view = Blueprint('notifications_alerts_view', __name__)

@notifications_alerts_view.route('/notifications', methods=['GET', 'POST'])
def notifications():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        new_subscriber = request.form.get('new_subscriber')
        new_message = request.form.get('new_message')
        content_update = request.form.get('content_update')
        NotificationsAlertsController.sendNotification(user_id, new_subscriber, new_message, content_update)
    return render_template('notifications.html')

@notifications_alerts_view.route('/alerts', methods=['GET', 'POST'])
def alerts():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        customize_alerts = request.form.get('customize_alerts')
        NotificationsAlertsController.customizeAlerts(user_id, customize_alerts)
    return render_template('alerts.html')
```