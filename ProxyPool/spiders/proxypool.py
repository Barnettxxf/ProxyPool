# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ProxyPool.items import ProxypoolItem
from ProxyPool.model import loadSession
from ProxyPool.model.rules import CrawlRules

session = loadSession()
rules = session.query(CrawlRules).filter(CrawlRules.enable == 1)


class ProxypoolSpider(RedisCrawlSpider):
    name = 'proxypool'
    allowed_domains = ['www.xicidaili.com']
    # start_urls = ['http://www.xicidaili.com/']
    redis_url = 'proxypool:start_url'

    def __init__(self):
        global rules
        self.rule_list = rules
        self.names = [rule.name for rule in rules]
        self.selenium_enable = [rule.selenium for rule in rules]
        self.allowed_domains = [rule.allowed_domains for rule in rules]
        self.start_urls = [rule.start_urls for rule in rules]
        rule_list = []
        for rule in rules:
            if len(rule.next_page):
                rule_list.append(Rule(LinkExtractor(restrict_xpaths=rule.next_page), follow=True))

            rule_list.append(Rule(LinkExtractor(allow=rule.allow_url.split(','),
                                                unique=True),
                                  follow=True,
                                  callback='parse_item'))
        self.rules = tuple(rule_list)
        super(ProxypoolSpider, self).__init__()

    def start_requests(self):
        for url, name, selenium_enable in zip(self.start_urls, self.names, self.selenium_enable):
            yield scrapy.Request(url, callback=self.parse_item, meta={'selenium': selenium_enable,
                                                                      'name': name})

    def parse_item(self, response):
        item = ProxypoolItem()
        name = response.meta.get('name', '')
        for rule in self.rule_list:
            if rule.name == name:
                if len(rule.loop_xpath):
                    for proxy in response.xpath(rule.loop_xpath):
                        if len(rule.ip_xpath):
                            item['ip'] = proxy.xpath(rule.ip_xpath).extract()
                        if len(rule.ip_img_xpath):
                            item['ip_img_url'] = proxy.xpath(rule.ip_img_xpath).extract()
                        if len(rule.port_xpath):
                            item['port'] = proxy.xpath(rule.port_xpath).extract()
                        if len(rule.port_img_xpath):
                            item['port_img_url'] = proxy.xpath(rule.port_img_xpath).extract()
                        if len(rule.location1_xpath):
                            location = proxy.xpath(rule.location1_xpath).extract()
                            if location is None:
                                location = []
                        if len(rule.location2_xpath):
                            location.extend(proxy.xpath(rule.location2_xpath).extract())
                        if len(rule.lifetime_xpath):
                            item['lifetime'] = proxy.xpath(rule.lifetime_xpath).extract()
                        if len(rule.lastcheck_xpath):
                            item['lastcheck'] = proxy.xpath(rule.lastcheck_xpath).extract()
                        if len(rule.type_xpath):
                            item['type'] = proxy.xpath(rule.type_xpath).extract()
                        if len(rule.speed_xpath):
                            item['speed'] = proxy.xpath(rule.speed_xpath).extract()

                        item['location'] = location
                        item['id'] = rule.id
                        item['source'] = response.url
                        item['update'] = str(datetime.datetime.now()).split('.')[0]
                        yield item


