# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import redis
from scrapy.exceptions import DropItem
from ProxyPool.model import loadSession
from scrapy import log
from ProxyPool.model import proxy
from pymysql.err import Error as PymsqlError

Redis = redis.StrictRedis(host='localhost', port=6379, db=0)


# 带完善，得到的item都是列表来的（先判断）
class ProxypoolPipeline(object):
    def process_item(self, item, spider):
        return item


class DuplicatesPipline(object):
    def process_item(self, item, spider):
        ip_port = item['ip'] + ':' + item['port']
        if Redis.exists('ip_port:%s' % ip_port):
            raise DropItem
        else:
            Redis.set('ip_port:%s' % ip_port, 1)
            return item


class MysqlPipline(object):
    def process_item(self, item, spider):
        if len(item['ip']):
            a = proxy.Proxy(
                ip=item['ip'],
                ip_img_url=item['ip'],
                port=item['port'],
                port_img_url=item['port'],
                type=item['type'],
                level=item['level'],
                location=item['location'],
                speed=item['speed'],
                lifetime=item['lifetime'],
                lastcheck=item['lastcheck'],
                source=item['source'],
                rule_id=item['rule_id'],
                update=item['update']
            )
            session = loadSession()
            try:
                session.add(a)
                session.commit()
            except PymsqlError as e:
                log.msg('Mysql Error: %s ' % str(e), _level=logging.WARNING)

            return item
        else:
            log.msg("ip_port is invalid!", _level=logging.WARNING)