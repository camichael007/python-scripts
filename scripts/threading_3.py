#!/usr/bin/env python

import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = 'new_' + self.name

    def run(self):
        print 'my name is %s' %self.name

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
        time.sleep(1)
        
