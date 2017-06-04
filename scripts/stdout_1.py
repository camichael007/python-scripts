#!/usr/bin/env python
#coding:utf8

import sys

f = open('/tmp/test1.txt', 'w')
f.read()
f.close()
with open('/tmp/test.txt', 'a') as f:
    f.write('alskjdflja\n')

