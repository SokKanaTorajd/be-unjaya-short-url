from typing import Optional
from starlette.responses import RedirectResponse
from config import app 
from pydantic import Field
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
    return {'message': 'User has been created', 'status': 'success'}

@app.post('/login')
def login_user(response:Response,request: OAuth2PasswordRequestForm = Depends()):
    response.set_cookie(key='username', value=request.username)
    mysql = Database_Handle()
    check_auth = mysql.auth_user(request.username)
    if check_auth is None:
        raise HTTPException(status_code=400, detail='Incorrect Username')
    access_token = create_access_token(data={'sub': check_auth['username']})
    if sha256_crypt.verify(request.password, check_auth['password']):
        return {'access_token': access_token, 'token_type': 'bearer', 'message': 'Data is valid', 'status': 'success'}
    else:
        raise HTTPException(status_code=400, detail='Incorrect Password')

@app.post("/home")
def homepage(request: Request, username: Optional[str] = Cookie(None), url: str = Form(...)):
    if username is None:
        return HTTPException(status_code=400, detail='Feature works after login')

    client_host = request.client.host
    shortCode = ShortUUID().random(length = 8)
    shorter_url = client_host + '/' + shortCode

    db = Database_Handle()
    sure_user = db.auth_user(username)
    sure_url = db.search_url(url, sure_user['id'])
    if sure_url is None:
        data = (sure_user['id'], url, shortCode, datetime.now(), 0)
        db.create_url(data)
        return {'message': 'URL shorten has created', 'shorten': shorter_url, 'status': 'success'}
    else:
        data = (sure_url['id'], shortCode, datetime.now(), 0)
        db.update_url(data)
        return { 'status': 'success', 'message': 'URL shorten has updated', 'shorten': shorter_url}

@app.get('/show_url')
def show_url(request:Request, username: Optional[str] = Cookie(None)):
    db = Database_Handle()
    sure_user = db.auth_user(username)

    if sure_user is None:
        raise HTTPException(status_code=400, detail="Cookie has expired")

    sure_url = db.URL(sure_user['id'])
    provide = []

    if sure_url is None:
        raise HTTPException(status_code=401, detail="URL did'nt created yet")
    else:
        for i in range(len(sure_url)):
            client_host = request.client.host 
            sure_url[i]['first_shorten'] =  client_host + '/' + sure_url[i]['first_shorten']
            sure_url[i]['update_short'] = client_host + '/' + sure_url[i]['update_short']
            provide.append(sure_url[i])
        return {'status': 'success', 'result': provide}

@app.get('/r/{url_shorten}')
def redirect_url(request:Request, url_shorten: str = Field):
    data = Database_Handle()

    db_bu = data.fetch_url_bu(url_shorten)
    db_au = data.fetch_url_au(url_shorten)
    
    if db_bu is None and db_au is None:
        raise HTTPException(status_code=400, detail="URL is None")
    
    if db_bu is not None:
        data.update_click_bu(db_bu['click_on'] + 1, url_shorten)
        return RedirectResponse(url=db_bu['url_before'], status_code=302)
    
    if db_au is not None:
        data.update_click_au(db_au['click_on'] + 1, url_shorten)
        return RedirectResponse(url=db_au['url_before'], status_code=302)