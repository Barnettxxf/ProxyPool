# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, Integer, DateTime
try:
    from __init__ import Base, engine
except:
    from . import Base, engine
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
    rule_name = Column(String(50), nullable=False)
    indate = Column(DateTime, nullable=False)
    update = Column(DateTime, nullable=False)

    def __init__(self, ip, ip_img_url, port_img_url, port, type, level, location, speed, lifetime, lastcheck, source, rule_name, update):
        self.ip = ip
        self.ip_img_url = ip_img_url
        self.port = port
        self.port_img_url = port_img_url
        self.type = type
        self.level = level
        self.location = location
        self.speed = speed
        self.lifetime = lifetime
        self.lastcheck = lastcheck
        self.source = source
        self.rule_name = rule_name
        self.indate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update = update


if __name__ == '__main__':
    Base.metadata.create_all(engine)