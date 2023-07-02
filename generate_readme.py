```python
from git import Repo
import os

REPO_PATH = "<path_to_your_repo>"
README_PATH = os.path.join(REPO_PATH, "README.md")

def generate_readme(repo_path, readme_path):
    repo = Repo(repo_path)
    commit_history = repo.git.log('--oneline')

    with open(readme_path, 'w') as readme:
        readme.write("# Commit History\n")
        for commit in commit_history.split('\n'):
            readme.write("- " + commit + "\n")

if __name__ == "__main__":
    generate_readme(REPO_PATH, README_PATH)
```