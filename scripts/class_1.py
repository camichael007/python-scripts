#!/usr/bin/python
#coding:utf8

class People(object):
    __age = 23
    def Think(self):
        self.color = 'white'
        print 'I am a %s' %self.color
        print 'I am a thinker'
        print self.__age


ren = People()
ren.Think()

ren.color = '白色人'
print ren.__dict__
print '#' * 30
print People.__dict__

# print People.color
# print ren.color
# print ren.__age
# ren.Think()
