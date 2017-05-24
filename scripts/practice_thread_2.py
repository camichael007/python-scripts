#!/usr/bin/env python

import thread
import time

def printWorld():
    for i in xrange(5):
        if w_lock.acquire():
            print 'world'
            h_lock.release()

h_lock = thread.allocate_lock()
w_lock = thread.allocate_lock()
thread.start_new_thread(printWorld, ())
w_lock.acquire()
for i in xrange(5):
    if h_lock.acquire():
        print 'hello',
        w_lock.release()
time.sleep(1)
