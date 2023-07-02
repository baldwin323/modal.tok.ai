import unittest
from src import authorization

class TestAuthorization(unittest.TestCase):

    def setUp(self):
        self.authorization = authorization.Authorization()

    def test_user_authorization(self):
        self.assertTrue(self.authorization.authorize_user('test_user', 'test_password'))

    def test_invalid_user_authorization(self):
        self.assertFalse(self.authorization.authorize_user('invalid_user', 'invalid_password'))

    def test_admin_authorization(self):
        self.assertTrue(self.authorization.authorize_admin('admin_user', 'admin_password'))

    def test_invalid_admin_authorization(self):
        self.assertFalse(self.authorization.authorize_admin('invalid_admin', 'invalid_password'))

if __name__ == '__main__':
    unittest.main()