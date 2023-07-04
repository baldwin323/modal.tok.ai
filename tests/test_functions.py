import unittest
from src import functions

class TestFunctions(unittest.TestCase):

    def test_sample_function(self):
        result = functions.sample_function()
        self.assertEqual(result, 'Expected Result')

if __name__ == '__main__':
    unittest.main()