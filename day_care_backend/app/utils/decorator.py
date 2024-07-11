#!/usr/bin/python3

from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify

def role_required(allowed_roles):
    """
    Decorator that checks if the current user has the required role(s) to access a route.
    Args:
        allowed_roles (list): List of roles that are allowed to access the route.
    Returns:
        function: Decorator function that wraps the original function.
    """
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def decorator_function(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role'] not in allowed_roles:
                return jsonify({"message": "Permission denied"}), 403
            return f(*args, **kwargs)
        return decorator_function
    return decorator
