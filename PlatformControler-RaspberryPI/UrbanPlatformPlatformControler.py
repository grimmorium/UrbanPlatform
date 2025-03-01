import smbus2
import time

bus = smbus2.SMBus(1)

def SendToArd(message, arduAddress):
    for c in list(message):
        # send data
        bus.write_byte(arduAddress,c)
        cr = bus.read_byte(arduAddress)
        print(str(cr) + " - " + chr(cr))

def SendToArd_block(message, arduAddress):
    # send data
    bus.write_i2c_block_data(arduAddress,0,list(message))
    cr = bus.read_byte(arduAddress)
    print(str(cr) + " - " + chr(cr))
        
i=0
#msg="just a test"
msg = [ord('j'),ord('u'),ord('s'),ord('t'),ord(' '),ord('a'),ord(' '),ord('t'),ord('e'),ord('s'),ord('t')]

while True:
    i=i+1
    
    SendToArd_block(msg, 4);
    print("sent");
    time.sleep(0.1);