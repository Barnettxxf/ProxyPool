# -*- coding:utf-8 -*-
import datetime
import re


def pipline(item):
    ip_list_text = item['ip']
    item['ip'] = parse_ip_list_text(ip_list_text)
    item['port'] = re.search('>(\d+)</span>', item['port'][-1]).group(1)
    item['lastcheck'] = parse_date_time(item['lastcheck'][0])
    if len(item['speed']) != 0:
        item['speed'] = item['speed'][0].split('秒')[0].strip()

    for key in item:
        if isinstance(item[key], list) and len(item[key]) != 0:
            item[key] = item[key][0]
        elif isinstance(item[key], list) and len(item[key]) == 0:
            item[key] = ''
        else:
            pass


def parse_ip_list_text(ip_list_text):
    li = ip_list_text
    re_1 = re.compile('<span>(.+)</span>')
    re_2 = re.compile('inline-block;">(.+)</')
    ip = ''
    for each in li:
        if re_1.search(each):
            text = re_1.search(each).group(1)
        elif re_2.search(each):
            text = re_2.search(each).group(1)
        else:
            text = ''
        # print(text)
        ip += text
    # print('ip: ', ip)
    return ip


def parse_date_time(time_text):
    dig = int(re.search('(.)分钟前', time_text).group(1))
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(minutes=-dig)
    yes_time = str(yes_time).split('.')[0]
    return yes_time
