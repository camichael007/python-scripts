#!/usr/bin/python
#coding:utf8

import sys, os
import hashlib

def md5sum(f):
    m = hashlib.md5()                                      ##实例化对象
    with open(f) as fd:
        while True:
            data = fd.read(4096)                          ##循环一次读取4096个字节
            if data:
                m.update(data)                               ##将所有的字节读取完毕
            else:
                break
    return m.hexdigest()                                   ##函数返回16进制的hash值

def file_md5sum(dir):
    dic = {}
    for r, d, f in os.walk(dir):
        for i in f:
            fn = os.path.join(r, i)
            md5 = md5sum(fn)
            if dic.has_key(md5):
                dic[md5].append(fn)
            else:
                dic[md5] = [fn]
            return dic

if __name__ == '__main__':
    dic = file_md5sum(sys.argv[1])
    for k, v in dic.items():
    #   if len(v) > 1:
        print k, v
	
