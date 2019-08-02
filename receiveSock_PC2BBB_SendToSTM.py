#can import 
import can

#socket import 
import socket
import os
import subprocess

can.rc['interface'] = 'socketcan_ctypes'
 
from can.interfaces.interface import Bus
from can import Message
 
def main():

    s = socket.socket()
    host = '192.168.7.1'
    port = 9999
    s.connect((host, port))
    can_interface = 'can0'
    bus = Bus(can_interface)
 
 
    print "Send a message..."
    Message.extended_id = True
    Message.is_remote_frame = False
    Message.id_type = 1
    Message.is_error_frame = False
    Message.arbitration_id = 0x65D
    Message.dlc = 1
    Message.data = [ 0x01]
    while True :
        data = s.recv(1024)
        if data == 'quit':
            s.close()
        print(data[:].decode("utf-8"))
        if data == 'true' :
            try:
                bus.send(Message);
                print("msg sent")
                data =='false'
            except:
                print "Ups something went wrong!"
        if data == 'true' :
            try:
                bus.send(Message);
                print("msg sent")
                data =='false'
            except:
                print "Ups something went wrong!"
 
if __name__ == "__main__":
   main()


