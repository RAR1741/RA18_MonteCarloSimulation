import random 
class Vault:
    def __init__(self, is_red_alliance):
        self.boost_cubes = 0
        self.force_cubes = 0
        self.lev_cubes = 0
        self.overflow_cubes = 0
        self.is_red_alliance = is_red_alliance
        
    # def add_boost_cube(self):
    #     if self.boost_cubes < 3:
    #         self.boost_cubes += 1
    # def add_force_cube(self):
    #     if self.force_cubes < 3:
    #         self.force_cubes += 1
    # def add_lev_cube(self):
    #     if self.lev_cubes < 3:
    #         self.lev_cubes += 1
    def add_random_cube(self):
        if self.boost_cubes == 3 and self.force_cubes == 3 and self.lev_cubes == 3:
            self.overflow_cubes += 1
        else:
            randomPick = random.randint(0, 2)
            if randomPick == 0:
                if self.boost_cubes < 3:
                    self.boost_cubes += 1
                else:
                    self.add_random_cube()
            if randomPick == 1:
                if self.force_cubes < 3:
                    self.force_cubes += 1
                else:
                    self.add_random_cube()
            if randomPick == 2:
                if self.lev_cubes < 3:
                    self.lev_cubes += 1
                else:
                    self.add_random_cube()
            