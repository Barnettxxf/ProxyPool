# -*- coding: utf-8 -*-

__author__ = 'barnett'

from . import Base
from sqlalchemy import Column, String, Integer, Sequence


class FilterRecord(Base):
    __tablename__ = 'filter_count'

    id = Column(Integer, Sequence('id', start=0, increment=1), primary_key=True)
    filter_count = Column(Integer, nullable=False)
    filter_time = Column(String(128), nullable=False)
    unit = Column(String(128), default='sec')

    def __init__(self, filter_count, filter_time, unit='sec'):
        self.filter_count = filter_count
        self.filter_time = filter_time
        self.unit = unit
