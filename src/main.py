```python
from flask import Flask
from src import config, views, controllers, database, authentication, authorization, api_integration

app = Flask(__name__)

# Load configuration
app.config.from_object(config)

# Initialize database
database.init_app(app)

# Initialize authentication
authentication.init_app(app)

# Initialize authorization
authorization.init_app(app)

# Initialize API integration
api_integration.init_app(app)

# Register views
app.register_blueprint(views.bp)

# Register controllers
app.register_blueprint(controllers.bp)

if __name__ == "__main__":
    app.run(debug=True)
```