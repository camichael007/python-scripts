#!/usr/bin/python
#coding:utf8

class FuncError(Exception):
    def __str__(self):
        return 'i am class FuncError'

def func():
    raise FuncError()

try:
    print '222'
    func()
except NameError, e:
    print e
    print '111'
except FuncError as e:
    print '222'
except Exception as e:
    print e
    print '333'
else:
    print 'no exception'
finally:
    print 'finally end'


