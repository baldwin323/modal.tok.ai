import unittest
from src.controllers.analytics_insights_controller import AnalyticsInsightsController

class TestAnalyticsInsights(unittest.TestCase):

    def setUp(self):
        self.controller = AnalyticsInsightsController()

    def test_track_growth(self):
        result = self.controller.track_growth(user_id=1)
        self.assertIsNotNone(result)

    def test_get_insights(self):
        result = self.controller.get_insights(user_id=1)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()