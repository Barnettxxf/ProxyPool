# -*- coding: utf-8 -*-

__author__ = 'barnett'

from . import loadSession, engine, Base
from sqlalchemy import Column, String, Integer, DateTime


class FilterIP(Base):
    __tablename__ = 'available'

    ip = Column(String(30), primary_key=True, nullable=False)
    port = Column(String(8), primary_key=True, nullable=False)
    type = Column(String(20), nullable=False)
    level = Column(String(20), nullable=True)
    location = Column(String(20), nullable=True)
    speed = Column(String(20), nullable=True)
    source = Column(String(500), nullable=False)
    rule_name = Column(String(50), nullable=False)
    update = Column(DateTime, nullable=False)

    def __init__(self, ip, port, type, level, location, speed, source,
                 rule_name, update):
        self.ip = ip
        self.port = port
        self.type = type
        self.level = level
        self.level = level
        self.location = location
        self.speed = speed
        self.source = source
        self.rule_name = rule_name
        self.update = update
