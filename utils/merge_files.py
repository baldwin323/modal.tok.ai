```python
from git import Repo
import os

def merge_files(repo_path, branch_names):
    repo = Repo(repo_path)
    file_list = []

    for branch_name in branch_names:
        try:
            repo.git.checkout(branch_name)
        except:
            print(f"Error: Could not checkout to branch {branch_name}")
            continue

        for root, dirs, files in os.walk(repo_path):
            for file in files:
                if file not in file_list:
                    file_list.append(file)

    return file_list
```