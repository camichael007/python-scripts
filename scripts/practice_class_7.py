#!/usr/bin/python
#coding:utf8

class MyClass(object):
	var1 = '类属性，类的公有属性 var1'
	__var2 = '类的私有属性 __var2'

	def func1(self):
		self.var3 = '对象的公有属性 var3'
		self.__var4 = '对象的私有属性 __var4'
		var5 = '函数的局部变量 var5'

mc = MyClass()
mc.func1()
print mc.var1
print mc.var3
print mc.__var4
