# -*- coding:utf-8 -*-
import sys
import os
import requests
from utils.captcha_identify import guess
from urllib.parse import urljoin

DIRNAME = 'image'
IMGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), DIRNAME)
BASEURL = 'https://proxy.mimvp.com/'

def pipline(item):
    port_list = guess_img(item['port_img_url'][0], item['ip'][0])


def guess_img(img_url, ip):
    if not os.path.exists(IMGDIR):
        os.mkdir(IMGDIR)
    img_name = IMGDIR + ip + '-' + '.png'
    headers = {'User-Agent': ''}
    response = requests.get(urljoin(BASEURL, img_url), headers=headers)
    with open(img_name, 'wb') as f:
        f.write(response.content)

    return guess(img_name)


