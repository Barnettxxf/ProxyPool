# -*- coding: utf-8 -*-

__author__ = 'barnett'

from . import Base
from sqlalchemy import Column, String, Integer, Sequence


class Record(Base):
    __tablename__ = 'record'

    id = Column(Integer, Sequence('id', start=0, increment=1), primary_key=True)
    crawl_time = Column(String(128), nullable=False)
    unit = Column(String(128), default='sec')

    def __init__(self, crawl_time, unit='sec'):
        self.crawl_time = crawl_time
        self.unit = unit
