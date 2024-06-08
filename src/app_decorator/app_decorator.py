# app_decorator.py

import jwt
from flask import request, jsonify
from functools import wraps
from src.config import SECRET_KEY

def app_decorator(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1] if len(auth_header.split(" ")) > 1 else None

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY['secret_key'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        return f(*args, **kwargs)

    return decorated
