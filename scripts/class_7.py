#!/usr/bin/python
#coding:utf8

class MyClass(object):
    var1 = '类属性，类的公有属性 var1'
    __var2 = '类的私有属性 __var2'

    def func1(self):
        self.var3 = '对象的公有属性 var3'
        self.__var4 = '对象的私有属性 __var4'
        global var5
        var5 = '函数的局部变量 var5'
    
    def func2(self):
        print self.var1
        #print self.var3
        print self.__var2
        print self.__var4
        print var5

#print MyClass.var1
#print MyClass.__var2
#print MyClass.var3
#print MyClass.__var4
#print MyClass.var5


mc = MyClass()
mc.func1()
mc.func2()
# print mc.var1
#
# print mc.__var2
# print mc.var3
# print mc.__var4
# print var5
