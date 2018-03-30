# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ProxyPool import settings
from ProxyPool.items import ProxypoolItem
from model import loadSession
from model.rules import CrawlRules


class StartspiderSpider(scrapy.Spider):
    name = 'startspider'
    allowed_domains = ['www.baidu.com']
    start_urls = []

    def __init__(self, name, **kwargs):
        super(StartspiderSpider, self).__init__(name, **kwargs)
        self.start_rulespider()

    def parse(self, response):
        pass

    def start_rulespider(self):
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
        process.start()


class ProxySpider(CrawlSpider):

    def __init__(self, rule, *a, **kw):
        self.rule = rule
        self.name = rule.name

        self.allowed_domains = rule.allowed_domains.split(',')
        self.start_urls = rule.start_urls.split(',')
        rule_list = []

        if len(rule.next_page):
            rule_list.append(Rule(LinkExtractor(restrict_xpaths=rule.next_page), follow=True))

        rule_list.append(Rule(LinkExtractor(
            allow=rule.allow_url.split(','),
            unique=True),
            follow=True,
            callback='parse_item'))

        self.rules = tuple(rule_list)
        super(ProxySpider, self).__init__(*a, **kw)

    def parse_item(self, response):
        item = ProxypoolItem()
        table = response.xpath(self.rule.loop_xpath)
        for proxy in table:
            if len(self.rule.ip_xpath):
                item['ip'] = proxy.xpath(self.rule.ip_xpath).extract()
            else:
                item['ip'] = ''
            if len(self.rule.ip_img_xpath):
                item['ip_img_url'] = proxy.xpath(self.rule.ip_img_xpath).extract()
            else:
                item['ip_img_url'] = ''
            if len(self.rule.port_xpath):
                item['port'] = proxy.xpath(self.rule.port_xpath).extract()
            else:
                item['port'] = ''
            if len(self.rule.port_img_xpath):
                item['port_img_url'] = proxy.xpath(self.rule.port_img_xpath).extract()
            else:
                item['port_img_url'] = ''
            if len(self.rule.location1_xpath):
                location = proxy.xpath(self.rule.location1_xpath).extract()
                if location is None:
                    location = []
                if len(self.rule.location2_xpath):
                    location.extend(proxy.xpath(self.rule.location2_xpath).extract())
                item['location'] = location
            else:
                item['location'] = ''
            if len(self.rule.lifetime_xpath):
                item['lifetime'] = proxy.xpath(self.rule.lifetime_xpath).extract()
            else:
                item['lifetime'] = ''
            if len(self.rule.lastcheck_xpath):
                item['lastcheck'] = proxy.xpath(self.rule.lastcheck_xpath).extract()
            else:
                item['lastcheck'] = ''
            if len(self.rule.type_xpath):
                item['type'] = proxy.xpath(self.rule.type_xpath).extract()
            else:
                item['type'] = ''
            if len(self.rule.speed_xpath):
                item['speed'] = proxy.xpath(self.rule.speed_xpath).extract()
            else:
                item['speed'] = ''
            if len(self.rule.level_xpath):
                item['level'] = proxy.xpath(self.rule.level_xpath).extract()
            else:
                item['level'] = ''

            item['rule_name'] = self.rule.name
            item['source'] = response.url
            item['update'] = str(datetime.datetime.now()).split('.')[0]
            yield item

