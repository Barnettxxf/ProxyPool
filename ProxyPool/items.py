# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxypoolItem(scrapy.Item):
    ip = scrapy.Field()
    ip_img_url = scrapy.Field()
    port = scrapy.Field()
    port_img_url = scrapy.Field()
    level = scrapy.Field()
    location = scrapy.Field()
    speed = scrapy.Field()
    lifetime = scrapy.Field()
    lastcheck = scrapy.Field()
    rule_id = scrapy.Field()
    source = scrapy.Field()
    update = scrapy.Field()
