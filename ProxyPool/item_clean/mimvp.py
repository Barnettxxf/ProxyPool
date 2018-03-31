# -*- coding:utf-8 -*-
import sys
import os
import requests
from utils.captcha_identify import guess

DIRNAME = 'image'
IMGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), DIRNAME)


def pipline(item):

    item['port'] = guess_img(item['port_img_url'], item['ip'])


def guess_img(img_url, ip):
    if not os.path.exists(IMGDIR):
        os.mkdir(IMGDIR)
    img_name = IMGDIR + ip + '-' + '.png'
    headers = {'User-Agent': ''}
    response = requests.get(img_url, headers=headers)
    with open(img_name, 'wb') as f:
        f.write(response.content)

    return guess(img_name)


