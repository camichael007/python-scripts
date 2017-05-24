#!/usr/bin/env python
#coding:utf8

import multiprocessing
import time, os

def func(i):
    print 'hello', i, os.getpid(), os.getppid()
    time.sleep(1)

for i in xrange(10):
    p = multiprocessing.Process(target=func, args=(i, ))
    p.start()
