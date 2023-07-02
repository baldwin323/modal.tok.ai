```python
import os
from content_data_schema import ContentData

def manageContent(user_id, file_path, content_type):
    content_data = ContentData(user_id, file_path, content_type)
    uploadContent(content_data)

def uploadContent(content_data):
    try:
        with open(content_data.file_path, 'rb') as file:
            file_content = file.read()
            # Here you would typically call your cloud storage API to upload the file
            # For example, if you were using AWS S3, you would do:
            # s3_client.upload_fileobj(file, 'your-bucket', content_data.file_path)
            print(f"Successfully uploaded {content_data.file_path}")
    except FileNotFoundError:
        print(f"File {content_data.file_path} does not exist")
    except Exception as e:
        print(f"An error occurred while uploading {content_data.file_path}: {str(e)}")

if __name__ == "__main__":
    user_id = input("Enter user id: ")
    file_path = input("Enter file path: ")
    content_type = input("Enter content type: ")
    manageContent(user_id, file_path, content_type)
```