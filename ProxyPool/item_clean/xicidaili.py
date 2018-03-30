# -*- coding:utf-8 -*-


def pipline(item):
    # 解析得到的字段都是(空)列表来的
    if len(item['speed']) != 0:
        item['speed'] = item['speed'][0].split('秒')[0]
    if len(item['lastcheck']) != 0:
        if not item['lastcheck'][0].startswith('20'):
            item['lastcheck'] = '20' + item['lastcheck'][0]

    for key in item:
        if isinstance(item[key], list) and len(item[key]) != 0:
            item[key] = item[key][0]
        elif isinstance(item[key], list) and len(item[key]) == 0:
            item[key] = ''
        else:
            pass
