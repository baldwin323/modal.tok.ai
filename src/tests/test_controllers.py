import unittest
from src import controllers

class TestControllers(unittest.TestCase):

    def setUp(self):
        self.controller = controllers.Controller()

    def test_registerUser(self):
        result = self.controller.registerUser("testUser", "testPassword")
        self.assertEqual(result, "userRegistered")

    def test_loginUser(self):
        result = self.controller.loginUser("testUser", "testPassword")
        self.assertEqual(result, "userLoggedIn")

    def test_fetchData(self):
        result = self.controller.fetchData("testUser")
        self.assertEqual(result, "dataFetched")

    def test_processPayment(self):
        result = self.controller.processPayment("testUser", 100)
        self.assertEqual(result, "paymentSuccessful")

    def test_encryptData(self):
        result = self.controller.encryptData("testData")
        self.assertNotEqual(result, "testData")

    def test_decryptData(self):
        encrypted_data = self.controller.encryptData("testData")
        result = self.controller.decryptData(encrypted_data)
        self.assertEqual(result, "testData")

if __name__ == '__main__':
    unittest.main()