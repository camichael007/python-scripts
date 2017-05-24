#!/usr/bin/python
import socket
import time
import tab

HOST = '192.168.14.131'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = raw_input('Please input a command: ')
    if cmd.lower() == 'exit' or cmd.lower() == 'quit':
        break
    if cmd.strip():
        s.sendall(cmd.strip())
        data = s.recv(1024)
        print data

s.close()
