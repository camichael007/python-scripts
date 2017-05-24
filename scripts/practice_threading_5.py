#!/usr/bin/env  python

import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global counter
        time.sleep(1)
        mutex.acquire()
        counter += 1
        print 'I am %s, set counter: %s' % (self.name, counter)
        mutex.release()

if __name__ == '__main__':
    counter = 0
    mutex = threading.Lock()
    for i in xrange(200):
        t = MyThread()
        t.start()
