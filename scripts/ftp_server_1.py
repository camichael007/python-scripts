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
    cmd_list = cmd.split()
    if cmd_list[0] == 'get':
        with open(cmd_list[1]) as fd:
            while True:
                data = fd.read(1024)
                conn.sendall(data)
                if not data:
                    conn.sendall('EOF')
                    break
    if not cmd: break
conn.close()
