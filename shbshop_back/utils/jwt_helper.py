import jwt
from functools import wraps
from flask import request, jsonify
import os
from enum import Enum

SECRET_KEY = os.getenv("SECRET_KEY")

class UserType(Enum):
    PERSONAL = 1
    COMMERCIAL = 2,
    ADMIN = 3

def generate_jwt(user_id, user_type):
    payload = {
        "user_id": user_id,
        "user_type": user_type
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].replace("Bearer ", "")

        if not token:
            return jsonify({"error": "토큰이 제공되지 않았습니다."}), 401

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "토큰이 만료되었습니다."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "유효하지 않은 토큰입니다."}), 401

        return f(payload["user_id"], payload["user_type"], *args, **kwargs)
    return decorated