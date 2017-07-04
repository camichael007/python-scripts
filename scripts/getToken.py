#/usr/bin/env python

import urllib, urllib2
import requests
import re



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}

session = requests.session()
params = {
    'language':"-1",
    'style':"-1",
    'df':"mail163_letter",
    'from':"web",
    'allssl':"false",
    'race':"618_621_-2_gz",
    'net':"c",
    'iframe':"1",
    'product':"mail163",
    'url2':"http://mail.163.com/errorpage/error163.htm",
    'savelogin':'1',
    'passtype':'1',
    'funcid':'loginone',
    
}

data = {
    'username':'stalena@163.com',
    'password':'cristiana2010',
    
}
url = 'https://mail.163.com/entry/cgi/ntesdoor?'
login = session.post(url=url, data=data, headers=headers, params=params)

re_sid = re.compile(r'href = "(.*?)"')
sid = re_url.findall(login.text)
print type(sid)
#r = session.get('http://global.163.com/urs/redirect.html?target=http://www.kaola.com/indexIframe.html?__da_gv3kdY_HssOaY&sid='+ sid+'&uid=stalena@163.com&host=mail.163.com&ver=js6&fontface=yahei&style=1&skin=skyblue&color=064977')