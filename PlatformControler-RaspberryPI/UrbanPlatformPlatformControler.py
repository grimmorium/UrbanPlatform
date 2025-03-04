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
    cr = bus.read_i2c_block_data(arduAddress,0,11)
    #print(cr)
        
i=0
#msg="just a test"
msg = [ord('<'),ord('S'),1,2,3,4,5,6,7,ord('>')];

while True:
    i=i+5
    if i>255:
        i=0
        
    msg = [ord('<'),ord('S'),i,i,i,i,i,i,i,ord('>')]
    
    SendToArd_block(msg, 4)
    print("sent")
    time.sleep(0.1)