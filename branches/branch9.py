```python
from GitPython import Repo

def retrieve_branch_files(branch_name):
    repo = Repo('./')
    branch = repo.branches[branch_name]
    files = []
    for commit in branch.iter_commits():
        files.extend(commit.stats.files.keys())
    return files

def retrieve_erased_files(branch_name):
    repo = Repo('./')
    branch = repo.branches[branch_name]
    erased_files = []
    for commit in branch.iter_commits():
        for file in commit.stats.files.keys():
            if commit.stats.files[file]['deletions'] > 0:
                erased_files.append(file)
    return erased_files

def retrieve_unmerged_files(branch_name):
    repo = Repo('./')
    branch = repo.branches[branch_name]
    unmerged_files = []
    for commit in branch.iter_commits():
        for file in commit.stats.files.keys():
            if commit.stats.files[file]['lines'] > commit.stats.files[file]['insertions']:
                unmerged_files.append(file)
    return unmerged_files

branch_name = 'branch9'
file_list = retrieve_branch_files(branch_name)
erased_files = retrieve_erased_files(branch_name)
unmerged_files = retrieve_unmerged_files(branch_name)

all_files = set(file_list + erased_files + unmerged_files)
print(all_files)
```