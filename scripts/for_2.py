#!/usr/bin/python

for i in xrange(1, 10):
    for j in xrange(1, i+1):
        print '%s x %s = %s' % (j, i , j*i),
    print
