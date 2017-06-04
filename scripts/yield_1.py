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
	for r, d, f in os.walk(dir):
		for i in f:
			fn = os.path.join(r, i)
			md5 = md5sum(fn)
			yield '%s %s' %(md5, fn)

if __name__ == '__main__':
	try:
		dir = sys.argv[1]
	except IndexError:
		print '%s follows an argument(directory)' %__file__
	generator = file_md5sum(dir)
	for i in generator:
		print i
	
	
