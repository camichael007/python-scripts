#!/usr/bin/python
#coding:utf8

from subprocess import Popen,PIPE

p = Popen('./test.sh', shell=True)
p.wait()
print 'main process'
