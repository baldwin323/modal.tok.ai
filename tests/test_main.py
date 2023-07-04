import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def test_main(self):
        self.assertEqual(main.run(), "Prompt.md - A complete repository that flows. Easy to follow readme directions.")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()