# -*- coding:utf-8 -*-

import os
import sys
from scrapy.cmdline import execute

from model import engine, Base

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

Base.metadata.create_all(engine)

execute('scrapy crawl proxypool'.split())