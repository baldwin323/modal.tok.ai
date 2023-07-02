import unittest
from src import api_integration, config, models

class TestAPIIntegration(unittest.TestCase):

    def setUp(self):
        self.config = config.load_config()
        self.api = api_integration.APIIntegration(self.config)

    def test_fetch_data_from_api(self):
        data = self.api.fetch_data()
        self.assertIsNotNone(data)

    def test_process_api_data(self):
        data = self.api.fetch_data()
        processed_data = self.api.process_data(data)
        self.assertIsNotNone(processed_data)

    def test_store_api_data(self):
        data = self.api.fetch_data()
        processed_data = self.api.process_data(data)
        result = models.store_data(processed_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()