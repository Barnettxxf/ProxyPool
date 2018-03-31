# -*- coding: utf-8 -*-

import logging
import os
import sys

from .model import loadSession
from scrapy import log
from .model import proxy
from pymysql.err import Error as PymsqlError

DIRNAME = 'item_clean'
ITEMCLEAN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), DIRNAME)
sys.path.append(ITEMCLEAN_DIR)
file_list = os.listdir(ITEMCLEAN_DIR)


class ProxypoolPipeline(object):
    def process_item(self, item, spider):

        # 自定义清理模块
        file_list = os.listdir(ITEMCLEAN_DIR)
        for module in file_list:
            try:
                if module == (item['rule_name'] + '.py'):
                    m = __import__(str(module.split('.')[0]))
                    pipline = getattr(m, 'pipline')
                    pipline(item)
            except Exception as e:
                log.msg('pipline import error: ', e)

        # 通用清理模块
        m2 = __import__('usual')
        pipline2 = getattr(m2, 'pipline')
        pipline2(item)

        return item


class MysqlPipline(object):
    def process_item(self, item, spider):
        if len(item['ip']):
            a = proxy.Proxy(
                ip=item['ip'],
                ip_img_url=item['ip_img_url'],
                port=item['port'],
                port_img_url=item['port_img_url'],
                type=item['type'],
                level=item['level'],
                location=item['location'],
                speed=item['speed'],
                lifetime=item['lifetime'],
                lastcheck=item['lastcheck'],
                source=item['source'],
                rule_name=item['rule_name'],
                update=item['update']
            )
            session = loadSession()
            try:
                session.merge(a)
                session.commit()
            except PymsqlError as e:
                log.msg('Mysql Error: %s ' % str(e))
            return item
        else:
            log.msg("ip_port is invalid!")
