# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider # 待网站多的时候在使用分布式，保留
from ProxyPool.items import ProxypoolItem
from ProxyPool.model import loadSession
from ProxyPool.model.rules import CrawlRules


session = loadSession()
rules = session.query(CrawlRules).filter(CrawlRules.enable == 1)


class ProxypoolSpider(CrawlSpider):
    name = 'proxypool'
    allowed_domains = ['www.xicidaili.com']
    # redis_url = 'proxypool:start_url'

    def __init__(self, *a, **kw):
        global rules
        self.rule_list = rules
        self.names = [rule.name for rule in rules]
        self.selenium_enable = [rule.selenium_enable for rule in rules]
        self.allowed_domains = [rule.allow_domains for rule in rules]
        self.start_urls = [rule.start_urls for rule in rules]
        rule_list = []
        for rule in rules:
            if len(rule.next_page):
                rule_list.append(Rule(LinkExtractor(restrict_xpaths=rule.next_page), follow=True))

            if ',' not in rule.allow_url:
                allow_url = (rule.allow_url, )
            else:
                allow_url = rule.allow_url.split(',')
            if ',' not in rule.deny_url:
                deny_url = (rule.deny_url, )
            elif len(rule.deny_url) == 0:
                deny_url = ()
            else:
                deny_url = rule.deny_url.split(',')
            rule_list.append(Rule(LinkExtractor(allow=allow_url, deny=deny_url,
                                                unique=True),
                                                follow=True,
                                                callback='parse_item'))
        self.rules = tuple(rule_list)
        super(ProxypoolSpider, self).__init__(*a, **kw)

    def parse_item(self, response):
        item = ProxypoolItem()
        for rule in self.rule_list:
            if rule.allow_domains in response.url:
                table = response.xpath(rule.loop_xpath)
                for proxy in table:
                    if len(rule.ip_xpath):
                        item['ip'] = proxy.xpath(rule.ip_xpath).extract()
                    else:
                        item['ip'] = ''
                    if len(rule.ip_img_xpath):
                        item['ip_img_url'] = proxy.xpath(rule.ip_img_xpath).extract()
                    else:
                        item['ip_img_url'] = ''
                    if len(rule.port_xpath):
                        item['port'] = proxy.xpath(rule.port_xpath).extract()
                    else:
                        item['port'] = ''
                    if len(rule.port_img_xpath):
                        item['port_img_url'] = proxy.xpath(rule.port_img_xpath).extract()
                    else:
                        item['port_img_url'] = ''
                    if len(rule.location1_xpath):
                        location = proxy.xpath(rule.location1_xpath).extract()
                        if location is None:
                            location = []
                        if len(rule.location2_xpath):
                            location.extend(proxy.xpath(rule.location2_xpath).extract())
                        item['location'] = location
                    else:
                        item['location'] = ''
                    if len(rule.lifetime_xpath):
                        item['lifetime'] = proxy.xpath(rule.lifetime_xpath).extract()
                    else:
                        item['lifetime'] = ''
                    if len(rule.lastcheck_xpath):
                        item['lastcheck'] = proxy.xpath(rule.lastcheck_xpath).extract()
                    else:
                        item['lastcheck'] = ''
                    if len(rule.type_xpath):
                        item['type'] = proxy.xpath(rule.type_xpath).extract()
                    else:
                        item['type'] = ''
                    if len(rule.speed_xpath):
                        item['speed'] = proxy.xpath(rule.speed_xpath).extract()
                    else:
                        item['speed'] = ''
                    if len(rule.level_xpath):
                        item['level'] = proxy.xpath(rule.level_xpath).extract()
                    else:
                        item['level'] = ''

                    item['rule_name'] = rule.name
                    item['source'] = response.url
                    item['update'] = str(datetime.datetime.now()).split('.')[0]
                    yield item


