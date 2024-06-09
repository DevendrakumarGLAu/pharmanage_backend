# app_decorator.py

import jwt
from flask import request, jsonify
from functools import wraps

from src.DB_connect.dbconnection import Dbconnect
from src.config import SECRET_KEY

def fetch_roles_permissions():
    db_connection = Dbconnect()
    connection = db_connection.dbconnects()
    if connection:
        sql_query = f"""SELECT * FROM roles_permissions"""
        cursor = connection.cursor()
        cursor.execute(sql_query)
        roles_permissions = {}
        for row in cursor.fetchall():
            role = row['role']
            permissions = [row[column] for column in row if column != 'role']
            roles_permissions[role] = permissions
        return roles_permissions

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
            # current_user = data['email']
            # current_role = data['role']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        # roles_permissions = fetch_roles_permissions()
        # if current_role not in roles_permissions or f.__name__ not in roles_permissions[current_role]:
        #     return jsonify({'message': 'Unauthorized access!'}), 403

        return f(*args, **kwargs)

    return decorated
