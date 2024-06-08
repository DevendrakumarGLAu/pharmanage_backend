import jwt
import datetime
from src.config import SECRET_KEY

def generate_token(email):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': email
        }
        token = jwt.encode(payload, SECRET_KEY['secret_key'], algorithm='HS256')
        return token
    except Exception as e:
        return str(e)
