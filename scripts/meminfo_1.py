#!/usr/bin/python
#coding:utf8

import sys, os
from subprocess import Popen,PIPE

def getPid(proc):
    process = proc
    p = Popen(['pidof',process], stdout=PIPE, stderr=PIPE)
    pids = p.stdout.read().split()
    return pids

def parsePid(pids):
    total_mem = 0
    for i in pids:
        fn = os.path.join('/proc',i ,'status')
        with open(fn) as fd:
            for line in fd:
                if line.startswith('VmRSS'):
                    mem = int(line.split()[1])
                    total_mem += mem
                    break
    return total_mem

if __name__ == '__main__':
    pids = getPid(sys.argv[1])
    total_mem = parsePid(pids)
    print 'process: %s, memory: %s MB' %(sys.argv[1], (total_mem/1000.0))
