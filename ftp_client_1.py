#!/usr/bin/python
import socket
import time
import tab
import os

HOST = '192.168.14.131'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = raw_input('Please input a command: ').strip()
    if cmd.lower() == 'exit' or cmd.lower() == 'quit':
        break
    cmd_list = cmd.split()
    if len(cmd_list) != 3:
        print 'Example: get file1(local) file2(remote)'
        continue
    else:
        s.sendall(cmd)
        if not os.path.exists(cmd_list[2]):
            dest_file = cmd_list[2]
        else:
            dest_file = cmd_list[2]+'.new'
        n = 1
        while True:
            data_rev = s.recv(1024)
            if data_rev[-3:] == 'EOF':
                data = data_rev[:-3]
            else:
                data = data_rev
            if n == 1:
                with open(dest_file, 'w') as fd:
                    fd.write(data)
                    print data
            else:
                with open(dest_file, 'a') as fd:
                    fd.write(data)
                    print data
            n += 1
            if data_rev[-3:] == 'EOF':
                break

s.close()
