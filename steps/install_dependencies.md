# Install Dependencies

In this step, we will install the necessary dependencies for our app. These dependencies include libraries and frameworks that are essential for cross-platform compatibility.

## Windows

On your Windows machine, open the command prompt and navigate to your project directory. Activate your virtual environment and use pip to install the dependencies:

```bash
cd your_project_directory
.\venv\Scripts\activate
pip install -r requirements.txt
```

## macOS

On your macOS machine, open the terminal and navigate to your project directory. Activate your virtual environment and use pip to install the dependencies:

```bash
cd your_project_directory
source venv/bin/activate
pip install -r requirements.txt
```

## Android

For Android, the dependencies will be handled by Gradle, which is integrated into Android Studio. Open your project in Android Studio, and it will automatically detect and install the necessary dependencies.

Remember to replace `your_project_directory` with the actual path to your project directory, and `requirements.txt` should be a file in your project directory listing all the necessary Python dependencies.

In the next step, we will build and run the app on each platform.