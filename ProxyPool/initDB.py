# -*- coding:utf-8 -*-
from model import Base, engine, loadSession
from model.rules import CrawlRules

Base.metadata.create_all(engine)

session = loadSession()

item = CrawlRules()
item.name = ''
item.allow_domains = ''
item.start_urls = ''
item.next_page = ''
item.extract_from = ''
item.loop_xpath = ''
item.ip_xpath = ''
item.ip_img_xpathxpath = ''
item.port_xpath = ''
item.port_img_xpath = ''
item.location1_xpath = ''
item.location2_xpath = ''
item.speed_xpath = ''
item.lifetime_xpath = ''
item.type_xpath = ''
item.level_xpath = ''
item.lastcheck_xpath = ''
item.enable = 1
item.selenium_enable = 0

session.add(item)
session.commit()
