#!/usr/bin/python

class People(object):
	color = 'yellow'
	__age = 23 

	class Chinese(object):
		name = 'I am chinese'

	def __str__(self):
		return 'This is a People class'

	def __init__(self,c='yellow'):
		print 'Init start ...'
		self.color = c
		self.think()

	def think(self):
		self.color = 'white'
		print 'I am a %s' %self.color
		print 'I am a thinker'
		print self.__age

	def __del__(self):
		print 'Delete start...'

	@classmethod
	def test(self):
		print 'this is a classmethod,it works!!!'

	@staticmethod
	def test1():
		print 'this is a staticmethod,it works !!!'

print 'Main function start...'
jacky = People()
print jacky
print 'Main function stop...'
