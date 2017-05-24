#!/usr/bin/python
import time
import sys

for i in xrange(10):
	if i == 3:
		continue
	elif i == 4:
		time.sleep(3)
	elif i == 6:
		pass
	elif i == 7:
		sys.exit()
	print i
else:
	print 'main end'
print 'done'
