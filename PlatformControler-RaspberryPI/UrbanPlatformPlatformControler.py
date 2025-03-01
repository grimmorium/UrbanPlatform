import smbus2
import time

bus = smbus2.SMBus(1)

def SendToArd(message, arduAddress):
    for c in list(message):
        # send data
        bus.write_byte(arduAddress,c)
        cr = bus.read_byte(arduAddress)
        print(cr + " - " + str(cr))
i=0
while True:
    i=i+1
    
    SendToArd([i], 4);
    print("sent");
    time.sleep(0.1);