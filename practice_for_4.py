#!/usr/bin/python
import random

num_random = random.randint(1, 20)

for i in xrange(1, 7):
	num = input('please input a num range in 1--20: ')
	if num > num_random:
		print '%s is bigger, try again' % num
		continue
	elif num < num_random:
		print '%s is smaller, try again' % num
		continue
	else: 
		print 'bingo, you are right'
		break
else:
	print 'run this game again'
	
