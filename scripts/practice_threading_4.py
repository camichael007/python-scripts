#!/usr/bin/env python
#coding:utf8

import threading
import time

def printHello():
    for i in xrange(5):
        if h_lock.acquire():
            print 'hello',
            w_lock.release()

def printWorld():
    for i in xrange(5):
        if w_lock.acquire():
            print 'world', time.ctime()
            h_lock.release()

h_lock = threading.Lock()
w_lock = threading.Lock()
w_lock.acquire()
t1 = threading.Thread(target=printHello, args=())
t2 = threading.Thread(target=printWorld, args=())

if __name__ == '__main__':
    t1.start()
    t2.start()
