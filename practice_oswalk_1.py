#!/usr/bin/python

import sys, os
import practice_hashlib_1

a = os.walk(sys.argv[1])
for r, d, f in a:
	for i in f:
		print 'file:%s md5sum:%s' % (os.path.join(r, i), practice_hashlib_1.md5sum(os.path.join(r, i)))

