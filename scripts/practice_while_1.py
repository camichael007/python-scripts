#!/usr/bin/python

x = ''
while x != 'q':
	print 'hello'
	x = raw_input('please input something ,q for quit: ')
	if not x:
		break
	if x == 'quit':
		continue
	print 'continue'
else:
	print 'world'
