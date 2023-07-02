import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = main.create_app()

    def test_app_creation(self):
        self.assertIsNotNone(self.app)

    def test_home_route(self):
        tester = self.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_api_route(self):
        tester = self.app.test_client(self)
        response = tester.get('/api', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()