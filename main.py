import jwt
from datelime import *
from configuration import settings
from fastapi import FastAPI

<<<<<<< HEAD
app = FastAPI()
=======
app = FastAPI()

def create_access_token(data: dict):
    file_copy = data.copy()
    expire = datetime.now() + timedelta (minutes=25)
    file_copy.update({'expire': expire.minute})
    encode_jwt = jwt.encode(playload = to_copy, key='OkeToken124342@', algorithm=settings.'HS256')
    return encode_jwt

def verify_token(token: str, credential_exception):
    try:
        payload = jwt.decode(playload=token, key='OkeToken124342@', algorithm='HS256')
        username: str = payload.get("sub")
        if username is None:
            raise credential_execption
    except Exception:
    raise credential_execption
    
    
    
    
# @app.get('/test')
# async def main():
#     return {'test': 'success'}

# @app.get('/root')
# async def root():
#     return {'root': 'oke'}
>>>>>>> 09e2aad389ace2f55dd70b0616eee9e2170655bb
