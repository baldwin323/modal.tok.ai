```python
from flask import Blueprint, render_template
from src.controllers.analytics_insights_controller import AnalyticsInsightsController

analytics_insights_view = Blueprint('analytics_insights_view', __name__)

@analytics_insights_view.route('/analytics-dashboard', methods=['GET'])
def analytics_dashboard():
    controller = AnalyticsInsightsController()
    data = controller.get_dashboard_data()
    return render_template('analytics_dashboard.html', data=data)

@analytics_insights_view.route('/subscriber-insights', methods=['GET'])
def subscriber_insights():
    controller = AnalyticsInsightsController()
    data = controller.get_subscriber_insights()
    return render_template('subscriber_insights.html', data=data)
```