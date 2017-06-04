#!/usr/bin/python
#coding:utf8

import thread
import time

def func(name, i, lock):
    for n in xrange(i):
        print name, n
        time.sleep(1)
    lock.release()

lock = thread.allocate_lock()
lock.acquire()
thread.start_new_thread(func, ('画面', 3, lock))
thread.start_new_thread(func, ('声音', 3, lock))

while lock.locked():
    pass
