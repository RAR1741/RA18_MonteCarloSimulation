class Scale:
    def __init__(self, is_red_alliance):
        self.red_cubes1 = 0
        self.blue_cubes1 = 0
        self.redpoints = 0
        self.bluepoints = 0

    def add_scale_cube(self, is_red_alliance):
        if is_red_alliance:
            self.red_cubes1 += 1
        else:
            self.blue_cubes1 += 1

    
            