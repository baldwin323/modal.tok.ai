import os
from src import functions, helpers

def main():
    readme_path = os.path.join(os.getcwd(), 'README.md')
    readme_content = functions.read_file(readme_path)
    formatted_content = helpers.format_content(readme_content)
    functions.write_file(readme_path, formatted_content)

if __name__ == "__main__":
    main()