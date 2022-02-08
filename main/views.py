from datetime import *
from config import app
from db import User, check_email, Handle
from fastapi import Depends, HTTPException, Cookie, Response, Request, UploadFile, File
from passlib.hash import sha256_crypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from config import create_access_token, verify_token
    
oauth = OAuth2PasswordBearer(tokenUrl='token')
    
async def get_current_user(token: str = Depends(oauth)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="System couldn't validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)

@app.post("/reg")
async def register(usr:User=Depends(), file: UploadFile = File(...)):
    try:
        db=Handle()
        hashing=sha256_crypt.hash(usr.password)
        if db.check(usr.email) is not None:
            raise HTTPException(status_code =400,detail="Email sudah digunakan")
        data=(usr.username,usr.email,hashing,usr.position_job, file)
        db.reg(data)
        return {"message":"Kamu berhasil mendaftar", "status":200}
    except:
        raise HTTPException(status_code=500,detail="Lengkapi form terlebih")

@app.post("/token")
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

@app.post("/getuser")
async def getuser(response:Response, request: Request, usr: check_email=Depends()):
    db = Handle()
    obj = db.check(usr.email)
    if obj is None:
        raise HTTPException(status_code=400,detail="Email kamu belum terdaftar")
    else:
        response.set_cookie(key='u-update', value=usr.email)
        return {"message":"cookie disimpan", "status": 200}

@app.post('/logout-update')
def logout(response:Response):
    response.delete_cookie(key='u-update')
    return {'status': 200, 'message': 'Cookie dihapus'}

@app.post('/logout-user')
def logout(response:Response):
    response.delete_cookie(key='username')
    return {'status': 200, 'message': 'Cookie dihapus'}


    
