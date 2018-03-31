# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.test.com']
    start_urls = ['http://www.test.com/']

    def __init__(self):
        super().__init__()


    def parse(self, response):
        pass
