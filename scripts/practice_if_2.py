#!/usr/bin/python
yn = raw_input('please input [yes/no]: ')
yn = yn.lower()
if yn == 'y' or yn == 'yes':
	print 'program is running'
elif yn == 'n' or yn == 'no':
	print 'program is exist'
else:
	print 'please input [yes/no]'

