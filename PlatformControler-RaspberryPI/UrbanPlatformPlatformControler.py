import smbus2
import time

bus = smbus2.SMBus(1)

def SendToArd(message, arduAddress):
    for c in list(message):
        # send data
        bus.write_byte(arduAddress,c)
        print(bus.read_byte(arduAddress))

while True:
    SendToArd("test", 4);
    print("sent");
    time.sleep(3);