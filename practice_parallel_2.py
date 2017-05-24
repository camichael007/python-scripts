#!/usr/bin/env python

import paramiko
import threading
import sys

def dsh(ip, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip, username='root', password='123456', timeout=5)
    except:
        print '%s: Timeout or not permitted' %ip
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdout = stdout.read()[:-1]
    stderr = stderr.read()[:-1]
    if stdout:
        print '%s: \t %s' % (ip, stdout)
        ssh.close()
    else:
        print '%s: \t %s' % (ip, stderr)
        ssh.close()

if __name__ == '__main__':
    ips = ['192.168.14.128','127.0.0.1']
    try:
        cmd = sys.argv[1]
    except IndexError:
        print '%s follows an argument' %__file__
        sys.exit(1)
    for ip in ips:
        t = threading.Thread(target=dsh, args=(ip, cmd))
        t.start()
        
    
