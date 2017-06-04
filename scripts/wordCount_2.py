#!/usr/bin/python

import sys
import os

try:
	fn = sys.argv[1]
except IndexError:
	print 'Please follow an argument at %s' %sys.argv[0]
	sys.exit()
if not os.path.exists(fn):
	print '%s is not exist,try another' %fn
	sys.exit()
fd = open(fn)
data = fd.read()
chars = len(data)
words = len(data.split())
lines = data.count('\n')

print '%(lines)s %(words)s %(chars)s' %locals()
