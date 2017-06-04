#!/usr/bin/env python

import multiprocessing
import os,time

def runTask(id):
    print 'running task id:%s,  pid:%s,  ppid:%s' % (id, os.getpid(), os.getppid())
    time.sleep(1)

if __name__ == '__main__':
    print 'parent process %s' %os.getpid()
    pool = multiprocessing.Pool(processes=2)
    for i in xrange(5):
        pool.apply_async(func=runTask, args=(i,))
    print 'wait'
    pool.close()
    pool.join()
    print 'done'
