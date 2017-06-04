#!/usr/bin/python

with open('/tmp/test.txt', 'r') as fd:
	while True:
		line = fd.readline()
		if not line:
			break
		print line,
