class Switch:
    def __init__(self, is_red_alliance):
      self.red_cubes = 0
      self.blue_cubes = 0

    def add_switch_cube(self, is_red_alliance):
      if is_red_alliance == True:
        self.red_cubes += 1
      else:
        self.blue_cubes +=1

    def switch_tilt(self):
      if  self.red_cubes > self.blue_cubes:
        pass
      elif self.blue_cubes > self.red_cubes:
        pass
      elif self.red_cubes == self.blue_cubes:
        pass 
      else:
        print("Something is wrong with the switch boi")