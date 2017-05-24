#!/usr/bin/python
#coding:utf8

class People(object):
	color = 'yellow'
	
	def __init__(self):
		self.home = 'Earth'

	def think(self):
		print 'I am a %s' %self.color
		print 'I live on %s' %self.home

class Martian(object):
    color = 'red'

    def __init__(self):
        self.home = 'Mar'

    def think(self):
        print 'I am a %s' %self.color
        print 'I live on %s' %self.home
 
class Chinese(Martian, People):
	def __init__(self):
#		super(Chinese, self).__init__()
		People.__init__(self)

cn = Chinese()
cn.think()
