import unittest
from src import models

class TestModels(unittest.TestCase):

    def setUp(self):
        self.user = models.User()

    def test_user_model(self):
        self.assertIsNotNone(self.user)

    def test_user_fields(self):
        self.user.username = "testuser"
        self.user.password = "testpassword"
        self.user.email = "testuser@example.com"

        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.password, "testpassword")
        self.assertEqual(self.user.email, "testuser@example.com")

    def test_message_model(self):
        message = models.Message()
        message.user_id = self.user.id
        message.content = "Hello, world!"

        self.assertEqual(message.user_id, self.user.id)
        self.assertEqual(message.content, "Hello, world!")

if __name__ == "__main__":
    unittest.main()