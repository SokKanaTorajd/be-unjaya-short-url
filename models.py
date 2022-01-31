import email
from pydantic import BaseModel
from datetime import *

class User(BaseModel):
    email : str
    username : str
    password : str
    position_job : str

class URL(BaseModel):
    url_before : str
    created_at : str
    click_on : int

class URL_UPDATE(BaseModel):
    new_url : int
    created_at : str
    click_on : int

class User_UPDATE(BaseModel):
    email : str
    