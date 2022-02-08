from MySQLdb import Binary
import sqlalchemy
import databases
from sqlalchemy.dialects.mysql import MEDIUMBLOB

DATABASE_URL = 'mysql+mysqlconnector://root:@localhost/db_dsc'

metadata = sqlalchemy.MetaData()


database = databases.Database(DATABASE_URL)

register = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(100)),
    sqlalchemy.Column("email", sqlalchemy.String(255), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(255), unique=True),
    sqlalchemy.Column("position_job", sqlalchemy.String(100)),
    sqlalchemy.Column("foto_profil", sqlalchemy.BLOB, nullable=True)
)
url = sqlalchemy.Table(
    "url",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer,sqlalchemy.ForeignKey("user.id")),
    sqlalchemy.Column("url_before", sqlalchemy.String(255)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("click_on", sqlalchemy.Integer),
)
url_update= sqlalchemy.Table(
    "url_update",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("url_id", sqlalchemy.Integer,sqlalchemy.ForeignKey("url.id")),
    sqlalchemy.Column("new_url", sqlalchemy.String(255)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("click_on", sqlalchemy.Integer),
)
 
engine = sqlalchemy.create_engine( DATABASE_URL)