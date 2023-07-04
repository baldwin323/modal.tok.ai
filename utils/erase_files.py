```python
import os
from git import Repo

def erase_files(file_list):
    repo = Repo('.')

    for file in file_list:
        if file in repo.untracked_files:
            os.remove(file)
        else:
            repo.git.rm(file, cached=True)
```