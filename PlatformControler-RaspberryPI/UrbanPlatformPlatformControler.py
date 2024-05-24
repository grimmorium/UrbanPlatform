import socket

import smbus
import time
import sys

bus = smbus.SMBus(1)
arduAddress = 0x04              # Arduino I2C Address

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

i2cData = False


while True:
    message, address = server_socket.recvfrom(1024)
    message = message.upper()
    
    print("from GUI:" + str(message))
    
    # send data
    i2cData = not i2cData
    bus.write_byte(arduAddress,i2cData)
    # request data
    print ("Arduino answer to RPi:", bus.read_byte(arduAddress))
        
    #time.sleep(1)
    
    print(message)

    server_socket.sendto(message, address)
