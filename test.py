```python
import unittest
from GitPython import Repo
from utils.retrieve_files import retrieve_files
from utils.merge_files import merge_files
from utils.erase_files import erase_files

class TestPromptMD(unittest.TestCase):
    def setUp(self):
        self.repo = Repo('.')
        self.branches = [b for b in self.repo.branches]
        self.file_list = []
        self.test_results = []

    def test_retrieve_files(self):
        for branch in self.branches:
            self.repo.git.checkout(branch)
            self.file_list.extend(retrieve_files())
        self.assertTrue(len(self.file_list) > 0)

    def test_merge_files(self):
        for branch in self.branches:
            self.repo.git.checkout(branch)
            merge_files()
        self.assertTrue(len(self.repo.untracked_files) == 0)

    def test_erase_files(self):
        erase_files()
        self.assertTrue(len(self.repo.untracked_files) == 0)

    def tearDown(self):
        self.repo.git.checkout('master')

if __name__ == '__main__':
    unittest.main()
```