#!/usr/bin/python
#coding:utf8

class People(object):
	color = 'yellow'
	
	def __init__(self, c):
		print 'Init ...'
		self.color = c

	def think(self):
		print 'I am a %s' %self.color

class Chinese(People):
	pass

cn = Chinese('red')
print People.color
print cn.color
cn.think()
