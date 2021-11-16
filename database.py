from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from config import Base 
from datetime import *

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(150), unique=True, nullable=False)
    nama = Column(String(100), nullable=False)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), unique=True, nullable=False)
    position_job = Column(String(100), nullable=False)
    url_table = relationship('URL', backref='url_id')

class URL(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    url_before = Column(String(255), nullable=False)
    url_detail = relationship('Detail', backref='new_shorten')

class Detail(Base):
    __tablename__ = 'url_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url_id = Column(Integer, ForeignKey('url.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    url_shortened = Column(String(255), nullable=False)
    created_at = Column(Date, default=datetime.now())
    click_on = Column(Integer, nullable=True)

