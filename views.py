from typing import Optional
from config import app 
from fastapi import Depends, Request, Cookie, HTTPException, Response, Form
from passlib.hash import sha256_crypt
from datetime import * 
from controls import Database_Handle
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from function import create_access_token, verify_token
from shortuuid import ShortUUID
from datetime import *

oauth = OAuth2PasswordBearer(tokenUrl='login_user')

def get_current_user(token: str = Depends(oauth)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="System couldn't validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)

@app.post('/register')
def register_user(username: str = Form(...), email: str = Form(...), nama: str = Form(...), password: str = Form(...), position_job : str = Form(...)):
    mysql = Database_Handle()
    check_before = mysql.check_user(email)
    if check_before is not None:
        raise HTTPException(status_code=400, detail='Email has been used')
    hash_pass = sha256_crypt.hash(password)
    join_req = (email, nama, username, hash_pass, position_job)
    mysql.create_user(join_req)
    return {'success': 'User has been created'}

@app.post('/login')
def login_user(response:Response,request: OAuth2PasswordRequestForm = Depends()):
    response.set_cookie(key='username', value=request.username)
    mysql = Database_Handle()
    check_auth = mysql.auth_user(request.username)
    if check_auth is None:
        raise HTTPException(status_code=400, detail='Incorrect Username')
    access_token = create_access_token(data={'sub': check_auth['username']})
    if sha256_crypt.verify(request.password, check_auth['password']):
        return {'access_token': access_token, 'token_type': 'bearer', 'success': 'Data is valid'}
    else:
        raise HTTPException(status_code=400, detail='Incorrect Password')

@app.post("/home")
def homepage(request: Request, username: Optional[str] = Cookie(None), url: str = Form(...)):
    if username is None:
        return HTTPException(status_code=400, detail='Feature works after login')

    db = Database_Handle()
    
    usr_check = db.auth_user(username)
    db.create_url(usr_check['id'], url)

    check_url = db.search_url(url, usr_check['id'])
    
    client_host = request.client.host
    shortCode = ShortUUID().random(length = 8)
    shorter_url = client_host + '/' + shortCode


    data = (check_url['id'], shorter_url, datetime.now(), 1)

    db.create_shorten(data)

    return {'success': 'URL shorten has created', 'username': username}
