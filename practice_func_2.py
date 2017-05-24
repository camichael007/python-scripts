#!/usr/bin/python

import sys
import os

def isNum(s):
	for i in s:
		if i in '0123456789':
			pass
		else:
			continue
	else:
		print '%s is a number' %s
for i in os.listdir('/proc'):
	isNum(i)
