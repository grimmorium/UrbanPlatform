import socket
import smbus2
import time

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
    
    print("from GUI:" + str(message))
    server_socket.sendto(message, address)
    
    i=5
    msg = [ord('<'),ord('S'),i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,ord('>')]
    
    SendToArd_block(msg, 4)
    print("sent" +  msg)
    
    
