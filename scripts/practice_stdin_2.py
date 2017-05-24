#!/sur/bin/env python
#coding:utf8

import sys

def lineCount(fd):
	n = 0
	for i in fd:
		n += 1
	return n

fd = sys.stdin
print lineCount(fd)
	
