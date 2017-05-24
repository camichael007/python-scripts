#!/usr/bin/env  python

import time
import random
import threading
import Queue

def producer(name, queue):
    for i in xrange(10):
        num = random.randint(1, 10)
        thread_name = threading.currentThread().getName() + '-' + name
        print '%s: %s ---> %s' % (time.ctime(), thread_name, num)
        queue.put(num)
        time.sleep(1)

def getOdd(name, queue):
    thread_name = threading.currentThread().getName() + '-' + name
    while True:
        try:
            val_odd = queue.get(1, 5)
            if val_odd % 2 != 0:
                print '%s: %s ---> %s' % (time.ctime(), thread_name, val_odd)
                time.sleep(1)
            else:
                queue.put(val_odd)
                time.sleep(1)
        except:
            print '%s: %s ---> finished' % (time.ctime(), thread_name)
            break
      
def getEven(name, queue):
    thread_name = threading.currentThread().getName() + '-' + name
    while True:
        try:
            val_even = queue.get(1, 5)
            if val_even % 2 == 0:
                print '%s: %s ---> %s' % (time.ctime(), thread_name, val_even)
                time.sleep(1)
            else:
                queue.put(val_even)
                time.sleep(1)
        except:
            print '%s: %s ---> finished' % (time.ctime(), thread_name)
            break

def main():
    queue = Queue.Queue(10)
    t_pro = threading.Thread(target=producer, args=('producer', queue))
    t_odd = threading.Thread(target=getOdd, args=('odd', queue))
    t_even = threading.Thread(target=getEven, args=('even', queue))
    t_pro.start()
    t_odd.start()
    t_even.start() 

if __name__ == '__main__':
    main()
