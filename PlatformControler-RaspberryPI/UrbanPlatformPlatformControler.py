import socket

import smbus
import time
import sys

bus = smbus.SMBus(1)
arduAddress1 = 0x04              # Arduino I2C Addresses
arduAddress2 = 0x05
arduAddress3 = 0x06

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

i2cData = 25


while True:
    message, address = server_socket.recvfrom(1024)
    message = message.upper()
    
    print("from GUI:" + str(message))
    
    for c in list(message):
        # send data
        #i2cData = not i2cData
        bus.write_byte(arduAddress1,c)
        print ("Arduino answer to RPi:", bus.read_byte(arduAddress1))
        # request data
    #print ("Arduino answer to RPi:", bus.read_byte(arduAddress1))
    #time.sleep(1)
    print(message)

    server_socket.sendto(message, address)
