from pydantic import BaseSettings
import jwt
from datetime import *

class Settings(BaseSettings):
    env: str = 'production'
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM = 'HS256'
    EXPIRE_JWT = 25

def create_access_token(data: dict):
    file_copy = data.copy()
    expire = datetime.now() + timedelta(minutes=25)
    file_copy.update({'expire': expire.minute})
    encode_jwt = jwt.encode(payload = file_copy, key='OkeToken124342@', algorithm='HS256')
    return encode_jwt

def verify_token(token: str, credential_exception):
    try:
        payload = jwt.decode(payload=token, key='OkeToken124342@', algorithm='HS256')
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        else:
            return {"message": "Auth berhasil"}
    except Exception:
        raise credential_exception