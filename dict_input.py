#!/usr/bin/python
dic = {}
name = raw_input('Please input your name: ')
age = raw_input('Please input your age: ')
gender = raw_input('Please input your gender(M/F): ')
dic['name'] = name
dic['age'] = age
dic['gender'] = gender
for k, v in dic.items():
    print '%s: %s' % (k, v)
print 'done'
