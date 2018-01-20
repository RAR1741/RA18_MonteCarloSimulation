import random
import numpy

class Robots:
  def __init__(self, field, is_red_alliance, name, skillRating):
    print("Robot init")
    self.field = field
    self.is_red_alliance = is_red_alliance
    self.name = name
    self.skillRating = skillRating

    self.action_time = 0
    self.action_success_rate = 0
    self.randomPick = 0
  
  def tick(self, time):
    self.action_time -= 1
    print(f"Time: {self.action_time}")

    if self.action_time <= 1:
      if self.action_success_rate >= random.randint(1,100):
        self.do_action()
      self.get_new_action()

  def get_new_action(self):
    self.randomPick = random.randint(0,2)

    # Robot Skill Level 1
    if(self.randomPick == 0 or self.randomPick == 1 or self.randomPick == 2):
      self.randomPick = 0
      self.action_time = int(numpy.random.normal(loc=45, scale=15, size=None))
      self.action_success_rate = 80

  def do_action(self):
    # Vault
    if self.randomPick == 0:
      self.field.add_boost_cube(self.is_red_alliance)

    # Switch
    elif self.randomPick == 1:
      pass

    # Scale
    elif self.randomPick == 2:
      pass

#C:\Program Files (x86)\Python36-32
#variables  *make sure to add stuff for powerups*


# #Robot Function
# def RobotAbility(RobotSkill):
#   if(RobotSkill == 1):
#     vault = True
#     if(randomPick == 0 or randomPick == 1 or randomPick == 2):
#       vaultTime = numpy.random.normal(loc=45, scale=15, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <= 80): #can score in the vault
#         while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=45, scale=15, size=None)
    
#     scale1 = False    
#     switch = False
#     climbing = False
#     parking = True
#     if(parking == True and parkingSuccess <=85):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=20, scale=10, size=None)  


  
#   elif(RobotSkill == 2):
#     vault = True
#     if(randomPick == 0 or randomPick == 1 or randomPick == 2):
#       vaultTime = numpy.random.normal(loc=35, scale=12.5, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <=83):
#         while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=35, scale=12.5, size=None)
      
#     scale1 = False    
#     switch = False
#     climbing = False
#     parking = True
#     if(parking == True and parkingSuccess <=89):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=15, scale=7.5, size=None) 
    
  
  
#   elif(RobotSkill == 3):
#     vault = True
#     if(randomPick == 0 or randomPick == 1 or randomPick == 2):
#       vaultTime = numpy.random.normal(loc=30, scale=10, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <=85):
#          while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=30, scale=10, size=None)
    
#       switch = True
#       switchTime = numpy.random.normal(loc=30, scale=15, size=None)
#       if(switch == True and switchSuccess <=66):
#         switchCubes += 1
#         switchTime = numpy.random.normal(loc=30, scale=15, size=None)
    
#     scale1 = False
#     climbing = False
#     parking = True
#     if(parking == True and parkingSuccess <=92):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=13, scale=7.5, size=None) 
  
  
  
#   elif(RobotSkill == 4):
#     vault = True
#     scale1 = True
#     switch = True
#     if(randomPick == 0):
#       vaultTime = numpy.random.normal(loc=25, scale=8, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <=86):
#         while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=25, scale=8, size=None)
  
#     if(randomPick == 1):
#       scaleTime = numpy.random.normal(loc=35, scale=15, size=None)
#       scaleSuccess = random.randint(0,100)
#       if (scale1 == True and scaleSuccess <=66):
#         scaleCubes += 1
#         scaleTime = numpy.random.normal(loc=35, scale=15, size=None)
  
    
#     if(randomPick == 2):
#       if(switch == True and switchSuccess <=73):
#         switchCubes += 1
#         switchTime = numpy.random.normal(loc=25, scale=10, size=None)

