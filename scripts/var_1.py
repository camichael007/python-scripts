#!/usr/bin/python

x = 100

def fun():
	global x
	x += 1
	print x
	global y
	y = 2
	print locals()

fun()
print y
print locals()

