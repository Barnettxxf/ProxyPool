# -*- coding: utf-8 -*-

BOT_NAME = 'ProxyPool'

SPIDER_MODULES = ['ProxyPool.spiders']
NEWSPIDER_MODULE = 'ProxyPool.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 0.1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# {
#     'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
#     'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
#     'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
#     'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
#     'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
#     'scrapy.contrib.downloadermiddleware.redirect.MetaRefreshMiddleware': 580,
#     'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 590,
#     'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
#     'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
#     'scrapy.contrib.downloadermiddleware.chunked.ChunkedTransferMiddleware': 830,
#     'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
#     'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
# }
# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    # 'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': None,
    'ProxyPool.middlewares.RotateUserAgentMiddleware': 400,
    'ProxyPool.middlewares.RandomProxyMiddleware': 750,
    'ProxyPool.middlewares.SeleniumMiddleware': 360,
    'ProxyPool.middlewares.StraightMiddleware': 410,
}


# Configure item pipelines
ITEM_PIPELINES = {
    'ProxyPool.pipelines.ProxypoolPipeline': 300,
    'ProxyPool.pipelines.MysqlPipline': 500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False


# SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"


# REDIS_URL = 'redis://101.132.73.130:6379'
# REDIS_HOST = 'localhost'
# REDIS_PROT = 6379
# REDIS_ENCODING = "utf-8"                            # redis编码类型             默认：'utf-8'
# REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient' # 指定连接Redis的Python模块  默认：redis.StrictRedis
# REDIS_PARAMS  = {}                                  # Redis连接参数             默认：REDIS_PARAMS = {'socket_timeout': 30,'socket_connect_timeout': 30,'retry_on_timeout': True,'encoding': REDIS_ENCODING,}）

# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'          # 默认使用优先级队列（默认），其他：PriorityQueue（有序集合），FifoQueue（列表）、LifoQueue（列表）
# SCHEDULER_QUEUE_KEY = '%(spider)s:requests'                         # 调度器中请求存放在redis中的key
# SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"                  # 对保存到redis中的数据进行序列化，默认使用pickle
# SCHEDULER_PERSIST = True                                            # 是否在关闭时候保留原来的调度器和去重记录，True=保留，False=清空
# SCHEDULER_FLUSH_ON_START = False                                     # 是否在开始之前清空 调度器和去重记录，True=清空，False=不清空
# SCHEDULER_IDLE_BEFORE_CLOSE = 10                                    # 去调度器中获取数据时，如果为空，最多等待时间（最后没数据，未获取到）。
# SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'                  # 去重规则，在redis中保存时对应的key
# SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'# 去重规则对应处理的类

# LOG_FILE = 'proxypool.log'

