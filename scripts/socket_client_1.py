#!/usr/bin/python
import socket
import time

HOST = '192.168.14.131'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    s.sendall('Hello, world')
    data = s.recv(1024)
    print data
    time.sleep(1)

s.close()
