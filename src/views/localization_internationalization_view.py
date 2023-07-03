```python
from flask import render_template, request
from src.controllers.localization_internationalization_controller import LocalizationInternationalizationController

class LocalizationInternationalizationView:
    def __init__(self):
        self.controller = LocalizationInternationalizationController()

    def set_language(self):
        user_id = request.args.get('user_id')
        language = request.args.get('language')
        result = self.controller.set_language(user_id, language)
        return render_template('set_language.html', result=result)

    def set_region(self):
        user_id = request.args.get('user_id')
        region = request.args.get('region')
        result = self.controller.set_region(user_id, region)
        return render_template('set_region.html', result=result)

    def get_supported_languages(self):
        languages = self.controller.get_supported_languages()
        return render_template('supported_languages.html', languages=languages)

    def get_supported_regions(self):
        regions = self.controller.get_supported_regions()
        return render_template('supported_regions.html', regions=regions)
```