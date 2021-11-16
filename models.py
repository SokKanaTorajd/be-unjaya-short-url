from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    email: str  
    nama: str 
    username: str 
    password: str 
    position_job: str 