dPilot = {"Darth Vader":9,"Luke SkyWalker":7,"Poe Daemeron":9}

print('moving')
### moving
listofTuples = sorted(dPilot.items() ,  key=lambda x: x[1])
for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] )

print('')

print('attacking')
### attacking
listofTuples = sorted(dPilot.items() ,  key=lambda x: x[1], reverse=True)
for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] )

lTestPilot = [("Darth Vader", 9, "E"), ("Luke Skywalker", 7, "R"), ("Poe Daemeron", 9, "R")]

