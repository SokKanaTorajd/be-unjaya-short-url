from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from fastapi.middleware.cors import CORSMiddleware

#root
app = FastAPI()

#db setup
DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/shorten_url'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

#cors setting
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
JWT_ALGORITHM = 'HS256'
EXPIRE_JWT = 25