import copy

class Command:
    commandID = -1
    i2cAddress = -1
    S1 = -1
    S2 = -1
    S3 = -1
    S4 = -1
    S5 = -1
    S6 = -1
    DC1 = -1
    DC2 = -1
    time = -1
    
    def GetI2cAddress(self):
        return self.i2cAddress
    
    def GetS1(self):
        return self.S1
    
    def GetS2(self):
        return self.S2
    
    def GetS3(self):
        return self.S3
    
    def GetS4(self):
        return self.S4
    
    def GetS5(self):
        return self.S5
    
    def GetS6(self):
        return self.S6
    
    def GetDC1(self):
        return self.DC1
    
    def GetDC2(self):
        return self.DC2
    
    def GetTime(self):
        return self.time
    
    def __init__(self, _i2cAddress, _S1, _S2, _S3, _S4, _S5, _S6, _DC1, _DC2, _time, _commandID):
        self.i2cAddress = _i2cAddress
        self.S1 = _S1
        self.S2 = _S2
        self.S3 = _S3
        self.S4 = _S4
        self.S5 = _S5
        self.S6 = _S6
        self.DC1 = _DC1
        self.DC2 = _DC2
        self.time = _time
        self.commandID = _commandID
    
    def __str__(self):
        return f"i2cAddress: {self.i2cAddress} S1: {self.S1} S2: {self.S2} S3: {self.S3} S4: {self.S4} S5: {self.S5} S6: {self.S6} DC1: {self.DC1} DC2: {self.DC2} time: {self.time} commandID: {self.commandID} "
    
class ComandStore:
    commandId = 0
    lastReturnedCommandID = 0
    
    store = [Command(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1)];
        
    def __init__(self):
        pass
    
    def __str__(self):
        return str("CommandStore - commands in buffer:" + str(self.StoreLen()-1))
    
    def _getNextCommandID(self):
        tmp_commandId = self.commandId
        self.commandId = self.commandId + 1
        return tmp_commandId
    
    def AddCommand(self, _i2cAddress, _S1, _S2, _S3, _S4, _S5, _S6, _DC1, _DC2, _time):
        self.store.append(Command(_i2cAddress, _S1, _S2, _S3, _S4, _S5, _S6, _DC1, _DC2, _time, self._getNextCommandID()) )
        pass
    
    def StoreLen(self):
        return self.store.__len__()-1
    
    def RemoveCommandByCommandID(self, _CommandID):
        result = False
        
        for i in range(len(self.store)):
            if(self.store[i].commandID == _CommandID):
                self.store.pop(i)
                result = True
                break
        
        return result
    
    def GetNextCommand(self):
        commandCopy = None
        for i in range(len(self.store)):
            if(self.store[i].commandID == self.lastReturnedCommandID):
                commandCopy = copy.deepcopy(self.store[i])
                self.store.pop(i)
                break
       
        self.lastReturnedCommandID = self.lastReturnedCommandID + 1
        return commandCopy