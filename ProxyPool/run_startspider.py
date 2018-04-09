# -*- coding:utf-8 -*-

import os
import sys
from scrapy.cmdline import execute
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
start = time.time()
execute('scrapy crawl startspider'.split())
print(time.time() - start)
