```python
from git import Repo
import os

def retrieve_files(branch_name):
    repo = Repo(os.getcwd())
    file_list = []

    for commit in repo.iter_commits(branch_name):
        for file in commit.stats.files:
            file_list.append(file)

    erased_files = [file for file in file_list if file not in os.listdir()]
    unmerged_files = repo.index.unmerged_blobs()

    for path, conflicts in unmerged_files.items():
        for (stage, blob) in conflicts:
            if stage == 2:
                file_list.append(path)

    return erased_files + list(set(file_list))
```