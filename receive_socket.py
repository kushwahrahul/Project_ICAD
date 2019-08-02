import socket
import os
import subprocess

s = socket.socket()
host = '192.168.7.1'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    print(data[:].decode("utf-8"))
    if data == 'quit':
        s.close()
    if data == 'true':
        print("CAN  CODE INITATED")
         
