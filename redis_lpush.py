# -*- coding:utf-8 -*-

from redis import StrictRedis
import settings
from model import loadSession
from model.rules import CrawlRules

session = loadSession()
rules = session.query(CrawlRules).filter(CrawlRules.enable == 1)

conn = StrictRedis(settings.REDIS_HOST, settings.REDIS_PROT, db=0)

start_url = [rule.start_urls for rule in rules]
for url in start_url:
    conn.lpush('proxypool:start_url %s' % url)