from Field import Field

# global priority

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

# global randomPick

#main
# blue1Skill = random.randint(1, 10)
# blue2Skill = random.randint(1, 10)
# blue3Skill = random.randint(1, 10)

# red1Skill = random.randint(1, 10)
# red2Skill = random.randint(1, 10)
# red3Skill = random.randint(1, 10)

# blue1 = Robots("B1", blue1Skill)
# blue2 = Robots("B2", blue2Skill)
# blue3 = Robots("B3", blue3Skill)

# red2 =  Robots("R2", red2Skill)
# red3 = Robots("R3", red3Skill)

# alliances = [[blue1, blue2, blue3],[red1, red2, red3]]


Field = Field()

for Time in range(0,150,1):
  if(Time <=15):
    ##add in auto points
    print("auto")
  else:
    ##add in regular points
    Field.tick(Time)


# vaultCubes = 0

# while (vaultCubes < 9)
#   randomChoice = random.randint(1,3)
#   if (randomChoice == 1)

#   elif (randomChoice == 2)

#   elif (randomChoice == 3)
#     vaultCubes += 1
    
# else    
#   randomChoice = random.randint(1,2)
#   if (randomChoice == 1)

#   elif (randomChoice == 2)     

    






#Function for checking who wins
#Function for checking who has control of switch or scale
  #possibly have variables for each alliance switch and the scale
#Function for randomiing powerups and tracking the number of cubes in vault
#Use Pseudocode for the Robot class  
#Use the input to determine what skill level the robot is 





#when the skill is chose
#pickAction rand(1,3)
#if(pick action == 1 && vaultCubes >= 9)
# then pickAction again
#else 
# do vault
#if pickAction  is 2 do switch
# if pickAction is 3 do your vault
  