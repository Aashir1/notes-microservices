import jwt
import time
from typing import Dict, Union
from auth_service.config import Config

JWT_SECRET = Config.jwt_secret
JWT_ALGORITHM = Config.jwt_algorithm


def token_response(token: str):
    return {"access_token": token}


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {"user_id": user_id, "expires": time.time() + 600}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str) -> Union[dict, None]:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception as e:
        print(e)
        return None


def check_password(password: str, hashed_password: str) -> bool:
    return false
