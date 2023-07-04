```python
from git import Repo
import os

def retrieve_erased_unmerged_files(repo_path):
    repo = Repo(repo_path)
    erased_files = []
    unmerged_files = []

    for commit in repo.iter_commits('HEAD'):
        for parent in commit.parents:
            diff_index = commit.diff(parent)
            for diff_item in diff_index.iter_change_type('D'):
                erased_files.append(diff_item.a_path)
            for diff_item in diff_index.iter_change_type('U'):
                unmerged_files.append(diff_item.a_path)

    return erased_files, unmerged_files

def main():
    repo_path = os.getcwd()
    erased_files, unmerged_files = retrieve_erased_unmerged_files(repo_path)
    all_files = erased_files + unmerged_files
    print(all_files)

if __name__ == "__main__":
    main()
```