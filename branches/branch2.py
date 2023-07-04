```python
from git import Repo

def retrieve_branch_files(branch_name):
    repo = Repo('path_to_your_repo')
    files = []
    for commit in repo.iter_commits(branch_name):
        files.extend(commit.stats.files)
    return files

def get_erased_files(branch_name):
    repo = Repo('path_to_your_repo')
    erased_files = []
    for commit in repo.iter_commits(branch_name):
        for file in commit.stats.files:
            if commit.stats.files[file]['deletions'] > 0:
                erased_files.append(file)
    return erased_files

def get_unmerged_files(branch_name):
    repo = Repo('path_to_your_repo')
    unmerged_files = repo.index.unmerged_blobs()
    return [file for file in unmerged_files if file not in repo.head.commit.tree]

branch_name = 'branch2'
all_files = retrieve_branch_files(branch_name)
erased_files = get_erased_files(branch_name)
unmerged_files = get_unmerged_files(branch_name)

all_possible_files = list(set(all_files + erased_files + unmerged_files))
```