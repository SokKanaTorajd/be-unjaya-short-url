from db import engine, metadata
from main import app

metadata.create_all(engine)