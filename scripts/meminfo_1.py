#!/usr/bin/python
#coding:utf8

import sys
from subprocess import Popen,PIPE

def getPid(proc):
    process = proc
    p = Popen(['pidof',process], stdout=PIPE, stderr=PIPE)
    pids = p.stdout.read().split()
    return pids

if __name__ == '__main__':
    print getPid(sys.argv[1])

