#/usr/bin/env python

import urllib, urllib2
import re



def getHtml(url):
    try:
        req = urllib2.Request(url, headers=headers)
        html = urllib2.urlopen(req)
        return html.read()
        #data = html.read()
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print e.code
        if hasattr(e, 'reason'):
            print e.reason
            
def parseHtml(html):
    re_pattern = re.compile(r'<div class="author.*?alt="(.*?)".*?<div class="content".*?<span>(.*?)</span>', re.S)
    items = re_pattern.findall(html)
    return items

def 


if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/'
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
    html = getHtml(url)
    section = parseHtml(html)
    for item in section:
        for i in item:
            print i.replace("<br/>","")
     



