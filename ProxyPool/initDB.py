# -*- coding:utf-8 -*-
from model import Base, engine, loadSession
from model.rules import CrawlRules
from model.proxy import Proxy           # 一定要导入此模块，不然proxy表不会在mysql里生成

Base.metadata.create_all(engine)
session = loadSession()
"""
免费代理网址
http://www.kxdaili.com/             //新增待爬
http://proxy.mimvp.com/free.php     // 已爬
http://www.xicidaili.com/wn/        // 已爬
http://www.ip181.com/               // 一个帖子，还行
https://www.kuaidaili.com/ops/proxylist/1/  //新增待爬
http://www.swei360.com/?page=1      //新增待爬
http://www.sslproxies.org/           // 新增待爬
http://www.us-proxy.org/             // 新增待爬
http://free-proxy-list.net/uk-proxy.html      // 新增待爬
http://www.socks-proxy.net/         // 新增待爬
http://www.data5u.com/free/index.shtml
http://www.data5u.com/free/gngn/index.shtml
http://www.data5u.com/free/gnpt/index.shtml
http://www.data5u.com/free/gwgn/index.shtml
http://www.data5u.com/free/gwpt/index.shtml
https://hidemy.name/en/proxy-list/
"""


def commit_data(item):
    session.merge(item)
    session.commit()


# --------------------------xicidaili------------------------------------------------
item_xici = CrawlRules()
item_xici.name = 'xicidaili'
item_xici.allow_domains = 'www.xicidaili.com'
item_xici.start_urls = 'http://www.xicidaili.com/wn/2'  #  这里需要取巧下，才能取到第一页(只要第一页)
item_xici.next_page = ''
item_xici.allow_url = 'wn/1$'
item_xici.deny_url = 'wn/[^1]+'
item_xici.extract_from = ''
item_xici.loop_xpath = '//*[@id="ip_list"]/tr[position()>1]'
item_xici.ip_xpath = './td[2]/text()'
item_xici.ip_img_xpathxpath = ''
item_xici.port_xpath = './td[3]/text()'
item_xici.port_img_xpath = ''
item_xici.location1_xpath = ''
item_xici.location2_xpath = ''
item_xici.speed_xpath = './td[7]/div/attribute::title'
item_xici.lifetime_xpath = ''
item_xici.type_xpath = './td[6]/text()'
item_xici.level_xpath = ''
item_xici.lastcheck_xpath = './td[10]/text()'
item_xici.enable = 0
item_xici.selenium_enable = 0
item_xici.proxy_require = 0
item_xici.straight_request = 0
commit_data(item_xici)

# --------------------------goubanjia------------------------------------------------
item_goubanjia = CrawlRules()
item_goubanjia.name = 'goubanjia'
item_goubanjia.allow_domains = 'www.goubanjia.com'
item_goubanjia.start_urls = 'http://www.goubanjia.com/'  #  这里需要取巧下，才能取到第一页(只要第一页)
item_goubanjia.next_page = ''
item_goubanjia.allow_url = ''
item_goubanjia.deny_url = 'help/,api/,buy/,user/'
item_goubanjia.extract_from = ''
item_goubanjia.loop_xpath = '//*[@id="services"]/div/div[2]/div/div/div/table/tbody/tr'
item_goubanjia.ip_xpath = './/td[1]/*'
item_goubanjia.ip_img_xpathxpath = ''
item_goubanjia.port_xpath = './/td[1]/*'
item_goubanjia.port_img_xpath = ''
item_goubanjia.location1_xpath = ''
item_goubanjia.location2_xpath = ''
item_goubanjia.speed_xpath = './td[6]/text()'
item_goubanjia.lifetime_xpath = ''
item_goubanjia.type_xpath = './td[3]/a/text()'
item_goubanjia.level_xpath = ''
item_goubanjia.lastcheck_xpath = './td[7]/text()'
item_goubanjia.enable = 0
item_goubanjia.selenium_enable = 1
item_goubanjia.proxy_require = 0
item_goubanjia.straight_request = 0
commit_data(item_goubanjia)

