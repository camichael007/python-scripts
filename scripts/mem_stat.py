#!/usr/bin/env python
#coding:utf8
with open('/proc/meminfo') as fd:
    for line in fd:
        if line.startswith('MemTotal'):
            total = line.split()[1]
            continue
        if line.startswith('MemFree'):
            free = line.split()[1]
            break
            
print '内存总数：%.2f MB' %(int(total)/1024.0)
print '剩余内存数：%.2f MB' %(int(free)/1024.0)