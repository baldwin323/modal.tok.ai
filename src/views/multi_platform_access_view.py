```python
from flask import Blueprint, render_template
from src.controllers.multi_platform_access_controller import MultiPlatformAccessController

multi_platform_access_view = Blueprint('multi_platform_access_view', __name__)

@multi_platform_access_view.route('/platforms', methods=['GET'])
def get_platforms():
    controller = MultiPlatformAccessController()
    platforms = controller.get_platforms()
    return render_template('platforms.html', platforms=platforms)

@multi_platform_access_view.route('/platforms/<platform_id>', methods=['GET'])
def get_platform(platform_id):
    controller = MultiPlatformAccessController()
    platform = controller.get_platform(platform_id)
    return render_template('platform.html', platform=platform)
```