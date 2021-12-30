from configuration import engine
from db import Base
from main import app

Base.metadata.create_all(bind=engine)