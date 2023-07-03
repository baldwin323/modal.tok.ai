import unittest
from src.controllers.notifications_alerts_controller import NotificationsAlertsController

class TestNotificationsAlerts(unittest.TestCase):

    def setUp(self):
        self.controller = NotificationsAlertsController()
        self.user_id = 1
        self.subscriber_id = 2
        self.content_id = 3

    def test_send_notification(self):
        result = self.controller.send_notification(self.user_id, "new-subscriber", self.subscriber_id)
        self.assertTrue(result)

    def test_customize_alerts(self):
        result = self.controller.customize_alerts(self.user_id, "new-message", False)
        self.assertTrue(result)

    def test_content_update_alert(self):
        result = self.controller.send_notification(self.user_id, "content-update", self.content_id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()