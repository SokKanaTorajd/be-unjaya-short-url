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

JWT_secret = 'JSONWEBTOKEN'
JWT_ALGORITHM = 'RS256'