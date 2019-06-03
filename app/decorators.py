from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

"""
Define two decorators using the functools library built into Python.
If the user does not have the specified permission, the 403 error code is returned, and access is prohibited.
"""

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.operation(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)