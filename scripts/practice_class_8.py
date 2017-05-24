#!/usr/bin/python
#coding:utf8

class MyClass(object):
	name = 'Test'

	def __init__(self):
		print '我是内置方法__init__'
		self.func1()
		self.__func2()
		self.classFun()
		self.staticFun()

	def func1(self):
		print self.name,
		print '我是公有方法'
#		self.__func2()

	def __func2(self):
		print self.name,
		print '我是私有方法'

	@classmethod
	def classFun(self):
		print self.name,
		print '我是类方法'

	@staticmethod
	def staticFun():
		print MyClass.name,
		print '我是静态方法'

mc = MyClass()
