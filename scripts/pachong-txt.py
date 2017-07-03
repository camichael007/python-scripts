#!/usr/bin/env python

import urllib, urllib2
import re


def getHtml(url):
    html = urllib2.urlopen(url)
    return html.read()


def getImage(html):
    re_img = re.compile(r'<img\ssrc=".*?"\sclass="lazy"\sd-src="\/\/(.*?)"\s.*">')
    img_list = re_img.findall(html)
    i = 1
    for img in img_list:
        img = 'http://' + img
        print img
        urllib.urlretrieve(img, filename='%s.jpg' % i)
        i += 1


if __name__ == '__main__':
    url = 'http://www.juanpi.com'
    html = getHtml(url)
    getImage(html)