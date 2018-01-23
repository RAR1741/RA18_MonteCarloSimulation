class Scale:
    def __init__(self, is_red_alliance):
        self.red_cubes1 = 0
        self.blue_cubes1 = 0
        self.redpoints = 0
        self.bluepoints = 0
        self.scale_state = 1

    def add_scale_cube(self, is_red_alliance):
        if is_red_alliance:
            self.red_cubes1 += 1
        else:
            self.blue_cubes1 += 1

    def scale_tilt_state(self, is_red_alliance):
        if is_red_alliance and self.red_cubes1 > self.blue_cubes1:
            self.scale_state = 1
        elif is_red_alliance is False and self.blue_cubes1 > self.red_cubes1:
            self.scale_state = 2
        else:
            self.scale_state = 0
            