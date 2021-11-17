from config import app 
from fastapi import Depends, Request, Cookie, status, HTTPException
from passlib.hash import sha256_crypt
from datetime import * 
from controls import Database_Handle
from models import Register, Login
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from function import create_access_token, verify_token

oauth = OAuth2PasswordBearer(tokenUrl='login_user')

@app.post('/register')
def register_user(request: Register = Depends()):
    mysql = Database_Handle()
    check_before = mysql.check_user(request.email)
    if check_before is not None:
        raise HTTPException(status_code=400, detail='Email has been used')
    hash_pass = sha256_crypt.hash(request.password)
    join_req = (request.email, request.nama, request.username, hash_pass, request.position_job)
    mysql.create_user(join_req)
    return {'success': 'User has been created'}

@app.post('/login')
def login_user(request: OAuth2PasswordRequestForm = Depends()):
    mysql = Database_Handle()
    check_auth = mysql.auth_user(request.username)
    if check_auth is None:
        raise HTTPException(status_code=400, detail='Incorrect Username')
    access_token = create_access_token(data={'sub': check_auth['username']})
    if sha256_crypt.verify(request.password, check_auth['password']):
        return {'access_token': access_token, 'token_type': 'bearer', 'success': 'Data is valid'}
    else:
        raise HTTPException(status_code=400, detail='Incorrect Password')

def get_current_user(token: str = Depends(oauth)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="System couldn't validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)
