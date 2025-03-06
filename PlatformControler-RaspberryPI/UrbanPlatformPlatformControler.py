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
    
    rideWalk = message_str[2:3] #ride / walk
    lowMidleHigh = message_str[3:4] #low / midle / high
    cross = message_str[4:5] #cross
    F1 = message_str[5:6] #F1
    F2 = message_str[6:7] #F2
    F3 = message_str[7:8] #F3
    
    print(rideWalk) #ride / walk
    print(lowMidleHigh) #low / midle / high
    print(cross) #cross
    print(F1) #F1
    print(F2) #F2
    print(F3) #F3

    rideWalkM=lowMidleHighM=1
    S1=S2=S3=S4=S5=S6=DC1=DC2=0
    
    if F3=="1":
        S1=5
    if F3=="2":
        S2=5
    if F3=="3":
        S3=5
    if F3=="4":
        S4=5
    if F3=="5":
        S5=5
    if F3=="6":
        S6=5
    
    if rideWalk=="W":
        rideWalkM = 2
    if lowMidleHigh=="M":
        lowMidleHighM = 2
    if lowMidleHigh=="H":
        lowMidleHighM = 5
    
    print("rideWalkM:" + str(rideWalkM))
    print("lowMidleHighM:" + str(lowMidleHighM))
    
    S1 = S1 * rideWalkM * lowMidleHighM
    S2 = S2 * rideWalkM * lowMidleHighM
    S3 = S3 * rideWalkM * lowMidleHighM
    S4 = S4 * rideWalkM * lowMidleHighM
    S5 = S5 * rideWalkM * lowMidleHighM
    S6 = S6 * rideWalkM * lowMidleHighM
    
    i=5
    msg = [ord('<'),ord('S'),S1,S2,S3,S4,S5,S6,DC1,DC2,ord('>')]
    
    SendToArd_block(msg, 4)
    print("sent")
    
    
