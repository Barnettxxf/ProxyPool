# -*- coding:utf-8 -*-
import os
import math
from PIL import Image
import hashlib
import string


class VectorCompare():
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


def buildvector(im):
    d1 = {}

    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1


v = VectorCompare()

iconset = []
for i in string.digits:
    iconset.append(i)

imageset = []

for letter in iconset:
    for img in os.listdir('./iconset/%s' % letter):
        temp = []
        if '.png' in img:
            temp.append(buildvector(Image.open('./iconset/%s/%s' % (letter, img))))
        imageset.append({letter: temp})
# print(imageset)

def guess(image):
    im = Image.open(image)
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
    port = ''
    count = 0
    for letter in letters:
        m = hashlib.md5()
        im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))

        guess = []
        for image in imageset:
            for x, y in image.items():
                if len(y) != 0:
                    guess.append((v.relation(y[0], buildvector(im3)), x))
        guess.sort(reverse=True)
        # print('', guess[0])
        count += 1
        port += guess[0][1]
    print('guess port', port)
    return port


if __name__ == '__main__':
    guess('/home/barnett/Python/ProxyFecth/example/53281.jpg')
