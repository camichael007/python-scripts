#!/usr/bin/python

class People(object):
	color = 'yellow'
	__age = 23 

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

People.test()
People.test1()
