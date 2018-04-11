# -*- coding: utf-8 -*-
import datetime
import time

import requests

__author__ = 'barnett'

import os, sys; sys.path.append(os.path.dirname(os.getcwd()))
from model.available import FilterIP
from model import loadSession, engine, Base
from model.proxy import Proxy
from model.filter_success import FilterRecord
from multiprocessing.dummy import Pool as ThreadPool
from urllib3 import disable_warnings


disable_warnings()

Base.metadata.create_all(engine)


class Filter(object):
    session = loadSession()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'}
    https_test_url = 'https://www.baidu.com'
    http_test_url = 'http://www.meizitu.com'

    def __init__(self, https_test_url=None, http_test_url=None, timeout=10):
        """
        Filter ip
        :param https_test_url: the test https url you wanted, default www.baidu.com.
        :param http_test_url: the test http url you wanted, default www.meizitu.com.
        :param timeout: request timeout, default 10 secs.
        """
        self.timeout = timeout
        if https_test_url is not None:
            self.https_test_url = https_test_url
        if http_test_url is not None:
            self.http_test_url = http_test_url
        self.count = 0

    def start(self):
        """ use threadpool to filter ip """
        data = self._get_data()
        pool = ThreadPool(8)
        pool.map(self._filter, data)
        pool.close()
        pool.join()

    def delete_old(self):
        """ delete unavailable ip in FilterIP which have not updated recently """
        old = self.session.query(FilterIP).all()
        for each in old:
            now = self.format_time(datetime.datetime.now())
            compare = self.format_time(each.update)
            d = now - compare
            if d.seconds > 18000:  # 5 hours
                self.session.delete(each)
        self.session.commit()

    def _filter(self, proxy):
        """ to save time, just request response's head instead of whole response's body"""
        if 'HTTPS' in proxy.type.upper():
            proxies = {'https': proxy.ip + ':' + proxy.port}
            url = self.https_test_url
        else:
            proxies = {'http': proxy.ip + ':' + proxy.port}
            url = self.http_test_url
        try:
            requests.head(url=url,
                          headers=self.headers,
                          proxies=proxies,
                          timeout=self.timeout,
                          verify=False)
            print('Successs: %s.' % (proxy.ip + ':' + proxy.port), ' Type: ', proxy.type)
            self._save(proxy)
            print('Get!!!', proxy.ip, proxy.port)
        except Exception as e:
            print('Failed: ', proxy.ip + ':' + proxy.port, ' Type: ', proxy.type)

    def _get_data(self):
        """ get proxy in last two days in Proxy table """
        data = self.session.query(Proxy).all()
        filter_data = []
        for proxy in data:
            now = self.format_time(datetime.datetime.now())
            compare = self.format_time(proxy.update)
            d = now - compare
            if d.seconds < 7200:  # 2 hours
                filter_data.append(proxy)
        self.count = len(filter_data)
        return filter_data

    def _save(self, proxy):
        """ make a new session each time to save data for Thread safe """
        avail = FilterIP(
            ip=proxy.ip,
            port=proxy.port,
            type=proxy.type.upper(),
            level=proxy.level,
            location=proxy.location,
            speed=proxy.speed,
            source=proxy.source,
            rule_name=proxy.rule_name,
            update=str(datetime.datetime.now()).split('.')[0],
        )
        session = loadSession()
        session.merge(avail)
        session.commit()
        session.remove()

    def close(self):
        self.session.close()

    def format_time(self, time):
        new = str(time)
        if '.' in new:
            new = new.split('.')[0]
        return datetime.datetime.strptime(new, '%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    start = time.time()
    t = Filter(http_test_url='http://www.xicidaili.com/')
    t.start()
    t.delete_old()
    t.close()
    cost = time.time() - start
    print('Cost %s secs.' % (time.time() - start))
    session = loadSession()
    record = FilterRecord(
        filter_count=t.count,
        filter_time=str(cost)
    )
    session.add(record)
    session.commit()
    session.close()
