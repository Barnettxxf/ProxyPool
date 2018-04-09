# -*- coding:utf-8 -*-
import datetime
import re
from scrapy.exceptions import DropItem


def pipline(item):

    # 通常的代理速度字段清理
    if len(item['speed']) != 0 and isinstance(item['speed'], list):
        if '秒' in item['speed'][0]:
            item['speed'] = item['speed'][0].split('秒')[0].strip()
        if 'ms' in item['speed'][0]:
            item['speed'] = int(item['speed'][0].split('ms')[0].strip()) / 1000

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
    now_time = datetime.datetime.now()
    if '分钟' in time_text:
        dig = int(re.search('(.*?)(分钟前|分钟)', time_text).group(1))
        yes_time = now_time + datetime.timedelta(minutes=-dig)
    elif 'minutes' in time_text:
        dig = int(re.search('(.*?)(minutes|minutes ago)', time_text).group(1))
        yes_time = now_time + datetime.timedelta(minutes=-dig)
    elif '秒' in time_text:
        dig = int(re.search('(.*?)(秒前|秒)', time_text).group(1))
        yes_time = now_time + datetime.timedelta(seconds=-dig)
    elif 'seconds' in time_text:
        dig = int(re.search('(.*?)(seconds|seconds ago)', time_text).group(1))
        yes_time = now_time + datetime.timedelta(seconds=-dig)
    elif '小时' in time_text:
        dig = int(re.search('(.*?)(小时前|小时)', time_text).group(1))
        yes_time = now_time + datetime.timedelta(hours=-dig)
    elif '天' in time_text:
        dig = int(re.search('(.*?)(天前|天)', time_text).group(1))
        yes_time = now_time + datetime.timedelta(days=-dig)
    elif '验证时间' in time_text:
        raise DropItem
    else:
        return time_text
    yes_time = str(yes_time).split('.')[0]
    return yes_time


if __name__ == '__main__':
    text = '59seconds'
    dig = parse_time(text)
    print(dig)
