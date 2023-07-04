import unittest
from flask import Flask
from app import forms

class TestForms(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()

    def test_login_form(self):
        form = forms.LoginForm(email='test@test.com', password='password')
        self.assertTrue(form.validate())

    def test_register_form(self):
        form = forms.RegisterForm(email='test@test.com', password='password', confirm='password')
        self.assertTrue(form.validate())

if __name__ == "__main__":
    unittest.main()