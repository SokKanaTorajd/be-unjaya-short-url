import jwt
from datetime import *
from config import JWT_ALGORITHM, EXPIRE_JWT, SECRET_KEY

def create_access_token(data: dict):
    to_copy = data.copy()
    expire = str(datetime.now() + timedelta(minutes=EXPIRE_JWT))
    to_copy.update({'expire': expire})
    encode_jwt = jwt.encode(payload=to_copy, key=SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encode_jwt

def verify_token(token: str, credential_exception):
    try:
        payload = jwt.decode(payload=token, key=SECRET_KEY, algorithms=JWT_ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
    except Exception:
        raise credential_exception
