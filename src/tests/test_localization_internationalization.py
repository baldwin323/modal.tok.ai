import unittest
from src.controllers.localization_internationalization_controller import LocalizationInternationalizationController

class TestLocalizationInternationalization(unittest.TestCase):

    def setUp(self):
        self.controller = LocalizationInternationalizationController()

    def test_localize_content(self):
        result = self.controller.localize_content('content_id', 'language')
        self.assertTrue(result)

    def test_internationalize_app(self):
        result = self.controller.internationalize_app('language')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()