# --------------------------mimvp------------------------------------------------
item_mimvp = CrawlRules()
item_mimvp.name = 'mimvp'
item_mimvp.allow_domains = 'proxy.mimvp.com'
item_mimvp.start_urls = 'https://proxy.mimvp.com/free.php'
item_mimvp.next_page = ''
item_mimvp.allow_url = 'free.php?proxy=in_tp&sort=&page=1'
item_mimvp.deny_url = 'product,price,fetchopen,stat,usercenter/,about'
item_mimvp.extract_from = ''
item_mimvp.loop_xpath = '//table//td'
item_mimvp.ip_xpath = './td[@class="tbl-proxy-ip"]/text()'
item_mimvp.ip_img_xpathxpath = ''
item_mimvp.port_xpath = ''
item_mimvp.port_img_xpath = './td[@class="tbl-proxy-port"]/@src'
item_mimvp.location1_xpath = ''
item_mimvp.location2_xpath = ''
item_mimvp.speed_xpath = './td[@class="tbl-proxy-pingtime"]/@title'
item_mimvp.lifetime_xpath = ''
item_mimvp.type_xpath = './td[@class="tbl-proxy-type"]/text()'
item_mimvp.level_xpath = ''
item_mimvp.lastcheck_xpath = './td[@class="tbl-proxy-checkdtime"]/text()'
item_mimvp.enable = 1
item_mimvp.selenium_enable = 0
item_mimvp.proxy_require = 0
item_mimvp.straight_request = 1
commit_data(item_mimvp)


# --------------------------kuaidaili------------------------------------------------
item_kuaidaili = CrawlRules()
item_kuaidaili.name = 'kuaidaili'
item_kuaidaili.allow_domains = 'www.kuaidaili.com'
item_kuaidaili.start_urls = 'https://www.kuaidaili.com/ops/proxylist/1/'
item_kuaidaili.next_page = ''
item_kuaidaili.allow_url = 'ops/proxylist/[1-3]/'
item_kuaidaili.deny_url = ''
item_kuaidaili.extract_from = ''
item_kuaidaili.loop_xpath = '//*[@id="freelist"]/table/tbody/tr'
item_kuaidaili.ip_xpath = './td[1]/text()'
item_kuaidaili.ip_img_xpathxpath = ''
item_kuaidaili.port_xpath = './td[2]/text()'
item_kuaidaili.port_img_xpath = ''
item_kuaidaili.location1_xpath = ''
item_kuaidaili.location2_xpath = ''
item_kuaidaili.speed_xpath = './td[7]/text()'
item_kuaidaili.lifetime_xpath = ''
item_kuaidaili.type_xpath = './td[4]/text()'
item_kuaidaili.level_xpath = ''
item_kuaidaili.lastcheck_xpath = './td[8]/text()'
item_kuaidaili.enable = 1
item_kuaidaili.selenium_enable = 0
item_kuaidaili.proxy_require = 0
item_kuaidaili.straight_request = 0
commit_data(item_kuaidaili)


# --------------------------swei360------------------------------------------------
item_swei360 = CrawlRules()
item_swei360.name = 'swei360'
item_swei360.allow_domains = 'www.swei360.com'
item_swei360.start_urls = 'http://www.swei360.com/?page=1'
item_swei360.next_page = ''
item_swei360.allow_url = '?page=[1-3]'
item_swei360.deny_url = ''
item_swei360.extract_from = ''
item_swei360.loop_xpath = '//*[@id="list"]/table/tbody/tr'
item_swei360.ip_xpath = './td[1]/text()'
item_swei360.ip_img_xpathxpath = ''
item_swei360.port_xpath = './td[2]/text()'
item_swei360.port_img_xpath = ''
item_swei360.location1_xpath = ''
item_swei360.location2_xpath = ''
item_swei360.speed_xpath = './td[7]/text()'
item_swei360.lifetime_xpath = ''
item_swei360.type_xpath = './td[4]/text()'
item_swei360.level_xpath = ''
item_swei360.lastcheck_xpath = './td[8]/text()'
item_swei360.enable = 1
item_swei360.selenium_enable = 0
item_swei360.proxy_require = 0
item_swei360.straight_request = 0
commit_data(item_swei360)


