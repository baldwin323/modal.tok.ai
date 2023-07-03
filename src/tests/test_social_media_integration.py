import unittest
from src.controllers.social_media_controller import SocialMediaController

class TestSocialMediaIntegration(unittest.TestCase):

    def setUp(self):
        self.controller = SocialMediaController()

    def test_integrateSocialMedia(self):
        result = self.controller.integrateSocialMedia()
        self.assertTrue(result, "Failed to integrate with social media platforms")

    def test_postContent(self):
        content_id = "test_content"
        result = self.controller.postContent(content_id)
        self.assertTrue(result, "Failed to post content to social media platforms")

if __name__ == '__main__':
    unittest.main()