#     climbing = True
#     if(climbing == True and climbingSuccess <=33):
#       climbedRobots += 1
#       climbingTime = numpy.random.normal(loc=30, scale=15, size=None)
#     elif(parking == True and parkingSuccess <=94):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=10, scale=5, size=None)  
    
    
    
#   elif (RobotSkill == 5):
#     vault = True
#     scale1 = True
#     switch = True
#     if(randomPick == 0):
#       vaultTime = numpy.random.normal(loc=20, scale=6, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <=89):
#         while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=20, scale=6, size=None)
      
#     if(randomPick == 1):
#       scaleTime = numpy.random.normal(loc=30, scale=12.5, size=None)
#       scaleSuccess = random.randint(0,100)
#       if (scale1 == True and scaleSuccess <=72):
#         scaleCubes += 1
#         scaleTime = numpy.random.normal(loc=30, scale=12.5, size=None)
    
#     if(randomPick == 2):
#       switchTime = numpy.random.normal(loc=20, scale=10, size=None)
#       if(switch == True and switchSuccess <=78):
#         switchCubes += 1
#         switchTime = numpy.random.normal(loc=25, scale=10, size=None)
  
#     climbing = True
#     if(climbing == True and climbingSuccess <=40):
#       climbedRobots += 1
#       climbingTime = numpy.random.normal(loc=27, scale=12.5, size=None)
#     elif(parking == True and parkingSuccess <=96):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=8, scale=4, size=None)  
    
    
  
#   elif(RobotSkill == 6):
#     vault = True
#     scale1 = True
#     switch = True
#     if(randomPick == 0):
#       vaultTime = numpy.random.normal(loc=15, scale=5, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <= 92):
#         while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=15, scale=5, size=None)
      
#     if(randomPick == 1):
#       scaleTime = numpy.random.normal(loc=25, scale=10, size=None)
#       scaleSuccess = random.randint(0,100)
#       if (scale1 == True and scaleSuccess <=77):
#         scaleCubes += 1
#         scaleTime = numpy.random.normal(loc=25, scale=10, size=None)
  
#     if(randomPick == 2):
#       switchTime = numpy.random.normal(loc=15, scale=7.5, size=None)
#       if(switch == True and switchSuccess <=85):
#         switchCubes += 1
#         switchTime = numpy.random.normal(loc=15, scale=7.5, size=None)

#     climbing = True 
#     if(climbing == True and climbingSuccess <=66):
#       climbedRobots += 1
#       climbingTime = numpy.random.normal(loc=24, scale=10, size=None)
#     elif(parking == True and parkingSuccess <=97):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=6, scale=3, size=None)
  
  
  
#   elif(RobotSkill == 7):
#     vault = True
#     scale1 = True
#     switch = True
#     if(randomPick == 0):
#       vaultTime = numpy.random.normal(loc=12.5, scale=4, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <= 95):
#         while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=12.5, scale=4, size=None)
  
#     if(randomPick == 1):
#       scaleTime = numpy.random.normal(loc=20, scale=7.5, size=None)
#       scaleSuccess = random.randint(0,100)
#       if (scale1 == True and scaleSuccess <=85):
#         scaleCubes += 1
#         scaleTime = numpy.random.normal(loc=20, scale=7.5, size=None)
  
#     if(randomPick == 2):
#       switchTime = numpy.random.normal(loc=12.5, scale=5, size=None)
#       if(switch == True and switchSuccess <=88):
#         switchCubes += 1
#         switchTime = numpy.random.normal(loc=12.5, scale=5, size=None)
    
#     climbing = True
#     if(climbing == True and climbingSuccess <=78):
#       climbedRobots += 1
#       climbingTime = numpy.random.normal(loc=18, scale=7.5, size=None)
#     elif(parking == True and parkingSuccess <=98):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=5, scale=3, size=None)
  
    
    
#   elif(RobotSkill == 8):
#     vault = True
#     scale1 = True
#     switch = True
#     if(randomPick == 0):
#       vaultTime = numpy.random.normal(loc=10, scale=3, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <= 97):
#         while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=10, scale=3, size=None)
  
