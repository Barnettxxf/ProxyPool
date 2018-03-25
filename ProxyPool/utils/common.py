# -*- coding:utf-8 -*-

import pymysql
from config_MySQL import MyAliyunServer as CONFIG


class MysqlConnection(object):
    def __init__(self):
        self.conn = pymysql.connect(**CONFIG)
        self.cursor = self.conn.cursor()

    def execute(self, sql, params=None):
        if params is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


