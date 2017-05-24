#!/usr/bin/env python

import threading
import time, os

def func():
    print 'hello', os.getpid(), os.getppid(), time.ctime()
    time.sleep(1)

if __name__ == '__main__':
    for i in xrange(10):
        t = threading.Thread(target=func, args=())
        t.start()
        
print 'end!!!'
