#!/usr/bin/python

class People(object):
	color = 'yellow'
	__age = 23
	def Think(self):
		self.color = 'white'
		print 'I am a %s' %self.color
		print 'I am a thinker'
		print self.__age
ren = People()
print ren.color
ren.Think()
