# -*- coding:utf-8 -*-

# from .common import MysqlConnection
#
#
# class GetIp(MysqlConnection):
#
#     @property
#     def ip_list(self):
#         return self.get_ip()
#
#     def get_ip(self):
#         query_sql = """
#             select ip,port from proxyhttps order by date_time DESC limit 20;
#         """
#         self.execute(query_sql)
#         return self.cursor.fetchall()
from sqlalchemy import desc

from ProxyPool.ProxyPool.model.available import FilterIP
from ProxyPool.ProxyPool.model import loadSession


class AbtainIp(object):

    @property
    def ip_list(self):
        return self._data

    def _data(self):
        session = loadSession()
        return session.query(FilterIP).order_by(desc(FilterIP.update))[:50]



