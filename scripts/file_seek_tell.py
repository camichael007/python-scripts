#/usr/bin/env python
#coding:utf8

import os
import re
import sys
import json

LOGDIR = '/vagrant_data/python-scripts/scripts/'

def get_file(logdir):
    files_name = []

    for dirpath, subpath, files in os.walk(logdir):
        for file in files:
            if re.match(r".+?.py$",file):
                files_name.append(LOGDIR + file)

    return files_name

def get_file_end(logfile):
    f = open(logfile,'r')
    f.seek(0,2)
    file_end = f.tell()
    f.close()
    return file_end




if __name__ == '__main__':
    files_name = get_file(LOGDIR)
    endpoint = {}
    for file in files_name:
        endpoint[file] = get_file_end(file)

    for domain in endpoint:
        print domain

    
    with open('/tmp/endpoint.log','w') as f:
        f.write(json.dumps(endpoint))

        
