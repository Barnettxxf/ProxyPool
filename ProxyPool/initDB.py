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
http://free-proxy-list.net/uk-proxy.html'      // 新增待爬
http://www.socks-proxy.net/'         // 新增待爬
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
item_goubanjia.enable = 1
item_goubanjia.selenium_enable = 1
commit_data(item_goubanjia)

