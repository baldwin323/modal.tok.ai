import unittest
from src.controllers.multi_platform_access_controller import MultiPlatformAccessController

class TestMultiPlatformAccess(unittest.TestCase):

    def setUp(self):
        self.controller = MultiPlatformAccessController()
        self.user_id = "test_user"
        self.platforms = ["web", "iOS", "Android"]

    def test_access_platform(self):
        for platform in self.platforms:
            response = self.controller.accessPlatform(self.user_id, platform)
            self.assertEqual(response['status'], 'success')

    def test_platform_availability(self):
        for platform in self.platforms:
            response = self.controller.checkPlatformAvailability(platform)
            self.assertTrue(response['available'])

if __name__ == '__main__':
    unittest.main()