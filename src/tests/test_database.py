import unittest
from src import database, models, config

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = database.Database(config.DATABASE_URI)
        self.sample_user = models.User("test_user", "test_password")

    def test_connection(self):
        self.assertIsNotNone(self.db.connection)

    def test_insert(self):
        result = self.db.insert_user(self.sample_user)
        self.assertTrue(result)

    def test_retrieve(self):
        self.db.insert_user(self.sample_user)
        user = self.db.get_user("test_user")
        self.assertEqual(user.username, "test_user")

    def test_update(self):
        self.db.insert_user(self.sample_user)
        self.db.update_user("test_user", "new_password")
        user = self.db.get_user("test_user")
        self.assertEqual(user.password, "new_password")

    def test_delete(self):
        self.db.insert_user(self.sample_user)
        self.db.delete_user("test_user")
        user = self.db.get_user("test_user")
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()