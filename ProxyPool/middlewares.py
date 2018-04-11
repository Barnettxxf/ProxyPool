# -*- coding: utf-8 -*-
import random

import requests
from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.http import HtmlResponse
from selenium import webdriver
from .utils.get_ip import AbtainIp

option = webdriver.ChromeOptions()
option.set_headless()
t = AbtainIp()


class RotateUserAgentMiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        print('User-Agent: ', ua)
        request.headers.setdefault('User-Agent', ua)
        # request.headers.setdefault('Refer', refer)

    # for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]


class SeleniumMiddleware(object):
    driver = webdriver.Chrome(chrome_options=option)

    def __init__(self, timeout=10, script_timeout=20):
        self.timeout = timeout
        self.script_timeout = script_timeout

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT', 10),
                   script_timeout=crawler.settings.get('selenium_script_timeout', 20))

    def spider_opened(self, spider):
        self.driver.set_page_load_timeout(self.timeout)
        self.driver.set_script_timeout(self.script_timeout)

    def process_request(self, request, spider):
        # try:
        for rule in spider.rule:
            if rule.allow_domains in request.url and rule.selenium_enable:
                return self.download(request)
        # except TimeoutError:
        #     return request
        # except AttributeError:
        #     return self.download()

    def spider_closed(self):
        self.driver.quit()

    def download(self, request):
        self.driver.get(request.url)
        text = self.driver.page_source
        return HtmlResponse(url=request.url, body=text, request=request, encoding='utf-8')


class SplashMiddleware(object):
    def process_request(self, request, spider):
        pass


class StraightMiddleware(object):
    def process_request(self, request, spider):
        for rule in spider.rule:
            if rule.allow_domains in request.url and rule.straight_request:
                headers = random.choice(RotateUserAgentMiddleware.user_agent_list)
                url = request.url
                text = requests.get(url=url, headers={'User-Agent': headers}).text
                return HtmlResponse(url=request.url, body=text, request=request, encoding='utf-8')


class RandomProxyMiddleware(object):
    ip_list = t.ip_list
    count = 0

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    @staticmethod
    def change_count():
        if RandomProxyMiddleware.count <= 200:
            RandomProxyMiddleware.count += 1
            return False
        else:
            RandomProxyMiddleware.count = 0
            return True

    def process_request(self, request, spider):
        for rule in spider.rule:
            if rule.allow_domains in request.url and rule.proxy_require:
                if self.change_count():
                    self.ip_list = t.ip_list
                    with open('ip_list.txt', 'a') as f:
                        f.write('-----------------------------------')
                        for line in self.ip_list:
                            f.write(str(line))
                        f.write('\n')
                proxy = random.choice(self.ip_list)
                print('new_ip: ', 'https://' + proxy.ip + ':' + proxy.port)
                request.meta['proxy'] = 'https://' + proxy.ip + ':' + proxy.port

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s' % spider.name)
