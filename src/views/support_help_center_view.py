```python
from flask import Blueprint, render_template, request
from controllers.support_help_center_controller import SupportHelpCenterController

support_help_center_view = Blueprint('support_help_center_view', __name__)

@support_help_center_view.route('/support', methods=['GET'])
def support():
    return render_template('support.html')

@support_help_center_view.route('/help-center', methods=['GET'])
def help_center():
    return render_template('help_center.html')

@support_help_center_view.route('/report-issue', methods=['POST'])
def report_issue():
    issue_details = request.form
    SupportHelpCenterController().report_issue(issue_details)
    return {"message": "Issue reported successfully"}

@support_help_center_view.route('/contact-support', methods=['POST'])
def contact_support():
    support_details = request.form
    SupportHelpCenterController().contact_support(support_details)
    return {"message": "Support contacted successfully"}
```