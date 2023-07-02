```python
import unittest
from src import views, models, authentication, authorization

class TestViews(unittest.TestCase):

    def setUp(self):
        self.view = views.View()
        self.model = models.Model()
        self.auth = authentication.Authentication()
        self.authz = authorization.Authorization()

    def test_login_view(self):
        response = self.view.login_view()
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.view.register_view()
        self.assertEqual(response.status_code, 200)

    def test_user_profile_view(self):
        response = self.view.user_profile_view()
        self.assertEqual(response.status_code, 200)

    def test_payment_form_view(self):
        response = self.view.payment_form_view()
        self.assertEqual(response.status_code, 200)

    def test_social_login_view(self):
        response = self.view.social_login_view()
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```