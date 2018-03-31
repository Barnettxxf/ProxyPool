# -*- coding:utf-8 -*-
import datetime
import re


def pipline(item):

    # 通常的代理速度字段清理
    if len(item['speed']) != 0 and isinstance(item['speed'], list) and '秒' in item['speed'][0]:
        item['speed'] = item['speed'][0].split('秒')[0].strip()

    if len(item['lastcheck']) != 0 and isinstance(item['lastcheck'], list):
        item['lastcheck'] = parse_time(item['lastcheck'][0])

    # 通常的代理校验时间字段清理
    for key in item:
        if isinstance(item[key], list) and len(item[key]) != 0:
            item[key] = item[key][0]
        elif isinstance(item[key], list) and len(item[key]) == 0:
            item[key] = ''
        else:
            pass


def parse_time(time_text):
    dig = int(re.search('(.*？)分钟前|分钟', time_text).group(1)) or \
          int(re.search('(.*？)minutes|minutes ago', time_text).group(1)) or \
          int(re.search('(.*？)秒前|秒', time_text).group(1)) or \
          int(re.search('(.*？)seconds|seconds ago', time_text).group(1))
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(minutes=-dig)
    yes_time = str(yes_time).split('.')[0]
    return yes_time


