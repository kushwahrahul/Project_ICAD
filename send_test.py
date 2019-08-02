
import can
can.rc['interface'] = 'socketcan_ctypes'

from threading import Thread,Lock
from time import sleep

from can.interfaces.interface import Bus
from can import Message

def main():
   data = 0x10 
   while(1):
        can_interface = 'can1'
        bus = Bus(can_interface)

        print "Sending a message..."
        Message.extended_id = False
        Message.is_remote_frame = False
        Message.id_type = 1
        Message.is_error_frame = False
        Message.arbitration_id = 0x01
        Message.dlc = 1

        Message.data = [data]
        try:
            bus.send(Message);
            print (Message.data)
            sleep(2)
        except:
            print ("Ups something went wrong!")
        sleep(0.1)


if __name__=="__main__":
    main()
