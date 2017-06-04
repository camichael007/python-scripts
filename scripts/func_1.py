#!/usr/bin/python

def fun():
    sth = raw_input('please input a num: ')
    try:
        if type(int(sth)) == type(1):
            print '%s is a number' %sth
    except:
        print '%s is not a number' %sth
if __name__ == '__main__':
    fun()

