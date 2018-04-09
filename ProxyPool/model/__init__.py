# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .config import *

username = USERNAME
password = PASSWORD
host = HOST
port = PORT
db = DATEBASE

__all__ = ['Base', 'engine', 'loadSession']

Base = declarative_base()

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8')


def loadSession():
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    session = Session()
    return session