class Switch:
    def __init__(self, is_red_alliance):
      self.switch_cubes = 0

    def add_switch_cube(self):
      self.switch_cubes += 1

    def switch_tilt(self):
      if redCubes > blueCubes:
        pass
      elif blueCubes > redCubes:
        pass
      elif redCubes == blueCubes:
        pass 
      else:
        print("Something is wrong with the switch boi")