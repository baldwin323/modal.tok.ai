```python
from git import Repo

branch_name = "branch3"

def retrieve_files(repo_path="."):
    repo = Repo(repo_path)
    files = []
    for commit in repo.iter_commits(branch_name):
        files.extend(commit.stats.files.keys())
    return list(set(files))

def get_unmerged_files(repo_path="."):
    repo = Repo(repo_path)
    unmerged_blobs = repo.index.unmerged_blobs()
    unmerged_files = [u[0] for u in unmerged_blobs]
    return unmerged_files

def get_erased_files(repo_path="."):
    repo = Repo(repo_path)
    erased_files = []
    for commit in repo.iter_commits(branch_name):
        for diff in commit.diff(commit.parents):
            if diff.deleted_file:
                erased_files.append(diff.a_path)
    return list(set(erased_files))

def get_all_files():
    repo_path = "."
    all_files = retrieve_files(repo_path)
    all_files.extend(get_unmerged_files(repo_path))
    all_files.extend(get_erased_files(repo_path))
    return list(set(all_files))

if __name__ == "__main__":
    print(get_all_files())
```