from datetime import *
from config import app
from db.models import User
from fastapi import Depends, HTTPException, Cookie, Response, Request
from passlib.hash import sha256_crypt
from db.controls import Handle
import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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

oauth = OAuth2PasswordBearer(tokenUrl='token')

async def get_current_user(token: str = Depends(oauth)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="System couldn't validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)

@app.post("/register")
async def register(usr:User=Depends()):
    try:
        db=Handle()
        hashing=sha256_crypt.hash(usr.password)
        if db.check(usr.email) is not None:
            raise HTTPException(status_code =400,detail="Email sudah digunakan")
        data=(usr.username,usr.email,hashing,usr.position_job)
        db.reg(data)
        return {"message":"Kamu berhasil mendaftar", "status":200}
    except:
        return {"message": "Lengkapi form terlebih dahulu", "status": 500}

@app.post("/login")
async def login(response:Response, request: OAuth2PasswordRequestForm = Depends()):
    response.set_cookie(key='u-login', value=request.username)
    db=Handle()
    check=db.login(request.username)
    if check is None:
        raise HTTPException(status_code=400,detail="Username belum terdaftar")

    if sha256_crypt.verify(request.password, check["password"]):
        access_token = create_access_token(data={'sub': check['username']})
        return {"message":"Proses sistem","status":200, 'auth': access_token}
        
    else:
        raise HTTPException(status_code=400,detail="Password salah")

@app.get("/user")
async def get_user(response:Response, request: Request):
    response.set_cookie(key='u-update', value=request.email)
    return {"message":"cookie disimpan", "status": 200}