#     if(randomPick == 1):
#       scaleTime = numpy.random.normal(loc=15, scale=5, size=None)
#       scaleSuccess = random.randint(0,100)
#       if (scale1 == True and scaleSuccess <=90):
#         scaleCubes += 1
#         scaleTime = numpy.random.normal(loc=15, scale=5, size=None)
    
#     if(randomPick == 2):
#       switchTime = numpy.random.normal(loc=10, scale=4.5, size=None)
#       if(switch == True and switchSuccess <=90):
#         switchCubes += 1
#         switchTime = numpy.random.normal(loc=10, scale=4.5, size=None)
    
#     climbing = True   
#     if(climbing == True and climbingSuccess <=85):
#       climbedRobots += 1
#       climbingTime = numpy.random.normal(loc=13, scale=5, size=None)
#     elif(parking == True and parkingSuccess <=99):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=4, scale=2, size=None)
    
    
    
#   elif(RobotSkill == 9):
#     vault = True
#     climbing = True
#     scale1 = True
#     switch = True
#     if(randomPick == 0):
#       vaultTime = numpy.random.normal(loc=7.5, scale=2, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <= 97):
#         while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=7.5, scale=2, size=None)
  
#     if(randomPick == 1):
#       scaleTime = numpy.random.normal(loc=12.5, scale=4, size=None)
#       scaleSuccess = random.randint(0,100)
#       if (scale1 == True and scaleSuccess <=95):
#         scaleCubes += 1
#         scaleTime = numpy.random.normal(loc=12.5, scale=4, size=None)
    
#     if(randomPick == 2):
#       switchTime = numpy.random.normal(loc=8.75, scale=2.5, size=None)
#       if(switch == True and switchSuccess <=95):
#         switchCubes += 1
#         switchTime = numpy.random.normal(loc=8.75, scale=2.5, size=None)

    
#     if(climbing == True and climbingSuccess <=90):
#       climbedRobots += 1
#       climbingTime = numpy.random.normal(loc=7, scale=3, size=None)
#     elif(parking == True and parkingSuccess <=99):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=3, scale=1.5, size=None)



#   elif(RobotSkill == 10):
#     vault = True
#     climbing = True
#     scale1 = True
#     switch = True
#     if(randomPick == 0):
#       vaultTime = numpy.random.normal(loc=5, scale=2, size=None)
#       vaultSuccess = random.randint(0,100)
#       if(vault == True and vaultSuccess <= 99):
#         while(vaultCubes < 9):
#           if(Time % vaultTime == 0):
#             vaultCubes += 1
#             vaultTime = numpy.random.normal(loc=5, scale=2, size=None)
  
#     if(randomPick == 1):
#       scaleTime = numpy.random.normal(loc=10, scale=3, size=None)
#       scaleSuccess = random.randint(0,100)
#       if (scale1 == True and scaleSuccess <=98):
#         scaleCubes += 1
#         scaleTime = numpy.random.normal(loc=10, scale=3, size=None)
    
#     if(randomPick == 2): 
#       switchTime = numpy.random.normal(loc=7, scale=2, size=None)
#       if(switch == True and switchSuccess <=99):
#         switchCubes += 1
#         switchTime = numpy.random.normal(loc=7, scale=2, size=None)

    
#     if(climbing == True and climbingSuccess <=95):
#       climbedRobots += 1
#       climbingTime = numpy.random.normal(loc=4, scale=2, size=None)
#     elif(parking == True and parkingSuccess <=99):
#       parkedRobots += 1
#       parkingTime = numpy.random.normal(loc=2, scale=1, size=None)
    


#   else:
#     print("The points were not cubes registered")
#     if(climbing == False and """add in charactersitics it needs to pass for climbing to succeed"""):
#       if(Time % vaultTime == 0):
#         """add points to the specific alliance"""
#     else:
#       print("Your Robot's skill is off the charts")