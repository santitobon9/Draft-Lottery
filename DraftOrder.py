import numpy as np

def ReadFromFile():
    members = list()
    with open("FBBleague.txt") as file:
        for line in file:
            lines = line.strip().split("\n")
            for l in lines:
                members.append(l)
    
    return members

def createOrder ():
    order = np.random.choice(12, size=12, replace=False)
    return order


members = ReadFromFile()
order = createOrder()
#print ("Before order change")
#print (members)

print("Draft Order:")
for i, o in enumerate(order):
    print(i+1, members[o])
    