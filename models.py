from pydantic import BaseModel
from datetime import *

<<<<<<< HEAD
class User(BaseModel):
=======
class Todo(BaseModel):
>>>>>>> 9542d332129dcb8a8b264766e447b14cf5f7b54f
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
<<<<<<< HEAD
    click_on : int
=======
    click_on : int

class LOGIN(BaseModel):
    username : str
    password : str
    

>>>>>>> 9542d332129dcb8a8b264766e447b14cf5f7b54f
