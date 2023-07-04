```python
from git import Repo

def retrieve_branch_files(branch_name):
    repo = Repo('.')

    # Get the specific branch
    branch = repo.branches[branch_name]

    # Checkout to the specific branch
    repo.git.checkout(branch)

    # Get all files in the branch
    file_list = [item.a_path for item in repo.index.diff(None)]
    
    return file_list

branch_name = "branch5"
file_list = retrieve_branch_files(branch_name)

print(f"All files in {branch_name}: {file_list}")
```