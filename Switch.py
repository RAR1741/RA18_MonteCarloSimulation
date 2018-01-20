class Switch:
    def __init__(self, is_red_alliance):
      self.red_cubes = 0
      self.blue_cubes = 0

    def add_switch_cube(self, is_red_alliance):
      if is_red_alliance == True:
        self.red_cubes += 1
      else:
        self.blue_cubes +=1

