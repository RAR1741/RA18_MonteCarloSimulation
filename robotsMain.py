from Field import Field


Field = Field()

for Time in range(0,150,1):
  if Time <=15:
    ##add in auto points
   Field.auto_tick(Time)
  elif Time >= 120:
    Field.endgame_tick(Time)
  else:
    Field.tick(Time)


Field.checkIfWin()




#Function for checking who wins
#Function for checking who has control of switch or scale
  #possibly have variables for each alliance switch and the scale
#Function for randomiing powerups and tracking the number of cubes in vault
#Use Pseudocode for the Robot class  
#Use the input to determine what skill level the robot is 

  