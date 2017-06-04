#!/usr/bin/python
#coding:utf8

from subprocess import Popen,PIPE
def getIfconfig():
    p = Popen(['ifconfig'], stdout=PIPE, stderr=PIPE)
    data = p.stdout.read().split('\n\n')
    return [i for i in data if i and not i.startswith('lo')]

def parseIfconfig(data):
    dic = {}
    for lines in data:
        line_list = lines.split('\n')
        devname = line_list[0].split()[0]
        macaddr = line_list[0].split()[-1]
        ipaddr = line_list[1].split()[1].split(':')[1]
        dic[devname] = [macaddr, ipaddr]
        return dic
if __name__ == '__main__':
    data = getIfconfig()
    print parseIfconfig(data)
    
