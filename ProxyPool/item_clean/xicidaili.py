# -*- coding:utf-8 -*-


def pipline(item):

    if len(item['lastcheck']) != 0:
        if not item['lastcheck'][0].startswith('20'):
            item['lastcheck'] = '20' + item['lastcheck'][0]

