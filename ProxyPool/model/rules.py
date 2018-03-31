# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, Integer
from . import Base


class CrawlRules(Base):

    __tablename__ = 'crawlrules'

    name = Column(String(100), nullable=False, primary_key=True)
    allow_domains = Column(String(100), nullable=False, primary_key=True)
    start_urls = Column(String(500), nullable=False)
    next_page = Column(String(500), nullable=False, default="")
    allow_url =  Column(String(500), nullable=False)
    deny_url =  Column(String(500), nullable=False)
    extract_from = Column(String(500), nullable=False, default="")
    loop_xpath = Column(String(500), nullable=False)
    ip_xpath = Column(String(500), nullable=False, default="")
    ip_img_xpath = Column(String(500), nullable=False, default="")
    port_xpath = Column(String(500), nullable=False, default="")
    port_img_xpath = Column(String(500), nullable=False, default="")
    location1_xpath = Column(String(500), nullable=False, default="")
    location2_xpath = Column(String(500), nullable=False, default="")
    speed_xpath = Column(String(500), nullable=False, default="")
    lifetime_xpath = Column(String(500), nullable=False, default="")
    type_xpath = Column(String(500), nullable=False, default="")
    level_xpath = Column(String(500), nullable=False, default="")
    lastcheck_xpath = Column(String(500), nullable=False, default="")
    enable = Column(Integer, nullable=False, default=1)
    selenium_enable = Column(Integer, nullable=False, default=0)
    proxy_require = Column(Integer, nullable=False, default=0)
    straight_request = Column(Integer, nullable=False, default=0)




