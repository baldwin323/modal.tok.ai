```python
import unittest
from src import authentication, models, database, config

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.db = database.Database(config)
        self.auth = authentication.Authentication(self.db, config)
        self.user_model = models.User()

    def test_register_user(self):
        user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com'
        }
        result = self.auth.register_user(user_data)
        self.assertEqual(result['status'], 'success')

    def test_login_user(self):
        user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        result = self.auth.login_user(user_data)
        self.assertEqual(result['status'], 'success')

    def test_social_media_login(self):
        social_data = {
            'provider': 'twitter',
            'access_token': 'testaccesstoken'
        }
        result = self.auth.social_media_login(social_data)
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
```