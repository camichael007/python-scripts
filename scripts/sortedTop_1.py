#!/usr/bin/python

import os, sys
import operator

def get_dic(topdir):
    dic = {}
    a = os.walk(topdir)
    for r, d, f in a:
        for i in f:
            fn = os.path.join(r, i)
            size = os.path.getsize(fn)
            dic[fn] = size
        sort = sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]
    return sort

if __name__ == '__main__':
    for k, v in get_dic(sys.argv[1]):
        print 'filename:%-60s size:%10sKB' % (k, v)
