```python
import unittest
from flask import url_for
from app import app, db

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.app.get(url_for('index'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.app.get(url_for('login'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.app.get(url_for('register'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```