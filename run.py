from views import app
from db import metadata,engine
metadata.create_all(engine)