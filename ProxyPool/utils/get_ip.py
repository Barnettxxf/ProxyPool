# -*- coding:utf-8 -*-

from sqlalchemy import desc

from ProxyPool.model.available import FilterIP
from ProxyPool.model import loadSession


class AbtainIp(object):

    @property
    def ip_list(self):
        return self._data

    def _data(self):
        session = loadSession()
        return session.query(FilterIP).order_by(desc(FilterIP.update))[:50]



