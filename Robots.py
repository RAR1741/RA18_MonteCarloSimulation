import random
import numpy

class Robots:
  def __init__(self, field, is_red_alliance, name, skillRating):
    #print("Robot init")
    self.field = field
    self.is_red_alliance = is_red_alliance
    self.name = name
    self.skillRating = skillRating
    self.get_endgame(skillRating)
  

    self.action_time = 0
    self.action_success_rate = 0
    self.randomPick = 0
    self.climbing_time = 0
    self.did_endgame = False
    self.climb = False
    self.platform = False
    self.auto_run = False
    self.can_auto = True
  
  def tick(self, time):
    # print(f"Time({self.name}):{self.action_time}:{self.randomPick}")
    self.action_time -= 1
    if self.action_time <= 1:
      if self.action_success_rate >= random.randint(1,100):
          self.do_action()
          
      if time < 15:
        print("=============================")
        print(f"{self.name}:{time}")
        self.get_new_action()
      elif time <120:
        self.get_new_action()
      else:
        self.action_time = 0
        self.climbing_time -= 1
        if self.climbing_time <= 1 and self.did_endgame == False:
          self.did_endgame = True
          if self.climbing_success_rate >= random.randint(1,100):
            self.climb = True
          else:
            self.platform = True



  def get_new_action(self):
    self.randomPick = random.randint(1,4)
   
   
    # Robot Skill Level 1
    if self.skillRating == 1:
      if self.randomPick == 0 or self.randomPick == 1 or self.randomPick == 2 or self.randomPick == 3:
        self.randomPick = 0
        self.action_time = int(numpy.random.normal(loc=45, scale=15, size=None))
        self.action_success_rate = 80

    #Robot skill level 2
    elif self.skillRating == 2:
      if self.randomPick == 0 or self.randomPick == 1 or self.randomPick == 2 or self.randomPick == 3:
        self.randomPick = 1
        self.action_time = int(numpy.random.normal(loc=30, scale=15, size=None))
        self.action_success_rate = 85

    #Robot skill level 3
    elif self.skillRating == 3:
      if self.randomPick == 3:
        self.randomPick == random.randint(0,2) 
      if self.randomPick == 0:
        self.randomPick = 0
        self.action_time = int(numpy.random.normal(loc=30, scale=10, size=None))
        self.action_success_rate = 85
      elif self.randomPick == 1:
        self.randomPick = 1
        self.action_time = int(numpy.random.normal(loc=30, scale=15, size=None))
        self.action_success_rate = 66
      elif self.randomPick == 2:
        self.randomPick = 2
        self.action_time = int(numpy.random.normal(loc=30, scale=15, size=None))
        self.action_success_rate = 66  

    #Robot skill level 4
    elif self.skillRating == 4:
      if self.randomPick == 3:
        self.randomPick == random.randint(0,2)     
      if self.randomPick == 0:
        self.randomPick = 0
        self.action_time = int(numpy.random.normal(loc=25, scale=8, size=None))
        self.action_success_rate = 86
      elif self.randomPick == 1:
        self.randomPick = 1
        self.action_time = int(numpy.random.normal(loc=35, scale=15, size=None))
        self.action_success_rate = 66
      elif self.randomPick == 2:
        self.randomPick = 2
        self.action_time = int(numpy.random.normal(loc=35, scale=15, size=None))
        self.action_success_rate = 66
      # elif self.randomPick == 4:
      #   self.randomPick = 4
      #   if self.field.time >= 120:
      #     self.action_time = self.action_time
      #     self.action_success_rate = 33   

    #Robot skill level 5
    elif self.skillRating == 5:   
      if self.randomPick == 0:
        self.randomPick = 0
        self.action_time = int(numpy.random.normal(loc=20, scale=6, size=None))
        self.action_success_rate = 89
      elif self.randomPick == 1:
        self.randomPick = 1
        self.action_time = int(numpy.random.normal(loc=20, scale=10, size=None))
        self.action_success_rate = 78
      elif self.randomPick == 2:
        self.randomPick = 2
        self.action_time = int(numpy.random.normal(loc=20, scale=10, size=None))
        self.action_success_rate = 78
      elif self.randomPick == 3:
        self.randomPick = 3
        self.action_time = int(numpy.random.normal(loc=30, scale=12.5, size=None))
        self.action_success_rate = 72
      # elif self.randomPick == 4:
      #   self.randomPick = 4
      #   if self.field.time >= 120:
      #     self.action_time = self.action_time
      #     self.action_success_rate = 40    

    #Robot skill level 6
    elif self.skillRating == 6:   
      if self.randomPick == 0:
        self.randomPick = 0
        self.action_time = int(numpy.random.normal(loc=15, scale=5, size=None))
        self.action_success_rate = 92
      elif self.randomPick == 1:
        self.randomPick = 1
        self.action_time = int(numpy.random.normal(loc=15, scale=7.5, size=None))
        self.action_success_rate = 85
      elif self.randomPick == 2:
        self.randomPick = 2
        self.action_time = int(numpy.random.normal(loc=15, scale=7.5, size=None))
        self.action_success_rate = 85
      elif self.randomPick == 3:
        self.randomPick = 3
        self.action_time = int(numpy.random.normal(loc=25, scale=10, size=None))
        self.action_success_rate = 77
      # elif self.randomPick == 4:
      #   self.randomPick = 4
      #   if (self.field.time >= 120):
      #     self.action_time = self.action_time
      #     self.action_success_rate = 66     

    #Robot skill level 7
    elif self.skillRating == 7:   
      if self.randomPick == 0:
        self.randomPick = 0
        self.action_time = int(numpy.random.normal(loc=12.5, scale=4, size=None))
        self.action_success_rate = 95
      elif self.randomPick == 1:
        self.randomPick = 1
        self.action_time = int(numpy.random.normal(loc=12.5, scale=5, size=None))
        self.action_success_rate = 88
      elif self.randomPick == 2:
        self.randomPick = 2
        self.action_time = int(numpy.random.normal(loc=12.5, scale=5, size=None))
        self.action_success_rate = 88
      elif self.randomPick == 3:
        self.randomPick = 3
        self.action_time = int(numpy.random.normal(loc=20, scale=7.5, size=None))
        self.action_success_rate = 85  
      # elif self.randomPick == 4:
      #   self.randomPick = 4
      #   if self.field.time >= 120:
      #     self.action_time = self.action_time
      #     self.action_success_rate = 78   

    #Robot skill level 8
    elif self.skillRating == 8:
      if self.randomPick == 0:
        self.randomPick = 0
        self.action_time = int(numpy.random.normal(loc=10, scale=3, size=None))
        self.action_success_rate = 97
      elif self.randomPick == 1:
        self.randomPick = 1
        self.action_time = int(numpy.random.normal(loc=10, scale=4.5, size=None))
        self.action_success_rate = 90
      elif self.randomPick == 2:
        self.randomPick = 2
        self.action_time = int(numpy.random.normal(loc=10, scale=4.5, size=None))
        self.action_success_rate = 90
      elif self.randomPick == 3:
        self.randomPick = 3
        self.action_time = int(numpy.random.normal(loc=15, scale=5, size=None))
        self.action_success_rate = 90
      # elif self.randomPick == 4:
      #   self.randomPick = 4
      #   if self.field.time >= 120:
      #     self.action_time = self.action_time
      #     self.action_success_rate = 85  

    #Robot skill level 9
    elif self.skillRating == 9:
      if self.randomPick == 0:
        self.randomPick = 0
        self.action_time = int(numpy.random.normal(loc=7.5, scale=2, size=None))
        self.action_success_rate = 97
      elif self.randomPick == 1:
        self.randomPick = 1
        self.action_time = int(numpy.random.normal(loc=8.75, scale=2.5, size=None))
        self.action_success_rate = 95
      elif self.randomPick == 2:
        self.randomPick = 2
        self.action_time = int(numpy.random.normal(loc=8.75, scale=2.5, size=None))
        self.action_success_rate = 95
      elif self.randomPick == 3:
        self.randomPick = 3
        self.action_time = int(numpy.random.normal(loc=12.5, scale=4, size=None))
        self.action_success_rate = 95
      # elif self.randomPick == 4:
      #   self.randomPick = 4
      #   if self.field.time >= 120:
      #     self.action_time = self.action_time
      #     self.action_success_rate = 90  

    #Robot skill level 10
    elif self.skillRating == 10:
      if self.randomPick == 0:
        self.randomPick = 0
        self.action_time = int(numpy.random.normal(loc=5, scale=2, size=None))
        self.action_success_rate = 99
      elif self.randomPick == 1:
        self.randomPick = 1
        self.action_time = int(numpy.random.normal(loc=7, scale=2, size=None))
        self.action_success_rate = 99
      elif self.randomPick == 2:
        self.randomPick = 2
        self.action_time = int(numpy.random.normal(loc=7, scale=2, size=None))
        self.action_success_rate = 99
      elif self.randomPick == 3:
        self.randomPick = 3
        self.action_time = int(numpy.random.normal(loc=10, scale=3, size=None))
        self.action_success_rate = 98
      # elif self.randomPick == 4:
      #   self.randomPick = 4
        # if (self.field.time >= 120):
        #   self.action_time = self.action_time
        #   self.action_success_rate = 95
  
  def do_action(self):
    # Vault
    if self.randomPick == 0:
      self.field.add_random_vault_cube(self.is_red_alliance)

    #MySwitch
    elif self.randomPick == 1:
      self.field.add_my_switch_cube(self.is_red_alliance)

    #TheirSwitch
    elif self.randomPick == 2:
      self.field.add_their_switch_cube(self.is_red_alliance)

    #Scale
    elif self.randomPick == 3:
      self.field.add_scale_cube(self.is_red_alliance)

  def get_endgame(self, skillRating):
    #Skills 1-3 must do parking only
    if skillRating == 1:
      self.climbing_time = numpy.random.normal(loc=20, scale=10, size=None) 
      self.climbing_success_rate = 0 
    elif skillRating == 2:
      self.climbing_time = numpy.random.normal(loc=15, scale=7.5, size=None)
      self.climbing_success_rate = 0
    elif skillRating == 3:
      self.climbing_time = numpy.random.normal(loc=13, scale=7.5, size=None)
      self.climbing_success_rate = 0
    #Skills 4-10 can climb, can resort to immediate parking
    elif skillRating == 4:  
      self.climbing_time = numpy.random.normal(loc=30, scale=15, size=None)
      self.climbing_success_rate = 33 
      if self.climbing_time > 30:
        self.climbing_time = 30
    elif skillRating == 5:
      self.climbing_time = int(numpy.random.normal(loc=27, scale=12.5, size=None))
      self.climbing_success_rate = 40
      if self.climbing_time > 30:
        self.climbing_time = 30
    elif skillRating == 6:
      self.climbing_time = int(numpy.random.normal(loc=24, scale=10, size=None))
      self.climbing_success_rate = 66 
      if self.climbing_time > 30:
        self.climbing_time = 30
    elif skillRating == 7:
      self.climbing_time = int(numpy.random.normal(loc=18, scale=7.5, size=None))
      self.climbing_success_rate = 78  
    elif skillRating == 8: 
      self.climbing_time = int(numpy.random.normal(loc=13, scale=5, size=None))
      self.climbing_success_rate = 85  
    elif skillRating == 9: 
      self.climbing_time = int(numpy.random.normal(loc=7, scale=3, size=None))
      self.climbing_success_rate = 90  
    elif skillRating == 10:
      self.climbing_time = int(numpy.random.normal(loc=4, scale=2, size=None)) 
      self.climbing_success_rate = 95
  
  def baseline(self):
    if self.can_auto == True:
      self.auto_success = random.randint(1,100)
      if self.auto_success <= 90:
        self.auto_run = True
        self.can_auto = False      
