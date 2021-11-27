from pydantic import BaseModel, BaseSettings

class User(BaseModel):
    username: str 
    email: str 
    nama: str 
    password: str 
    position_job: str

class URL(BaseModel):
    url_before: str

class Settings(BaseSettings):
    env: str = 'production'
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM = 'HS256'
    EXPIRE_JWT = 25