#!/usr/bin/python

import sys

input = sys.stdin
data = input.read()
chars = len(data)
words = len(data.split())
lines = data.count('\n')

print '%(lines)s %(words)s %(chars)s' %locals()
print locals()
