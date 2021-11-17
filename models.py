from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    email: str = Field(...)
    nama: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)
    position_job: str = Field(...)