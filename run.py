from config import engine 
from database import Base
from main import app 

Base.metadata.create_all(bind=engine)