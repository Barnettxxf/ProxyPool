# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__all__ = ['Base', 'engine', 'loadSession']

Base = declarative_base()

engine = create_engine('mysql+pymysql://root:xxf99311@localhost:3306/proxypool')


def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session