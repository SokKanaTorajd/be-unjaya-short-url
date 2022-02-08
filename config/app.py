from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseSettings
from .conf import Settings

app = FastAPI()

class Settings(BaseSettings):
    env: str = 'production'
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM = 'HS256'
    EXPIRE_JWT = 25

settings = Settings()

origins = dict(
  development=["http://localhost:8000"], 
  production=["http://localhost:3000"]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins[settings.env],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

