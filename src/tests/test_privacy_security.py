import unittest
from src.controllers.privacy_security_controller import PrivacySecurityController
from src.models.user import User
from src.models.content import Content

class TestPrivacySecurity(unittest.TestCase):

    def setUp(self):
        self.controller = PrivacySecurityController()
        self.user = User(user_id="test_user")
        self.content = Content(content_id="test_content")

    def test_set_content_as_private(self):
        self.controller.setPrivacy(self.user, self.content, True)
        self.assertTrue(self.content.is_private)

    def test_restrict_access_to_specific_subscribers(self):
        self.controller.setSecurity(self.user, self.content, ["subscriber1", "subscriber2"])
        self.assertEqual(self.content.access_list, ["subscriber1", "subscriber2"])

    def test_report_abusive_behavior(self):
        report = self.controller.reportAbuse(self.user, "Abusive behavior")
        self.assertEqual(report, "Abusive behavior reported successfully.")

    def test_report_inappropriate_behavior(self):
        report = self.controller.reportAbuse(self.user, "Inappropriate behavior")
        self.assertEqual(report, "Inappropriate behavior reported successfully.")

if __name__ == '__main__':
    unittest.main()