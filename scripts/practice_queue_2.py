#!/usr/bin/env python
#coding:utf8

import threading
import random
import Queue
import time

class Consumer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        while True:
            data = self.queue.get()
            if data == None:
                break
            print self.name, data, time.ctime()
            time.sleep(1)

if __name__ == '__main__':
    queue = Queue.Queue(10)
    for i in xrange(3):
        c = Consumer(queue)
        c.start()
    for i in xrange(10):
        queue.put(random.randint(1,9))

    queue.put(None)
    queue.put(None)
    queue.put(None)
