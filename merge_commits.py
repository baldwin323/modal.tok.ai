from git import Repo
import os

# Shared variables
REPO_PATH = '/path/to/your/repo'
README_PATH = os.path.join(REPO_PATH, 'README.md')

# Initialize repository
repo = Repo(REPO_PATH)

def merge_all_commits():
    # Get all branches
    branches = repo.branches

    # Merge all branches into master
    for branch in branches:
        if branch != 'master':
            repo.git.checkout('master')
            repo.git.merge(branch)

    # Get commit history
    commit_history = repo.git.log('--oneline')

    return commit_history

def generate_readme(commit_history):
    # Open README file
    with open(README_PATH, 'w') as f:
        f.write("# Commit History\n")
        f.write(commit_history)

# Merge all commits and generate README
commit_history = merge_all_commits()
generate_readme(commit_history)