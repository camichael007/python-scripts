#!/usr/bin/python

class People(object):
	color = 'yellow'
	__age = 23 

	class Chinese(object):
		name = 'I am chinese'

	def think(self):
		self.color = 'white'
		print 'I am a %s' %self.color
		print 'I am a thinker'
		print self.__age

	@classmethod
	def test(self):
		print 'this is a classmethod,it works!!!'

	@staticmethod
	def test1():
		print 'this is a staticmethod,it works !!!'

print People.Chinese.name
