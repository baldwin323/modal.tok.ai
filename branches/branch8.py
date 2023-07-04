```python
from git import Repo
import os

# Define the repository
repo = Repo(os.getcwd())

# Define the branch name
branch_name = "branch8"

# Check out to the branch
repo.git.checkout(branch_name)

# Get the list of all files in the branch
file_list = [item.a_path for item in repo.index.diff(None)]

# Retrieve erased files
erased_files = [item.a_path for item in repo.index.diff("HEAD") if item.deleted_file]

# Retrieve unmerged files
unmerged_files = repo.index.unmerged_blobs()

# Add erased and unmerged files to the file list
file_list.extend(erased_files)
for unmerged_file in unmerged_files.keys():
    file_list.append(unmerged_file)

# Remove duplicates from the file list
file_list = list(set(file_list))

# Print the file list
for file in file_list:
    print(file)
```