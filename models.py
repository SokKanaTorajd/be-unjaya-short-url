from pydantic import BaseModel, Field
from typing import Optional

class Register(BaseModel):
    email: str = Field(...)
    nama: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)
    position_job: str = Field(...)

class NotUser(BaseModel):
    url: str = Field(...)
