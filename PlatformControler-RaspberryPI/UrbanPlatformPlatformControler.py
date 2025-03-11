import socket
import smbus2
import time
from commandStore import ComandStore

i2cAddrA = 4
i2cAddrB = 5
i2cAddrC = 6

commands = ComandStore()

bus = smbus2.SMBus(1)
time.sleep(1)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))
server_socket.setblocking(False)

timeinterval = 1.0
nextTm = time.time() + timeinterval

def SendToArd_block(message, arduAddress):
    # send data
    bus.write_i2c_block_data(arduAddress,0,list(message))

def functionsStore(_rideWalk, _lowMidleHigh, _cross, _F1, _F2, _F3):
    print(f"{_rideWalk} {_lowMidleHigh} {_cross} {_F1} {_F2} {_F3}")
    #startup initialisation
    if str(_cross) == 'X':
        commands.DelleteAllCommands()
    
    if int(_F1)==0 and int(_F2)==0 and int(_F3)==1:
        print("startup initialisation")
        commands.AddCommand(180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 1000)
    
    #set all to 0
    if int(_F1)==0 and int(_F2)==0 and int(_F3)==9:
        print("set all to 0")
        commands.AddCommand(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1000)
        
    #set a series of commands
    if int(_F1)==0 and int(_F2)==0 and int(_F3)==5:
        print("set a series of commands")
        commands.AddCommand(180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 1000)
        commands.AddCommand(90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 1000)
        commands.AddCommand(180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 1000)
        commands.AddCommand(90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 1000)
        commands.AddCommand(180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 1000)
        commands.AddCommand(90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 1000)
        commands.AddCommand(180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 1000)
        commands.AddCommand(90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 1000)
        
    #print(f"functionsStore end: {commands}")
    pass

while True:
    #time.sleep(1000)
    try:
        message, address = server_socket.recvfrom(1024)
    except BlockingIOError:
        message = "  RM%000"       
    
    message = message.upper()
    message_str = str(message)
    #print("from GUI:" + message_str)
    try:
        server_socket.sendto(message, address)
    except Exception as e:
        #print("nothing to resend")
        pass
    
    rideWalk = message_str[2:3] #ride / walk
    lowMidleHigh = message_str[3:4] #low / midle / high
    cross = message_str[4:5] #cross
    F1 = message_str[5:6] #F1
    F2 = message_str[6:7] #F2
    F3 = message_str[7:8] #F3
    
    functionsStore(rideWalk, lowMidleHigh, cross, F1, F2, F3)
    
    if nextTm < time.time():
        
        if(commands.StoreLen() > 0):
            cmd = commands.GetNextCommand()
            #print(str(cmd))
            msgA = [ord('<'),ord('S'),cmd.GetAS1(),cmd.GetAS2(),cmd.GetAS3(),cmd.GetAS4(),cmd.GetAS5(),cmd.GetAS6(),cmd.GetADC1(),cmd.GetADC2(),ord('>')]
            msgB = [ord('<'),ord('S'),cmd.GetBS1(),cmd.GetBS2(),cmd.GetBS3(),cmd.GetBS4(),cmd.GetBS5(),cmd.GetBS6(),cmd.GetBDC1(),cmd.GetBDC2(),ord('>')]
            msgC = [ord('<'),ord('S'),cmd.GetCS1(),cmd.GetCS2(),cmd.GetCS3(),cmd.GetCS4(),cmd.GetCS5(),cmd.GetCS6(),cmd.GetCDC1(),cmd.GetCDC2(),ord('>')]
            timeinterval = cmd.GetTime()/1000
            
            try:
                SendToArd_block(msgA, i2cAddrA)
            except Exception as eA:
                print("Error when sending msg to reciever A[i2c addr " + str(i2cAddrA) + "]", eA)
            
            try:
                SendToArd_block(msgB, i2cAddrB)
            except Exception as eB:
                print("Error when sending msg to reciever B[i2c addr " + str(i2cAddrB) + "]", eB)
            
            try:
                SendToArd_block(msgC, i2cAddrC)
            except Exception as eC:
                print("Error when sending msg to reciever C[i2c addr " + str(i2cAddrC) + "]", eC)
            
            #time.sleep(cmd.GetTime()/1000)
            
            #print("sent")
            del cmd
            print(f"{commands}")
        else:
            timeinterval = 0.1
            print(f"on hold {commands} ")
        nextTm = time.time() + timeinterval
    
    
