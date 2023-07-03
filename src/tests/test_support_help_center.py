import unittest
from src.controllers.support_help_center_controller import SupportHelpCenterController

class TestSupportHelpCenter(unittest.TestCase):

    def setUp(self):
        self.controller = SupportHelpCenterController()

    def test_provide_support(self):
        response = self.controller.provide_support('FAQs')
        self.assertEqual(response, 'FAQs support provided')

    def test_report_issue(self):
        issue = 'App crashes on startup'
        response = self.controller.report_issue(issue)
        self.assertEqual(response, 'Issue reported: App crashes on startup')

    def test_contact_support(self):
        response = self.controller.contact_support('Need help with account recovery')
        self.assertEqual(response, 'Support contacted: Need help with account recovery')

if __name__ == '__main__':
    unittest.main()