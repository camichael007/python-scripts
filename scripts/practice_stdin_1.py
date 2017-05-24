#!/usr/bin/python
#coding:utf8

import sys
fd = sys.stdin
print type(fd)
data = fd.read()
print type(data)
sys.stdout.write(data)

