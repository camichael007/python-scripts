#!/usr/bin/python

fd = open('/tmp/test.txt', 'r')
for line in fd:
    print line,
fd.close
