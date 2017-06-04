#!/usr/bin/env python

import multiprocessing
from subprocess import Popen, PIPE

def run(id):
    p = Popen(['vim'], stdout=PIPE, stderr=PIPE)
    p.communicate()
    print 'task: %s' %id

pool = multiprocessing.Pool()
for i in xrange(5):
    pool.apply_async(func=run, args=(i,))

print 'wait'
pool.close()
pool.join()
print 'done'
