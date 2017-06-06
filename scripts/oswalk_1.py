#!/usr/bin/python
#coding:utf8
##遍历目录下所有文件的MD5

import sys, os
import hashlib_1

a = os.walk(sys.argv[1])
for r, d, f in a:
    for i in f:
        print 'file:%s md5sum:%s' % (os.path.join(r, i), hashlib_1.md5sum(os.path.join(r, i)))

