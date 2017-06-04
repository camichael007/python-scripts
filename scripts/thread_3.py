#!/usr/bin/env python
#coding:utf8

import thread

h_lock = thread.allocate_lock()
w_lock = thread.allocate_lock()
m_lock = thread.allocate_lock()
w_lock.acquire()
m_lock.acquire()
def printHello():
    for i in xrange(5):
        if h_lock.acquire():
            print 'hello',
            w_lock.release()

def printWorld():
    for i in xrange(5):
        if w_lock.acquire():
            print 'world'
            h_lock.release()
    m_lock.release()

thread.start_new_thread(printHello, ()) 
thread.start_new_thread(printWorld, ()) 

while m_lock.locked():
    pass
