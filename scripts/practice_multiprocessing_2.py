#!/usr/bin/env python
#coding:utf8

import multiprocessing
import time, os

def func():
    while 1:
        1 + 1

for i in xrange(100):
    p = multiprocessing.Process(target=func, args=( ))
    p.start()
