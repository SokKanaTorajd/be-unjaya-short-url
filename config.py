from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from fastapi.middleware.cors import CORSMiddleware
from function import Settings

#root
app = FastAPI()
settings = Settings()
#db setup
DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/shorten_url'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

#cors setting
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
