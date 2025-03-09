from commandStore  import ComandStore

cs = ComandStore()

cs.AddCommand(4, 1, 2, 3, 4, 5, 6, 10, 11, 100)
cs.AddCommand(4, 1, 2, 3, 4, 5, 6, 10, 11, 100)
cs.AddCommand(4, 1, 2, 3, 4, 5, 6, 10, 11, 100)

cs.AddCommand(5, 1, 2, 3, 4, 5, 6, 10, 11, 100)
cs.AddCommand(5, 1, 2, 3, 4, 5, 6, 10, 11, 100)
cs.AddCommand(5, 1, 2, 3, 4, 5, 6, 10, 11, 100)

print(str(cs.store[0]))
print(str(cs.store[1]))
print(str(cs.store[2]))
print(str(cs.store[3]))
print(str(cs.store[4]))
print(str(cs.store[5]))
print(str(cs.store[6]))
print(cs)



print("Get command:" + str(cs.GetNextCommand()))
print("Get command:" + str(cs.GetNextCommand()))
print("Get command:" + str(cs.GetNextCommand()))

print(cs)
print(str(cs.store[0]))
print(str(cs.store[1]))
print(str(cs.store[2]))
print(str(cs.store[3]))














