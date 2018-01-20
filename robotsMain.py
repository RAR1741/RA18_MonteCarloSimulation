from Field import Field

# global switch
# global switchAuto
# global switchChance
# global switchCubes

# global vault
# global vaultAuto
# global vaultChance
# global vaultCubes

# global scale1
# global scale1Auto
# global scaleChance
# global scaleCubes

# global climbing
# global climbingChance
# global climbedRobots

# global parking
# global parkingChance
# global parkedRobots

# global Time
# global blue
# global bluePoints
# global redPoints
# global red


Field = Field()

for Time in range(0,150,1):
  if(Time <=15):
    ##add in auto points
    print("auto")
  else:
    ##add in regular points
    Field.tick(Time)







#Function for checking who wins
#Function for checking who has control of switch or scale
  #possibly have variables for each alliance switch and the scale
#Function for randomiing powerups and tracking the number of cubes in vault
#Use Pseudocode for the Robot class  
#Use the input to determine what skill level the robot is 

  