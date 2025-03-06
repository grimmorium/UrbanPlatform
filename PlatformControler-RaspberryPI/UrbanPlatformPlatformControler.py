import socket
import smbus2
import time

S1 = -1
S2 = -1
S3 = -1
S4 = -1
S5 = -1
S6 = -1
DC1 = -1
DC2 = -1

bus = smbus2.SMBus(1)
time.sleep(1)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

def SendToArd_block(message, arduAddress):
    # send data
    bus.write_i2c_block_data(arduAddress,0,list(message))

while True:
    
    message, address = server_socket.recvfrom(1024)
    message = message.upper()
    message_str = str(message)
    print("from GUI:" + message_str)
    server_socket.sendto(message, address)
    
    print(message_str[0:1])
    print(message_str[1:2])
    print(message_str[2:3])
    print(message_str[3:4])
    print(message_str[4:5])
    print(message_str[5:6])
    print(message_str[6:7])
    print(message_str[7:8])
    print(message_str[8:9])
    print(message_str[9:10])
    
    
    i=5
    msg = [ord('<'),ord('S'),i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,ord('>')]
    
    SendToArd_block(msg, 4)
    print("sent")
    
    