# --------------------------free-proxy-list------------------------------------------------
item_freeproxylist = CrawlRules()
item_freeproxylist.name = 'freeproxylist'
item_freeproxylist.allow_domains = 'free-proxy-list.net'
item_freeproxylist.start_urls = 'https://free-proxy-list.net/'
item_freeproxylist.next_page = ''
item_freeproxylist.allow_url = '^$'
item_freeproxylist.deny_url = ''
item_freeproxylist.extract_from = ''
item_freeproxylist.loop_xpath = '//*[@id="list"]/table/tbody/tr'
item_freeproxylist.ip_xpath = './td[1]/text()'
item_freeproxylist.ip_img_xpathxpath = ''
item_freeproxylist.port_xpath = './td[2]/text()'
item_freeproxylist.port_img_xpath = ''
item_freeproxylist.location1_xpath = ''
item_freeproxylist.location2_xpath = ''
item_freeproxylist.speed_xpath = ''
item_freeproxylist.lifetime_xpath = ''
item_freeproxylist.type_xpath = './td[7]/text()'
item_freeproxylist.level_xpath = ''
item_freeproxylist.lastcheck_xpath = './td[8]/text()'
item_freeproxylist.enable = 1
item_freeproxylist.selenium_enable = 0
item_freeproxylist.proxy_require = 0
item_freeproxylist.straight_request = 0
commit_data(item_freeproxylist)


# --------------------------data5u------------------------------------------------
item_data5u = CrawlRules()
item_data5u.name = 'data5u'
item_data5u.allow_domains = 'www.data5u.com'
item_data5u.start_urls = 'http://www.data5u.com/free/index.shtml'
item_data5u.next_page = ''
item_data5u.allow_url = 'free/\w+/index.shtml'
item_data5u.deny_url = ''
item_data5u.extract_from = ''
item_data5u.loop_xpath = '/html/body/div[5]/ul/li[2]/ul'
item_data5u.ip_xpath = './span[1]/li/text()'
item_data5u.ip_img_xpathxpath = ''
item_data5u.port_xpath = './span[2]/li/text()'
item_data5u.port_img_xpath = ''
item_data5u.location1_xpath = ''
item_data5u.location2_xpath = ''
item_data5u.speed_xpath = './span[8]/li/text()'
item_data5u.lifetime_xpath = ''
item_data5u.type_xpath = './span[4]/li/a/text()'
item_data5u.level_xpath = ''
item_data5u.lastcheck_xpath = './span[9]/li/text()'
item_data5u.enable = 1
item_data5u.selenium_enable = 0
item_data5u.proxy_require = 0
item_data5u.straight_request = 0
commit_data(item_data5u)


# --------------------------hidemy------------------------------------------------
item_hidemy = CrawlRules()
item_hidemy.name = 'hidemy'
item_hidemy.allow_domains = 'hidemy.name'
item_hidemy.start_urls = 'https://hidemy.name/en/proxy-list/'
item_hidemy.next_page = ''
item_hidemy.allow_url = '/en/proxy-list/(.*?)#list'
item_hidemy.deny_url = ''
item_hidemy.extract_from = ''
item_hidemy.loop_xpath = '//*[@id="content-section"]/section[1]/div/table/tbody/tr'
item_hidemy.ip_xpath = './span[1]/li/text()'
item_hidemy.ip_img_xpathxpath = ''
item_hidemy.port_xpath = './span[2]/li/text()'
item_hidemy.port_img_xpath = ''
item_hidemy.location1_xpath = ''
item_hidemy.location2_xpath = ''
item_hidemy.speed_xpath = './span[8]/li/text()'
item_hidemy.lifetime_xpath = ''
item_hidemy.type_xpath = './span[4]/li/a/text()'
item_hidemy.level_xpath = ''
item_hidemy.lastcheck_xpath = './span[9]/li/text()'
item_hidemy.enable = 1
item_hidemy.selenium_enable = 1
item_hidemy.proxy_require = 1
item_hidemy.straight_request = 0
commit_data(item_hidemy)