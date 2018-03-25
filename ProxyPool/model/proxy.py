# -*- coding:utf-8 -*-

from sqlalchemy import  Column, String, Integer, DateTime
from . import Base
import datetime


class Proxy(Base):
    __tablename__ = 'proxies'

    ip = Column(String(30), primary_key=True, nullable=False)
    ip_img_url = Column(String(500), nullable=False)
    port = Column(String(8), primary_key=True, nullable=False)
    port_img_url = Column(String(500), nullable=False)
    type = Column(String(20), nullable=False)
    level = Column(String(20), nullable=True)
    location = Column(String(20), nullable=True)
    speed = Column(String(20), nullable=True)
    lifetime = Column(String(20), nullable=True)
    lastcheck = Column(String(20), nullable=True)
    source = Column(String(500), nullable=False)
    rule_id = Column(Integer, nullable=False)
    indate = Column(DateTime, nullable=False)
    update = Column(DateTime, nullable=False)

    def __init__(self, ip, port, type, level, location, speed, lifetime, lastcheck, source, rule_id, update):
        self.ip = ip
        self.port = port
        self.type = type
        self.level = level
        self.location = location
        self.speed = speed
        self.lifetime = lifetime
        self.lastcheck = lastcheck
        self.source = source
        self.rule_id = rule_id
        self.indate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update = update