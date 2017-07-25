#/usr/bin/env python
#coding:utf8

import re
import sys, os
import commands

logdir = sys.argv[1]

def get_file(logdir):
    file_name = []
    files = os.walk(logdir)
    for file in list(files)[0][2]:
        if re.match(r".+?.py$",file):
            file_name.append(logdir + file)

    return file_name

if __name__ == "__main__":
    files = get_file(logdir)
    ip_cmd = "/sbin/ifconfig | grep inet | grep -v inet6 | grep -v '127.0.0.1' |grep '192.168'| awk '{print $2}' | awk -F ':' '{print $2}'"
    ip = commands.getoutput(ip_cmd)
    print ip