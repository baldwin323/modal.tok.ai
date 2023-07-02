```python
from flask import g, request
from werkzeug.exceptions import abort
from src.authentication import verify_token
from src.models import User

def authorize_request():
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        abort(401, 'Authorization header is missing')

    parts = auth_header.split()

    if parts[0].lower() != 'bearer':
        abort(401, 'Authorization header must start with Bearer')
    elif len(parts) == 1:
        abort(401, 'Token not found')
    elif len(parts) > 2:
        abort(401, 'Authorization header must be Bearer token')

    token = parts[1]

    g.user = verify_token(token)

def requires_auth(f):
    def wrapper(*args, **kwargs):
        authorize_request()
        return f(*args, **kwargs)
    return wrapper

def requires_role(role):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if g.user.role != role:
                abort(403, 'Insufficient role')
            return f(*args, **kwargs)
        return decorator
```