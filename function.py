import jwt
from datetime import *
from base import Settings

settings = Settings()

def create_access_token(data: dict):
    to_copy = data.copy()
    expire = str(datetime.now() + timedelta(minutes=settings.EXPIRE_JWT))
    to_copy.update({'expire': expire})
    encode_jwt = jwt.encode(payload=to_copy, key=settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encode_jwt

def verify_token(token: str, credential_exception):
    try:
        payload = jwt.decode(payload=token, key=settings.SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
    except Exception:
        raise credential_exception
