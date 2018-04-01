# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import *

username = USERNAME
password = PASSWORD
host = HOST
port = PORT
db = DATEBASE

__all__ = ['Base', 'engine', 'loadSession']

Base = declarative_base()

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{db}')


def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session