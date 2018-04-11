# -*- coding: utf-8 -*-
import datetime
import logging
import os

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ProxyPool import settings
from ProxyPool.items import ProxypoolItem
from ProxyPool.model import loadSession
from ProxyPool.model.rules import CrawlRules
from time import time

from model.record_run_time import Record

start_time = time()


class StartspiderSpider(scrapy.Spider):
    name = 'startspider'
    allowed_domains = ['www.baidu.com']
    start_urls = []

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {},
    }

    def __init__(self):
        super(StartspiderSpider, self).__init__()
        self.start_rulespider()
        scrapy.Spider.close(StartspiderSpider, reason='finished')

    def parse(self, response):
        """ do nothing """
        pass

    def start_rulespider(self):
        """ start all rules spider in CrawlRule """
        my_settings = Settings()
        my_settings.set("ITEM_PIPELINES", settings.ITEM_PIPELINES)
        my_settings.set("DOWNLOADER_MIDDLEWARES", settings.DOWNLOADER_MIDDLEWARES)
        my_settings.set("DOWNLOAD_DELAY", settings.DOWNLOAD_DELAY)
        my_settings.get("COOKIES_ENABLED", settings.COOKIES_ENABLED)
        my_settings.get("ROBOTSTXT_OBEY", settings.ROBOTSTXT_OBEY)

        process = CrawlerProcess(my_settings)
        session = loadSession()
        rules = session.query(CrawlRules).filter(CrawlRules.enable == 1)
        for rule in rules:
            process.crawl(ProxySpider, rule)
            print('crawl rule: ', rule.name)
        process.start()

    @staticmethod
    def closed(reason):
        """ shutdown abort startspider, or it will raise exception ... """
        from _signal import SIGKILL
        msg = 'Spider close: ' + StartspiderSpider.name + '(%s)' % reason
        logging.info(msg,)
        cost = time() - start_time
        session = loadSession()
        record = Record(
            crawl_time=str(cost)
        )
        session.add(record)
        session.commit()
        session.close()
        pid = os.getpid()
        print('Total cost: %s seconds.' % cost)
        os.kill(pid, SIGKILL)


class ProxySpider(CrawlSpider):
    name = 'magic'

    def __init__(self, rule, *a, **kw):
        """ create all spider by rules """
        self.rule = [rule, ]
        self.name = rule.name

        self.allowed_domains = rule.allow_domains.split(',')
        self.start_urls = rule.start_urls.split(',')
        rule_list = []

        if len(rule.next_page):
            rule_list.append(Rule(LinkExtractor(restrict_xpaths=rule.next_page), follow=True))

        if ',' not in rule.allow_url:
            allow_url = (rule.allow_url,)
        else:
            allow_url = rule.allow_url.split(',')
        if ',' not in rule.deny_url:
            deny_url = (rule.deny_url,)
        elif len(rule.deny_url) == 0:
            deny_url = ()
        else:
            deny_url = rule.deny_url.split(',')
        rule_list.append(Rule(LinkExtractor(
            allow=allow_url,
            deny=deny_url,
            unique=True),
            follow=True,
            callback='parse_item'))

        self.rules = tuple(rule_list)
        super(ProxySpider, self).__init__(*a, **kw)

    def parse_item(self, response):
        """ usual html parse function """
        item = ProxypoolItem()
        table = response.xpath(self.rule[0].loop_xpath)
        for proxy in table:
            if len(self.rule[0].ip_xpath):
                item['ip'] = proxy.xpath(self.rule[0].ip_xpath).extract()
            else:
                item['ip'] = ''
            if len(self.rule[0].ip_img_xpath):
                item['ip_img_url'] = proxy.xpath(self.rule[0].ip_img_xpath).extract()
            else:
                item['ip_img_url'] = ''
            if len(self.rule[0].port_xpath):
                item['port'] = proxy.xpath(self.rule[0].port_xpath).extract()
            else:
                item['port'] = ''
            if len(self.rule[0].port_img_xpath):
                item['port_img_url'] = proxy.xpath(self.rule[0].port_img_xpath).extract()
            else:
                item['port_img_url'] = ''
            if len(self.rule[0].location1_xpath):
                location = proxy.xpath(self.rule[0].location1_xpath).extract()
                if location is None:
                    location = []
                if len(self.rule[0].location2_xpath):
                    location.extend(proxy.xpath(self.rule[0].location2_xpath).extract())
                item['location'] = location
            else:
                item['location'] = ''
            if len(self.rule[0].lifetime_xpath):
                item['lifetime'] = proxy.xpath(self.rule[0].lifetime_xpath).extract()
            else:
                item['lifetime'] = ''
            if len(self.rule[0].lastcheck_xpath):
                item['lastcheck'] = proxy.xpath(self.rule[0].lastcheck_xpath).extract()
            else:
                item['lastcheck'] = ''
            if len(self.rule[0].type_xpath):
                item['type'] = proxy.xpath(self.rule[0].type_xpath).extract()
            else:
                item['type'] = ''
            if len(self.rule[0].speed_xpath):
                item['speed'] = proxy.xpath(self.rule[0].speed_xpath).extract()
            else:
                item['speed'] = ''
            if len(self.rule[0].level_xpath):
                item['level'] = proxy.xpath(self.rule[0].level_xpath).extract()
            else:
                item['level'] = ''

            item['rule_name'] = self.rule[0].name
            item['source'] = response.url
            item['update'] = str(datetime.datetime.now()).split('.')[0]
            yield item
