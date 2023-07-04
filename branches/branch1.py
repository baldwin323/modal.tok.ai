```python
from git import Repo

def retrieve_branch_files(branch_name):
    repo = Repo('path_to_your_repo')
    files = []
    
    for commit in repo.iter_commits(branch_name):
        files.extend(commit.stats.files)
    
    return files

def retrieve_erased_files(branch_name):
    repo = Repo('path_to_your_repo')
    erased_files = []
    
    for commit in repo.iter_commits(branch_name):
        for file in commit.stats.files:
            if commit.stats.files[file]['deletions'] > 0:
                erased_files.append(file)
    
    return erased_files

def retrieve_unmerged_files(branch_name):
    repo = Repo('path_to_your_repo')
    unmerged_files = repo.index.unmerged_blobs()
    
    return [file for file in unmerged_files]

branch_name = 'branch1'
file_list = retrieve_branch_files(branch_name)
erased_files = retrieve_erased_files(branch_name)
unmerged_files = retrieve_unmerged_files(branch_name)

all_files = file_list + erased_files + unmerged_files
all_files = list(set(all_files))  # remove duplicates

print(all_files)
```