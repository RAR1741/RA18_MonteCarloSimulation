class Switch:
    def __init__(self, is_red_alliance):
      self.red_cubes = 0
      self.blue_cubes = 0
      self.switch_state = 0

    def add_switch_cube(self, is_red_alliance):
      if is_red_alliance:
        self.red_cubes += 1
      else:
        self.blue_cubes +=1

    def switch_tilt_state(self, is_red_alliance):
        if is_red_alliance and self.red_cubes > self.blue_cubes:
            self.switch_state = 1
        elif is_red_alliance is False and self.blue_cubes > self.red_cubes:
            self.scale_state = 2
        else:
            self.scale_state = 0  

    