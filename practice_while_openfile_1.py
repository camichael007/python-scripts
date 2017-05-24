#!/usr/bin/python

fd = open('/tmp/test.txt', 'r')
while True:
	line = fd.readline()
	if not line:
		break
	print line,
fd.close()
