#!/usr/bin/python
#coding:utf8

import hashlib
import sys

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

if __name__ == '__main__':
    try:                                                             ##针对sys.argv做异常处理
        print md5sum(sys.argv[1])
    except IndexError:
        print '%s should follow an argumemt' %__file__

