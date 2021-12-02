from pydantic import BaseModel

class User(BaseModel):
    username: str 
    email: str 
    nama: str 
    password: str 
    position_job: str

class URL(BaseModel):
    url_before: str
