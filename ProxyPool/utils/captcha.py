# -*- coding:utf-8 -*-
import os
import math
from PIL import Image
import hashlib
import string

"""
用来切割port端口号的图片，分开每个数字存储为对应文件夹的图片,图片放在example文件夹，并将图片的数字（字母）给图片命名。
"""

example_path = os.getcwd() + os.sep + 'example/'
if not os.path.exists(example_path):
    os.mkdir('example')


def split_image(image_name):
    im = Image.open(example_path + image_name)
    im.convert('P')
    im2 = Image.new('P', im.size, 255)

    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y, x))
            # print(pix, end='|')
            if pix == 1:
                im2.putpixel((y, x), 0)
    # im2.show()
    inletter = False
    foundletter = False
    start = 0
    end = 0

    letters = []

    for y in range(im2.size[0]):
        for x in range(im2.size[1]):
            pix = im2.getpixel((y, x))
            # print(pix, end='|')
            if pix != 255:
                inletter = True
        if foundletter is False and inletter is True:
            foundletter = True
            start = y

        if foundletter is True and inletter is False:
            foundletter = False
            end = y
            letters.append((start, end))

        inletter = False
    # print(letters)

    count = 0
    name = example_path + '{}.png'
    for letter in letters:
        m = hashlib.md5()
        im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
        im3.save(name.format(jpg_name[count]))
        count += 1


if __name__ == '__main__':
    split_image('9999.jpg')
