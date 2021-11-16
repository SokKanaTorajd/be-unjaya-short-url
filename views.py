from config import app 
from fastapi import Depends, Request, Cookie, status 
from passlib.hash import sha256_crypt
import jwt 
from datetime import * 
from typing import Dict
from controls import Database_Handle
from models import User
from fastapi.security import OAuth2PasswordRequestForm


@app.post('/register')
def register_user(request: User):
    mysql = Database_Handle()
    check_before = mysql.check_user(request.email)
    if check_before is not None:
        return {'message': 'Email has been used'}
    hash_pass = sha256_crypt.hash(request.password)
    join_req = (request.email, request.nama, request.username, hash_pass, request.position_job)
    mysql.create_user(join_req)
    return {'success': 'User has been created'}
